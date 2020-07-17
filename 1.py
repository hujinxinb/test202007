# -*- coding: UTF-8 -*-
from concurrent.futures import ThreadPoolExecutor
import threading
import time

# 定义一个准备作为线程任务的函数
def action(max,a):
    my_sum = 0
    for i in range(max):
        print(threading.current_thread().name + '  ' + str(i))
        my_sum += i
    return my_sum


for i in range(4):
    pool = ThreadPoolExecutor(2)
    future1 = pool.submit(action, 5,1)
    future2 = pool.submit(action, 5,1)

    def get_result(future):
        print(future.result())
    future1.add_done_callback(get_result)
    future2.add_done_callback(get_result)
    print('--------------')
    pool.shutdown(wait=True)




# # 创建一个包含2条线程的线程池
# with ThreadPoolExecutor(max_workers=2) as pool:
#     # 向线程池提交一个task, 50会作为action()函数的参数
#     future1 = pool.submit(action, 5)
#     # 向线程池再提交一个task, 100会作为action()函数的参数
#     future2 = pool.submit(action, 5)
#     def get_result(future):
#         print(future.result())
#     # 为future1添加线程完成的回调函数
#     future1.add_done_callback(get_result)
#     # 为future2添加线程完成的回调函数
#     future2.add_done_callback(get_result)
#     print('--------------')



#!/usr/bin/python
# -*- coding: UTF-8 -*-
# class Parent: # 定义父类
#     parentAttr = 100
#     def __init__(self):
#         print ("调用父类构造函数")
#     def parentMethod(self):
#         print ('调用父类方法')
#     def setAttr(self, attr):
#         Parent.parentAttr = attr
#     def getAttr(self):
#         print ("父类属性 :", Parent.parentAttr)
#
# class Child(Parent): # 定义子类
#     def __init__(self):
#         print ("调用子类构造方法")
#     def childMethod(self):
#         print ('调用子类方法')
#
# c = Child() # 实例化子类
# c.childMethod() # 调用子类的方法
# c.parentMethod() # 调用父类方法
# c.setAttr(200) # 再次调用父类的方法 - 设置属性值
# c.getAttr() # 再次调用父类的方法 - 获取属性值