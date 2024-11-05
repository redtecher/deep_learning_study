# 多层感知机

# note: s1 = x1 not_and x2
#       s2 = x1 or x2
#       y  = s1 and s2
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
    
def XOR(x1,x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    tmp = AND(s1,s2)
    return tmp

if __name__=='__main__':
    print(XOR(0,0))
    print(XOR(1,0))
    print(XOR(0,1))
    print(XOR(1,1))