# D01 面向对象  数组、栈、队列
########################## D01-01 ###################################### 0001
# LC1603. 设计停车系统
# class ParkingSystem(object):
#
#     def __init__(self, big, medium, small):
#         # 数组的第 0 位置初始化为 0，起到占位符的作用
#         # 这样在 addCar 方法里面
#         # park[1] 就是 big 的数量
#         # park[2] 就是 medium 的数量
#         # park[3] 就是 small 的数量
#         self.park = [0, big, medium, small]
#
#     def addCar(self, carType):
#         # 当前类型没有车位了，返回 False
#         if self.park[carType] == 0:
#             return False
#
#         # 否则当前类型车位数量减少一个
#         self.park[carType] -= 1
#         return True
from collections import deque


########################## D01-01 ###################################### 0001-MmCopy
# LC1603. 设计停车系统
# class ParkingSystem(object):
#     def __init__(self,big,medium,small):
#         # 数组的第 0 位置初始化为 0，起到占位符的作用
#         # 这样在 addCar 方法里面
#         # park[1] 就是 big 的数量
#         # park[2] 就是 medium 的数量
#         # park[3] 就是 small 的数量
#         self.park = [0,big,medium,small]
#
#     def addCar(self,carType):
#         # 当前类型没有车位了，返回 False
#         if self.park[carType] == 0:
#             return False
#         # 否则当前类型车位数量减少一个
#         self.park[carType] -= 1
#         return True

# 测试代码讲解：
# 创建一个停车系统对象，分别设置大车位、中车位和小车位的数量
# parking = parkingSystem2(2, 2, 2)
#
# # 尝试添加不同类型的车辆，并打印是否成功
# print(parking.addCar(1))  # 尝试添加一辆大型车big，应该返回True
# print(parking.addCar(3))  # 尝试添加一辆小型车small，应该返回True
# print(parking.addCar(2))  # 尝试添加一辆中型车medium，应该返回True
# print(parking.addCar(2))  # 尝试添加一辆中型车medium，应该返回True
# print(parking.addCar(2))  # 尝试添加一辆中型车medium，应该返回False 应该返回False，因为小车位已满
#
# 测试代码的作用是创建一个parkingSystem2对象，
# 设置不同类型车位的数量，然后分别尝试添加不同类型的车辆。每次添加车辆后，会打印出添加是否成功的结果。
# 这样可以验证给定的停车系统类是否按预期工作，例如是否正确减少对应类型的车位数量，并在车位已满时返回False。
#
# 在addCar方法中，参数carType表示车辆的类型，其中：
# - 1
# 代表大型车
# - 2
# 代表中型车
# - 3
# 代表小型车
#
# 在测试代码中，通过传入不同的参数来模拟添加不同类型的车辆，并根据返回值来判断添加是否成功。
# 在实际应用中，可以根据具体情况来确定要传入的参数类型，例如根据车辆的尺寸或类别来决定传入的参数值。
#
# MM编写的测试代码：
# parking = parkingSystem2(4,8,6) # big4辆，medium8辆，small6辆
# print(parking.addCar(1)) # 添加1辆big
# print(parking.addCar(1))
# print(parking.addCar(1))
# print(parking.addCar(1))
# print(parking.addCar(1))
#
# print('-----------------------------')
# print(parking.addCar(2)) # 添加1辆medium
# print(parking.addCar(2))
# print(parking.addCar(2))
# print(parking.addCar(2))
# print(parking.addCar(2))
# print(parking.addCar(2))
# print(parking.addCar(2))
# print(parking.addCar(2))
# print(parking.addCar(2))
# print('-----------------------------')
#
# print(parking.addCar(3)) # 添加1辆small
# print(parking.addCar(3))
# print(parking.addCar(3))
# print(parking.addCar(3))
# print(parking.addCar(3))
# print(parking.addCar(3))
# print(parking.addCar(3))
# print('-----------------------------')
#
# 运行结果：
# True
# True
# True
# True
# False
# -----------------------------
# True
# True
# True
# True
# True
# True
# True
# True
# False
# -----------------------------
# True
# True
# True
# True
# True
# True
# False
# ---------------------

########################## D01-02 ###################################### 0002
## 有效的括号（ LC20 ）:https://leetcode-cn.com/problems/valid-parentheses
# // 有效的括号（ LeetCode 20 ）:https://leetcode-cn.com/problems/valid-parentheses
# class Solution:
#     def isValid(self, s: str) -> bool:
#         # 当字符串长度为奇数的时候，属于无效情况，直接返回 False
#         if len(s) % 2 == 1:
#             # 无效情况，返回 False
#             return False
#
#         # 构建一个栈，用来存储括号
#         stack = list()
#
#         # 遍历字符串数组中的所有元素
#         for c in s:
#
#             # 如果字符为左括号 ( ，那么就在栈中添加对左括号 （
#             if c == '(':
#
#                 # 添加对左括号 （
#                 stack.append('(')
#
#             # 如果字符为左括号 [ ，那么就在栈中添加对左括号 [
#             elif c == '[':
#
#                 # 添加对应的右括号 ]
#                 stack.append('[')
#
#             # 如果字符为左括号 { ，那么就在栈中添加对左括号 {
#             elif c == '{':
#
#                 # 添加对应的右括号 }
#                 stack.append('{')
#
#                 # 否则的话，说明此时 c 是 ）] } 这三种符号中的一种
#             else:
#
#                 # 如果栈已经为空，而现在遍历的字符 c 是 ）] } 这三种符号中的一种
#                 # 找不到可以匹配的括号，返回 False
#                 # 比如这种情况  }{，直接从右括号开始，此时栈为空
#                 if not stack:
#                     return False
#
#                 # 如果栈不为空，获取栈顶元素
#                 top = stack[-1]
#
#                 # 将栈顶元素和此时的元素 c 进行比较，如果相同，则将栈顶元素移除
#                 if (top == '(' and c == ')') or (top == '[' and c == ']') or (top == '{' and c == '}'):
#                     # 移除栈顶元素
#                     stack.pop()
#                 else:
#                     # 如果不相同，说明不匹配，返回 False
#                     return False
#
#         # 遍历完整个字符数组，判断栈是否为空
#         # 如果栈为空，说明字符数组中的所有括号都是闭合的
#         # 如果栈为空，说明有未闭合的括号
#         return not stack

########################## D01-02 ###################################### 0002--MmCopy1
## 有效的括号（ LC20 ）:https://leetcode-cn.com/problems/valid-parentheses
# class Solution:
#     def isValid(self, s: str) -> bool:
#
#         # 构建一个栈，用来存储括号
#         stack = list()
#
#         # 构建一个配对列表，列表由三对元组组成，每个元组是一堆匹配的括号
#         pairs = [('(', ')'), ('{', '}'), ('[', ']')]
#
#         # 当字符串长度为奇数的时候，属于无效情况，直接返回 False
#         if len(s) % 2 == 1:
#             # 无效情况，返回 False
#             return False
#
#         # 遍历字符串数组中的所有元素
#         for ch in s:
#             # 如果字符为左括号 ( 、{、[，那么就在栈中添加对左括号 ( 、{、[
#             if ch == '(' or ch == '[' or ch == '{':
#                 stack.append(ch)
#             # 否则的话，说明此时的字符ch 是 ）] } 这三种符号中的一种
#             else:
#                 # 如果栈已经为空，而现在遍历的字符 ch 是 ）] } 这三种符号中的一种
#                 # 找不到可以匹配的括号，返回 False
#                 # 比如这种情况  }{，直接从右括号开始，此时栈为空
#                 # if len(stack) == 0:
#                 if not stack:
#                     return False
#                 # 如果栈不为空，获取并弹出栈顶元素   获取并弹出栈顶元素的写法: stack.pop()  只获取栈顶元素的写法：  stack[-1]
#                 # ch_stack_top = stack[-1]
#                 ch_stack_top = stack.pop()
#
#                 # 判断当前获取的栈顶元素与当前遍历的字符ch 是否在配对列表中，如果不在，返回false
#                 if (ch_stack_top, ch) not in pairs:
#                     return False
#
#         # 遍历完整个字符数组，判断栈是否为空
#         # 如果栈为空，说明字符数组中的所有括号都是闭合的
#         # 如果栈为空，说明有未闭合的括号
#         # return len(stack)==0
#         return not stack


# # 测试代码：
# solution = Solution()
#
# # 测试用例1: 括号匹配
# input_str1 = "()"
# print(solution.isValid(input_str1))  # 预期结果：True
#
# # 测试用例2: 括号不匹配
# input_str2 = "([)]"
# print(solution.isValid(input_str2))  # 预期结果：False

# class Solution1:
#     def isValid(self,s:str)->bool:
#         # stack = []
#         stack = list()
#         pairs = [('(',')'),('{','}'),('[',']')]
#         isError = False
#
#         if len(s) % 2 == 1:
#             return isError
#
#         for ch in s:
#             if ch == '(' or ch == '{' or ch == '[':
#                 stack.append(ch)
#             else:
#                 # if len(stack) == 0:
#                 if not stack:
#                     return isError
#                 ch_stack_top = stack[-1]
#                 if (ch_stack_top,ch) not in pairs:
#                     stack.pop()
#                     return isError
#         return not stack

######################### D01-03 ###################################### 0003
# 【栈】2023Q1A-括号检查
# 题目描述与示例
# 题目
# 现有一字符串 仅由 '(', ')', '{', '}', '[', ']' 一共六种括号组成。若字符串满足以下条件之一，则为无效字符串
# 1. 任意类型的左右括号数量不相等
# 2. 存在未按正确顺序（先左后右）合的括号，
# 输出括号的最大嵌套深度，若字符串无效则输出 0。0 <= 字符串长度 <= 100000
# 输入
# 一个只包括 '(', ')', '{', '}', '[', ']' 以一共6种字符的字符串。
# 输出
# 一个整数，表示最大的括号深度。若字符串无效，则输出 0
# 示例一
# 输入
# []
# 输出
# 1
# 说明
# 该字符串有效，且最大嵌套深度为 1
# 示例二
# 输入
# ([]{()})
# 输出
# 3
# 说明
# 该字符串有效，且最大嵌套深度为 3

# 题目：2023Q1A-括号检查
# 分值：100

# s = input()
# # 初始化用于判断异常的变量isError，初始化为False表示没有异常
# isError = False
# # 初始化答案变量ans和记录当前深度的变量cur_depth
# ans, cur_depth = 0, 0
# # 构建三种括号的两两配对关系
# pairs = [('(', ')'), ('{', '}'), ('[', ']')]
#
# # 若字符串长度为奇数，必定无法配对，isError设置为True
# if len(s) % 2 == 1:
#     isError = True
# else:
#     # 使用列表list初始化一个空栈
#     stack = list()
#     # 一次遍历字符串s中的每一个字符ch
#     for ch in s:
#         # 若ch为某种左括号
#         if ch == '(' or ch == '{' or ch == '[':
#             # 则将ch加入栈顶，同时括号深度+1，更新最大括号深度
#             stack.append(ch)
#             cur_depth += 1
#             ans = max(ans, cur_depth)
#         # 若ch为某种右括号
#         else:
#             # 若此时栈为空
#             if len(stack) == 0:
#                 # 该右括号无法与左括号配对，出现异常，isError设置为True，同时退出循环
#                 isError = True
#                 break
#             # 若栈不为空，则弹出栈顶字符，同时括号深度-1
#             ch_stack_top = stack.pop()
#             cur_depth -= 1
#             # 若栈顶左括号字符ch_stack_top和当前右括号字符ch不配对，
#             # 出现异常，isError设置为True，同时退出循环
#             if (ch_stack_top, ch) not in pairs:
#                 isError = True
#                 break
#     # 经过一次遍历后，若仍存在元素，说明存在括号未配对，出现异常，isError设置为True
#     if len(stack) > 0:
#         isError = True
#
# # 如果isError标志为True，说明前面某一步出现异常，输出0，否则输出最大深度ans
# print(0 if isError else ans)

######################### D01-03 ###################################### 0003--MmCopy
# 2023Q1A-括号检查括号最大深度-100
# s = input()
# ans,cur_depth = 0,0
# pairs = [('(',')'),('{','}'),('[',']')]
#
# stack = list()
# isError = False
#
# if len(s) % 2 == 1:
#     isError = True
# else:
#     for ch in s:
#         if ch == '(' or ch == '{' or ch == '[':
#             stack.append(ch)
#             cur_depth += 1
#             ans = max(ans,cur_depth)
#         else:
#             if len(stack) == 0:
#                 isError = True
#                 break
#             ch_stack_top = stack.pop()
#             cur_depth -= 1
#             if (ch_stack_top,ch) not in pairs:
#                 isError = True
#                 break
#     # if not stack:
#     if len(stack) > 0:
#         isError = True
#
# print(0 if isError else ans)


########################## D01-04 ###################################### 0004
# LCR041
# 剑指 Offer II 041. 滑动窗口的平均值
# 题目描述
# 给定一个整数数据流和一个窗口大小，根据该滑动窗口的大小，计算滑动窗口里所有数字的平均值。
# 实现 MovingAverage 类：
# - MovingAverage(int size) 用窗口大小 size 初始化对象。
# - double next(int val) 成员函数 next 每次调用的时候都会往滑动窗口增加一个整数，请计算并返回数据流中最后 size 个值的移动平均值，即滑动窗口里所有数字的平均值。
# 示例：
# 输入：
# inputs = ["MovingAverage", "next", "next", "next", "next"]
# inputs = [[3], [1], [10], [3], [5]]
# 输出：
# [null, 1.0, 5.5, 4.66667, 6.0]
#
# 解释：
# MovingAverage movingAverage = new MovingAverage(3);
# movingAverage.next(1); // 返回 1.0 = 1 / 1
# movingAverage.next(10); // 返回 5.5 = (1 + 10) / 2
# movingAverage.next(3); // 返回 4.66667 = (1 + 10 + 3) / 3
# movingAverage.next(5); // 返回 6.0 = (10 + 3 + 5) / 3

# class MovingAverage:
#     def __init__(self, size: int):
#         # 1、记录当前窗口的大小
#         self.size = size
#         # 2、记录当前窗口里面所有元素的和
#         self.sum = 0
#         # 3、由于数字进入滑动窗口和移出滑动窗口的规则符合先进先出，因此可以使用队列存储滑动窗口中的数字
#         self.q = deque()
#
#     def next(self, val: int) -> float:
#         # 4、在添加 val 之前，先判断滑动窗口的长度是否已经达到了最大容量 size
#         if len(self.q) == self.size:
#             # 5、如果达到了，此时先将窗口最左边的元素移除去，即 popleft
#             # 那么当前 滑动窗口 里面的元素和就发生了变化，也需要减去
#             self.sum -= self.q.popleft()
#         # 6、再把 val 累加到 sum 上面去
#         self.sum += val
#         # 7、同时 val 也加入到了队列里面
#         self.q.append(val)
#         # 8、最后，计算平均值就行
#         return self.sum / len(self.q)

