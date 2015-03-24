'''
Created on 24 Mar 2015

@author: Dean
'''
import numpy as np
from timeit import default_timer as timer
from numbapro import vectorize

@vectorize(["float32(float32, float32)"], target = 'gpu')
def VectorAdd(a,b):
    return a+b

def main():
    N = 32000000
    
    A = np.ones(N, dtype=np.float32)
    B = np.ones(N, dtype=np.float32)
    C = np.zeros(N, dtype=np.float32)
    
    start = timer()
    C = VectorAdd(A, B)
    VectorAdd_time = timer() - start
    
    print("c[:5] = " + str(C[:5]))
    print("c[-5:] = " + str(C[-5:]))
    print("VectorAdd took %f seconds" % VectorAdd_time)
    
if __name__ == '__main__':
    main()