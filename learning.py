#!/user/bin/env python3
# -*- coding: utf-8 -*-

#生成杨辉三角形
def triangles():
    i=0
    L=[1]
    while True :
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]

    return

def Display():
    print('Hello World!')
    name = input('请输入你的名字：')
    print('Hello', name, '!')

    return

def main():
    #Display()
    n=0
    for g in triangles():
        print (g)
        n=n+1
        if n == 11 :
            break

    return

main()

