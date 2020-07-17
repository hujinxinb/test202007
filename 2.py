
# -*- coding:utf-8 -*-
import sys
import json
import numpy as np
import os
import codecs

import sys
reload(sys)
sys.setdefaultencoding('utf8')

f = open('./test.txt','r')
data_set = json.loads(f.read());


for person in data_set.keys():
    print str(person)

#深拷贝
#b = [1,2,2,4,3,2,1,6,8]
#c = b[:]

#先确定特殊情况  多申请变量，有时候逆序处理更好  for i in range(len(strs)-1, -1, -1)

#for i in range(len(strs))

#地板除//, mid=(start+end)//2
s
# c=[0 for i in range(10)]     for i in range(10): c[i]=int(input())
#列表：c=[]  c.sort()  c.append()  del c[2]//小心，del掉后序号就不能加1  c.reverse()  c.count(value)  c.index(value)  c.insert(index,value)
# c[:4]即到c[3]为止 c[4:]即c[4]到最后 c[1:5:2] c[::2]

#二维数组（列表）： [[] for i in range(4)] 或[[0]*5 for i in range(4)] 或np.zero((4,5))
#只有np可以用x[:,0] x[:,m:n]等

#字符串转列表 str="hi hello world" str.split(" ")即["hi","hello","world"] 如果str是"hihelloworld"，结果是["hihelloworld"]
#字符串： 都可以找子串 str.count(value)  str.find(value)找到第一个index，找不到返回-1  str.replace(old,new) 反转用str[::-1]
#in not in  str.lower()  str.upper()  str[:-3]开始到倒4  str[-3:]倒3到最后

#if __name__ == '__main__':


# class TreeNode(object):
#     def __init__(self, data=0, left=0, right=0):
#         self.data = data
#         self.left = left
#         self.right = right
#
#
# class BTree(object):
#     def __init__(self, root=0):
#         self.root = root
#
#     def preOrder(self, treenode):
#         if treenode is 0:
#             return
#         print(treenode.data)
#         self.preOrder(treenode.left)
#         self.preOrder(treenode.right)
#
#     def inOrder(self, treenode):
#         if treenode is 0:
#             return
#         self.inOrder(treenode.left)
#         print(treenode.data)
#         self.inOrder(treenode.right)
#
#     def postOrder(self, treenode):
#         if treenode is 0:
#             return
#         self.postOrder(treenode.left)
#         self.postOrder(treenode.right)
#         print(treenode.data)
#
#
# if __name__ == '__main__':
#     n1 = TreeNode(data=1)
#     n2 = TreeNode(2, n1, 0)
#     n3 = TreeNode(3)
#     n4 = TreeNode(4)
#     n5 = TreeNode(5, n3, n4)
#     n6 = TreeNode(6, n2, n5)
#     n7 = TreeNode(7, n6, 0)
#     n8 = TreeNode(8)
#     root = TreeNode('root', n7, n8)
#
#     bt = BTree(root)
#     print("preOrder".center(50, '-'))
#     print(bt.preOrder(bt.root))
#
#     print("inOrder".center(50, '-'))
#     print (bt.inOrder(bt.root))
#
#     print("postOrder".center(50, '-'))
#     print (bt.postOrder(bt.root))
#
#
# #单链表
# class Node(object):
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next  # 指针
#
# class LinkedList(object):
#     # 链表的数据结构
#     def __init__(self):
#         self.head = 0  # 头部
#
#     def init_list(self, n): # 按列表给出
#         if n<=0:
#             return False
#         if n==1:
#             return Node(1)
#         else:
#             root=Node(1)
#             tmp=root
#             for i in range(2,n+1):
#                 tmp.next=Node(i)
#                 tmp=tmp.next
#             tmp.next=root 环的 比如约瑟夫环 		if tmp.next==tmp:break 说明只有一个元素了
#             return root