# 测试代码
# import unittest
# from collections import deque
#
#
# class TestMovingAverage(unittest.TestCase):
#
#     def test_moving_average(self):
#         obj = MovingAverage(3)
#         self.assertEqual(obj.next(1), 1.0)  # 测试初始插入一个元素的情况
#         self.assertEqual(obj.next(10), 5.5)  # 测试插入两个元素后的平均值
#         self.assertEqual(obj.next(3), 4.666666666666667)  # 测试插入三个元素后的平均值
#         self.assertEqual(obj.next(5), 6.0)  # 测试插入第四个元素后的平均值
#
#
# if __name__ == '__main__':
#     unittest.main()

# 对测试代码的解释：
# 1.unittest是Python的内置单元测试框架，用于编写和运行测试。
# 2.TestMovingAverage类包含了一个测试方法test_moving_average ，用于测试MovingAverage类的功能。
# 3.在test_moving_average方法中，创建了一个MovingAverage对象obj ，并依次调用next方法，并使用assertEqual断言方法来验证计算得到的移动平均值是否符合预期。
# 4.在这个例子中，测试了向MovingAverage对象中依次添加数字1、10、3和5后计算得到的移动平均值是否正确。
#
# 通过运行这些测试代码，可以验证给定的MovingAverage类是否按预期工作。

########################## D01-04 ###################################### 0004--MmCopy
# 滑动窗口平均值 LCR041
# class MovingAverge(object):
#       #带有初始化的函数  类声明时都需要传一个object参数？
#     def __init__(self,size:int):
#         self.size = size
#         self.sum = 0
#         self.q = deque()
#
#     def next(self,val:int)->float:
#         if len(self.q) == self.size:
#             self.sum -= self.q.popleft()
#         self.sum += val
#         self.q.append(val)
#         return self.sum/len(self.q)

########################## D01-05 ###################################### 0005
# LeetCode 1614、括号的最大嵌套深度
# 视频地址：https://uha.xet.tech/s/38MaIi
# 一、题目描述
# 如果字符串满足以下条件之一，则可以称之为 有效括号字符串*（valid parentheses string，可以简写为 VPS）：
# - 字符串是一个空字符串 ""，或者是一个不为 "(" 或 ")" 的单字符。
# - 字符串可以写为 AB（A 与 B 字符串连接），其中 A 和 B 都是 有效括号字符串 。
# - 字符串可以写为 (A)，其中 A 是一个 有效括号字符串 。
# 类似地，可以定义任何有效括号字符串 S 的 嵌套深度 depth(S)：
# - depth("") = 0
# - depth(C) = 0，其中 C 是单个字符的字符串，且该字符不是 "(" 或者 ")"
# - depth(A + B) = max(depth(A), depth(B))，其中 A 和 B 都是 有效括号字符串
# - depth("(" + A + ")") = 1 + depth(A)，其中 A 是一个 有效括号字符串
# 例如：""、"()()"、"()(()())" 都是 有效括号字符串（嵌套深度分别为 0、1、2），而 ")(" 、"(()" 都不是 有效括号字符串 。
# 给你一个 有效括号字符串 s，返回该字符串的 s 嵌套深度 。
# 示例 1：
# 输入：s = "(1+(2*3)+((8)/4))+1"
# 输出：3
# 解释：数字 8 在嵌套的 3 层括号中。
# 示例 2：
# 输入：s = "(1)+((2))+(((3)))"
# 输出：3
# 提示：
# - 1 <= s.length <= 100
# - s 由数字 0-9 和字符 '+'、'-'、'*'、'/'、'('、')' 组成
# - 题目数据保证括号表达式 s 是 有效的括号表达式
# class Solution:
#     def maxDepth(self, s: str) -> int:
#
#         # size 表示栈的大小
#         # ans 表示 size 的最大值，也就是最终的结果值
#         ans, size = 0, 0
#
#         # 遍历字符串 s
#         for ch in s:
#             # 如果遇到了一个左括号，将其入栈
#             if ch == '(':
#                 # 栈中元素的个数加 1
#                 size += 1
#                 # 更新深度的值
#                 ans = max(ans, size)
#             # 如果遇到了一个右括号，弹出栈顶的左括号
#             elif ch == ')':
#                 # 栈中元素的个数减 1
#                 size -= 1
#         # 返回最大值
#         return ans

# 测试代码
# import unittest
# class TestSolution(unittest.TestCase):
#
#     def test_maxDepth(self):
#         sol = Solution()
#         self.assertEqual(sol.maxDepth("(1+(2*3)+((8)/4))+1"), 3)  # 测试包含多层括号的情况
#         self.assertEqual(sol.maxDepth("(1)+((2))+(((3)))"), 3)  # 测试连续嵌套括号的情况
#         self.assertEqual(sol.maxDepth("1+(2*3)/(2-1)"), 1)  # 测试没有括号的情况
#         self.assertEqual(sol.maxDepth(""), 0)  # 测试空字符串的情况
#
#
# if __name__ == '__main__':
#     unittest.main()

# 对测试代码的解释：
# 1.unittest是Python的内置单元测试框架，用于编写和运行测试。
# 2.TestSolution类包含了一个测试方法test_maxDepth ，用于测试Solution类的maxDepth方法的功能。
# 3.在test_maxDepth方法中，创建了一个Solution对象sol ，并依次调用maxDepth方法，并使用assertEqual断言
# 方法来验证计算得到的最大深度是否符合预期。
#
# 4.在这个例子中，测试了包含多层括号、连续嵌套括号、没有括号和空字符串的情况下计算得到的最大深度是否正确。
# 通过运行这些测试代码，可以验证给定的Solution类的maxDepth方法是否按预期工作。


########################## D01-05 ###################################### 0005--MmCopy
# LC1614 括号的最大嵌套深度
# class Solution:
#     def maxDepth(self,s:str)-> int:
#         ans,depth = 0,0
#
#         for ch in s:
#             if ch == '(':
#                 depth += 1
#                 ans = max(ans,depth)
#             elif ch == ')':
#                 depth -= 1
#         return ans

########################## D01-06 ###################################### 0006
# LC1047. 删除字符串中的所有相邻重复项
# 如果作业完成有难度，可以查看我的讲解视频。
# https://uha.xet.tech/s/2rTqDk
# 一、题目描述
# 给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
# 在 S 上反复执行重复项删除操作，直到无法继续删除。
# 在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。
# 示例：
# 输入："abbaca"
# 输出："ca"
# 解释：
# 例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。
# 提示：
# 1. 1 <= S.length <= 20000
# 2. S 仅由小写英文字母组成。

# https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string/submissions/
# class Solution:
#     def removeDuplicates(self, s: str) -> str:
#         # 1、两个相邻且相同字符会被同时删除
#         # 2、删除字符串中两个相邻并且相同的字符后可能会产生一组新的相邻并且相同的字符，需要继续删除
#         # 说明需要记录之前的元素，将最靠近现在访问的元素与现在正在访问的元素进行对比
#         # 使用栈
#         stack = []
#
#         # 从头到尾访问所有的元素
#         # 正在访问的元素
#         for cur in s:
#
#             # 在访问过程中
#             # 1、如果栈为空，直接把当前访问的元素添加进去
#             if not stack:
#
#                 # 直接把当前访问的元素添加进去
#                 stack.append(cur)
#
#             # 2、如果栈不为空，并且栈顶元素不等于正在访问的元素
#             elif cur != stack[-1]:
#
#                 # 也把当前访问的元素添加进去
#                 stack.append(cur)
#
#             # 3、如果栈不为空，并且栈顶元素等于正在访问的元素
#             else:
#                 # 说明这两个元素应该被删除，那么不仅当前这个元素无法加入到栈，同时和这个元素相同的栈顶元素得从栈中移除
#                 stack.pop()
#
#         # 返回结果
#         return "".join(stack)

# 测试代码
# import unittest
#
#
# class TestSolution(unittest.TestCase):
#
#     def test_removeDuplicates(self):
#         sol = Solution()
#         self.assertEqual(sol.removeDuplicates("abbaca"), "ca")  # 测试包含重复字符的情况
#         self.assertEqual(sol.removeDuplicates("azxxzy"), "ay")  # 测试多个连续重复字符的情况
#         self.assertEqual(sol.removeDuplicates("aaaaa"), "a")  # 测试全部字符都重复的情况
#         self.assertEqual(sol.removeDuplicates("abcde"), "abcde")  # 测试没有重复字符的情况
#
#
# if __name__ == '__main__':
#     unittest.main()

# 对测试代码的解释：
# 1.unittest是Python的内置单元测试框架，用于编写和运行测试。
# 2.TestSolution类包含了一个测试方法test_removeDuplicates ，用于测试Solution类的removeDuplicates方法的功能。
# 3.在test_removeDuplicates方法中，创建了一个Solution对象sol ，并依次调用removeDuplicates方法，并使用assertEqual断言方法来验证计算得到的结果是否符合预期。
# 4.在这个例子中，测试了包含重复字符、多个连续重复字符、全部字符都重复以及没有重复字符的情况下调用removeDuplicates方法的结果是否正确。
#
# 通过运行这些测试代码，可以验证给定的Solution类的removeDuplicates方法是否按预期工作。

########################## D01-06 ###################################### 0006--MmCopy
# LC1047 删除字符串中的所有相邻重复项
# class Solution:
#     def removeDuplicates(self,s:str) -> str:
#         # 1、两个相邻且相同字符会被同时删除
#         # 2、删除字符串中两个相邻并且相同的字符后可能会产生一组新的相邻并且相同的字符，需要继续删除
#         # 说明需要记录之前的元素，将最靠近现在访问的元素与现在正在访问的元素进行对比
#         # 使用栈
#         # stack = list() # 声明空列表方式1
#         stack = [] # 声明空列表方式2
#
#         # 从头到尾访问所有的元素
#         # 正在访问的元素
#         for ch in s:
#             # 在访问过程中
#             # 1、如果栈为空，直接把当前访问的元素添加进去
#             # 2、如果栈不为空，并且栈顶元素不等于正在访问的元素
#             if not stack or ch != stack[-1]:
#                 # 满足1、2这两种情况，则直接把当前访问的元素添加进去
#                 stack.append(ch)
#             # 3、如果栈不为空，并且栈顶元素等于正在访问的元素
#             else:
#                 # 说明这两个元素应该被删除，那么不仅当前这个元素无法加入到栈，同时和这个元素相同的栈顶元素得从栈中移除
#                 stack.pop()
#         # 返回结果
#         #"".join(stack)这段代码的作用是将一个栈中的元素连接成一个字符串并返回。
#         # 1.首先，使用`join`方法将栈中的所有元素连接成一个字符串。
#         # 2.最后，返回这个连接后的字符串。
#         return "".join(stack)
#
# # 测试代码
# import unittest
#
#
# class TestSolution(unittest.TestCase):
#
#     def test_removeDuplicates(self):
#         sol = Solution()
#         self.assertEqual(sol.removeDuplicates("abbaca"), "ca")  # 测试包含重复字符的情况
#         self.assertEqual(sol.removeDuplicates("azxxzy"), "ay")  # 测试多个连续重复字符的情况
#         self.assertEqual(sol.removeDuplicates("aaaaa"), "")  # 测试全部字符都重复的情况
#         self.assertEqual(sol.removeDuplicates("abcde"), "abcde")  # 测试没有重复字符的情况
#
#
# if __name__ == '__main__':
#     unittest.main()


########################## D01-07 ###################################### 0007
# 【排序】2023C-身高体重排序
# 题目描述与示例
# 题目描述
# 某学校举行运动会,学生们按编号(1、2、3.....n) 进行标识,
# 现需要按照身高由低到高排列，对身高相同的人，按体重由轻到重排列，对于身高体重都相同的人，维持原有的编号顺序关系。
# 请输出排列后的学生编号
# 输入描述
# 两个序列，每个序列由 n 个正整数组成(0 < n < 100)。第一个序列中的数值代表身高，第二个序列中的数值代表体重。
# 输出描述
# 排列结果，每个数值都是原始序列中的学生编号，编号从 1 开始
# 示例一
# 输入
# 4
# 100 100 120 130
# 40 30 60 50
# 输出
# 2134
# 示例二
# 输入
# 3
# 90 110 90
# 45 60 45
# 输出
# 132
# 解题思路
# 我们一共有三个列表，身高列表h，体重列表w，以及编号列表idx。
#
# 为了让身高、体重和编号的信息能够一一对应，我们使用zip()函数将这三个列表里面的内容绑定为一个包含n个三元元组的列表lst，即
# lst = list(zip(h, w, idx))
# 在排序方面，题目要求我们按身高从小到大排序，身高相同再按体重从小到大排序，身高体重相同则按照编号从小到大排序，均为升序排序。所以直接调用列表的方法sort()或者内置函数sorted()即可完成。即
# lst.sort()
# 最终再将排序后的lst中的编号信息取出来，再用字符串的join()方法将排序后的编号顺序组合成一个字符串即可。即
# print("".join([str(item[2]) for item in lst]))

# 题目：2023Q1A-身高提供排序
# 分值：100

# n = int(input())
# h = list(map(int, input().split()))
# w = list(map(int, input().split()))
#
# idx = [i for i in range(1, n+1)]    # 编号列表，1到n
# lst = list(zip(h, w, idx))          # 身高、体重、编号整合为三元的元组，组成一个新的列表lst
#
# lst.sort()                 # 直接对lst排序，会先按照身高排序，再按照体重排序，再按照编号排序
# print("".join(str(item[2]) for item in lst))   # 排序后取编号，组成字符串，即为答案

# 时空复杂度
# 时间复杂度：O(NlogN)。排序时间复杂度。
# 空间复杂度：O(N)。
# 进阶
# 如果本题稍作修改，要求我们先按照身高升序排列，再按照体重降序排列，应该如何修改代码呢？这个时候就要祭出神器lambda匿名函数了。语法如下：
# lst.sort(key = lambda x: (x[0], -x[1]))
# key是sort()方法或sorted()内置函数的参数，表示排序的依据。
# lambda匿名函数中的x表示的就是lst中的元素，即一个个的三元元组。
# 由于sort()默认的排序方式是升序，(x[0], -x[1])表示对列表先按照x[0]升序排列，在x[0]相同的情况下再按照-x[1]升序排列，即按照x[1]降序排列。
# 通过这样的方式，我们就实现了身高升序排列，再按照体重降序排列的目的。
# 对于原题目而言，如果我们也想显式地写出lambda匿名函数，则代码为：
# lst.sort(key = lambda x: (x[0], x[1]))
# 如果还想再把编号按照升序排列也显式地写出，则代码为
# lst.sort(key = lambda x: (x[0], x[1], x[2]))
# lambda匿名函数的作用很多。除了sort()之外，取最值的两个函数max()和min()中包含参数key，表示取最大值或最小值的依据，譬如：
# max(lst, key = lambda x: x[0] * x[1]))
# 表示取身高和体重之积最大的那个人所对应的三元元组。


