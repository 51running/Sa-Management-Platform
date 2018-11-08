#!/bin/env python
#coding:utf-8
import os

f = open('user.txt')

'''
# readline 一行行读取，每行的数据类型为字符串
num = 1
while True:
    line = f.readline()
    print repr(line)     #打印原始数据，eg: 'wd:123456\n' 类型为字符串且带了\n 这个字符
    print "%s-->%s" %(num,line.rstrip("\n")) #每输出一行，前面加个行号，line.rstrip("\n")是把\n干掉
    num = num + 1
    if len(line) == 0:
        break;
'''
# 读取所有，并将结果存为字典
dict = {}
content = f.readlines()
f.close()
#print content
for user in content:
    #print user.rstrip("\n")
    #print user.rstrip("\n").split(":")
    name = user.rstrip("\n").split(":")[0]
    #print name
    dict[name] = user.rstrip("\n").split(":")[1]
    #sys.exit(1)
#print dict

# 判断用户的帐号密码，都ok提示登录成功，否则失败
count = 0
while  True:
    count = count + 1
    if count > 3:
        print "对不起，您输入错误过多，账户已经锁定，请联系管理员"
        break
    name = raw_input("请输入姓名：").strip()
    if name not in dict:
        print "用户不存在，请重新输入"
        continue
    password = raw_input("请输入密码：").strip()
    if password != dict[name]:
        print "密码输入有误"
        continue
    else:
        print "恭喜你，登录成功"
        break
