#!/user/bin/env python3
# -*- coding: utf-8 -*-

def triangles(max):
    n=0
    i=0
    L=[1]
    while n<max :
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]
        n=n+1

    return

def Display():
    print('Hello World!')
    name = input('请输入你的名字：')
    print('Hello', name, '!')

    return

def main():
    #Display()

    for g in triangles(7):
        print (g)

    return

main()

