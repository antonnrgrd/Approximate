import os
from linear_algebra import *
def main():
    linear_algebra = MatrixOperators(generate_report = True, verbose = False)
    linear_algebra.matrix_mult(np.random.rand(2,20),np.random.rand(20,2))
    
    
if __name__ == '__main__':
    main()
