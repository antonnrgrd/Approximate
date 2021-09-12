import os
from linear_algebra import *
def main():
    linear_algebra = MatrixOperators(generate_report = True, verbose = False)
    linear_algebra.matrix_mult(np.random.rand(10,10),np.random.rand(10,10))
    
    
if __name__ == '__main__':
    main()
