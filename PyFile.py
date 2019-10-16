from ctypes import *
import os

def getClib():
    so_file = ''
    # Search for file path
    for fname in os.listdir():
        if 'so' in fname.split('.'):
            so_file = os.path.abspath(fname)
            break
    
    # Calling the C lib in Python
    print("Opening the C Lib: ", so_file)
    if so_file != '':
        utilLib = CDLL(so_file)
        return utilLib
    else:
        print("Error: Could not find the .SO file")
    


def randomFunction():
    # Calling Random function from the C library
    print("Calling the random function ...")
    retVal = Clib.randomFunction()
    print("Return Value: ", retVal)


def fun1():
    print('')
    # Calling the fun1
    print("Calling the fun1 ...")

    x = 1
    y = c_int(2)
    z = c_int(3)
    # Defining the arg type for the input fun1 
    Clib.fun1.argtypes = [c_int, POINTER(c_int), POINTER(c_int)]
    Clib.fun1.restype  = c_int
    retVal = Clib.fun1(x, byref(y), byref(z))
    print("Return Value: ", retVal)


def fun11():
    print('')
    # Calling the fun11
    print("Calling the fun11 ...")

    x = c_double(1.2)
    y = c_double(2.0)
    # Defining the arg type for the input fun1 
    Clib.fun1.argtypes = [c_double, POINTER(c_double)]
    Clib.fun11.restype  = c_int
    retVal = Clib.fun11(x, byref(y))
    print("Return Value: ", retVal)


def fun12():
    print('')
    # Calling the fun12
    print("Calling the fun12 ...")

    xlen = 5
    x = (c_double*xlen)()
    for i in range(xlen):
        x[i] = i
    # Defining the arg type for the input fun1 
    Clib.fun1.argtypes = [c_double*xlen]
    Clib.fun11.restype  = c_int
    retVal = Clib.fun12(x, c_int(xlen))
    print("Return Value: ", retVal)



def fun13():
    print('')
    # Calling the fun13
    print("Calling the fun13 ...")

    string = b"abc"
    
    # Defining the arg type for the input fun13
    Clib.fun1.argtypes = [c_char_p]
    Clib.fun11.restype  = c_int
    retVal = Clib.fun13(string)
    print("Return Value: ", retVal)





def fun2(sockfd, flagWrite, nDblWrite, simTimWrite, dblValWrite):

    print('')
    # Calling the fun22
    print("Calling the fun2 ...")

    # Defining the variable type
    sockfd = c_int(sockfd)
    flaWri = c_int(flagWrite)
    flaRea = c_int()
    
    simTimRea = c_double()
    simTimWri = c_double(simTimWrite)
    
    nDblWri = c_int(nDblWrite)
    dblValWri = (c_double*nDblWri.value)()
    
    nDblRea = c_int()
    dblValRea = (c_double*nDblRea.value)()
    
    for i in range(nDblWri.value):
        dblValWri[i] =  dblValWrite[i]

    # Defining the arg type for the input fun1 
    Clib.fun1.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_double), c_double*nDblWri.value, POINTER(c_double), c_double*nDblRea.value]
    Clib.fun11.restype  = c_int

    # Return Value from the function
    retVal = Clib.fun2( byref(sockfd), byref(flaWri), byref(flaRea), byref(nDblWri), byref(nDblRea), byref(simTimWri), dblValWri, byref(simTimRea), dblValRea)
    print("Return Value: ", retVal)

    return retVal


if __name__ == "__main__":
    # Calling the C Library
    Clib = getClib()

#    sockfd = 505
#    flagWrite = 3
#    nDblWrite = 2
#    simTimWrite = 4
#    dblValWrite = list(range(nDblWrite))
#
#    fun2(sockfd, flagWrite, nDblWrite, simTimWrite, dblValWrite)

    fun13()
