# -*- coding: utf-8 -*-
import sys
import os
def main():
    print(sys.platform)
    print(2 ** 100)
    x = 'Spam!'
    print(x * 8)
    print u"这是来自lym\'的问候"
    print "os.getcwd():" + os.getcwd()
    food = [1,"aa",1.2,]
    for i in food:
        print i
    for i in range(10):
        print i
    func(1,10,10)

def func(i,j,k):
    print "first:%s\nsecond:%s\nthired:%s" %(i,j,k)
    if i<0 and j>0 or k>10 :
        print "balalala"
    elif k<10:
        print "hahaha"
    else:
        print "...."
main()
