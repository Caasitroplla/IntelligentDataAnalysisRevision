import numpy as np

DOCUMENTS = [
    """The cat sat on the windowsill, watching birds flutter across the trees outside. It purred softly, basking in the warmth of the morning sun. A breeze stirred the curtains, and leaves danced in the light. The house was quiet, filled with gentle shadows and golden light. In the kitchen, a kettle whistled. The cat’s ears twitched at every sound. It leapt gracefully from the windowsill, landing without a sound. Footsteps echoed softly on the wooden floor. A hand reached down and scratched behind its ears. The cat purred louder, pressing into the touch. Outside, the birds kept singing, free and unaware.""",

    """Birds filled the morning sky with song, flitting from branch to branch in a dance of feathers. A robin perched on a windowsill, peering inside with curious eyes. The sun crept higher, painting the world in gold. Dewdrops sparkled on the grass, untouched and shimmering. A quiet breeze whispered through the garden, stirring petals and rustling leaves. Children laughed in the distance. A gardener knelt, planting seeds with care. He paused to watch a butterfly glide past. Nature pulsed gently with life. Nearby, a squirrel dashed along a fence, vanishing into the trees. Morning unfolded slowly, wrapped in sound and light.""",

    """A dog barked excitedly in the yard, chasing its tail in endless circles. Its owner laughed, sipping coffee on the porch. Morning light spilled across the lawn, casting long shadows. A bird landed nearby, ignored by the playful pup. The dog's fur gleamed in the sun. Across the street, a jogger waved. The mail truck rolled by with a rumble, and the dog barked again. A cat lounged on the fence, unimpressed. The owner tossed a ball, and the chase began. Laughter rang out again. The world felt light, full of small joys. Somewhere nearby, a lawnmower buzzed into action.""",

    """She brewed coffee slowly, savoring the rich aroma that filled the quiet room. Sunlight streamed through the window, casting patterns on the table. She opened a well-worn book, its pages soft from years of reading. Birds sang outside. The first sip of coffee was perfect—warm and bold. She underlined a sentence with a pencil, thoughtful. The house remained still. A breeze stirred the curtains. A cat stretched across the rug. Time passed without notice. She paused her reading to write a few lines in her journal. The morning passed gently, page by page, word by word, moment by peaceful moment.""",

    """The library was nearly silent, filled with the scent of paper and old wood. Shelves stretched high, packed with knowledge. A student flipped pages carefully, highlighter in hand. Footsteps echoed now and then. Light filtered through stained glass, painting rainbows on the carpet. A librarian sorted books methodically. Somewhere, a printer hummed. A group whispered near the history section. Outside, rain tapped lightly on the windows. A boy scribbled notes in a worn notebook. The clock ticked on, steady and soft. In this quiet world, stories waited to be found. Knowledge lingered in the air like a whispered invitation to think.""",

    """He ran at sunrise, breath visible in the cold air. The street was empty, quiet. His shoes struck the pavement rhythmically. Trees stood still in the fog. Each breath was a push forward. His muscles burned, but he welcomed the ache. A car passed slowly. He nodded at another runner. Birds began to stir in the trees. The horizon glowed faintly. Step after step, he felt lighter. Worries faded behind him. A dog barked in a distant yard. He reached the park and slowed, heart pounding. The city was waking. He stretched under a tree, sweat on his brow, ready to begin.""",

    """Runners gathered at the park, stretching and talking quietly. The sky was gray, but spirits were high. A whistle blew, and the group began moving as one. Shoes thudded against gravel. Water bottles rattled. Breath came in unison. Trees blurred past. A coach barked encouragement. Some lagged, others surged ahead. Determination showed on every face. One runner tripped, but quickly rose. A dog barked from the sidelines. Cheers erupted from a small crowd. The finish line drew near. With final effort, they sprinted. Sweat flew. Hearts raced. Applause echoed. Medals clinked. Smiles spread. Tired but proud, the runners caught their breath together.""",

    """The kitchen smelled of cinnamon and vanilla. Dough was rolled on the counter. Hands moved with practiced ease. Butter sizzled in a pan. The oven glowed warm. A child peeked over the table’s edge. Flour dusted the air. The timer beeped. Cookies baked to golden perfection. A cat meowed, weaving between legs. Laughter filled the room. Plates clattered. A pie cooled on the sill. The radio played soft jazz. Tea steeped beside the stove. A breeze fluttered the curtains. The table was set with care. Dinner simmered on the stove. This kitchen, full of sounds and smells, felt like the heart of home.""",

    """The chef sharpened his knife carefully, preparing for dinner service. Flames flared under pans. Orders rang out. The kitchen moved with practiced chaos. Garlic hit hot oil, releasing fragrance. Steam rose in clouds. A bell chimed. Plates were assembled like art. He wiped sweat from his brow. Behind him, staff plated pasta, grilled meat, delicate desserts. Timing was everything. He tasted the sauce—perfect. The head waiter appeared, nodding approval. Outside, guests laughed and sipped wine. The rhythm continued: slice, sear, plate, repeat. The chef didn’t stop. In this heat, under pressure, he thrived. Dinner was served, delicious and precisely timed.""",

    """Rain fell steadily outside as she wrote in her journal. The lamp cast a golden glow across the desk. Her pen moved quickly, words flowing with emotion. Pages turned. A teacup steamed nearby. Wind whistled through cracks in the window. Thunder rumbled gently. She paused, staring out at the gray world. Memories stirred—quiet walks, old songs, unread letters. She wrote more, slower now. Each word was a release. The room smelled faintly of lavender. A candle flickered on the shelf. Time blurred. Her cat purred softly on the bed. As the storm raged on, she kept writing, steady and unshaken.""",
]


