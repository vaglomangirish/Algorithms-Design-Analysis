import argparse
import time
import random
import sys
import math

__author__ = "Mangirish_Wagle"

"""
This Python program can be run as:-

# python MatrixMultiplication <MAXSIZE>

The output would be a 'product_times.csv' with matrix multiplication times of Standard Iterative, Standard Recursive
and Strassens methods, for square matrix sizes which are power of 2, ranging from 1, 2, .... , MAXSIZE.

"""

sys.setrecursionlimit(500000)


class MatrixMultiplication:
    """
    Class that performs Matrix Multiplication using Standard iterative, recursive and Strassens Method.
    """

    def __init__(self):
        return

    @classmethod
    def generate_random_matrix(cls, dim):
        """
        Function to generate a random square dim * dim matrix.

        Data Structure used for Matrix is List of Lists in python:-

        list  of lists:- [ [ 1, 2 ], [ 3, 4 ] ] represents:-

        [ 1, 2 ]
        [ 3. 4 ]

        :param dim: size of row/ column
        :return: dim * dim matrix of floating point elements.
        """

        matrix = []

        for x in xrange(0, dim):
            elem_matrix = []
            for y in xrange(0, dim):
                elem_matrix.append(random.uniform(1.0, 9.0))

            matrix.append(elem_matrix)

        return matrix

    @classmethod
    def print_matrix(cls, matrix):
        """
        Function to print matrix in a legible form.
        :param matrix: Matrix to print.
        :return: Nothing
        """

        for elem in matrix:
            print(str(elem))

    @classmethod
    def add(cls, matrix1, matrix2):
        """
        Function to add two matrices.
        :param matrix1:
        :param matrix2:
        :return: Sum Matrix
        """

        result = []

        for i in range(len(matrix1)):
            submat1, submat2 = matrix1[i], matrix2[i]
            result.append([(x+y) for x, y in zip(submat1, submat2)])

        return result

    @classmethod
    def subtract(cls, matrix1, matrix2):
        """
        Function to subtract two matrices.
        :param matrix1:
        :param matrix2:
        :return: Result matrix after subtraction.
        """

        result = []

        for i in range(len(matrix1)):
            submat1, submat2 = matrix1[i], matrix2[i]
            result.append([(x-y) for x, y in zip(submat1, submat2)])

        return result

    @classmethod
    def divide_matrix(cls, matrix):
        """
        Function to divide matrix into 4 equal sub matrices.
        :param matrix: Matrix to divide.
        :return: Four sub matrices.
        """

        m11 = []
        m12 = []
        m21 = []
        m22 = []
        half_point = len(matrix)/2

        for x in xrange(len(matrix)):
            if x < half_point:
                m11.append(matrix[x][:half_point])
                m12.append(matrix[x][half_point:])
            else:
                m21.append(matrix[x][:half_point])
                m22.append(matrix[x][half_point:])

        return m11, m12, m21, m22

    @classmethod
    def standard_multiply(cls, matrix1, matrix2):
        """
        Function that carries out standard iterative multiplication of two matrices.
        :param matrix1:
        :param matrix2:
        :return: Product matrix.
        """

        result_matrix = []

        for x in xrange(0, len(matrix1)):
            sub_matrix = []
            for y in xrange(0, len(matrix2)):
                prod_sum = 0.0
                for z in xrange(0, len(matrix2)):
                    prod_sum = prod_sum + (matrix1[x][z] * matrix2[z][y])
                sub_matrix.append(prod_sum)
            result_matrix.append(sub_matrix)

        return result_matrix

    @classmethod
    def standard_multiply_recursive(cls, matrix1, matrix2):
        """
        Function that carries out standard recursive multiplication of two matrices.
        :param matrix1:
        :param matrix2:
        :return: Product Matrix
        """

        result = []
        # Base condition: If matrix contains just 1 element, return the result with simple multiplication.
        if len(matrix1) == 1 and len(matrix2) == 1:
            submat = list()
            submat.append(matrix1[0][0] * matrix2[0][0])
            result.append(submat)
        else:

            # Divide
            a11, a12, a21, a22 = cls.divide_matrix(matrix1)
            b11, b12, b21, b22 = cls.divide_matrix(matrix2)

            # Initializing four quadrant matrices of the result matrix
            c11 = []
            c12 = []
            c21 = []
            c22 = []

            # Conquer
            c11 = cls.add(cls.standard_multiply_recursive(a11, b11), cls.standard_multiply_recursive(a12, b21))
            c12 = cls.add(cls.standard_multiply_recursive(a11, b12), cls.standard_multiply_recursive(a12, b22))
            c21 = cls.add(cls.standard_multiply_recursive(a21, b11), cls.standard_multiply_recursive(a22, b21))
            c22 = cls.add(cls.standard_multiply_recursive(a22, b22), cls.standard_multiply_recursive(a21, b12))

            # Combine
            result = cls.combine_matrices(c11, c12, c21, c22)

        return result

    @classmethod
    def strassens_multiply(cls, matrix1, matrix2):
        """
        Function that carries out Strassens recursive multiplication of two matrices.
        :param matrix1:
        :param matrix2:
        :return: Product Matrix.
        """

        result = []
        # Base condition: If matrix contains just 1 element, return the result with simple multiplication.
        if len(matrix1) == 1 and len(matrix2) == 1:
            submat = list()
            submat.append(matrix1[0][0] * matrix2[0][0])
            result.append(submat)
        else:
            # Divide
            a11, a12, a21, a22 = cls.divide_matrix(matrix1)
            b11, b12, b21, b22 = cls.divide_matrix(matrix2)

            # Conquer
            # (A11 + A22)*(B11 + B22)
            m1 = cls.strassens_multiply(cls.add(a11, a22), cls.add(b11, b22))

            # (A21 + A22) * B11
            m2 = cls.strassens_multiply(cls.add(a21, a22), b11)

            # A11 * (B12 - B22)
            m3 = cls.strassens_multiply(a11, cls.subtract(b12, b22))

            # A22 * (B21 - B11)
            m4 = cls.strassens_multiply(a22, cls.subtract(b21, b11))

            # (A11 + A12) * B22
            m5 = cls.strassens_multiply(cls.add(a11, a12), b22)

            # (A21 - A11) * (B11 + B12)
            m6 = cls.strassens_multiply(cls.subtract(a21, a11), cls.add(b11, b12))

            # (A12 - A22) * (B21 + B22)
            m7 = cls.strassens_multiply(cls.subtract(a12, a22), cls.add(b21, b22))

            # Applying Strassens formulae.
            c11 = cls.add(cls.add(m1, m7), cls.subtract(m4, m5))
            c12 = cls.add(m3, m5)
            c21 = cls.add(m2, m4)
            c22 = cls.add(cls.add(m1, m6), cls.subtract(m3, m2))

            # Combine
            result = cls.combine_matrices(c11, c12, c21, c22)

        return result

    @classmethod
    def combine_matrices(cls, mat1, mat2, mat3, mat4):
        """
        Function that combines the 4 matrices into one matrix.
        :param mat1:
        :param mat2:
        :param mat3:
        :param mat4:
        :return: Combined Matrix.
        """

        result = []
        base = len(mat1)
        for i in range(base * 2):
            if i < base:
                sub_matrix = mat1[i % base] + mat2[i % base]
            else:
                sub_matrix = mat3[i % base] + mat4[i % base]

            result.append(sub_matrix)

        return result

    @classmethod
    def plot_graph(cls, data):
        print("To be implemented")


