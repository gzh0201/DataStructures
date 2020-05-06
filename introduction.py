# 注册牛客网，LeetCode(必刷)

# 如果a+b+c = 1000,并且a^2 + b^2 = c^2,求出所有的a,b,c可能的组合
#解决同一个问题，时间短的算法更好

#第一种算法,三重循环
# import time

# start_time = time.time()
# for a in range(0,1001):
#     for b in range(0,1001):
#         for c in range(0,1001):
#             if a+b+c == 1000 and a**2+b**2 == c**2:
#                 print("a,b,c:%d,%d,%d"%(a,b,c))

# end_time=time.time()

# print("运行时间为:%f"%(end_time - start_time))

'''
    a,b,c:0,500,500
    a,b,c:200,375,425
    a,b,c:375,200,425
    a,b,c:500,0,500
    运行时间为:177.737113
'''

# 为了让执行的时间更短，提出第二个算法，双重循环

# import time
# start_time = time.time()

# for a in range(0,1001):
#     for b in range(0,1001):
#         c = 1000 - a - b
#         if a**2+b**2 == c**2:
#             print("a,b,c:%d,%d,%d"%(a,b,c))

# end_time = time.time()

# print("执行时间为：%f"%(end_time - start_time))

'''
    a,b,c:0,500,500
    a,b,c:200,375,425
    a,b,c:375,200,425
    a,b,c:500,0,500
    执行时间为：2.232172
'''


# 思考：都可以从哪些角度去优化程序




'''
    1.什么是算法？
        算法是独立存在的一种解决问题的方法和思想！
    2.算法的五大特性？
        输入：算法具有0个或者多个输入
        输出：算法至少具有1个或者多个输出
        有穷性：算法是在有限的步骤之后会自动结束而不会无限循环，并且每一个步骤可以在可接受的时间内完成；
        确定性：算法的每一个步骤都要有确定的含义，不会出现二义性；
        可行性：算法的每一步都是可行的(也就是说每一步都能够执行有限的次数完成)
    3.算法效率衡量
        实现算法程序的执行时间可以反应出来算法的效率
        单纯依靠运行时间来比较算法的优劣不一定是客观准确地(程序的运行离不开计算机环境，所以和硬件，操作系统都有关系)
    4.最终算法用什么去衡量?
        时间复杂度
    5.表示法：大O记法
        O(n^3)
        O(n^2)


'''


# 作业：计算前1000个正整数的和(2种算法)

# 第一种方法
# sum = 0
# for i in range(0,1001):
#     sum += i
# print(sum)

# 第二种方法
# s = 0
# i = 1
# while i<1001:
#     s += i
#     i += 1
# print(s)

# 第三种方法
# print(sum(range(1,1001)))

# 第四种方法
print(sum([ x for x in range(0,1001)]))
