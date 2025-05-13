import numpy as np

# Dimensional analysis by co-occurence: Latent Semantic Analysis

a = [
    [45, 68, 96],
    [65, 66, 34],
    [71, 16, 54],
    [75, 12, 22],
    [28, 50, 75]
]

az = [
    [-0.5958, 0.9522, 1.2928],
    [0.4141, 0.8778, -0.7730],
    [0.7170, -0.9820, 0.0600],
    [0.9190, -1.1307, -1.1729],
    [-1.4542, 0.2827, 0.5931]
]

vz = [
    [0.6116, -0.2317, 0.7565],
    [-0.5309, -0.8291, 0.7531],
    [-0.5867, 0,5088, 0.6301]
]

uz = [
    [0.5454, 0.0043, 0.5401, 0.6398, -0.0373],
    [0.0806, -0.8356, -0.0203, 0.1224, 0.5291],
    [0.3097, 0.4659, 0.4154, -0.0481, 0.7157],
    [0.6198, 0.0878, -0.2462, 0.7278, -0.1336],
    [-0.4647, 0.2775, -0.6890, 0.2089, 0.4344]
]

sigmaz = [
    [2.9855, 0, 0],
    [0, 24566, 0,],
    [0, 0, 0.9825],
    [0, 0 ,0],
    [0, 0, 0]
]

# First calculate D which is V Σ^2 V∗

D = np.dot(vz, np.dot(np.dot(sigmaz, sigmaz), np.transpose(vz)))

# Then calculate W which is U Σ^2 U∗

W = np.dot(uz, np.dot(np.dot(sigmaz, sigmaz), np.transpose(uz)))

'''These values can then be used to calculate the similarity among entities. The values are relative to each other.'''

print (f"D: {D}")
print (f"W: {W}")