########################## D02-01 ###################################### 0008
# LC0150 逆波兰表达式求值
# 预习和复习可以查看我的讲解视频。
# https://uha.xet.tech/s/D7LEJ
# 一、题目描述
# 根据 逆波兰表示法，求表达式的值。
# 有效的算符包括 +、-、*、/ 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
# 注意 两个整数之间的除法只保留整数部分，向零截断。
# 可以保证给定的逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
# 示例 1：
# 输入：tokens = ["2","1","+","3","*"]
# 输出：9
# 解释：该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9
# 示例 2：
# 输入：tokens = ["4","13","5","/","+"]
# 输出：6
# 解释：该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6
# 示例 3：
# 输入：tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# 输出：22
# 解释：该算式转化为常见的中缀算术表达式为：
#   ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
# 提示：
# - 1 <= tokens.length <= 10^4
# - tokens[i] 是一个算符（"+"、"-"、"*" 或 "/"），或是在范围 [-200, 200] 内的一个整数
# 逆波兰表达式：
# 逆波兰表达式是一种后缀表达式，所谓后缀就是指算符写在后面。
# - 平常使用的算式则是一种中缀表达式，如 ( 1 + 2 ) * ( 3 + 4 ) 。
# - 该算式的逆波兰表达式写法为 ( ( 1 2 + ) ( 3 4 + ) * ) 。
# 逆波兰表达式主要有以下两个优点：
# - 去掉括号后表达式无歧义，上式即便写成 1 2 + 3 4 + *也可以依据次序计算出正确结果。
# - 适合用栈操作运算：遇到数字则入栈；遇到算符则取出栈顶两个数字进行计算，并将结果压入栈中

# class Solution:
#     def evalRPN(self, tokens: list[str]) -> int:
#         # 使用一个列表作为栈，存储操作数，从左到右遍历逆波兰表达式
#         result = []
#
#         # 遍历字符串数组
#         for token in tokens:
#             # 如果是运算符
#             if token in "+-*/":
#                 # 先出栈的是右操作数
#                 rightNum = result.pop()
#                 # 后出栈的是左操作数
#                 leftNum = result.pop()
#                 # 计算结果
#                 if token == "+":
#                     ans = leftNum + rightNum
#                 elif token == "-":
#                     ans = leftNum - rightNum
#                 elif token == "*":
#                     ans = leftNum * rightNum
#                 elif token == "/":
#                     ans = int(leftNum / rightNum)
#             else:
#                 # 转换为数字
#                 ans = int(token)
#
#             # 存储结果
#             result.append(ans)
#
#         # 返回栈顶元素
#         return result[-1]

# 测试代码
# import unittest
#
#
# class TestSolution(unittest.TestCase):
#
#     def test_evalRPN(self):
#         sol = Solution()
#         self.assertEqual(sol.evalRPN(["2", "1", "+", "3", "*"]), 9)  # 测试简单的加法和乘法表达式
#         self.assertEqual(sol.evalRPN(["4", "13", "5", "/", "+"]), 6)  # 测试包含除法和加法的表达式
#         self.assertEqual(sol.evalRPN(["10", "6", "9", "3", "/", "-11", "*", "+", "*", "17", "+", "5", "+"]),
#                          22)  # 测试复杂的逆波兰表达式
#
# if __name__ == '__main__':
#     unittest.main()


########################## D02-01 ###################################### 0008MmCopy
# class Solution:
#     def evalRPN(self,tokens:list[str]) ->int:
#         # ans = list()
#         resultStack = []
#         for token in tokens:
#             if token in '+-*/':
#                 rightNum = resultStack.pop()
#                 leftNum = resultStack.pop()
#
#                 if token == '+':
#                     ans = leftNum + rightNum
#                 elif token == '-':
#                     ans = leftNum - rightNum
#                 elif token == '*':
#                     ans = leftNum * rightNum
#                 elif token == '/':
#                     ans = int(leftNum / rightNum)
#
#             else:
#                 ans = int(token)
#             resultStack.append(ans)
#
#         return resultStack[-1]

# 测试代码
# 创建一个Solution对象
# sol = Solution()
#
# # 测试用例1：计算逆波兰表达式 ["2", "1", "+", "3", "*"] 的值
# tokens1 = ["2", "1", "+", "3", "*"]
# print(sol.evalRPN(tokens1))  # 应该输出 9
#
# # 测试用例2：计算逆波兰表达式 ["4", "13", "5", "/", "+"] 的值
# tokens2 = ["4", "13", "5", "/", "+"]
# print(sol.evalRPN(tokens2))  # 应该输出 6


########################## D02-02 ###################################### 0009
# LeetCode155、最小栈
# 预习和复习可以查看我的讲解视频。
# https://uha.xet.tech/s/2lSHgF
# 一、题目描述
# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
# - push(x) —— 将元素 x 推入栈中。
# - pop() —— 删除栈顶的元素。
# - top() —— 获取栈顶元素。
# - getMin() —— 检索栈中的最小元素。
# 二、题目解析
# 由于需要在常数时间内找到最小的元素，那么说明肯定是不能使用遍历，因为遍历是 O(n) 级别的时间复杂度，那么只能使用辅助空间进行存储，这是一种空间换时间的思想。
# 这里我们设置两个栈：普通栈和辅助栈。
# 1. push 操作
# 普通栈：直接添加 push 进来的值
# 辅助栈：每次 push 一个新元素的时候，将普通栈中最小的元素 push 进辅助栈中
# 2. pop 操作
# 普通栈：直接移除普通栈中的栈顶元素
# 辅助栈：判断普通栈中刚刚移除的栈顶元素值是否和此时辅助栈中的栈顶元素相同，如果是则将辅助栈中的栈顶元素移除，否则不执行操作，这样的目的是为了让辅助栈中的栈顶元素始终是普通栈中的最小值。
# 3. top 操作
# 普通栈：返回普通栈的栈顶元素
# 辅助栈：不执行操作
# 4. getMin 操作
# 普通栈：不执行操作
# 辅助栈：返回辅助栈的栈顶元素


# 最小栈（ LeetCode 155 ）:https://leetcode-cn.com/problems/min-stack/
# class MinStack:
#     def __init__(self):
#         # 首先定义好两个栈
#
#         # 一个栈叫做 stack，负责栈的正常操作
#         self.stack = []
#
#         # 一个栈叫做 min_stack，负责获取 stack 中的最小值，它等价于遍历 stack 中的所有元素，把升序的数字都删除掉，留下一个从栈底到栈顶降序的栈
#         self.min_stack = []
#
#     def push(self, x: int) -> None:
#
#         # 新添加的元素添加到 stack 中
#         self.stack.append(x)
#
#         # 判断 min_stack 是否为空，如果为空，直接同时把新添加的元素添加到 minStack 中
#         # 如果 min_stack 不为空
#         if self.min_stack:
#            # 获取 min_stack 的栈顶元素
#            top = self.min_stack[-1]
#
#            # 只有新添加的元素不大于 top 才允许添加到 minStack 中，目的是为了让 minStack 从栈底到栈顶是降序的
#            if x <= top :
#               self.min_stack.append(x)
#
#         # min_stack 中没有元素，所以直接把新添加的元素添加到 min_stack 中
#         else:
#             self.min_stack.append(x)
#
#
#     def pop(self) -> None:
#
#         # 让 stack 执行正常的 pop 操作就行
#         pop =  self.stack[-1]
#
#         self.stack.pop()
#
#         # 由于 minStack 中的所有元素都是来自于 stack 中，所以 stack 删除元素后，minStack 也要考虑是否需要删除元素
#         # 否则的话，minStack 有可能保存一个 stack 中不存在的元素
#
#         # 首先，获取 minStack 的栈顶元素
#         top = self.min_stack[-1]
#
#         # 再判断 top 这个栈顶元素是否和 stack 移除的元素相等，如果相等，那么需要把 minStack 中的栈顶元素一并移除
#         if pop == top:
#             # 移除 min_stack 的栈顶元素
#             self.min_stack.pop()
#
#     def top(self) -> int:
#         # 返回 stack 的栈顶元素
#         return self.stack[-1]
#     def getMin(self) -> int:
#         # 返回 min_stack 的栈顶元素
#         return self.min_stack[-1]

# 测试代码
# import unittest
#
#
# class TestMinStack(unittest.TestCase):
#
#     def test_minStack(self):
#         min_stack = MinStack()
#         min_stack.push(-2)
#         min_stack.push(0)
#         min_stack.push(-3)
#         self.assertEqual(min_stack.getMin(), -3)  # 测试获取最小值
#         min_stack.pop()
#         self.assertEqual(min_stack.top(), 0)  # 测试获取栈顶元素
#         self.assertEqual(min_stack.getMin(), -2)  # 测试获取最小值
#
#
# if __name__ == '__main__':
#     unittest.main()

########################## D02-02 ###################################### 0009MmCopy
# LC0155 最小栈
# 最小栈（ LeetCode 155 ）:https://leetcode-cn.com/problems/min-stack/
# class MinStack:
#     def __init__(self):
#         # 首先定义好两个栈
#         # 一个栈叫做 stack，负责栈的正常操作
#         # self.stack = []
#         self.stack = list()
#         # 一个栈叫做 min_stack，负责获取 stack 中的最小值，它等价于遍历 stack 中的所有元素，把升序的数字都删除掉，留下一个从栈底到栈顶降序的栈
#         # self.min_stack = []
#         self.min_stack = list()
#
#     def push(self,x:int) -> None:
#         # 新添加的元素添加到 stack 中
#         self.stack.append(x)
#
#         # 判断 min_stack 是否为空，如果为空，直接同时把新添加的元素添加到 minStack 中
#         # 即：min_stack 中没有元素，所以直接把新添加的元素添加到 min_stack 中
#         if not self.min_stack:
#             self.min_stack.append(x)
#
#         # 如果 min_stack 不为空
#         else:
#             # 只有新添加的元素不大于 栈顶元素min_stack[-1] 才允许添加到 minStack 中，目的是为了让 minStack 从栈底到栈顶是降序的
#             if x <= self.min_stack[-1]:
#                 self.min_stack.append(x)
#
#     def pop(self) -> None:
#         # 让 stack 执行正常的 pop 操作就行
#         pop = self.stack[-1]
#         self.stack.pop()
#
#         # 由于 minStack 中的所有元素都是来自于 stack 中，所以 stack 删除元素后，minStack 也要考虑是否需要删除元素
#         # 否则的话，minStack 有可能保存一个 stack 中不存在的元素
#
#         # 首先，获取 minStack 的栈顶元素
#         top = self.min_stack[-1]
#
#         # 再判断 top 这个栈顶元素是否和 stack 移除的元素相等，如果相等，那么需要把 minStack 中的栈顶元素一并移除
#         if pop == top:
#             # 移除 min_stack 的栈顶元素
#             self.min_stack.pop()
#
#     def top(self)->int:
#         # 返回 stack 的栈顶元素
#         return self.stack[-1]
#
#     def getMin(self) -> int:
#         # 返回 min_stack 的栈顶元素
#         return self.min_stack[-1]
#
# # 测试代码:
# # 创建一个MinStack对象
# min_stack = MinStack()
#
# # 测试用例1: push一系列元素，然后测试getMin方法
# # min_stack.push(3)
# # min_stack.push(5)
# # min_stack.push(2)
# # min_stack.push(1)
# # print(min_stack.getMin())  # 应该输出 1
#
# # 测试用例2: push一系列元素后，连续pop，然后测试getMin方法
# min_stack.push(4)
# min_stack.push(2)
# print(min_stack.getMin())  # 应该输出 2

########################## D02-03 ###################################### 0010
# LC394. 字符串解码
# 预习和复习可以查看我的讲解视频。
# https://uha.xet.tech/s/3ndvbk
# 一、题目描述
# 给定一个经过编码的字符串，返回它解码后的字符串。
# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
# 示例 1：
# 输入：s = "3[a]2[bc]"
# 输出："aaabcbc"
# 示例 2：
# 输入：s = "3[a2[c]]"
# 输出："accaccacc"
# 示例 3：
# 输入：s = "2[abc]3[cd]ef"
# 输出："abcabccdcdcdef"
# 示例 4：
# 输入：s = "abc3[cd]xyz"
# 输出："abccdcdcdxyz"
# 提示：
# - 1 <= s.length <= 30
# - s 由小写英文字母、数字和方括号 '[]' 组成
# - s 保证是一个 有效 的输入。
# - s 中所有整数的取值范围为 [1, 300]

# class Solution:
#     def decodeString(self, s: str) -> str:
#         # 创建数字栈，在遍历编码字符串过程中记录出现的数字
#         numStack = []
#
#         # 创建字符栈，在遍历编码字符串过程中记录出现的字符串
#         strStack = []
#
#         # 在访问编码字符串的过程中，用来记录访问到字符串之前出现的数字，一开始为 0
#         digit = 0
#
#         # 在访问编码字符串的过程中，把得到的结果存放到 res 中
#         res = ""
#
#         # 从头到尾遍历编码字符串
#         for ch in s:
#
#             # 在遍历过程中，字符会出现 4 种情况
#             # 先获取此时访问的字符
#             # 1、如果是数字，需要把字符转成整型数字
#             # 注意数字不一定是 1 位，有可能是多位
#             # 比如  123a，在字母 a 的前面出现了 123，表示 a 重复出现 123 次
#             # 那么一开始 ch 为 1，当访问到 ch 为 2 的时候，1 和 2 要组成数字 12
#             # 再出现 3 ，12 和 3 组成数字 123
#             if '0' <= ch <= '9':
#
#                 # 先将字符转成整型数字 ch-‘0’
#                 # 补充知识：将字符'0'-'9'转换为数字，只需将字符变量减去'0'就行
#                 # 因为字符和数字在内存里都是以 ASCII 码形式存储的
#                 # 减去 '0' ，其实就是减去字符 '0' 的 ASCII 码，而字符 '0' 的 ASCII 码是 30
#                 # 所以减去'0'也就是减去30，然后就可以得到字符对应的数字了。
#                 num = int(ch)
#
#                 # 再将这个数字和前面存储的数字进行组合
#                 # 1 和 2 组成数字 12，也就是 1 * 10 + 2 = 12
#                 # 12 和 3 组成数字 123，也就是 12 * 10 + 3 = 123
#                 digit = digit * 10 + num
#
#                 # 2、如果是字符
#             elif ch >= 'a' and ch <= 'z':
#
#                 # 说明它就出现一次，可以直接存放到 res 中
#                 res += ch
#
#             # 3、如果是"["
#             # 出现了嵌套的内层编码字符串，而外层的解码需要等待内层解码的结果
#             # 那么之前已经扫描的字符需要存放起来，等到内层解码之后再重新使用
#             elif ch == '[':
#
#                 # 把数字存放到数字栈
#                 numStack.append(digit)
#
#                 # 把外层的解码字符串存放到字符串栈
#                 strStack.append(res)
#
#                 # 开始新的一轮解码
#                 # 于是，digit 归零
#                 digit = 0
#
#                 # res 重新初始化
#                 res = ""
#
#             # 4、如果是"]"
#             elif ch == ']':
#
#                 # 此时，内层解码已经有结果，需要把它和前面的字符串进行拼接
#
#                 # 第一步，先去查看内层解码的字符串需要被重复输出几次
#                 # 比如 e3[abc]，比如内层解码结果 abc 需要输出 3 次
#                 # 通过数字栈提取出次数
#                 count = numStack.pop()
#
#                 # 第二步，通过字符串栈提取出之前的解码字符串
#                 outString = strStack.pop()
#
#                 # 第三步，不断的把内层解码的字符串拼接起来
#                 for j in range(0, count):
#                     # 拼接到 outString 后面，拼接 count 次
#                     outString += res
#
#                 # 再把此时得到的结果赋值给 res
#                 res = outString
#
#         # 返回解码成功的字符串
#         return res

