'''
Created on 24 Mar 2015

@author: Dean
'''
import numpy as np
from timeit import default_timer as timer
from numbapro import vectorize

@vectorize(["int16(int16, int16)"], target = 'cpu')
def VectorAdd(a,b):
    return a+b

def main():
    N = 32000000
    
    A = np.ones(N, dtype=np.int16)
    B = np.ones(N, dtype=np.int16)
    #C = np.zeros(N, dtype=np.int16)
    
    start = timer()
    C = VectorAdd(A, B)
    VectorAdd_time = timer() - start
    
    print("c[:5] = " + str(C[:5]))
    print("c[-5:] = " + str(C[-5:]))
    print("VectorAdd took %f seconds" % VectorAdd_time)
    
if __name__ == '__main__':
    main()