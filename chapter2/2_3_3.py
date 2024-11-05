import numpy as np
# 与门
def AND(x1,x2):
    x=np.array([x1,x2])      # input
    w=np.array([0.5,0.5])   # weight
    b= -0.7
    tmp = np.sum(w*x)+b
    if(tmp<=0):
        return 0 
    elif(tmp>0):
        return 1
    
def NAND(x1,x2):
    x=np.array([x1,x2])      # input
    w=np.array([-0.5,-0.5])   # weight
    b= 0.7
    tmp = np.sum(w*x)+b
    if(tmp<=0):
        return 0 
    elif(tmp>0):
        return 1

def OR(x1,x2):
    x=np.array([x1,x2])      # input
    w=np.array([0.5,0.5])   # weight
    b= -0.3
    tmp = np.sum(w*x)+b
    if(tmp<=0):
        return 0 
    elif(tmp>0):
        return 1
    
if __name__=='__main__':
    print(OR(0,0))
    print(OR(1,0))
    print(OR(0,1))
    print(OR(1,1))