# 测试代码
# import unittest
#
#
# class TestSolution(unittest.TestCase):
#
#     def test_decodeString(self):
#         sol = Solution()
#         self.assertEqual(sol.decodeString("3[a]2[bc]"), "aaabcbc")  # 测试包含多个字符重复的情况
#         self.assertEqual(sol.decodeString("3[a2[c]]"), "accaccacc")  # 测试嵌套的情况
#         self.assertEqual(sol.decodeString("2[abc]3[cd]ef"), "abcabccdcdcdef")  # 测试多个重复字符和嵌套的情况
#
#
# if __name__ == '__main__':
#     unittest.main()


########################## D02-03 ###################################### 0010MmCopy
# JDT-LC394. 字符串解码   # JDT 经典题
# class Solution:
#     def decodeString(self,s:str)->str:
#         # numStack = list()
#         numStack = []
#         # strStack = list()
#         strStack = []
#         digit = 0
#         res = ''
#
#         for ch in s:
#             # if ch >= '0' and ch <= '9':
#             # if ch.isdigit():
#             if '0' <= ch <= '9':
#                 num = int(ch)
#                 digit = digit * 10 + num
#
#             # elif ch.isalpha():
#             elif 'a' <= ch <= 'z':
#                 res += ch
#
#             elif ch == '[':
#                 numStack.append(digit)
#                 strStack.append(res)
#                 digit = 0
#                 res = ''
#
#             elif ch == ']':
#                 count = numStack.pop()
#                 outString = strStack.pop()
#
#                 # for i in range(0,count):
#                 for _ in range(count):
#                     outString += res
#
#                 res = outString
#
#         return res
#
# # 测试代码
# # 创建一个Solution对象
# sol = Solution()
#
# # 测试用例1：解码字符串 "3[a]2[bc]"
# input_str1 = "3[a]2[bc]"
# output_str1 = sol.decodeString(input_str1)
# print(output_str1)  # 应该输出 "aaabcbc"
#
# # 测试用例2：解码字符串 "3[a2[c]]"
# input_str2 = "3[a2[c]]"
# output_str2 = sol.decodeString(input_str2)
# print(output_str2)  # 应该输出 "accaccacc"

########################## D02-04 ###################################### 0011
# LC224. 基本计算器
# 预习和复习可以查看我的讲解视频。
# https://uha.xet.tech/s/1PmkLa
# 一、题目描述
# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
# 示例 1：
# 输入：s = "1 + 1"
# 输出：2
# 示例 2：
# 输入：s = " 2-1 + 2 "
# 输出：3
# 示例 3：
# 输入：s = "(1+(4+5+2)-3)+(6+8)"
# 输出：23
# 提示：
# - 1 <= s.length <= 3 * 105
# - s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
# - s 表示一个有效的表达式

# 四、复杂度分析
# 时间复杂度：O(n)，其中 n 为字符串 s 的长度。需要遍历字符串 s 一次，计算表达式的值。
# 空间复杂度：O(n)，其中 n 为字符串 s 的长度。空间复杂度主要取决于栈的空间，栈中的元素数量不超过 n。
# 五、直接调API解法
# 如果上述内容实在学得吃力，但机试中又不幸遇到。可以直接使用内置函数eval()解题。内置函数eval()能够直接计算一个字符串表达式的值，能够识别加减乘除以及括号。
# s = input()
# print(eval(s))


# 基本计算器（ LeetCode 224 ）:https://leetcode-cn.com/problems/basic-calculator
# class Solution:
#     def calculate(self, s: str) -> int:
#
#         # 使用栈来储存字符串表达式中的数字
#         stack = list()
#
#         # 为了方便计算，所有的操作都视为加法操作
#         # 那么原先的减法操作就相当于是加一个负数
#         # 默认都是正数
#         sign = 1
#
#         # 保存计算的结果
#         res = 0
#
#         # 获取字符串的长度，然后获取里面的每个字符
#         length = len(s)
#
#         # 从 0 开始访问字符串中的每个字符
#         i = 0
#
#         # 获取字符串里面的每个字符
#         while i < length:
#             # 获取此时的字符
#             ch = s[i]
#
#             if ch == ' ':
#                 i += 1
#             # 如果当前字符是数字的话
#             elif ch.isdigit():
#                 # 那么把获取到的数累加到结果 res 上
#                 value = ord(s[i]) - ord('0')
#
#                 # 去查看当前字符的后一位是否存在
#                 # 如果操作并且后一位依旧是数字，那么就需要把后面的数字累加上来
#                 while i + 1 < length and s[i + 1].isdigit():
#                     i += 1
#                     value = value * 10 + ord(s[i]) - ord('0')
#
#                 # 那么把获取到的数累加到结果 res 上
#                 res += value * sign
#
#                 i += 1
#
#             # 如果是 '+'
#             elif ch == '+':
#                 # 那么说明直接加一个正数
#                 sign = 1
#
#                 i += 1
#
#             # 如果是 '-'
#             elif ch == '-':
#
#                 # 那么说明加一个负数
#                 sign = -1
#
#                 i += 1
#
#             # 如果是 '('
#             elif ch == '(':
#                 # 根据数学计算规则，需要先计算括号里面的数字
#                 # 而什么时候计算呢？
#                 # 遇到 ) 为止
#                 # 所以，在遇到 ) 之前需要把之前计算好的结果存储起来再计算
#                 # ( ) 直接的计算规则和一开始是一样的
#
#                 # 1、先把 ( 之前的结果存放到栈中
#                 stack.append(res)
#
#                 # 2、重新初始化 res 为 0
#                 res = 0
#                 # 3、把 ( 左边的操作符号存放到栈中
#                 # 比如如果是 5 - （ 2 + 3 ） ，那么就是把 -1 存放进去
#                 # 比如如果是 5 +（ 2 + 3 ） ，那么就是把 1 存放进去
#                 stack.append(sign)
#
#                 # 4、为了方便计算，所有的操作都视为加法操作
#                 # 那么原先的减法操作就相当于是加一个负数
#                 # 默认都是正数
#                 sign = 1
#
#                 i += 1
#
#                 # 如果是 ')'
#             elif ch == ')':
#
#                 # 那么就需要把栈中存放的元素取出来了
#                 # 在 ch == '（' 这个判断语句中，每次都会往栈中存放两个元素
#                 # 1、先存放左括号外面的结果
#                 # 2、再存放左括号外面的符号
#
#                 # 1、先获取栈顶元素，即左括号外面的符号，查看是 + 还是 -
#                 # 把栈顶元素弹出
#                 formerSign = stack.pop()
#
#                 # 2、再获取栈顶元素，即左括号结果
#                 # 把栈顶元素弹出
#                 formerRes = stack.pop()
#
#                 # 那结果就是括号外面的结果 + 括号里面的结果，至于是加正数还是负数，取决于左括号外面的符号
#                 res = formerRes + formerSign * res
#
#                 i += 1
#
#         # 返回计算好的结果
#         return res

# 测试代码
# import unittest
#
#
# class TestSolution(unittest.TestCase):
#
#     def test_calculate(self):
#         sol = Solution()
#         self.assertEqual(sol.calculate("1 + 1"), 2)  # 测试简单的加法
#         self.assertEqual(sol.calculate(" 2-1 + 2 "), 3)  # 测试带空格的减法和加法
#         self.assertEqual(sol.calculate("(1+(4+5+2)-3)+(6+8)"), 23)  # 测试带括号的复杂表达式
#
#
# if __name__ == '__main__':
#     unittest.main()

########################## D02-05 ###################################### 0012
# LC71. 简化路径
# 一、题目描述
# 给你一个字符串 path ，表示指向某一文件或目录的 Unix 风格 绝对路径 （以 '/' 开头），请你将其转化为更加简洁的规范路径。
# 在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..） 表示将目录切换到上一级（指向父目录）；两者都可以是复杂相对路径的组成部分。任意多个连续的斜杠（即，'//'）都被视为单个斜杠 '/' 。 对于此问题，任何其他格式的点（例如，'...'）均被视为文件/目录名称。
# 请注意，返回的 规范路径 必须遵循下述格式：
# - 始终以斜杠 '/' 开头。
# - 两个目录名之间必须只有一个斜杠 '/' 。
# - 最后一个目录名（如果存在）不能 以 '/' 结尾。
# - 此外，路径仅包含从根目录到目标文件或目录的路径上的目录（即，不含 '.' 或 '..'）。
# 返回简化后得到的 规范路径 。
# 示例 1：
# 输入：path = "/home/"
# 输出："/home"
# 解释：注意，最后一个目录名后面没有斜杠。
# 示例 2：
# 输入：path = "/../"
# 输出："/"
# 解释：从根目录向上一级是不可行的，因为根目录是你可以到达的最高级。
# 示例 3：
# 输入：path = "/home//foo/"
# 输出："/home/foo"
# 解释：在规范路径中，多个连续斜杠需要用一个斜杠替换。
# 示例 4：
# 输入：path = "/a/./b/../../c/"
# 输出："/c"
# 提示：
# - 1 <= path.length <= 3000
# - path 由英文字母，数字，'.'，'/' 或 '_' 组成。
# - path 是一个有效的 Unix 风格绝对路径。
# 二、题目解析
# 我们首先将给定的字符串  path 根据 / 分割成一个由若干字符串组成的列表，记为 names。根据题目中规定的「规范路径的下述格式」，names 中包含的字符串只能为以下几种：
# 1、空字符串。例如当出现多个连续的 /，就会分割出空字符串；
# 2、一个点  .；
# 3、两个点 ..；
# 4.只包含英文字母、数字或 _ 的目录名。
# 对于「空字符串」以及「一个点」，我们实际上无需对它们进行处理，因为「空字符串」没有任何含义，而「一个点」表示当前目录本身，我们无需切换目录。
# 对于「两个点」或者「目录名」，我们则可以用一个栈来维护路径中的每一个目录名。当我们遇到「两个点」时，需要将目录切换到上一级，因此只要栈不为空，我们就弹出栈顶的目录。当我们遇到「目录名」时，就把它放入栈。
# 这样一来，我们只需要遍历names 中的每个字符串并进行上述操作即可。在所有的操作完成后，我们将从栈底到栈顶的字符串用 / 进行连接，再在最前面加上/ 表示根目录，就可以得到简化后的规范路径。
# 三、参考代码
# class Solution:
#     def simplifyPath(self, path: str) -> str:
#
#         # 分割字符串为列表形式
#         names = path.split("/")
#         # / / /
#
#         # 利用栈来处理
#         stack = list()
#
#         # 访问列表里面的元素
#         for name in names:
#             print(name)
#             # 1、如果是 ..
#             if name == "..":
#                 # 在栈不为空的情况下
#                 if stack:
#                     # 弹出栈顶元素
#                     stack.pop()
#             # 2、如果是有效值
#             # 字母
#             elif name and name != ".":
#                 stack.append(name)
#         # stack = ['Python', 'World', 'Hello']
#         # new_string = '/ '.join(stack)
#         # print(new_string)
#         # 输出结果 Python/ World/ Hello
#         # 我们使用/ 作为分隔符，将栈stack中的元素连接成一个新的字符串。
#         # 每个元素之间使用/ 进行分隔，因此输出结果中每个元素都以/ 结尾（除了最后一个元素）。
#         return "/" + "/".join(stack)

# 测试代码
# import unittest
# class TestSolution(unittest.TestCase):
#
#     def test_simplifyPath(self):
#         sol = Solution()
#         self.assertEqual(sol.simplifyPath("/home/"), "/home")  # 测试简单路径
#         self.assertEqual(sol.simplifyPath("/a/./b/../../c/"), "/c")  # 测试包含特殊符号的路径
#         self.assertEqual(sol.simplifyPath("/../"), "/")  # 测试返回根目录
#
#
# if __name__ == '__main__':
#     unittest.main()

########################## D02-06 ###################################### 0013
# LC946. 验证栈序列
# 预习和复习可以查看我的讲解视频。
# https://uha.xet.tech/s/N5F05
# 一、题目描述
# 给定 pushed 和 popped 两个序列，每个序列中的 值都不重复，只有当它们可能是在最初空栈上进行的推入 push 和弹出 pop 操作序列的结果时，返回 true；否则，返回false 。
# 示例 1：
# 输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# 输出：true
# 解释：我们可以按以下顺序执行：
# push(1), push(2), push(3), push(4), pop() -> 4,
# push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
# 示例 2：
# 输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# 输出：false
# 解释：1 不能在 2 之前弹出。
# 提示：
# - 1 <= pushed.length <= 1000
# - 0 <= pushed[i] <= 1000
# - pushed 的所有元素 互不相同
# - popped.length == pushed.length
# - popped 是 pushed 的一个排列
# 二、题目解析
#
# 三、参考代码

# Java实现
# class Solution {
#     public boolean validateStackSequences(int[] pushed, int[] popped) {
#
#         // 利用栈来模拟入栈和出栈操作
#         Stack<Integer> s = new Stack<Integer>();
#
#         // index 表示 popped 数组中元素的下标
#         // 比如 popped 是 [4,5,3,2,1]
#         // 那么第 0 个下标元素是 4 这个数字
#         // 先去判断这个数字能否正常的出栈
#         int index = 0;
#
#         // 遍历 pushed 数组中的每个元素
#         for(int i = 0 ; i < pushed.length; i ++){
#
#             // 在遍历 pushed 数组时，把当前遍历的元素加入到栈中
#             s.push(pushed[i]);
#
#             // 加入完之后，不断的执行以下的判断
#             // 1、栈中是否有元素
#             // 2、栈顶元素是否和 popped 当前下标的元素相同
#             // 如果同时满足这两个条件
#             // 说明这个元素可以满足要求，即可以在最初空栈上进行推入 push 和弹出 pop 操作
#             while(!s.isEmpty() && popped[index] == s.peek()){
#
#                 // 那么就把栈顶元素弹出
#                 s.pop();
#
#                 // 同时 index++，观察 popped 下一个元素
#                 index++;
#             }
#         }
#
#         // 遍历完 pushed 数组中的每个元素之后，如果发现栈不为空
#         if(!s.isEmpty()){
#
#             // 那么说明出栈序列不合法，返回 false
#             return false;
#
#         }
#
#         // 否则返回 true
#         return true;
#
#     }
# }

