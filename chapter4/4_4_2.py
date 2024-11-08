import sys,os
sys.path.append(os.pardir)
import numpy as np
from common.functions import softmax,cross_entropy_error
from common.gradient import numerical_gradient
class SimpleNet:
    def __init__(self) -> None:
        self.W = np.random.randn(2,3)

    def predict(self,x):
        return np.dot(x,self.W)
    
    def loss(self,x,t):
        z=self.predict(x)
        y=softmax(z)
        print(z)
        print(y)
        loss = cross_entropy_error(y,t)

        return loss

def f(W):
    return net.loss(x,t)


if __name__=='__main__':
    simplenet = SimpleNet()
    # print(simplenet.W)
    x= np.array([0.6,0.9])
    # print(np.argmax(p))
    t = np.array([0,0,1])
    print(simplenet.loss(x,t))
    dW = numerical_gradient(f,simplenet.W)
    print(dW)
