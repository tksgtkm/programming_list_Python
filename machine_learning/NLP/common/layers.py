from common.config import GPU

if GPU:
    import jax.numpy as np
    from jax import random
    key = random.PRNGKey(42)
else:
    import numpy as np
    
from common.functions import softmax, cross_entropy_error

class MatMul:

    def __init__(self, W):
        self.params = [W]
        self.grads = [np.zeros_like(W)]
        self.x = None

    def forward(self, x):
        W, = self.params
        out = np.dot(x, W)
        self.x = x
        return out
    
    def backward(self, dout):
        W, = self.params
        dx = np.dot(dout, W.T)
        dW = np.dot(self.x.T, dout)
        if GPU:
            self.grads[0] = self.grads[0].at[...].set(dW)
        else:
            self.grads[0][...] = dW
        return dx
    
class SoftmaxWithLoss:

    def __init__(self):
        self.params, self.grads = [], []
        self.y = None
        self.t = None

    def forward(self, x, t):
        self.t = t
        self.y = softmax(x)

        if self.t.size == self.y.size:
            self.t = self.t.argmax(axis=1)

        loss = cross_entropy_error(self.y, self.t)

        return loss
    
    def backward(self, dout=1):
        batch_size = self.t.shape[0]

        dx = self.y.copy()
        if GPU:
            dx = dx.at[np.arange(batch_size), self.t].add(-1)
        else:
            dx[np.arange(batch_size), self.t] -= 1
        dx *= dout
        dx = dx / batch_size

        return dx
    
class SigmoidWithLss:

    def __init__(self):
        self.params, self.grads = [], []
        self.loss = None
        self.y = None
        self.t = None

    def forward(self, x, t):
        self.t = t
        self.y = 1 / (1 + np.exp(-x))
        self.loss = cross_entropy_error(np.c_[1 - self.y, self.y], self.t)

        return self.loss
    
    def backward(self, dout=1):
        batch_size = self.t.shape[0]
        dx = (self.y - self.t) * dout / batch_size
        return dx
    
class Embedding:

    def __init__(self, W):
        self.params = [W]
        self.grads = [np.zeros_like(W)]
        self.idx = None

    def forward(self, idx):
        W, = self.params
        self.idx = idx
        out = W[idx]
        return out
    
    def backward(self, dout):
        dW, = self.grads
        if GPU:
            dW = dW.at[...].set(0)
        else:
            dW[...] = 0
            
        if GPU:
            dW.at[self.idx].add(dout)
        else:
            np.add.at(dW, self.idx, dout)
        return None