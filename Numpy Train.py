import numpy as np
import sys
# np.set_printoptions(threshold=sys.maxsize)
a = np.arange(4)#.reshape(3,3)
b = np.array([20,30,40,50]).reshape(2,2)
#print(b)
#print(a)
#print(b-a) # + * (/) if not div by zero
checkBigger = b>=30
print(checkBigger)