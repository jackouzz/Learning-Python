#!/user/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

def prod(L):
    print(L)
    def fx(x,y):
        return x*y

    return reduce(fx,L)

#字符串首写字母大写其余小写
def normalize(name):
    return name.capitalize()

#演示map()用法，将一组英文字符串全部改为首字母大写，其余字母小写
def ShowMap():
    L = ['adam', 'LISA', 'barT']
    L2 = list(map(normalize, L))
    print(L2)
    print(L)

    return

#生成杨辉三角形
def triangles():
    i=0
    L=[1]
    while True :
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]

    return

#调用杨辉三角形函数示范
def Showtriangles():
    n = 0
    for g in triangles():
        print (g)
        n=n+1
        if n == 11 :
            break

    return

def Display():
    print('Hello World!')
    name = input('请输入你的名字：')
    print('Hello', name, '!')

    return

def main():
    #Display()
    #Showtriangles()
    ShowMap()
    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

    return

main()