def create_document_term_matrix(documents):
    # Pre process all words in the documents to save time
    processed = []
    for i, doc in enumerate(documents):
        words = doc.split()
        words = [word.lower() for word in words]
        words = [word.strip(".,()!?") for word in words]
        words = [word for word in words if word]
        processed.append(words)

    # Get a list of unique words
    unique_words = set()
    for words in processed:
        unique_words.update(words)

    unique_words = list(unique_words) # This is our x-axis
    unique_words.sort() # Sort the words to maintain consistency

    document_term_matrix = [[0 for _ in unique_words] for _ in documents]

    # For each document have a frequency count of each word
    for i, words in enumerate(processed):
        for word in unique_words:
            document_term_matrix[i][unique_words.index(word)] = words.count(word)

    return document_term_matrix, unique_words


def singular_value_decomposition(matrix):
    # Convert the document-term matrix to a NumPy array
    matrix = np.array(matrix)

    # Perform Singular Value Decomposition
    U, S, Vt = np.linalg.svd(matrix, full_matrices=False)

    # S is returned as a 1D array, convert it to a diagonal matrix
    S = np.diag(S)

    return U, S, Vt


def reconstruct_matrix(U, S, Vt, k=10):
    # Keep only the top k singular values and corresponding vectors
    U_k = U[:, :k]
    S_k = S[:k, :k]
    Vt_k = Vt[:k, :]
    # Reconstruct the original matrix from U, S, and Vt
    reconstructed_matrix = np.dot(U_k, np.dot(S_k, Vt_k))

    # Bit of post processing to round the values to the nearest integer + to integers
    for i in range(len(reconstructed_matrix)):
        for j in range(len(reconstructed_matrix[i])):
            reconstructed_matrix[i][j] = int(round(reconstructed_matrix[i][j]))

    return reconstructed_matrix


if __name__ == "__main__":
    # Example usage
    document_term_matrix, unique_words = create_document_term_matrix(DOCUMENTS)
    print("Document-Term Matrix:")
    for row in document_term_matrix:
        print(row)

    U, S, V = singular_value_decomposition(document_term_matrix)

    res = reconstruct_matrix(U, S, V)

    print("\nReconstructed Matrix:")
    for row in res:
        print(row)

    # For each document show the important words
    important_words = []
    for i, row in enumerate(res):
        print(f"\nDocument {i + 1} important words:")
        for j, count in enumerate(row):
            if count > 0:
                important_words.append((count, unique_words[j]))
                print(f"Word: {unique_words[j]}, Count: {count}")
