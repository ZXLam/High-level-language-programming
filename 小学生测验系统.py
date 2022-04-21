'''
小学生测试系统: 50以内加减法
Author: Zhu XiaoLin
Date: 2022-4-21
'''

import numpy as np
import time

count = 0  # 计题数初始为0
res = 0  # 计算结果初始为0
totle_num = 0  # 总分初始为0


def add_n(a, b):
    '''
    input: 加法的结果
    output：正确则输出True
    '''
    result = eval(input('{0} + {1} = '.format(a, b)))
    if result == a + b:
        return True


def sub_n(a, b):
    '''
    input: 减法的结果
    output：正确则输出True
    '''
    result = eval(input('{0} - {1} = '.format(a, b)))
    if result == a - b:
        return True

print('欢迎进入小学生测试系统，我们将进行50以内加减法测试。')
print('准备开始')
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
print('开始\n')
while count != 10:  # 共10道题，count为计题数
    # 随机输入两个1-50的整数
    num_One = np.random.randint(1, 51)
    num_Two = np.random.randint(1, 51)
    # 判断两个数的和是否大于50，小于0.如果是则创新随机
    if (num_One + num_Two) > 50 or (num_One - num_Two) < 0:
        continue  # 不执行下面的代码直接返回循环开始位置
    else:
        print('第{0}题：'.format(count + 1))
        ran_sign = np.random.randint(1, 3)  # 随机加法运算还是减法运算，1为加法，2为减法
        times = 0  # 计算次数
        while True:
            if ran_sign == 1:
                res = add_n(num_One, num_Two)
            else:
                res = sub_n(num_One, num_Two)
            if res == True:
                break  # 如果正确，退出循环
            else:
                print('答案错误，请重新做答')
                times += 1
            if times == 3:
                if ran_sign == 1:
                    print('小朋友,正确答案是:{0}'.format(num_One + num_Two))
                else:
                    print('小朋友,正确答案是:{0}'.format(num_One - num_Two))
                break  # 如果计算超过3次，退出循环
        if times == 0:
            totle_num += 10  # 根据计算次数把分数加到总分
        elif times == 1:
            totle_num += 7
        elif times == 2:
            totle_num += 5
        count += 1  # 有效题目+1，当count等于10则退出循环


print('小朋友，你的得分为 {0} 分'.format(totle_num))  # 测试用
if totle_num >= 90:
    print('SMART')
elif totle_num < 90 and totle_num > 80:
    print('GOOD')
elif totle_num < 80 and totle_num > 70:
    print('OK')
elif totle_num < 70 and totle_num > 60:
    print('PASS')
else:
    print('TRY AGAIN')