# Python
# class Solution:
#     def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
#         # 利用列表来模拟入栈和出栈操作
#         stack = []
#
#         # index 表示 popped 数组中元素的下标
#         # 比如 popped 是 [4,5,3,2,1]
#         # 那么第 0 个下标元素是 4 这个数字
#         # 先去判断这个数字能否正常的出栈
#         index = 0
#
#         # 遍历 pushed 数组中的每个元素
#         for i in range(len(pushed)):
#             # 在遍历 pushed 数组时，把当前遍历的元素加入到列表中
#             stack.append(pushed[i])
#
#             # 加入完之后，不断的执行以下的判断
#             # 1、列表中是否有元素
#             # 2、列表末尾元素是否和 popped 当前下标的元素相同
#             # 如果同时满足这两个条件
#             # 说明这个元素可以满足要求，即可以在最初空列表上进行推入 push 和弹出 pop 操作
#             while stack and popped[index] == stack[-1]:
#                 # 那么就把列表末尾元素弹出
#                 stack.pop()
#
#                 # 同时 index++，观察 popped 下一个元素
#                 index += 1
#
#         # 遍历完 pushed 数组中的每个元素之后，如果发现列表不为空
#         if stack:
#             # 那么说明出栈序列不合法，返回 False
#             return False
#
#         # 否则返回 True
#         return True

# 测试代码
# import unittest
# class TestSolution(unittest.TestCase):
#
#     def test_validateStackSequences(self):
#         sol = Solution()
#         self.assertTrue(sol.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))  # 测试合法的出栈序列
#         self.assertFalse(sol.validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))  # 测试不合法的出栈序列
#         self.assertTrue(sol.validateStackSequences([1, 2, 3, 4, 5], [3, 2, 1, 5, 4]))  # 测试合法的出栈序列
#
# if __name__ == '__main__':
#     unittest.main()

########################## D02-07 ###################################### 0014
# 【栈】2023Q1A-投篮大赛
# 一、题目描述与示例
# 题目描述
# 你现在是一场采用特殊赛制投篮大赛的记录员。这场比赛由若干回合组成，过去几回合的得分可能会影响以后几回合的得分。比赛开始时，记录是空白的。你会得到一个记录操作的字符串列表 ops，其中 ops[i] 是你需要记录的第 i 项操作，ops 遵循下述规则：
# 1. 整数 x 表示本回合新获得分数 x
# 2. + 表示本回合新获得的得分是前两次得分的总和。
# 3. D 表示本回合新获得的得分是前一次得分的两倍。
# 4. C 表示本回合没有分数，并且前一次得分无效，将其从记录中移除。
# 请你返回记录中所有得分的总和。
# 输入
# 输入为一个字符串数组
# 输出描述
# 输出为一个整形数字
# 备注
# 1. 1 ≤ ops.length ≤ 1000
# 2. ops[i] 为 C、D、+，或者一个表示整数的字符串。整数范围是 [−3×10^4,3×10^4]
# 3. 需要考虑异常的存在，如有异常情况，请返回-1：
# 4. 对于 + 操作，题目数据不保证记录此操作时前面总是存在两个有效的分数
# 5. 对于 C 和 D 操作，题目数据不保证记录此操作时前面存在一个有效的分数
# 6. 题目输出范围不会超过整型的最大范围
# 示例一
# 输入
# 5 2 C D +
# 输出
# 30
# 说明
# 5 记录加 5 ，记录现在是 [5]
# 2 记录加 2 ，记录现在是 [5, 2]
# C 使前一次得分的记录无效并将其移除，记录现在是 [5].
# D 记录加 2 * 5 = 10 ，记录现在是 [5, 10].
# + 记录加 5 + 10 = 15 ，记录现在是 [5, 10, 15].
# 所有得分的总和 5 + 10 + 15 = 30
# 示例二
# 输入
# 5 -2 4 C D 9 + +
# 输出
# 27
# 说明
# 5 记录加 5 ，记录现在是 [5]
# -2 记录加 -2 ，记录现在是 [5, -2]
# 4 记录加 4 ，记录现在是 [5, -2, 4]
# C 使前一次得分的记录无效并将其移除，记录现在是 [5, -2]
# D 记录加 2 * -2 = -4 ，记录现在是 [5, -2, -4]
# 9 记录加 9 ，记录现在是 [5, -2, -4, 9]
# + 记录加 -4 + 9 = 5 ，记录现在是 [5, -2, -4, 9, 5]
# + 记录加 9 + 5 = 14 ，记录现在是 [5, -2, -4, 9, 5, 14]
# 所有得分的总和 5 + -2 + -4 + 9 + 5 + 14 = 27
# 示例三
# 输入
# 1
# 输出
# 1
# 示例四
# 输入
# +
# 输出
# -1
# 二、解题思路
# 注意，本题和LC682. 棒球比赛几乎完全一致。唯一的区别在于，本题需要考虑异常的存在，稍微增加了难度。
#
# 对于所有的输入，我们可以分为两类：
# 1. 数字
# 2. 操作符，包括"C"，"D"，"+"
#
# 这三种操作符，都是对最近的一次或两次得分进行操作。看到最近二字，我们应该马上想到使用后进先出LIFO的栈来解题，本质上也是一道表达式求值/化简类型的栈题。
#
# 我们首先构建一个空栈stack，然后遍历ops数组中的字符串record，对不同类型的record进行不同操作：
# 1. 遇到数字型字符串：直接数字入栈，要注意将字符串类型str转化为整数类型int。
# if record.isdigit():
#     stack.append(int(record))
# 2. 遇到"D"：将栈顶元素的两倍入栈，要注意判断此时栈中元素个数len(stack)是否大于等于1。
# if record == 'D' and len(stack) >= 1:
#     stack.append(stack[-1] * 2)
# 3. 遇到"C"：弹出栈顶元素，要注意判断此时栈中元素个数len(stack)是否大于等于1。
# if record == 'C' and len(stack) >= 1:
#     stack.pop()
# 4. 遇到"+"：将栈顶的前两个元素相加后入栈，要注意判断此时栈中元素个数len(stack)是否大于等于2。
# if record == '+' and len(stack) >= 2:
#     stack.append(stack[-1] + stack[-2])
# 5. 如果不满足上述的任何一个条件，则说明此时出现异常。应该输出-1。对于可能出现的异常，我们应该在最开始初始化一个标记isError = False，用于标记是否出现异常的标志，初始化为False表示最开始没有异常。当出现异常时，我们修改isError = True，并且break退出循环。
#
# 在循环体外，如果isError == True，说明出现了异常，应该直接输出-1，否则输出sum(stack)表示得分总和。
#
# 三、参考代码
# Java
# import java.util.*;
#
# public class Main {
#     public static void main(String[] args) {
#         Scanner scanner = new Scanner(System.in);
#
#         // 输入表示n个操作的数组ops
#         String[] ops = scanner.nextLine().split(" ");
#
#         Stack<Integer> stack = new Stack<>();  // 初始化一个空栈
#
#         boolean isError = false;  // 用于标记是否出现异常的标志，初始化为false表示没有异常
#
#         for (String record : ops) {
#             // 若record为数字，则直接将该数字加入栈中，注意要将字符串转为整数
#             if (!record.equals("D") && !record.equals("C") && !record.equals("+")) {
#                 stack.push(Integer.parseInt(record));
#             }
#             // 若record为'D'，且栈长度大于等于1，则在栈顶压入两倍的原栈顶值
#             else if (record.equals("D") && stack.size() >= 1) {
#                 stack.push(stack.peek() * 2);
#             }
#             // 若record为'C'，且栈长度大于等于1，则弹出栈顶元素
#             else if (record.equals("C") && stack.size() >= 1) {
#                 stack.pop();
#             }
#             // 若record为'+'，且栈长度大于等于2，则在栈顶压入原栈顶的两个值的和
#             else if (record.equals("+") && stack.size() >= 2) {
#                 int top1 = stack.pop();
#                 int top2 = stack.pop();
#                 stack.push(top2);
#                 stack.push(top1);
#                 stack.push(top1 + top2);
#             }
#             // 如果不满足上述的任何条件，说明出现了异常
#             // 将isError修改为true，同时直接退出循环
#             else {
#                 isError = true;
#                 break;
#             }
#         }
#
#         // 如果出现异常，输出-1
#         // 如果没有异常，输出整个栈中数字的总和
#         int sum = 0;
#         if (!isError) {
#             while (!stack.isEmpty()) {
#                 sum += stack.pop();
#             }
#         }
#         System.out.println(isError ? -1 : sum);
#
#         scanner.close();
#     }
# }

# python
# 题目：2023Q1A-投篮大赛
# 分值：100
# 算法：栈

# 输入表示n个操作的数组ops
# ops = input().split(" ")
#
# stack = list()      # 初始化一个空栈，在python中可以用list表示栈
# isError = False     # 用于标记是否出现异常的标志，初始化为False表示没有异常
#
# for record in ops:  # 遍历整个ops数组
#     # 若record为数字，则直接将该数字加入栈中，注意要将str转为int
#     if record != 'D' and record != 'C' and record != '+':
#         stack.append(int(record))
#     # 若record为'D'，且栈长度大于等于1，则在栈顶压入两倍的原栈顶值
#     elif record == 'D' and len(stack) >= 1:
#         stack.append(stack[-1] * 2)
#     # 若record为'C'，且栈长度大于等于1，则弹出栈顶元素
#     elif record == 'C' and len(stack) >= 1:
#         stack.pop()
#     # 若record为'+'，且栈长度大于等于2，则在栈顶压入原栈顶的两个值
#     elif record == '+' and len(stack) >= 2:
#         stack.append(stack[-1] + stack[-2])
#     # 如果不满足上述的任何条件，说明出现了异常，
#     # 将isError修改为True，同时直接退出循环
#     else:
#         isError = True
#         break
#
# # 如果出现异常，输出-1
# # 如果没有异常，输出整个栈中数字的总和
# print(-1 if isError else sum(stack))

# 时空复杂度
# 时间复杂度：O(N)。仅需一次遍历数组。
# 空间复杂度：O(N)。栈所占用的额外空间。

########################## D02-08 ###################################### 0015
# 【栈】2023Q1A-解压缩算法
# 一、题目描述与示例
# 题目描述
# 现需要实现一种算法，能将一组压缩字符串还原成原始字符串，还原规则如下：
# 1. 字符后面加数字 N，表示重复字符 N 次。例如：压缩内容为 A3，表示原始字符串为 AAA。
# 2. 花括号中的字符串加数字 N，表示花括号中的字符串重复 N 次。例如：压缩内容为{AB}3，表示原始字符串为 ABABAB。
# 3. 字符加 N 和花括号后面加 N，支持任意的嵌套，包括互相嵌套。例如：压缩内容可以{A3B1{C}3}3。
# 输入描述
# 输入一行压缩后的字符串
# 输出描述
# 输出压缩前的字符串
# 说明
# 输入输出的字符串区分大小写。
# 输入的字符串长度的范围为[1, 10000]，输出的字符串长度的范围为[1, 100000]，数字 N 范围[1, 10000]
# 示例一
# 输入
# A3
# 输出
# AAA
# 说明
# A3 代表 A 字符重复 3 次
# 示例二
# 输入
# {A3B1{C}3}3
# 输出
# AAABCCCAAABCCCAAABCCC
# 说明
# {A3B1{C}3}3 代表 A 字符重复 3 次，B 字符重复 1 次，花括号中的 C 字符重复 3 次，最外层花括号中的 AAABCCC 重复 3 次
# 二、解题思路
# 注意，本题和LC394. 字符串解码非常类似。区别在于，本题用花括号表示嵌套而不是中括号，数字出现在花括号之后而不是之前。由于数字出现在括号后，属于一种后缀表达式，而后缀表达式是更加适合栈的计算的，因此本题更加简单。
#
# 这题也属于括号配对和表达式求值综合起来的栈题。我们从前往后一次遍历原始字符串s中的字符ch，存在以下几种情况：
# 1. 遇到字母，入栈
# 2. 遇到左括号"{"，入栈，作为解压标识符
# 3. 遇到右括号"}"，说明在此之前肯定存在一个左括号已经入栈，我们需要考虑这对括号之间的所有字符串，并且把这些字符串都合并在一起。所以我们要反复地弹出栈顶元素并记录在一个新的字符串str_in_bracket中，直到遇到左括号"{"，
# 4. 遇到数字，说明数字之前的字符串需要被重复，需要记录这个数字。
#
# 对于前两种入栈的情况，我们可以合并代码，即
# if ch == "{" or ch.isalpha():
#     stack.append(ch)
#
# 对于遇到右括号"}"的情况，代码如下：
# if ch == "}":
#     str_in_bracket = str()
#     while(stack[-1] != "{"):
#         str_in_bracket = stack.pop() + str_in_bracket
#     stack.pop()    # 此时栈顶元素是"{"，直接弹出
#     stack.append(str_in_bracket)
#
# 对于遇到数字的情况，有两个地方需要考虑：
# 1. 数字num的位数超过1位，如何储存数字。以下代码能够储存位数超过1的数字。
# num = num * 10 + int(ch)
# 2. 数字什么时候要使用。当一个数字num已经被完全储存，则应该使栈顶的字符串stack[-1]重复num次。这里的判断逻辑是，ch的下一位已经不是数字，或者ch已经到达s的尾部，说明数字已经储存完毕。
# if i == len(s)-1 or not s[i+1].isdigit():
#     stack[-1] *= num
#     num = 0
# 另外要注意，数字num使用完毕之后，需要重置为0。
# 上述代码整理后得到：
# if ch.isdigit():
#     num = num * 10 + int(ch)
#     if i == len(s)-1 or not s[i+1].isdigit():
#         stack[-1] *= num
#         num = 0
#
#
# 三、代码
# Java
# import java.util.*;
#
# public class Main {
#     public static void main(String[] args) {
#         Scanner scanner = new Scanner(System.in);
#         String s = scanner.next();
#
#         Stack<String> stack = new Stack<>();
#         int num = 0;
#
#         for (int i = 0; i < s.length(); i++) {
#             char ch = s.charAt(i);
#
#             if (Character.isDigit(ch)) {
#                 num = num * 10 + (ch - '0');
#                 if (i == s.length() - 1 || !Character.isDigit(s.charAt(i + 1))) {
#                     int repeat = num;
#                     num = 0;
#                     String top = stack.pop();
#                     StringBuilder repeated = new StringBuilder();
#                     while (repeat-- > 0) {
#                         repeated.append(top);
#                     }
#                     stack.push(repeated.toString());
#                 }
#             } else if (ch == '{' || Character.isLetter(ch)) {
#                 stack.push(String.valueOf(ch));
#             } else if (ch == '}') {
#                 StringBuilder strInBracket = new StringBuilder();
#                 while (!stack.isEmpty() && !stack.peek().equals("{")) {
#                     strInBracket.insert(0, stack.pop());
#                 }
#                 stack.pop();
#                 stack.push(strInBracket.toString());
#             }
#         }
#
#         StringBuilder result = new StringBuilder();
#         while (!stack.isEmpty()) {
#             result.insert(0, stack.pop());
#         }
#
#         System.out.println(result.toString());
#     }
# }



