import os
import linear_algebra 
def main():
    linear_algebra = MatrixOperators(generate_report = True, verbose = False)
    linear_algebra.matrix_mult(np.rand(2,3),np.rand(3,2))
    
if __name__ == '__main__':
    main()