"""
Main method
"""
if __name__ == '__main__':

    # Parsing command line arguments
    argparser = argparse.ArgumentParser()
    argparser.add_argument('MAXSIZE', help='Maximin Size of square matrix (2^k) to be considered.')
    args = argparser.parse_args()

    sampling_count = 10

    # Preparing to write the results to a csv file.
    f = open("product_times.csv", "w")
    f.write("Size,Standard_Iterative,Standard_Recursive,Strassens\n")

    for x in xrange(int(args.MAXSIZE)):
        matsize = int(math.pow(2, x))
        if matsize <= int(args.MAXSIZE):
            print("For Matrix Size: {}".format(matsize))

            matmul = MatrixMultiplication()
            matrix1 = matmul.generate_random_matrix(matsize)
            matrix2 = matmul.generate_random_matrix(matsize)

            # Standard Iterative
            stdsum = 0.0
            for itr in xrange(sampling_count):
                # print("Standard Iteration {}".format(itr))
                std_start_time = time.time()
                resultstd = matmul.standard_multiply(matrix1, matrix2)
                std_end_time = time.time()
                stdsum = stdsum + (std_end_time - std_start_time)

            std_time = (stdsum*1000.0)/float(sampling_count)

            # Standard Recursive
            stdsumrec = 0.0
            for itr in xrange(sampling_count):
                # print("Standard Iteration {}".format(itr))
                std_rec_start_time = time.time()
                resultstdrec = matmul.standard_multiply_recursive(matrix1, matrix2)
                std_rec_end_time = time.time()
                stdsumrec = stdsumrec + (std_rec_end_time - std_rec_start_time)

            std_rec_time = (stdsumrec*1000.0)/float(sampling_count)

            # Strassens Recursive
            strsum = 0.0
            for itr in xrange(sampling_count):
                # print("Strassens Iteration {}".format(itr))
                strass_start = time.time()
                resultstrass = matmul.strassens_multiply(matrix1, matrix2)
                strass_end = time.time()
                strsum = strsum + (strass_end - strass_start)

            str_time = (strsum*1000.0)/float(sampling_count)

            # INFO: Uncomment the following lines to view the matrix output results.
            # These have been kept commented so that the output is clean and readable with just the content necessary.
            """
            print("Result by standard multiplication:-")
            matmul.print_matrix(resultstd)

            print("Result by standard recursive multiplication:-")
            matmul.print_matrix(resultstdrec)

            print("Result by strassen multiplication:-")
            matmul.print_matrix(resultstrass)
            """

            # Results added to csv file.
            f.write("{},{},{},{}\n".format(matsize, std_time, std_rec_time, str_time))

            print("Time for standard: {} milliseconds".format(std_time))
            print("Time for standard recursive: {} milliseconds".format(std_rec_time))
            print("Time for strassens: {} milliseconds".format(str_time))
        else:
            break
    f.close()