# python
# 题目：2023Q1A-解压缩算法
# 分值：200
# 算法：栈

# s = input()
# stack = list()  # 初始化一个栈，在python中可以用list代替栈
# num = 0         # 初始化一个变量num为0，用于栈中数字的记录
#
# # 遍历整个字符串s
# for i, ch in enumerate(s):
#     # 遇到数字，进行数字的计算
#     if ch.isdigit():
#         # num乘10后加上int(ch)
#         num = num * 10 + int(ch)
#         # 如果i是s的最后一位索引，或者i的下一个位置i+1不是数字
#         if i == len(s)-1 or not s[i+1].isdigit():
#             # 那么需要令栈顶字符串重复num次
#             stack[-1] *= num
#             # 由于num已经使用完毕，需要重置num为0
#             num = 0
#     # 遇到左括号"{"或者字母，入栈
#     elif ch == "{" or ch.isalpha():
#         stack.append(ch)
#     # 遇到右括号"}"，说明前面必然存在一个左括号与其闭合
#     # 将栈顶元素不断弹出，弹出的内容构建成一个新的字符串str_in_bracket
#     # 直到遇到与其闭合的左括号，将str_in_bracket重新加入栈顶
#     elif ch == "}":
#         # 初始化该对闭合括号内的字符串str_in_bracket
#         str_in_bracket = str()
#         # 不断弹出栈顶元素，直到栈顶元素为一个左括号"{"
#         while(stack[-1] != "{"):
#             # 将弹出的元素加在str_in_bracket的前面
#             str_in_bracket = stack.pop() + str_in_bracket
#         # 把左括号弹出
#         stack.pop()
#         # 把str_in_bracket重新加入栈顶
#         stack.append(str_in_bracket)
#
# # 最后需要将栈中的所有字符串再用join()方法合并在一起并输出
# print("".join(stack))

# 时空复杂度
# 时间复杂度：O(N)。仅需一次遍历数组，每一个字符最多出入栈各一次。
# 空间复杂度：O(N)。栈所占用的额外空间。


### D03 哈希表（python中对应字典） ###
# python中，字典dic是特殊的哈希表  哈希表是无序的
# 八股点：哈希（字典）的键必须是不可变类型，例如字符、数字等；元组不可变 所以可以作为字典的键；列表、字典可变  所以不能作为字典的键
# 字典中的键必须各不相同
# 特殊算法技巧：某些情况下，可以使用列表代替哈希表
# 哈希集合 存储数据值，即存储元素 不是存储键值对  哈希集合中的值是不同的 无序的
# python中，用set实现哈希集合
# 可哈希的：指的是所储存的元素不可以被修改  不可变 哈希表中的键、哈希集合中的元素都是可哈希的  不可以被修改的


# 统计元素频率的题  虽然dic可以解  但是不建议用dic  最好还是用counter
# 只要出现统计次数，就使用hash表的counter类来实现

# LC：leetCode  HJ：牛客网

########################## D03-01 ###################################### 0016
# LC217. 存在重复元素
# 视频地址。
# https://uha.xet.tech/s/7Av8z
# 一、题目描述
# 给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false 。
# 示例 1：
# 输入：nums = [1,2,3,1]
# 输出：true
# 示例 2：
# 输入：nums = [1,2,3,4]
# 输出：false
# 示例 3：
# 输入：nums = [1,1,1,3,3,4,3,2,4,2]
# 输出：true
# 提示：
# - 1 <= nums.length <= 10^5
# - -10^9 <= nums[i] <= 10^9
# 二、题目解析
# 三、参考代码

# 代码一
# 哈希集合调API讨巧解法
# 题目：LC217. 存在重复元素
# 难度：简单
# 作者：闭着眼睛学数理化
# 算法：哈希集合调API讨巧解法
# 代码看不懂的地方，请直接在群上提问

# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         return (len(set(nums)) != len(nums))
# 对上述代码的注释：
# 由于哈希集合具有不包含重复元素的性质，
# 如果nums列表中存在重复元素，将其转换成哈希集合后长度必然减少
# 所以我们只需要判断set(nums)的长度和nums的长度是否一致即可得到答案
# 如果长度一致，则返回False，说明nums不包含重复元素
# 如果长度不一致，则返回True，说明nums包含重复元素

# 代码二
# 哈希集合遍历解法
# 1. Java 代码

# // 登录 AlgoMooc 官网获取更多算法图解
# // https://www.algomooc.com
# // 作者：程序员吴师兄
# // 微信：wzb_3377
# // 代码有看不懂的地方一定要私聊咨询吴师兄呀
# // 存在重复元素（LeetCode 217）:https://leetcode.cn/problems/contains-duplicate/
# class Solution {
#     public boolean containsDuplicate(int[] nums) {
#
#         // 使用数据结构 set 来存放 nums 里面的所有数字
#         Set<Integer> set = new HashSet<>();
#
#         // 遍历数组
#         for (int num: nums) {
#
#             // 如果数字已经存在于 set 中，直接返回 true
#             if (set.contains(num)) {
#                 return true;
#             }
#
#             // 把元素添加到 set 中
#             set.add(num);
#         }
#
#         // 如果成功遍历完数组，则表示没有重复元素，返回 false
#         return false;
#     }
# }

# 2. Python 代码
# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         # 使用数据结构 set 来存放 nums 里面的所有数字
#         pre = set()
#         # 遍历数组
#         for num in nums:
#             # 如果数字已经存在于 set 中，直接返回 true
#             if num in pre:
#                 return True
#             # 把元素添加到 set 中
#             pre.add(num)
#         # 如果成功遍历完数组，则表示没有重复元素，返回 false
#         return False
# 测试代码
# import unittest
# class TestContainsDuplicate(unittest.TestCase):
#
#     def test_contains_duplicate(self):
#         sol = Solution()
#         self.assertTrue(sol.containsDuplicate([1, 2, 3, 1]))  # 有重复元素1
#         self.assertFalse(sol.containsDuplicate([1, 2, 3, 4]))  # 没有重复元素
#         self.assertTrue(sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # 有重复元素1, 3, 4, 2
#
# if __name__ == '__main__':
#     unittest.main()


########################## D03-02 ###################################### 0017
# LC349. 两个数组的交集
# 视频地址。
# https://uha.xet.tech/s/4pkrpU
# 一、题目描述
# 给定两个数组 nums1 和 nums2 ，返回 它们的交集 。输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序 。
# 示例 1：
# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2]
# 示例 2：
# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[9,4]
# 解释：[4,9] 也是可通过的
# 提示：
# - 1 <= nums1.length, nums2.length <= 1000
# - 0 <= nums1[i], nums2[i] <= 1000
# 二、题目解析
# 三、参考代码
# 方法一
# 哈希集合调API解法

# 题目：LC349. 两个数组的交集
# 难度：简单
# 作者：闭着眼睛学数理化
# 算法：哈希集合调API
# 代码看不懂的地方，请直接在群上提问
# class Solution:
#     def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
#         # set(nums1) & set(nums2)代码的作用：
#         # 这段代码`set(nums1) & set(nums2)`的作用是将列表`nums1`和`nums2`转换为集合，然后使用` & ` 运算符找到这两个集合的交集。
#         # 具体解释如下：
#         # -  `set(nums1)`: 将列表`nums1`转换为集合。这将消除`nums1`中的重复元素。
#         # -  `set(nums2)`: 将列表`nums2`转换为集合。这将消除`nums2`中的重复元素。
#         # -  ` & ` ： ` & ` 运算符用于找到两个集合的交集，即返回一个新的集合，其中只包含同时存在于`nums1`和`nums2`中的元素。
#         # 因此，表达式
#         # `set(nums1) & set(nums2)`将得到一个集合，其中只包含同时存在于`nums1`和`nums2`中的元素，实际上是找到这两个列表中的共同元素，同时去除重复项。
#         return list(set(nums1) & set(nums2))
# 上述代码注释：
# 先将两个数组nums1和nums2用set(nums1)和set(nums2)转化为哈希集合
# 再使用两个集合的取交集操作&，得到set(nums1)和set(nums2)的交集
# 由于题目要求返回一个列表，我们还需要把交集再转化为list()，即可返回

# 哈希集合遍历解法
# class Solution:
#     def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
#         # 先获得nums1对应的哈希集合
#         nums1_set = set(nums1)
#         # 构建一个答案集合，初始化为空
#         ans_set = set()
#
#         # 遍历nums2中的元素num
#         for num in nums2:
#             # 如果num位于nums1对应的哈希集合nums1_set中
#             if num in nums1_set:
#                 # 则说明num同时位于nums1和nums2中
#                 # 将其加入ans_set
#                 ans_set.add(num)
#
#         # 最后将ans_set转化为列表后返回
#         return (list(ans_set))

# 时空复杂度
# 时间复杂度：O(m+n)。nums1和nums2各自需要遍历一次。
# 空间复杂度：O(m+n)。两个哈希集合所占用的空间。

# 方法二*
# 排序+双指针解法（暂不要求掌握）
# class Solution:
#     def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
#         # 首先对两个数组进行排序
#         nums1.sort()
#
#         nums2.sort()
#
#         # 计算出两个数组的长度
#         length1 = len(nums1)
#
#         length2 = len(nums2)
#
#         # 两个数组的交集结果数组长度必然是小于等于最短数组的长度
#         res = list()
#
#         # 设置三个索引指针
#
#         # index 指向结果数组 res ，每当 index 指向的位置填充了元素就向后移动
#         # index = 0
#
#         # index1 指向数组 nums1 中的元素，将该元素和 index2 指向数组 nums2 中的元素进行比较
#         index1 = 0
#
#         # index2 指向数组 nums2 中的元素，将该元素和 index1 指向数组 nums1 中的元素进行比较
#         index2 = 0
#
#         # 移动 index1 和 index2
#         while index1 < length1 and index2 < length2:
#
#             # 获取 index1 指向的元素值
#             num1 = nums1[index1]
#
#             # 获取 index2 指向的元素值
#             num2 = nums2[index2]
#
#             # num1 和 num2 的大小关系有三种
#
#             # 1、num1 == num2
#             if num1 == num2:
#
#                 # 由于输出结果中的每个元素一定是 【唯一】 的，所以要做一下判断
#                 # 如果 res 中的 index 在起始位置，说明还没有存放元素
#                 # 那么这个相等的元素可以存放到 res 中
#
#                 # 如果 res 中的 index 不在起始位置
#                 # 当它前面存放的元素并不是现在想要存放的元素
#                 # 那么这个相等的元素可以存放到 res 中
#                 if not res or num1 != res[-1]:
#                     res.append(num1)
#
#                 # 移动 index1 ，比较其它元素
#                 index1 += 1
#                 # 移动 index2 ，比较其它元素
#                 index2 += 1
#
#             # 2、num1 < num2
#             elif num1 < num2:
#
#                 # 由于两个数组已经排序了，说明此时 num1 肯定会小于 nums2 数组中 num2 后面所有的数
#                 # 那 num1 肯定是无法在 nums2 中找到相等的元素
#                 # 移动 index1 ，比较其它元素
#                 index1 += 1
#
#             # 3、num1 > num2
#             else:
#
#                 # 由于两个数组已经排序了，说明此时 num2 肯定会小于 nums1 数组中 num1 后面所有的数
#                 # 那 num2 肯定是无法在 nums1 中找到相等的元素
#                 # 移动 index2 ，比较其它元素
#                 index2 += 1
#
#         # 最后返回结果数组中有值的那些元素就行
#         return res

# 时空复杂度
# 时间复杂度：O(mlogm+nlogn)。两数组快排时间复杂度分别是O(mlogm)、O(nlogn)，双指针遍历需要O(m+n)，复杂度取决于较大的O(mlogm+nlogn)。
# 空间复杂度：O(logm+logn)。排序使用的额外空间。


########################## D03-03 ###################################### 0018
# LC242. 有效的字母异位词
# 视频地址。
# https://uha.xet.tech/s/3ev2qz
# 一、题目描述
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
# 注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。
# 示例 1:
# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 示例 2:
# 输入: s = "rat", t = "car"
# 输出: false
# 提示:
# - 1 <= s.length, t.length <= 5 * 104
# - s 和 t 仅包含小写字母
# 进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
# 二、题目解析
# 题目讲的是让你判断两个字符串中的字母是否一致，比如 示例1 中，s  包含字母 a、n、g、r、m，而 t 中也包含 a、n、g、r、m ，都是只有这五个字母，并且 频次 相同，只是顺序不同。
# 看到 频次 这个词，你脑海中第一想法是什么？
# 没错，就是 哈希表 ！
# 解法思路很简单。
# 1、首先先判断两个字符串长度是否相同，不相同直接返回 false
# 2、然后把 s 中所有的字符出现个数使用 计数器 统计起来，存入一个大小为 26 的数组中（注意题目的说明）
# 3、最后再来统计 t 字符串，即遍历 t 时将对应的字母频次进行减少，如果期间  计数器  出现小于零的情况，则说明 t 中包含一个不存在于 s 中的字母，直接返回 false。
# 4、最后检查计数器是否归零。
# 三、参考代码
# 代码一
# 哈希集合调API讨巧解法

# 题目：LC242. 有效的字母异位词
# 难度：简单
# 作者：闭着眼睛学数理化
# 算法：哈希集合调API讨巧解法
# 代码看不懂的地方，请直接在群上提问

# 导入collections中的Counter计数器类
# from collections import Counter
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return Counter(s) == Counter(t)
# 上述代码注释：
# 直接获得s和t的计数结果Counter(s)和Counter(t)
# 若两者相等，说明s和t中的元素以及频率完全一致，互为字母异位词
# 若两者不相等，说明s和t中的元素以及频率不完全一致，不是一组有效的字母异位词

# 代码二
# 哈希集合遍历解法

