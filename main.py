#!/usr/bin/python
# -*- coding: utf-8 -*-import socket
from multiprocessing import Process, Pool
import numpy as np

def element(index, A, B, res):
    glodal res
    i, j = index
    res = 0
    N = len(A[0]) or len(B)
    for k in range(N):
        res += A[i][k] * B[k][j]
    return res


matrix_a = np.array([1,2,3],[4,5,6])
matrix_b = np.array([7,8],[9,10],[11,12])

def main():

p1 = Process(target=element, args=[(0, 0), matrix_a, matrix_b, res])
p1.start()
p1.join()

print(res)

if __name__ == "__main__":
    main()