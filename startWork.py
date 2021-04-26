#启动VMware 地址：E:\soft\vmware.exe
import os

#启动软件
def open_app(app_dir):
    os.startfile(app_dir)
# open_app("E:\\soft\\vmware.exe")

def a ():
    for i in range(1,10) :
        yield i

result, candidates = list(), [a()]

"""
@param N: That means you should return the N-th magical number.
@param A: Parameter A.
@param B: Parameter B.
@return: Return the N-th magical number. 
"""


def nthMagicalNumber( N, A, B):
    # Write your code here.
    x = abs(A - B)
    if A >= B:
        x = A-B
    else:
        x = B-A
        A = B
    i = 0
    num = 0
    while N != i :
        num += 1
        s = num % A
        if s == 0 or s == x:
            i += 1
    return num


def aplusb( a, b):
    # write your code here
    a &= 0xFFFFFFFF
    b &= 0xFFFFFFFF
    while b != 0:
        carry = a & b
        a ^= b
        b = ((carry) << 1) & 0xFFFFFFFF
    return a if a < 0x80000000 else ~(a ^ 0xFFFFFFFF)

aplusb(a=4,b=5)