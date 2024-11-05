import numpy as np
x=np.array([0,1])      # input
w=np.array([0.5,0.5])  # weight
# b=np.array([0.2,0.2])  
b=-0.7   # bias
print(x*w)
print(np.sum(x*w))
print(np.sum(w*x)+b)