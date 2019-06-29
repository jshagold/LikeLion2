# -*- coding: utf-8 -*-


a = int(input('input a : '))
b = int(input("input b : "))
c = int(input("input c : "))



if(a > b) and (b > c) :
    print a,b,c
elif(a > b) and (b < c) and (a > c) :
    print(a,c,b)
elif(b > a) and (a > c) :
    print(b,a,c)
elif(b > a) and (a < c) and (b > c) :
    print(b,c,a)
elif(c > a) and (a > b) :
    print(c,a,b)
elif(c > a) and (b > a) and (c > b) :
    print(c,b,a)