# 题目：LC242. 有效的字母异位词
# 难度：简单
# 作者：闭着眼睛学数理化
# 算法：哈希集合遍历解法
# 代码看不懂的地方，请直接在群上提问

# 导入collections中的Counter计数器类
# from collections import Counter
#
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         # 如果两个字符串长度不同，必然不可能构成一组有效的字母异位词，返回False
#         if len(s) != len(t):
#             return False
#         # 使用Counter()计数器，得到两个字符串对应的哈希表
#         cnt1, cnt2 = Counter(s), Counter(t)
#         # 遍历cnt1中的键（即某个特定字符）
#         for ch in cnt1:
#             # 如果这个字符在cnt1中的频率和在cnt2中的频率不相等
#             if cnt1[ch] != cnt2[ch]:
#                 # 返回False
#                 return False
#         # 如果在上述循环中没有返回False，说明这两个字符串互为字母异位词
#         return True

# 代码三
# 用列表表示哈希表进行统计
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#
#         # 如果两个字符串的长度都不一致，那么肯定是无法成为字母异位词的
#         if len(s) != len(t):
#             # 直接返回 False
#             return False
#
#         # 让 a - z 这 26 个字母对应的下标变成 0 - 25 方便存到数组中
#         # 比如 a 对应的索引就是 0
#         # b 对应的索引就是 1
#         table = [0] * 26
#
#         # 从头到尾遍历字符串 s
#         for i in s:
#             # 把访问的字符转换为整数的形式
#             # 比如访问字母 a，那么 -'a' 之后就是 0，就是 a 对应的索引为 0
#             index = ord(i) - ord('a')
#
#             # 那么意味着这个字母出现的频次需要加 1
#             table[index] += 1
#
#         for i in t:
#
#             # 把访问的字符转换为整数的形式
#             # 比如访问字母 a，那么 -'a' 之后就是 0，就是 a 对应的索引为 0
#             index = ord(i) - ord('a')
#
#             # 那么意味着这个字母出现的频次需要减 1
#             table[index] -= 1
#
#             # 如果说发现这个字母出现的频次小于了 0
#             # 说明 t 中出现了 s 中不曾用的字母
#             if table[index] < 0:
#                 # 那就不是字母异位词
#                 return False
#
#         # 否则，说明是字母异位词
#         return True
# 复杂度分析
# - 时间复杂度：O(n)，其中 n 为 s 的长度。
# - 空间复杂度：O(S)，其中 S 为字符集大小，此处 S = 26 。


########################## D03-04 ###################################### 0019
# LC383. 赎金信（HJ81. 字符串字符匹配）
# 视频地址。
# https://uha.xet.tech/s/3J5UKp
# 一、题目描述
# 给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。
# 如果可以，返回 true ；否则返回 false 。
# magazine 中的每个字符只能在 ransomNote 中使用一次。
# 示例 1：
# 输入：ransomNote = "a", magazine = "b"
# 输出：false
# 示例 2：
# 输入：ransomNote = "aa", magazine = "ab"
# 输出：false
# 示例 3：
# 输入：ransomNote = "aa", magazine = "aab"
# 输出：true
# 提示：
# - 1 <= ransomNote.length, magazine.length <= 10^5
# - ransomNote 和 magazine 由小写英文字母组成
# 二、题目解析
# 三、参考代码
# 方法一
# 哈希集合遍历解法

# 题目：LC383. 赎金信
# 难度：简单
# 作者：闭着眼睛学数理化
# 算法：哈希集合遍历解法
# 代码看不懂的地方，请直接在群上提问

# 导入collections中的Counter计数器类，使用dict()也可以但是代码就要多一些判断
# from collections import Counter
# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         # 用两个哈希表保存R和M两个字符串中所有元素出现的频率
#         cnt_R, cnt_M = Counter(ransomNote), Counter(magazine)
#
#         # 由于要计算R是否能够被M完全包含，所以我们要遍历R中的字符
#         # 遍历cnt_R中的所有字符
#         for ch in cnt_R:
#             # 如果发现ch在R中的数目大于在M中的数目，则返回False
#             if cnt_R[ch] > cnt_M[ch]:
#                 return False
#
#         # 成功退出循环，返回True
#         return True

# 方法二
# 用列表表示哈希表进行统计
# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         # 手动设置哈希表
#         # 这里的哈希表的作用是计数器
#         # 由于小写字母的个数为 26 个，所以数组大小为 26
#         # 上一行这里吴师兄的注释有问题，这种声明方式声明的变量cnt是个列表，而不是数组； python原生数据结构只有列表和元组，没有数组，使用数组需要导入numpy库
#         # 不过 似乎 对普通用户和出题解题而言  可以将数组理解为列表  列表理解为数组
#         cnt = [0] * 26
#
#         # 记录 magazine 里字母出现的次数
#         for ch in magazine:
#             # 对于数组类型，其下标为 int 类型
#             # 可以直接使用 char 类型变量，默认强制转换，存储的就是字母对应的 ASCII 码
#             # 比如 ch 是 b 字符，那么 b - a = 1，即 needs[1] 表示记录 b 出现的频次
#             idx = ord(ch) - ord('a')
#             cnt[idx] += 1
#
#         # 再用 ransomNote 去验证这个数组是否包含了 ransomNote 所需要的所有字母
#         for ch in ransomNote:
#             # 在遍历过程中，每遍历一个字母，对应的频次减 1
#             cnt[ord(ch) - ord('a')] -= 1
#
#             # 如果发现某个字母的频次小于了 0
#             # 说明在 ransomNote 中出现了 magazine 未曾有的字母
#             # 即 ransomNote 不能由 magazine 里面的字符构成
#             if cnt[ord(ch) - ord('a')] < 0:
#                 return False
#
#         # 说明可以，返回 true
#         return True

# 测试：
# s = 'dfasfd'
# cnt = Counter(s)
# print(cnt.items())
# print(cnt.keys())
# print(cnt.values())
# min_cnt = min(cnt.values())

# 输出：
# dict_items([('d', 2), ('f', 2), ('a', 1), ('s', 1)])
# dict_keys(['d', 'f', 'a', 's'])
# dict_values([2, 2, 1, 1])


########################## D03-05 ###################################### 0020
# 【哈希表】2023Q1A-集五福
# 题目描述与示例
# 集五福
# 题目描述
# 集五福作为近年来大家喜闻乐见迎新春活动，集合爱国福、富强福、和谐福、友善福、敬业福即可分享超大红包。
# 以 0 和 1 组成的长度为 5 的字符串代表每个人所得到的福卡，每一位代表一种福卡，1 表示已经获得该福卡，
# 单类型福卡不超过 1 张，随机抽取一个小于 10 人团队，求该团队最多可以集齐多少套五福？
#
# 输入描述
# 输入若干个由0、1组成的长度等于5的字符串，代表团队中每个人福卡获得情况
# 注意1：1人也可以是一个团队
# 注意2：1人可以有0到5张福卡，但福卡不能重复
# 输出描述
# 输出该团队最多能凑齐多少套五福
# 示例一
# 输入
# 11001,11101
# 输出
# 0
# 示例二
# 输入
# 11101,10111
# 输出
# 1
# 解题思路
# 一共有五种不同的福卡，假设我们按照在长度等于5的字符串中的索引给这些福卡编号，即分别有0 1 2 3 4一共5种福卡。我们直接统计整个团队中，每种福卡的个数，而能够凑齐的福卡的套数，由数目最少的那一种福卡的数目来决定。
#
# 为了统计每一种福卡的个数，我们既可以使用哈希表来完成，也可以使用一个长度为5的列表来完成。这两种计数方式没有本质区别。
#
# 本题显然也是哈希表在【统计元素频率】类型的题目中的典型应用。
#
# 代码
# 代码一
# 用哈希表进行统计
# 题目：2023Q1A-集五福
# 分值：100
# 作者：闭着眼睛学数理化
# 算法：哈希表
# 代码看不懂的地方，请直接在群上提问

# 导入collections中的Counter计数器类，使用dict()也可以但是代码就要多一些判断
# from collections import Counter
# # 团队数组，包含了n个字符串，表示每个人拥有的五福
# team = input().split(",")
# # 用于统计团队中各种五福个数的长度为的哈希表
# cnt = Counter()
#
# # 遍历团队中的每一个人
# for person in team:
#     # 遍历每一个人拥有的五福
#     for i, num in enumerate(person):
#         # 如果这个人拥有第i个五福，那么计数+1
#         if num == "1":
#             cnt[i] += 1
#
# # 整个团队中最少的那个五福的数目，决定了能凑齐五福的套数
# # 要注意：如果哈希表长度小于5，说明有某个福字的数量为0，应该输出0
# print(0) if len(cnt) < 5 else print(min(cnt.values()))

# 代码一变体，用dic代替counter实现，不推荐用这种方式，只是作为一个演示：
# team = input().split(",")
# dic = dict()
#
# for person in team:
#     for i,card in enumerate(person):
#         # 必须要这样为dic做判断，否则dic[i]会报错keyError # 这里的讲解 需要回看视频再理一下
#         if i not in dic:
#             dic[i] = int(card)
#         else:
#             dic[i] += int(card)
# print(min(dic.values()))

# 代码二
# 用列表表示哈希表进行统计
# # 题目：2023Q1A-集五福
# # 分值：100
# # 作者：闭着眼睛学数理化
# # 算法：用列表表示哈希表
# # 代码看不懂的地方，请直接在群上提问
#
# # 团队数组，包含了n个字符串，表示每个人拥有的五福
# team = input().split(",")
# # 用于统计团队中各种五福个数的长度为5的列表
# cnt = [0] * 5
#
# # 遍历团队中的每一个人
# for person in team:
#     # 遍历每一个人拥有的五福
#     for i, num in enumerate(person):
#         # 如果这个人拥有第i个五福，那么计数+1
#         if num == "1":
#             cnt[i] += 1
#
# # 整个团队中最少的那个五福的数目，决定了能凑齐五福的套数
# print(min(cnt))
#
# 时空复杂度
# 时间复杂度：O(N)。仅需一次遍历字符串数组。
# 空间复杂度：O(1)。无论是哈希表还是列表，长度最多为5，为常数级别空间。

########################## D03-06 ###################################### 0021
# 【哈希表】2023Q1A-删除最少字符
# 题目描述与示例
# 题目
# 删除字符串s中出现次数最少的字符，如果多个字符出现次数一样则都删除。
# 输入
# 输入只包含小写字母
# 输出描述
# 输出删除后剩余的字符串；若删除后字符串长度为0，则输出字符串"empty"
# 示例一
# 输入
# abcdd
# 输出
# dd
# 示例二
# 输入
# aabbccdd
# 输出
# empty
# 解题思路
# 为了删除掉字符串s中出现次数最少的字符，我们必须先统计s中的所有字母的出现个数，很容易想到使用哈希表的Counter()来完成这个功能。
# 然后我们再统计哪些字母出现的次数为最小出现次数，用一个哈希集合记录这些需要删除的字母，再使用字符串的replace()方法或者join()方法即可完成删除。
#
# 本题显然也是哈希表在统计元素频率类型的题目中的典型应用。
#
# 代码
# Python
# 推导式代码简便 理解复杂的写法

# 题目：2023Q1A-删除最少字符
# 分值：100
# 作者：闭着眼睛学数理化
# 算法：哈希表
# 代码看不懂的地方，请直接在群上提问

# # 导入collections中的Counter计数器类，使用dict()也可以，但是代码就要多一些判断
# from collections import Counter
#
# # 输入原始字符串s
# s = input()
#
# # 直接调用Counter()计数器类，获得所有字符的频率
# cnt = Counter(s)
#
# # 获得所有频率中的最小值，即最小频率min_cnt
# min_cnt = min(cnt.values())
#
# # 如果某个字符ch的频率等于最小频率，则记录在哈希集合min_cnt_set中
# min_cnt_set = set(ch for ch, ch_cnt in cnt.items() if ch_cnt == min_cnt)
#
# # 再次遍历s中的所有字符ch，如果ch不位于哈希集合min_cnt_set中，则可以保留，储存在ans数组中
# ans = [ch for ch in s if ch not in min_cnt_set]
#
# # 如果ans的长度为0，说明所有字符均被删除，此时需要输出"empty"
# # 否则，则用字符串的join()方法，将ans数组转化为字符串并输出
# print("empty" if len(ans) == 0 else "".join(ans))


# 常规写法（易于理解）
# from collections import Counter
# s = input()
# cnt = Counter(s)
# min_cnt = min(cnt.values())
#
# print(cnt)
# print(min_cnt)
#
# del_set = set()
# for ch ,num in cnt.items():
#     if num == min_cnt:
#         del_set.add(ch)
#
# print(del_set)
#
# ans = list()
# for ch in s:
#     if ch not in del_set:
#         ans.append(ch)
# print("".join(ans))

# 可以换一种写法
# ans = str()
# for ch in s:
#      if ch not in del_set:
#           ans += ch
# print(ans)

# 时空复杂度
# 时间复杂度：O(N)。仅需一次遍历字符串数组。
# 空间复杂度：O(1)。无论是哈希表还是列表，长度最多为26，为常数级别空间。


########################## D03-07 ###################################### 0022
# LC387. 字符串中的第一个唯一字符
# 视频地址 https://uha.xet.tech/s/ZpcpL
# 一、题目描述
# 给定一个字符串 s ，找到 它的第一个不重复的字符，并返回它的索引 。如果不存在，则返回 -1 。
# 示例 1：
# 输入: s = "leetcode"
# 输出: 0
#
# 示例 2:
# 输入: s = "loveleetcode"
# 输出: 2
#
# 示例 3:
# 输入: s = "aabb"
# 输出: -1
# 提示:
# - 1 <= s.length <= 10^5
# - s 只包含小写字母
# 二、参考代码

# 本题涉及到 Python 的一些语法知识
# Python常用内置函数、方法、技巧汇总
# https://og7kl7g6h8.feishu.cn/docx/AbbMdd4YHoGeQRxRGKJcJZs6nDb

# from collections import Counter
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         # Counter 可以直接统计字符串、列表等可迭代对象的元素频率
#         # s = "leetcode"
#         # cnt = Counter({'e': 3, 'l': 1, 't': 1, 'c': 1, 'o': 1, 'd': 1})
#         cnt = Counter(s)
#         print(cnt)
#
#         # 如果想在for循环中同时获得列表的索引 i 和元素值 v
#         # 可以使用枚举内置函数 enumerate()
#         for i, ch in enumerate(s):
#             # 如果找到了某个字符出现的频率为 1
#             if cnt[ch] == 1:
#                 # 返回它的下标即可
#                 return i  # return会跳出函数 找到了那个 就是第1个不重复的 跳出函数即可
#
#         # 如果不存在，则返回 -1
#         return -1

# sol = Solution()
# print(sol.firstUniqChar('leetcode'))


