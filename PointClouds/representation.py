import matplotlib.pyplot as plt

# Tokenise a word into an ortohganal list

sentence = "The cate ate hot pie"

words = sentence.split(" ")

vectors = []

for word in words:
    tokenised = []
    for char in word:
        tokenised.append(ord(char))

    vectors.append(tokenised)


# Plot these points in a 3D space
plt.figure()
ax = plt.axes(projection='3d')
for i in range(0, len(words)):
    ax.scatter(vectors[i][0], vectors[i][1], vectors[i][2], label=words[i])

plt.legend()

plt.show()
