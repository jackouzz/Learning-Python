#!/user/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

#map，reduce混合用法示范
def str2float(s):
    L1=s[:s.index('.')]
    L2=s[s.index('.')+1:]
    L2=L2[::-1]
    print(L1)
    print(L2)
    def fn(x, y):
        return x * 10 + y
    def char2num(k):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[k]
    def fm(x,y):
        return x * 0.1 + y
    return reduce(fn,map(char2num,L1)) + reduce(fm,map(char2num,L2))*0.1

#reduce用法示范
def prod(L):
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
    #ShowMap()
    #print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
    print('str2float(\'123.456\') =', str2float('123.456'))

    return

main()

