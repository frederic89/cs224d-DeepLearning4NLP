import numpy as np
import matplotlib.pyplot as plt


words = ["I", "like", "enjpy", "deep", "learning", "NLP", "flying", "."]
X = np.array([[0, 2, 1, 0, 0, 0, 0, 0], [2, 0, 0, 1, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 1, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 0]])
U, s, Vh = np.linalg.svd(X, full_matrices=False)

for i in range(len(words)):
    plt.plot(U[i, 0], U[i, 1], 'o')
    plt.text(U[i, 0], U[i, 1], words[i])
plt.axis([-0.8, 0.2, -1, 1]) # X轴范围,Y轴范围
plt.show()