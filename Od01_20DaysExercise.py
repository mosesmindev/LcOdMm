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

class Solution:
    def decodeString(self, s: str) -> str:
        # 创建数字栈，在遍历编码字符串过程中记录出现的数字
        numStack = []

        # 创建字符栈，在遍历编码字符串过程中记录出现的字符串
        strStack = []

        # 在访问编码字符串的过程中，用来记录访问到字符串之前出现的数字，一开始为 0
        digit = 0

        # 在访问编码字符串的过程中，把得到的结果存放到 res 中
        res = ""

        # 从头到尾遍历编码字符串
        for ch in s:

            # 在遍历过程中，字符会出现 4 种情况
            # 先获取此时访问的字符
            # 1、如果是数字，需要把字符转成整型数字
            # 注意数字不一定是 1 位，有可能是多位
            # 比如  123a，在字母 a 的前面出现了 123，表示 a 重复出现 123 次
            # 那么一开始 ch 为 1，当访问到 ch 为 2 的时候，1 和 2 要组成数字 12
            # 再出现 3 ，12 和 3 组成数字 123
            if '0' <= ch <= '9':

                # 先将字符转成整型数字 ch-‘0’
                # 补充知识：将字符'0'-'9'转换为数字，只需将字符变量减去'0'就行
                # 因为字符和数字在内存里都是以 ASCII 码形式存储的
                # 减去 '0' ，其实就是减去字符 '0' 的 ASCII 码，而字符 '0' 的 ASCII 码是 30
                # 所以减去'0'也就是减去30，然后就可以得到字符对应的数字了。
                num = int(ch)

                # 再将这个数字和前面存储的数字进行组合
                # 1 和 2 组成数字 12，也就是 1 * 10 + 2 = 12
                # 12 和 3 组成数字 123，也就是 12 * 10 + 3 = 123
                digit = digit * 10 + num

                # 2、如果是字符
            elif ch >= 'a' and ch <= 'z':

                # 说明它就出现一次，可以直接存放到 res 中
                res += ch

            # 3、如果是"["
            # 出现了嵌套的内层编码字符串，而外层的解码需要等待内层解码的结果
            # 那么之前已经扫描的字符需要存放起来，等到内层解码之后再重新使用
            elif ch == '[':

                # 把数字存放到数字栈
                numStack.append(digit)

                # 把外层的解码字符串存放到字符串栈
                strStack.append(res)

                # 开始新的一轮解码
                # 于是，digit 归零
                digit = 0

                # res 重新初始化
                res = ""

            # 4、如果是"]"
            elif ch == ']':

                # 此时，内层解码已经有结果，需要把它和前面的字符串进行拼接

                # 第一步，先去查看内层解码的字符串需要被重复输出几次
                # 比如 e3[abc]，比如内层解码结果 abc 需要输出 3 次
                # 通过数字栈提取出次数
                count = numStack.pop()

                # 第二步，通过字符串栈提取出之前的解码字符串
                outString = strStack.pop()

                # 第三步，不断的把内层解码的字符串拼接起来
                for j in range(0, count):
                    # 拼接到 outString 后面，拼接 count 次
                    outString += res

                # 再把此时得到的结果赋值给 res
                res = outString

        # 返回解码成功的字符串
        return res

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

