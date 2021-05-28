import numpy as np
import matplotlib.pyplot as plt

learning_rate = 0.01
n_iters = 10000

X = np.array([1,2,3,4,5])
y = np.array([6,15,4,2,21])

params = [0,0]

# y = mx + b
# params = [m, b]

def cost(X, y, params):
    n = len(y)
    h = params[0] * X + params[1]
    return 1/n * np.sum((h - y)**2)


def gradient_descent(X, y, params, learning_rate, n_iters):
    n = len(y)
    cost_history = np.zeros((n_iters,3))

    for i in range(n_iters):
        m = params[0] - 2/n * np.dot(X, params[0]*X + params[1] - y) * learning_rate
        b = params[1] - 2/n * np.sum(params[0]*X + params[1] - y) * learning_rate
        params[0] = m
        params[1] = b

        cost_history[i] = [m,b,cost(X, y, params)]

    return (cost_history, params)



lin_model = gradient_descent(X, y, params, learning_rate, n_iters)

history = [lin_model[0][i][2] for i in range(len(lin_model[0]))]

print (lin_model[1][0], lin_model[1][1])

plt.figure()
plt.scatter(X,y)
plt.plot(X, lin_model[1][0]*X + lin_model[1][1])
plt.show()

