import numpy as np
from itertools import product

def find_min_natural_solution(A, b):
    nonzero_elements = A[np.nonzero(A)]  # 获取非零元素
    min_value = np.min(nonzero_elements)  # 找到非零元素中的最小值
    max_value = np.max(nonzero_elements)  # 找到非零元素中的最大值
    min_value2 = 360
    if max_value >=180:
        min_value2 = 360-max_value
    min_value=min(min_value,min_value2)
    for i in range(0, 360//min_value+1):
        for j in range(0, 360//min_value+1):
            for k in range(0, 360//min_value+1):
                X = np.array([i, j, k])
                Y = np.dot(X, A)
                Y_mod = np.mod(Y, 360)  # 对 Y 中的每个元素进行取余 360 操作
                if np.array_equal(Y_mod, b):  # 检查 Y_mod 是否等于 b
                    return X
    return None  # 如果找不到解决方案，则返回 None

input_mode = input("请输入模式，0为默认，1为输入")
if input_mode == "0":
    action1 = [240,300,0]
    action2 = [240,0,120]
    action3 = [0,300, 120]
    diffrences = [0,0,120]
else:
    # 一次性输入多个值，使用空格分隔
    input_str = input("请输入第一个动作能控制的三个罗盘的角度（顺时针为正）: ")
    # 将输入拆分为一个字符串列表
    input_list = input_str.split()
    action1 = [int(x) for x in input_list]
    print(action1)

    input_str = input("请输入第二个动作能控制的三个罗盘的角度（顺时针为正）: ")
    # 将输入拆分为一个字符串列表
    input_list = input_str.split()
    action2 = [int(x) for x in input_list]
    print(action2)

    input_str = input("请输入第三个动作能控制的三个罗盘的角度（顺时针为正）: ")
    # 将输入拆分为一个字符串列表
    input_list = input_str.split()
    action3 = [int(x) for x in input_list]
    print(action3)

    # 一次性输入多个值，使用空格分隔
    input_str = input("请输入三级罗盘分别距离目标的角度（顺时针为正）: ")
    # 将输入拆分为一个字符串列表
    input_list = input_str.split()
    diffrences = [int(x) for x in input_list]
    print(diffrences)


# 定义系数矩阵 A 和常数向量 b
A = np.array([action1,
              action2,
              action3])

solution = find_min_natural_solution(A, diffrences)

if solution is not None:
    print(f'i = {solution[0]}')
    print(f'j = {solution[1]}')
    print(f'k = {solution[2]}')
else:
    print('未找到整数解')
