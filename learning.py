#!/user/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

#装饰器使用
def log(func):
    def wrapper(*args, **kw):
        print('begin call: %s():' % func.__name__)
        func(*args, **kw)
        return print('end call')
    return wrapper

@log
def now():
    print('2015-3-25')

def by_score(t):
    i = t[1]
    print (i)
    return i

def by_name(t):
    i = t[0]
    print (i)
    return i

#判断是否回数
def is_palindrome(n):
    if n < 10 :
        return False
    L=str(n)
    i=0
    for i in range(int(len(L)/2)):
        if L[i] != L[len(L)-i-1]:
            return False
    return True

#map，reduce混合用法示范
def str2float(s):
    L1=s[:s.index('.')]
    L2=s[s.index('.')+1:]
    L2=L2[::-1]

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
def showMap():
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

#调用杨辉三角形函数示范
def showtriangles():
    n = 0
    for g in triangles():
        print (g)
        n=n+1
        if n == 11 :
            break
    return

def display():
    print('Hello World!')
    name = input('请输入你的名字：')
    print('Hello', name, '!')
    return

def main():
    #display()
    #showtriangles()
    #showMap()
    #print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
    #print('str2float(\'123.456\') =', str2float('123.456'))
    #output = filter(is_palindrome, range(9999, 99999))
    #print(list(output))
    #L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    #print(L)
    #L2=sorted(L,key=by_score)
    #print(L2)
    #L2 = sorted(L, key=by_name)
    #print(L2)
    now()

    return

main()