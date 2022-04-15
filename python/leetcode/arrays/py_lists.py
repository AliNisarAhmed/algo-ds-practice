import sys


def py_list_mem(n):
    data = []
    for k in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
        data.append(None)
    for k in range(n):
      a = len(data)
      b = sys.getsizeof(data)
      print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
      data.pop()

py_list_mem(10)


def py_list_cap(n):
    data = []
    size_old = 0
    for k in range(n):
        size = sys.getsizeof(data)
        if size != size_old:
            print(len(data))
        size_old = size
        data.append(None)


py_list_cap(10)
