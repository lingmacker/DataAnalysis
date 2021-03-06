import numpy as np

T = np.array([9, 15, 25, 14, 10, 18, 0, 16, 5, 19, 16, 20])
S = np.array([39, 56, 93, 61, 50, 75, 32, 85, 42, 70, 66, 80])
T = T[:, np.newaxis]
S = S[:, np.newaxis]
X = np.hstack((T, S))
print(X)
co = np.cov(X.T)

# 协方差输出如下
# array([[47.71969697, 122.9469697],
#        [122.9469697, 370.08333333]])
