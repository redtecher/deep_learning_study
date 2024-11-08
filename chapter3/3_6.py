# 手写数字识别
# MNIST数据集
import sys,os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image
import pickle
# print(x_train.shape)
# print(t_train.shape)
# print(x_test.shape)
# print(t_test.shape)
def img_show(img): 
    pil_img = Image.fromarray(np.int8(img))
    pil_img.show()

def sigmoid(x):
    x_ravel = x.ravel()  # 将numpy数组展平
    length = len(x_ravel)
    y = []
    for index in range(length):
        if x_ravel[index] >= 0:
            y.append(1.0 / (1 + np.exp(-x_ravel[index])))
        else:
            y.append(np.exp(x_ravel[index]) / (np.exp(x_ravel[index]) + 1))
    return np.array(y).reshape(x.shape)


# def sigmoid(x):
#         return 1/(1+np.exp(-x))

def softmax(a): 
    c = np.max(a)
    exp_a = np.exp(a - c) # 溢出对策 
    sum_exp_a = np.sum(exp_a) 
    y = exp_a / sum_exp_a
    return y 

def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)
    return x_test,t_test

def init_network():
    with open("sample_weight.pkl",'rb') as f:
        network = pickle.load(f)
    return network


def predict(network, x): 
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    a1 = np.dot(x, W1) + b1 
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2 
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3 
    y = softmax(a3)
    return y



if __name__=='__main__':
    
    x,t=get_data()
    network = init_network()
    accuracy_cnt =0
    print(x.shape)
    print(t.shape)
    accuracy_cnt = 0
    for i in range(len(x)):
        y = predict(network=network,x=x[i])
        p = np.argmax(y)
        if p==t[i]:
            accuracy_cnt+=1

    print("Accuracy:"+str(float(accuracy_cnt)/len(x)))


