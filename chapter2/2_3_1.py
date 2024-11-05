#感知机

# 与门
def AND(x1,x2):
    w1,w2,theta = 0.5,0.5,0.7
    tmp = w1*x1+w2*x2
    if(tmp<=theta):
        return 0 
    elif(tmp>theta):
        return 1
    
# 与非门
def NAND(x1,x2):
    w1,w2,theta = -0.5,-0.5,-0.7
    tmp = w1*x1+w2*x2
    if(tmp<=theta):
        return 0 
    elif(tmp>theta):
        return 1
    
# 或门
def OR(x1,x2):
    w1,w2,theta = 0.5,0.5,0.3
    tmp = w1*x1+w2*x2
    if(tmp<=theta):
        return 0 
    elif(tmp>theta):
        return 1

print(OR(0,0))
print(OR(1,0))
print(OR(0,1))
print(OR(1,1))