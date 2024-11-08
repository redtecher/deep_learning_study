# 神经网络的学习
# 从数据中学习
import numpy as np
import sys,os
sys.path.append(os.pardir)
from dataset.mnist import load_mnist
#均方误差 E=1/2 *sigma((yk-tk)²)
def mean_squared_error(y, t): 
    return 0.5 * np.sum((y-t)**2)


#交叉熵误差 E=-sigma(tk*log(yk))
# def cross_entropy_error(y, t): 
#     delta = 1e-7
#     return -np.sum(t * np.log(y + delta))

def cross_entropy_error(y, t): 
    print(y.ndim)
    if y.ndim == 1: 
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    batch_size = y.shape[0] 
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size


def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True,one_hot_label=True)
    return (x_train, t_train), (x_test, t_test)

if __name__=='__main__':
    # y = [0.1, 0.05, 0.6, 0.0 , 0.05, 0.1, 0  , 0.1, 0.0, 0.0]
    # t = [0  , 0   ,  1  , 0  , 0   , 0  , 0  ,  0 , 0  , 0  ] 
    # # result =mean_squared_error(np.array(y),np.array(t))
    # result = cross_entropy_error(np.array(y),np.array(t))
    (x_train, t_train), (x_test, t_test)=get_data()
    train_size = x_train.shape[0]
    print(train_size)
    batch_size = 10
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask] 
    t_batch = t_train[batch_mask]
    print(x_batch)
    print(t_batch)
    