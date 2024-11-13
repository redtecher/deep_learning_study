import sys,os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
from common import twolayernet

if __name__=='__main__':
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True,one_hot_label=True)
    print(x_train.shape)  #训练集图像
    print(t_train.shape)  #训练集tag
    print(x_test.shape)   #测试集图像
    print(t_test.shape)   #测试集tag
    train_loss_list = []  
    iters_num = 10000     
    train_size = x_train.shape[0]  # 60000
    batch_size = 100
    learning_rate = 0.2
    network = twolayernet.TwoLayerNet(input_size=784, hidden_size=100, output_size=10)
    for i in range(iters_num): # 获取mini-batch
        batch_mask = np.random.choice(train_size, batch_size)
        # print(batch_mask) 
        x_batch = x_train[batch_mask].astype(int)
        t_batch = t_train[batch_mask].astype(int)
        #样本 100个
        # 计算梯度
        # grad = network.numerical_gradient(x_batch, t_batch) 
        grad = network.gradient(x_batch, t_batch) # 高速版!
        # 更新参数 
        for key in ('W1', 'b1', 'W2', 'b2'): 
            network.params[key] -= learning_rate * grad[key] 
        # 记录学习过程
        loss = network.loss(x_batch, t_batch)
        train_loss_list.append(loss)
        print('第'+str(i)+'次：'+' ')
        print(loss)