########################## D03-08 ###################################### 0023
# LeetCode 350、两个数组的交集II
# 视频地址：
# 一、题目描述
# 给你两个整数数组nums1和nums2 ，请你以数组形式返回两数组的交集。
# 返回结果中每个元素出现的次数，应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。可以不考虑输出结果的顺序。
#
# 示例
# 1：
# 输入：nums1 = [1, 2, 2, 1], nums2 = [2, 2]
# 输出：[2, 2]
# 示例
# 2:
# 输入：nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
# 输出：[4, 9]
#
# 提示：
# - 1 <= nums1.length, nums2.length <= 1000
# - 0 <= nums1[i], nums2[i] <= 1000
# 二、参考代码

# 1. Java 代码
# class Solution {
#     public int[] intersect(int[] nums1, int[] nums2) {
#         Map<Integer, Integer> count1 = new HashMap<>();
#         Map<Integer, Integer> count2 = new HashMap<>();
#         List<Integer> result = new ArrayList<>();
#
#         // Count occurrences in the first array
#         for (int num : nums1) {
#             count1.put(num, count1.getOrDefault(num, 0) + 1);
#         }
#
#         // Count occurrences in the second array
#         for (int num : nums2) {
#             count2.put(num, count2.getOrDefault(num, 0) + 1);
#         }
#
#         // Find the intersection of elements and add to the result list
#         for (int key : count1.keySet()) {
#             if (count2.containsKey(key)) {
#                 int commonCount = Math.min(count1.get(key), count2.get(key));
#                 for (int i = 0; i < commonCount; i++) {
#                     result.add(key);
#                 }
#             }
#         }
#
#         // Convert the list to an array
#         int[] resultArray = new int[result.size()];
#         for (int i = 0; i < result.size(); i++) {
#             resultArray[i] = result.get(i);
#         }
#
#         return resultArray;
#     }
# }

# 2.Python 代码
# 1、简便写法
# from collections import Counter
# class Solution:
#     def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
#         cnt1 = Counter(nums1)
#         cnt2 = Counter(nums2)
#         ans = list()
#         for k in cnt1:
#             ans += [k] * min(cnt1[k], cnt2[k])
#         return ans


# 2、复杂易于理解写法-mm
# from collections import Counter
# class Solution:
#     def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
#         cnt1 = Counter(nums1)
#         cnt2 = Counter(nums2)
#         ans = list()
#         for k_num_value,v_count in cnt1.items():
#             ans += [k_num_value] * min(cnt1[k_num_value], cnt2[k_num_value])
#         return ans


########################## D03-09 ###################################### 0024
# 【哈希集合】2023Q1A-寻找关键钥匙
# 题目描述与示例
# 题目描述
# 小强正在参加《密室逃生》游戏，当前关卡要求找到符合给定密码 K（升序的不重复小写字母组成）的箱子，并给出箱子编号，箱子编号为 1~N。
# 每个箱子中都有一个字符串 s，字符串由大写字母，小写字母，数字，标点符号，空格组成，需要在这些字符串中找出所有的字母，忽略大小写且去重后排列出对应的密码串，并返回匹配密码的箱子序号。
# 注意：满足条件的箱子不超过 1 个。
# 输入描述
# 第一行为表示密码 K 的字符串
# 第二行为一系列箱子 boxes，为字符串数组样式，以空格分隔
# 箱子 N 数量满足 1<=N<=10000，代表每一个箱子的字符串 s 的长度满足 0 <= s.length <= 50，密码为仅包含小写字母的升序字符串，且不存在重复字母，密码 K 长度满足1 <= K.length <= 26
# 输出描述
# 返回对应箱子编号，如不存在符合要求的密码箱，则返回-1
# 补充说明
# 箱子中字符拼出的字符串与密码的匹配忽略大小写，且要求与密码完全匹配，如密码 abc 匹配 aBc，但是密码 abc 不匹配 abcd
# 示例 1
# 输入
# abc
# s,sdf134 A2c4b
# 输出
# 2
# 说明
# 第 2 个箱子中的 Abc，符合密码 abc
# 示例 2
# 输入
# abc
# s,sdf134 A2c4bd 523[]
# 输出
# -1
# 说明
# 第 2 个箱子中的 Abcd，与密码不完全匹配，不符合要求。
# 解题思路
# 本题思路非常直接。由于密码K不包含重复字符，每一个箱子字符串s也要做去重处理，因此我们可以直接分别用哈希集合K_set和s_set来表示密码和箱子字符串。
#
# 遍历boxes中的每一个字符串s，并且挑选出其中的所有字母ch，并做ch.lower()即转为小写的处理，再所有转为小写的字母构建为s_set，再比较K_set和s_set是否完全相等即可。若相等，则该箱子字符串s所对应的编号i+1（之所以+1是因为箱子的编号是从1而不是从0开始的）即为答案。
#
# 思考：如果稍微修改本题的条件，即箱子字符串不做去重处理，即s = "aa" 与 K = "a"不能匹配，那么应该如何修改代码？

# 参考代码
# Python
# 1、mm
# key = input()
# boxes = input().split(",")
#
# k_set = set(key)
# ans = -1
# for i,box in enumerate(boxes):
#     box_lower = str()
#     for ch in box:
#         if ch.isalpha():
#             box_lower += ch.lower()
#     box_lower_set = set(box_lower)
#     if k_set == box_lower_set:
#         ans = i + 1
#         break
# print(ans)

# kset = set("abcdef")
# aset = set("fdebca")
# print(kset == aset) # 输出TRUE  只要哈希集合中的元素一样，两个哈希集合，与元素顺序无关  所以能直接用if k_set == box_lower_set:来判断  不用考虑为box_lower_set排序

# 2、
# 题目：2023Q1A-寻找关键钥匙
# 分值：100
# 作者：闭着眼睛学数理化
# 算法：哈希集合
# 代码有看不懂的地方请直接在群上提问

# K = input()  # 输入密码字符串K
# boxes = input().split()  # 输入箱子字符串数组boxes
#
# ans = -1  # 初始化答案为-1
# K_set = set(K)  # 得到密码字符串所对应的集合
#
# # 遍历boxes字符串中的所有索引i和字符串s
# for i, s in enumerate(boxes):
#     # 得到字符串s中所有字母的集合，其中大写字母均转化为小写字母
#     s_set = {ch.lower() for ch in s if ch.isalpha()}
#
#     if K_set == s_set:  # 如果该集合与密码集合相等，则得到了符合要求的箱子编号
#         ans = i + 1  # 注意箱子编号是从1开始的
#         break  # 因为只有一个箱子满足要求，所以此时直接退出循环即可
#
# print(ans)

# Java
# import java.util.HashSet;
# import java.util.Scanner;
#
# public class Main {
#     public static void main(String[] args) {
#         Scanner scanner = new Scanner(System.in);
#
#         String K = scanner.nextLine();                  // 输入密码字符串K
#         String[] boxes = scanner.nextLine().split(" "); // 输入箱子字符串数组boxes
#
#         int ans = -1;                                   // 初始化答案为-1
#         HashSet<Character> K_set = new HashSet<>();     // 得到密码字符串所对应的集合
#         for (char ch : K.toCharArray()) {
#             K_set.add(ch);
#         }
#
#         // 遍历boxes字符串中的所有索引i和字符串s
#         for (int i = 0; i < boxes.length; i++) {
#             String s = boxes[i];
#             HashSet<Character> s_set = new HashSet<>(); // 得到字符串s中所有字母的集合，其中大写字母均转化为小写字母
#             for (char ch : s.toCharArray()) {
#                 if (Character.isLetter(ch)) {
#                     s_set.add(Character.toLowerCase(ch));
#                 }
#             }
#
#             if (K_set.equals(s_set)) {                   // 如果该集合与密码集合相等，则得到了符合要求的箱子编号
#                 ans = i + 1;                             // 注意箱子编号是从1开始的
#                 break;                                   // 因为只有一个箱子满足要求，所以此时直接退出循环即可
#             }
#         }
#
#         System.out.println(ans);
#         scanner.close();
#     }
# }


########################## D03-10 ###################################### 0025
# 【哈希集合】2023Q1A-明明的随机数
# 题目描述与示例
# 题目描述
# 明明生成了N 个 1 至 500 之间的随机整数。请你删去其中重复的数字，即相同的数字只保留一个，把其余相同的数去掉，然后再把这些数从小到大排序，按照排好的顺序输出。
# 数据范围： 1 ≤ N ≤ 1000 ，输入的数字大小 val 满足 1 ≤ val ≤ 500
# 输入描述
# 第一行先输入随机整数的个数 N 。 接下来的 N 行每行输入一个整数，代表明明生成的随机数。
# 输出描述：
# 输出多行，表示输入数据处理后的结果。
# 示例 1
# 输入
# 3
# 2
# 2
# 1
# 输出
# 1
# 2
# 说明
# 输入解释：
# 第一个数字是 3，也即这个样例的 N = 3，说明用计算机生成了 3 个 1 到 500 之间的随机整数，接下来每行一个输入随机数字，共 3 行，也即这 3 个随机数字为：2 2 1
# 输出解释：2 2 1中，出现了重复的2，只需要输出一个2即可，而且要按照从小到大的顺序输出全部整数，即依次输出1 2
# 解题思路
# 这道题直接运用哈希集合不包含重复元素的性质，将每一个整数都加入哈希集合num_set中。
#
# 由于哈希集合是一种无序的数据结构，为了从小到大依次输出所有元素，需要在所有元素输入完毕之后，将哈希集合num_set转化为列表num_lst。对列表num_lst就可以进行排序了，排序完成后，在一个for循环内依次输出num_lst中的所有元素即可。
# 代码
# Python

# 1、X
# 题目：2023Q1A-明明的随机数
# 分值：100
# 作者：闭着眼睛学数理化
# 算法：哈希集合
# 代码有看不懂的地方请直接在群上提问

# N = int(input())
#
# # 初始化一个哈希集合num_set，用于储存所有不重复元素
# num_set = set()
#
# # 遍历N次，依次输入数字
# for _ in range(N):
#     num_set.add(int(input()))
#
# # 哈希集合是无序的数据结构，所以要将哈希集合转化为列表后再排序
# num_lst = list(num_set)
# # 对列表进行排序
# num_lst.sort()
#
# # 遍历num_lst中的所有元素，按照从小到大的顺序依次输出
# for num in num_lst:
#     print(num)

# 2、MosesMin--简化版
# N = int(input())
# num_set = set()
#
# for _ in range(N):
#     num_set.add(int(input()))
#
# for num in sorted(num_set):
#     print(num)

# Java
# import java.util.HashSet;
# import java.util.ArrayList;
# import java.util.Collections;
# import java.util.Scanner;
#
# public class Main{
#     public static void main(String[] args) {
#         Scanner scanner = new Scanner(System.in);
#
#         int N = scanner.nextInt();
#         HashSet <Integer> num_set = new HashSet<>();
#
#         for(int i = 0; i < N; i++) {
#             num_set.add(scanner.nextInt());
#         }
#
#         ArrayList<Integer> num_lst = new ArrayList<>(num_set);
#         Collections.sort(num_lst);
#
#         for(int num: num_lst){
#             System.out.println(num);
#         }
#     }
# }

########################## D03-11 ###################################### 0026
# 【哈希表】2023Q1A-统计匹配的二元组个数
# 题目描述与示例
# 题目
# 给定两个数组 A 和 B，若数组 A 的某个元素 A[i] 与数组 B 中的某个元素 B[j] 满足 A[i]==B[j]，则寻找到一个匹配的二元组(i,j) ，请统计再这两个数组 A 和 B 中，一共存在多少个这样的二元组。
# 输入描述
# 第一行输入数组 A 的长度 M ；
# 第一行输入数组 B 的长度 N ；
# 第三行输入数组 A 的值；
# 第四行输入数组 B 的值。
# 1 ≤ M, N ≤ 100000
# A，B 数组中数值的取值均小于 100000
# 输出描述
# 输出匹配的二元组个数
# 示例一
# 输入
# 5
# 4
# 1 2 3 4 5
# 4 3 2 1
# 输出
# 4
# 说明
# 若下标从 0 开始，则匹配的二元组分别为(0,3)，(1,2)，(2,1)，(3,0)，共计 4 对二元组。
# 示例二
# 输入
# 6
# 3
# 1 2 4 4 2 1
# 1 2 3
# 输出
# 4
# 解题思路
# 数组 A 和 B中各个元素的频率我们都需要统计，可以用两个哈希表进行储存，分别记为cnt_A和cnt_B。接下来我们就来统计能构成的二元组的个数。
#
# 接下来我们考虑如何计算二元组的数目。某一个数字num在A中出现的次数为cnt_A[num]，存在两种情况：
# 1. 如果它在B中没有出现，那么能构成的二元组的个数为0
# 2. 如果它在B中出现过，出现次数为cnt_B[num]，那么基于简单的乘法原理，能构成的二元组个数为cnt_A[num] * cnt_B[num]
#
# 以示例二为例子：元素1在数组A中出现了两次，下标分别为0和5，在数组B中出现了一次，下标为0，所以对于元素1可以构成2 * 1 = 2组二元组，分别为(0, 0)和(5, 0)。元素2也可以构成2组二元组，分别为(1, 1)和(4, 1)。所以一共可以构成2 + 2 = 4组二元组。
#
# 如果我们是使用计数器Counter()来储存元素频率，上述两种情况其实可以合并。因为如果num不位于cnt_B的键中，我们会得到cnt_B[num] = 0。因此计算cnt_A[num] * cnt_B[num] = 0。
#
# 所以我们只需要遍历cnt_A中的所有键num，计算cnt_A[num]*cnt_B[num]的结果并求和即可。
#
# 代码
#
# Python
# 1、X
# 题目：2023Q1A-统计匹配的二元组个数
# 分值：200
# 作者：闭着眼睛学数理化
# 算法：哈希表
# 代码看不懂的地方，请直接在群上提问

# 导入collections中的Counter计数器类，使用dict()也可以，但是代码就要多一些判断
from collections import Counter

nA = int(input())
nB = int(input())
cnt_A = Counter(input().split())
cnt_B = Counter(input().split())
# 基于乘法原理，计算能够构成的二元组的个数
print(sum(cnt_A[num] * cnt_B[num] for num in cnt_A))

# 2、MosesMin
from collections import Counter
A_M = int(input())
B_N = int(input())

# cnt_A = Counter(int(input().split())) # TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
cnt_A = Counter(input().split())
cnt_B = Counter(input().split())

ans = 0;
for num in cnt_A:
    # ans = sum(cnt_A[num]*cnt_B[num]) # sum(cnt_A[num]*cnt_B[num]) 这个表达式是不可迭代的  not iterable 无法在每一次遍历时这样运行
    ans += cnt_A[num]*cnt_B[num]

print(ans)



