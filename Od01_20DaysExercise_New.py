# D01 面向对象  数组、栈、队列
# --------------------------------- D01-01 --------------------------------- 0001
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
# from collections import deque


# --------------------------------- D01-01 --------------------------------- 0001-MmCopy
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
# print('------------------------------------------')
# print(parking.addCar(2)) # 添加1辆medium
# print(parking.addCar(2))
# print(parking.addCar(2))
# print(parking.addCar(2))
# print(parking.addCar(2))
# print(parking.addCar(2))
# print(parking.addCar(2))
# print(parking.addCar(2))
# print(parking.addCar(2))
# print('------------------------------------------')
#
# print(parking.addCar(3)) # 添加1辆small
# print(parking.addCar(3))
# print(parking.addCar(3))
# print(parking.addCar(3))
# print(parking.addCar(3))
# print(parking.addCar(3))
# print(parking.addCar(3))
# print('------------------------------------------')
#
# 运行结果：
# True
# True
# True
# True
# False
# ------------------------------------------
# True
# True
# True
# True
# True
# True
# True
# True
# False
# ------------------------------------------
# True
# True
# True
# True
# True
# True
# False
# ----------------------------------

# --------------------------------- D01-02 --------------------------------- 0002
# 有效的括号（ LC20 ）:https://leetcode-cn.com/problems/valid-parentheses
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

# --------------------------------- D01-02 --------------------------------- 0002--MmCopy1
# 有效的括号（ LC20 ）:https://leetcode-cn.com/problems/valid-parentheses
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

# --------------------------------- D01-03 --------------------------------- 0003
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

# --------------------------------- D01-03 --------------------------------- 0003--MmCopy
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

# --------------------------------- D01-04 --------------------------------- 0004
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


# --------------------------------- D01-04 --------------------------------- 0004--MmCopy
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

# --------------------------------- D01-05 --------------------------------- 0005
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

# --------------------------------- D01-05 --------------------------------- 0005--MmCopy
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


# --------------------------------- D01-06 --------------------------------- 0006
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


# --------------------------------- D02-01 --------------------------------- 0008
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


# --------------------------------- D02-01 --------------------------------- 0008MmCopy
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


# --------------------------------- D02-02 --------------------------------- 0009
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

# --------------------------------- D02-02 --------------------------------- 0009MmCopy
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

# --------------------------------- D02-03 --------------------------------- 0010
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


# --------------------------------- D02-03 --------------------------------- 0010MmCopy
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

# --------------------------------- D02-04 --------------------------------- 0011
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

# --------------------------------- D02-05 --------------------------------- 0012
# LC71. 简化路径
# 一、题目描述
# 给你一个字符串 path ，表示指向某一文件或目录的 Unix 风格 绝对路径 （以 '/' 开头），请你将其转化为更加简洁的规范路径。
# 在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..） 表示将目录切换到上一级（指向父目录）；
# 两者都可以是复杂相对路径的组成部分。任意多个连续的斜杠（即，'//'）都被视为单个斜杠 '/' 。
# 对于此问题，任何其他格式的点（例如，'...'）均被视为文件/目录名称。

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

# --------------------------------- D02-06 --------------------------------- 0013
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

# --------------------------------- D02-07 --------------------------------- 0014
# 【栈】2023Q1A-投篮大赛
# 一、题目描述与示例
# 题目描述
# 你现在是一场采用特殊赛制投篮大赛的记录员。这场比赛由若干回合组成，过去几回合的得分可能会影响以后几回合的得分。
# 比赛开始时，记录是空白的。你会得到一个记录操作的字符串列表 ops，其中 ops[i] 是你需要记录的第 i 项操作，ops 遵循下述规则：

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

# 5. 如果不满足上述的任何一个条件，则说明此时出现异常。
# 应该输出-1。对于可能出现的异常，我们应该在最开始初始化一个标记isError = False，
# 用于标记是否出现异常的标志，初始化为False表示最开始没有异常。当出现异常时，我们修改isError = True，并且break退出循环。


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

# --------------------------------- D02-08 --------------------------------- 0015
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


# Python

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


# -------------- D03 哈希表（python中对应字典） --------------
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

# --------------------------------- D03-01 --------------------------------- 0016
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


# --------------------------------- D03-02 --------------------------------- 0017
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


# --------------------------------- D03-03 --------------------------------- 0018
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


# --------------------------------- D03-04 --------------------------------- 0019
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


# --------------------------------- D03-05 --------------------------------- 0020
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

# --------------------------------- D03-06 --------------------------------- 0021
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


# --------------------------------- D03-07 --------------------------------- 0022
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


# --------------------------------- D03-08 --------------------------------- 0023
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
#         list<Integer> result = new Arraylist<>();
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


# --------------------------------- D03-09 --------------------------------- 0024
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


# --------------------------------- D03-10 --------------------------------- 0025
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
# import java.util.Arraylist;
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
#         Arraylist<Integer> num_lst = new Arraylist<>(num_set);
#         Collections.sort(num_lst);
#
#         for(int num: num_lst){
#             System.out.println(num);
#         }
#     }
# }

# --------------------------------- D03-11 --------------------------------- 0026
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
# 以示例二为例子：元素1在数组A中出现了两次，下标分别为0和5，在数组B中出现了一次，
# 下标为0，所以对于元素1可以构成2 * 1 = 2组二元组，分别为(0, 0)和(5, 0)。
# 元素2也可以构成2组二元组，分别为(1, 1)和(4, 1)。所以一共可以构成2 + 2 = 4组二元组。
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
# from collections import Counter
#
# nA = int(input())
# nB = int(input())
# cnt_A = Counter(input().split())
# cnt_B = Counter(input().split())
# # 基于乘法原理，计算能够构成的二元组的个数
# print(sum(cnt_A[num] * cnt_B[num] for num in cnt_A))

# 2、MosesMin
# from collections import Counter
# A_M = int(input())
# B_N = int(input())

# TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
# cnt_A = Counter(int(input().split()))

# cnt_A = Counter(input().split())
# cnt_B = Counter(input().split())
#
# ans = 0;
# for num in cnt_A:
#     # ans = sum(cnt_A[num]*cnt_B[num]) # sum(cnt_A[num]*cnt_B[num]) 这个表达式是不可迭代的  not iterable 无法在每一次遍历时这样运行
#     ans += cnt_A[num]*cnt_B[num]
#
# print(ans)


# --------------------------------- D04-01 --------------------------------- 0027
# LC1.两数之和
# 一、题目描述
# 给定一个整数数组nums# 和一个整数目标值target，请你在该数组中找出和为目标值target的那两个整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。你可以按任意顺序返回答案。
#
# 示例
# 1：
# 输入：nums = [2, 7, 11, 15], target = 9
# 输出：[0, 1]
# 解释：因为
# nums[0] + nums[1] == 9 ，返回[0, 1] 。
# 示例
# 2：
# 输入：nums = [3, 2, 4], target = 6
# 输出：[1, 2]
# 示例
# 3：
# 输入：nums = [3, 3], target = 6
# 输出：[0, 1]
#
# 提示：
# - 2 <= nums.length <= 10(4)
# - -10(9) <= nums[i] <= 10(9)
# - -10(9) <= target <= 10(9)
# - 只会存在一个有效答案
# 二、题目解析
#
# 三、参考代码
# 1、W
# 登录 AlgoMooc 官网获取更多算法图解
# https://www.algomooc.com
# 作者：程序员吴师兄
# 代码有看不懂的地方一定要私聊咨询吴师兄呀
# 两数之和（LeetCode 1）:https://leetcode-cn.com/problems/two-sum/
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#        # 首先构建一个哈希表，用来存放数组的元素值以及索引值
#        # 其中 key 是数组中的元素值
#        # value 为数组中元素值的索引
#        map = dict()
#
#        # 接下来，遍历整个数组
#        for i, num in enumerate(nums):
#            # 目标值为 target，将 target 与 nums[i] 求差
#            # 获取与 nums[i] 配对的那个数 anotherNum
#            anotherNum = target - num
#
#            # 判断哈希表中是否存在那个与 nums[i] 配对的数 anotherNum
#            if anotherNum in map :
#
#                # 由于哈希表中所有 key 都是来自于数组中，
#                # 所以，如果发现哈希表存在那个与 nums[i] 配对的数 anotherNum
#                # 也就说明数组中存在一个数，可以和 nums[i] 相加为 target
#                # 此时， anotherNum 这个 key 对应的 value 为这个数在数组中的索引
#                # 所以，返回 map.get(anotherNum) 和 i 就是这两个值的下标
#                return [ map[ target - num ] , i ]
#            else:
#               # 如果发现哈希表中目前不存在那个与 nums[i] 配对的数 anotherNum
#               # 那么就把此时观察的数 nums[i] 和它的索引存放到哈希表中
#               # 等待后面的数能和它配对为 target
#              map[nums[i]] = i
#
#        # 如果遍历完整个数组都找不到和为 target 的两个数，返回 0
#        return []

# 2、MosesMin
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#        # 首先构建一个哈希表，用来存放数组的元素值以及索引值
#        # 其中 key 是数组中的元素值
#        # value 为数组中元素值的索引
#        map = dict()
#
#        # 接下来，遍历整个数组
#        for i, num in enumerate(nums):
#            # 目标值为 target，将 target 与 nums[i] 求差
#            # 获取与 nums[i] 配对的那个数 anotherNum
#            anotherNum = target - num
#
#            # 判断哈希表中是否存在那个与 nums[i] 配对的数 anotherNum
#            if anotherNum in map :
#
#                # 由于哈希表中所有 key 都是来自于数组中，
#                # 所以，如果发现哈希表存在那个与 nums[i] 配对的数 anotherNum
#                # 也就说明数组中存在一个数，可以和 nums[i] 相加为 target
#                # 此时， anotherNum 这个 key 对应的 value 为这个数在数组中的索引
#                # 所以，返回 map.get(anotherNum) 和 i 就是这两个值的下标
#                return [map[anotherNum] ,i]
#            else:
#               # 如果发现哈希表中目前不存在那个与 nums[i] 配对的数 anotherNum
#               # 那么就把此时观察的数 nums[i] 和它的索引存放到哈希表中
#               # 等待后面的数能和它配对为 target
#              map[num] = i
#
#        # 如果遍历完整个数组都找不到和为 target 的两个数，返回 0
#        return []

# --------------------------------- D04-02 --------------------------------- 0028
# LC219. 存在重复元素II
# 一、题目描述
# 给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，
# 满足 nums[i] == nums[j] 且 abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false 。
# 示例 1：
# 输入：nums = [1,2,3,1], k = 3
# 输出：true
# 示例 2：
# 输入：nums = [1,0,1,1], k = 1
# 输出：true
# 示例 3：
# 输入：nums = [1,2,3,1,2,3], k = 2
# 输出：false
# 提示：
# - 1 <= nums.length <= 10^5
# - -109 <= nums[i] <= 10^9
# - 0 <= k <= 10^5
# 二、题目解析
#
# 三、参考代码
# 1、W
# class Solution:
#     def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
#
#         # 使用哈希集合
#         pos = {}
#
#         # 如果想在 for 循环中同时获得列表的索引 i 和元素值 v
#         # 可以使用枚举内置函数 enumerate()
#         for i, v in enumerate(nums):
#             # 1、如果发现当前这个元素 v 已经存在于哈希集合里面
#             # 说明在此之前就已经访问到了一个元素，值为 v
#             # 2、pos[v] 表示的是之前访问到的元素值所在的索引
#             # 判断 i - pos[v] <= k
#             if v in pos and i - pos[v] <= k:
#                 # 符合要求，就返回 True
#                 return True
#             # 否则，把 v 和 i 存储到哈希集合里面
#             pos[v] = i
#
#         # 最终没有找到，返回 False
#         return False

# 2、MosesMin
# class Solution:
#     def mm(self,nums:list[int],k:int)->list[int]:

#         # hashSave = {} # 不推荐的哈希集合 哈希表 字典的写法
#         hashSave = dict()
#         for i,num in enumerate(nums):
#             if num in hashSave and i - hashSave[num] <= k:
#                 return True
#
#             hashSave[num] = i
#         return False
#
# sol = Solution()
# print(sol.mm([1,2,3,1,1],1))


# --------------------------------- D04-03 --------------------------------- 0029
# LC205.同构字符串
# 一、题目描述
# 给定两个字符串s和t ，判断它们是否是同构的。
# 如果s中的字符可以按某种映射关系替换得到t ，那么这两个字符串是同构的。
# 每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。
# 不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。
#
# 示例
# 1:
# 输入：s = "egg", t = "add"
# 输出：true
# 示例
# 2：
# 输入：s = "foo", t = "bar"
# 输出：false
# 示例
# 3：
# 输入：s = "paper", t = "title"
# 输出：true
# 提示：
# - 1 <= s.length <= 5 * 10 ^ 4
# - t.length == s.length
# - s和t由任意有效的ASCII字符组成
#
# 二、参考代码
# 1、W
# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#
#         # 设置一个哈希集合用来存储字符串 s 当中的元素  # 吴师兄的注释 有错误
#         # MosesMin：上一行WSX的注释是有问题的，这里应该是设置了哈希表(即python中的字典dict)，而不是哈希集合；
#         # 哈希集合中的元素是不重复的，哈希表中key不能重复，但是哈希表的元素的value是可以重复的
#         # python中，哈希表可以用{}、或者字典dict()声明，但是哈希集合要用set()
#         dic1 = {}
#
#         # 设置一个哈希集合用来存储字符串 t 当中的元素
#         dic2 = {}
#
#         # 由于 t.length == s.length
#         # 按照顺序访问 s 和 t 中对应的元素
#         for i in range(len(s)):
#
#             # 1、访问的元素 s[i] 存在于 dic1 中
#             # 并且发现它对应的元素值和当前 t 中元素 t[i] 不相同
#             # 返回 False
#             if s[i] in dic1 and dic1[s[i]] != t[i]:
#                 return False
#
#             # 2、访问的元素 t[i] 存在于 dic2 中
#             # 并且发现它对应的元素值和当前 s 中元素 s[i] 不相同
#             # 返回 False
#             if t[i] in dic2 and dic2[t[i]] != s[i]:
#                 return False
#
#             # 3、访问的元素 s[i] 不存在于 dic1 中
#             # 存放到哈希集合中
#             if s[i] not in dic1:
#                 # dic1[s[i]] = t[i]
#                 dic1[s[i]] = t[i]
#
#             # 3、访问的元素 t[i] 不存在于 dic2 中
#             # 存放到哈希集合中
#             if t[i] not in dic2:
#                 # dic2[t[i]] = s[i]
#                 dic2[t[i]] = s[i]
#         # 返回 True
#         return True

# 2、MosesMin
# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#
#         # 设置一个字典-即哈希表，用以存储字符s中的元素
#         dicS = dict()
#
#         # 设置一个字典-即哈希表，用以存储字符t中的元素
#         dicT = dict()
#
#         # 由于 t.length == s.length
#         # 按照顺序访问 s 和 t 中对应的元素
#         for i in range(len(s)):
#
#             # 1、访问的元素 s[i] 存在于 dicS 中
#             # 并且发现它对应的元素值和当前 t 中元素 t[i] 不相同
#             # 返回 False
#             if s[i] in dicS and dicS[s[i]] != t[i]:
#                 return False
#
#             # 2、访问的元素 t[i] 存在于 dicT 中
#             # 并且发现它对应的元素值和当前 s 中元素 s[i] 不相同
#             # 返回 False
#             if t[i] in dicT and dicT[t[i]] != s[i]:
#                 return False
#
#             # 3、访问的元素 s[i] 不存在于 dicS 中
#             # 存放到哈希集合中
#             if s[i] not in dicS:
#                 dicS[s[i]] = t[i]
#
#             # 3、访问的元素 t[i] 不存在于 dicT 中
#             # 存放到哈希集合中
#             if t[i] not in dicT:
#                 dicT[t[i]] = s[i]
#         # 返回 True
#         return True


# --------------------------------- D04-04 --------------------------------- 0030
# LC49. 字母异位词分组
# 一、题目描述
# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
# 字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。
# 示例 1:
# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
# 示例 2:
# 输入: strs = [""]
# 输出: [[""]]
# 示例 3:
# 输入: strs = ["a"]
# 输出: [["a"]]
# 提示：
# - 1 <= strs.length <= 10^4
# - 0 <= strs[i].length <= 100
# - strs[i] 仅包含小写字母
# 二、参考代码

# 1、W
# class Solution:
#     def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
#         # 互为字母异位词的两个字符串包含的字母相同
#         # 因此两个字符串中的相同字母出现的次数一定是相同的
#         # 可以将每个字母出现的次数使用字符串表示，作为哈希表的键
#         mp = collections.defaultdict(list)
#
#         for s in strs:
#             # counts 代表每个小写字母出现的频次
#             counts = [0] * 26
#
#             # 利用 for 循环，统计 str 当中每个字母出现的频次
#             for c in s:
#                 counts[ord(c) - ord('a')] += 1
#
#             # 将每个出现次数大于 0 的字母和出现次数按顺序拼接成字符串，作为哈希表的键
#             key = ''.join(['#'+str(count) for count in counts])
#
#             # 在哈希表 mp 当中找出这个 key 对应的字符串 str 来
#             # 1、如果有这个 key，那么这个 key 对应的 数组 会新增一个 str 进去
#             # 2、如果没有这个 key，那么会初始化一个数组，用来新增这个 str
#             mp[key].append(s)
#
#         # 返回结果
#         return list(mp.values())


# 2、MosesMin
# import collections
# class Solution:
#     def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
#         # 互为字母异位词的两个字符串包含的字母相同
#         # 因此两个字符串中的相同字母出现的次数一定是相同的
#         # 可以将每个字母出现的次数使用字符串表示，作为哈希表的键
#         # 下行代码初始化的map的样式   {0:[]}
#         map = collections.defaultdict(list)
#
#         for string in strs:
#             # counts 代表每个小写字母出现的频次
#             countString = [0] * 26
#
#             # 利用 for 循环，统计 str 当中每个字母出现的频次
#             for ch in string:
#                 countString[ord(ch) - ord('a')] += 1
#
#             # 将每个出现次数大于 0 的字母和出现次数按顺序拼接成字符串，作为哈希表的键
#             key = ''.join(['#'+str(countCh) for countCh in countString])
#
#             # 在哈希表 map 当中找出这个 key 对应的字符串 string 来
#             # 1、如果有这个key，那么这个key对应的数组会新增一个string进去
#             # 即为map中的key添加string
#             # 2、如果没有这个key，那么会初始化一个数组，用来新增这个string
#             # 即将key和string 作为键值对一同添加进map
#             map[key].append(string)
#
#         # 返回结果
#         return list(map.values())


# --------------------------------- D04-05 --------------------------------- 0031
# LC290. 单词规律
# 一、题目描述
# 给定一种规律 pattern 和一个字符串 s ，判断 s 是否遵循相同的规律。
# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 s 中的每个非空单词之间存在着双向连接的对应规律。
# 示例1:
# 输入: pattern = "abba", s = "dog cat cat dog"
# 输出: true
# 示例 2:
# 输入:pattern = "abba", s = "dog cat cat fish"
# 输出: false
# 示例 3:
# 输入: pattern = "aaaa", s = "dog cat cat dog"
# 输出: false
# 提示:
# - 1 <= pattern.length <= 300
# - pattern 只包含小写英文字母
# - 1 <= s.length <= 3000
# - s 只包含小写英文字母和 ' '
# - s 不包含 任何前导或尾随对空格
# - s 中每个单词都被 单个空格 分隔
# 二、参考代码

# 1、W
# class Solution:
#     def wordPattern(self, pattern: str, s: str) -> bool:
#
#         s = s.split()
#
#         if len(pattern) != len(s):
#             return False
#
#         t = pattern
#
#         # 接下来的逻辑和 LC205. 同构字符串 一模一样
#
#         # 设置一个哈希集合用来存储字符串 s 当中的元素
#         dic1 = {}
#
#         # 设置一个哈希集合用来存储字符串 t 当中的元素
#         dic2 = {}
#
#         # 由于 t.length == s.length
#         # 按照顺序访问 s 和 t 中对应的元素
#         for i in range(len(pattern)):
#
#             # 1、访问的元素 s[i] 存在于 dic1 中
#             # 并且发现它对应的元素值和当前 t 中元素 t[i] 不相同
#             # 返回 False
#             if s[i] in dic1 and dic1[s[i]] != t[i]:
#                 return False
#
#             # 2、访问的元素 t[i] 存在于 dic2 中
#             # 并且发现它对应的元素值和当前 s 中元素 s[i] 不相同
#             # 返回 False
#             if t[i] in dic2 and dic2[t[i]] != s[i]:
#                 return False
#
#             # 3、访问的元素 s[i] 不存在于 dic1 中
#             # 存放到哈希集合中
#             if s[i] not in dic1:
#                 # dic1[s[i]] = t[i]
#                 dic1[s[i]] = t[i]
#
#             # 3、访问的元素 t[i] 不存在于 dic2 中
#             # 存放到哈希集合中
#             if t[i] not in dic2:
#                 # dic2[t[i]] = s[i]
#                 dic2[t[i]] = s[i]
#         # 返回 True
#         return True

# 2、MosesMin
# class Solution:
#     def wordPattern(self, pattern: str, s: str) -> bool:
#
#         s = s.split()
#
#         if len(pattern) != len(s):
#             return False
#
#         t = pattern
#
#         # 接下来的逻辑和 LC205. 同构字符串 一模一样
#         # 设置一个字典-即哈希表，用以存储字符s中的元素
#         dicS = dict()
#
#         # 设置一个字典-即哈希表，用以存储字符t中的元素
#         dicT = dict()
#
#         # 由于 t.length == s.length
#         # 按照顺序访问 s 和 t 中对应的元素
#         for i in range(len(s)):
#
#             # 1、访问的元素 s[i] 存在于 dicS 中
#             # 并且发现它对应的元素值和当前 t 中元素 t[i] 不相同
#             # 返回 False
#             if s[i] in dicS and dicS[s[i]] != t[i]:
#                 return False
#
#             # 2、访问的元素 t[i] 存在于 dicT 中
#             # 并且发现它对应的元素值和当前 s 中元素 s[i] 不相同
#             # 返回 False
#             if t[i] in dicT and dicT[t[i]] != s[i]:
#                 return False
#
#             # 3、访问的元素 s[i] 不存在于 dicS 中
#             # 存放到哈希集合中
#             if s[i] not in dicS:
#                 dicS[s[i]] = t[i]
#
#             # 3、访问的元素 t[i] 不存在于 dicT 中
#             # 存放到哈希集合中
#             if t[i] not in dicT:
#                 dicT[t[i]] = s[i]
#         # 返回 True
#         return True

# --------------------------------- D04-06 --------------------------------- 0032
# 【哈希表】2023Q1A-字符串重新排序
# 题目描述
# 给定一个字符串 s，s 包含以空格分隔的若干个单词，请对 s 进行如下处理后输出：
# 1. 单词内部调整：对每个单词字母重新按字典序排序；
# 2. 单词间顺序调整：
#   1. 统计每个单词出现的次数，并按次数降序排列；
#   2. 次数相同时，按单词长度升序排列；
#   3. 次数和单词长度均相同时，按字典序升序排列。
# 请输出处理后的字符串，每个单词以一个空格分隔。
# 输入描述
# 一行字符串，每个字符取值范围：[a-z, A-Z, 0-9] 以及空格" "，字符串长度范围：[1, 1000]
# 输出描述,
# 重新排序后的字符串，每个单词间隔 1 个空格，且首尾无空格
# 示例一
# 输入
# This is an apple
# 输出
# an is This aelpp
# 示例二
# 输入
# My sister is in the house not in the yard
# 输出
# in in eht eht My is not adry ehosu eirsst
# 解题思路
# 本题包含单词内和单词间的两种排序。先考虑单词内的排序，再考虑单词间的排序。
#
# 对于单词内的排序，需要对每个单词字母重新按字典序排序。所以我们在代码，对于lst中的每一个单词word：
# 1. 用list(word)将字符串word转化为列表
# 2. 用sorted()内置函数得到按照字典序排序的结果
# 3. 用join()方法将排序结果重新转化为字符串
# 最后再使用列表推导式，可以得到每个单词内部进行排序后的新列表new_lst。
# new_lst = ["".join(sorted(list(word))) for word in lst]
# 对于单词间的排序，需要依次考虑三个因素：
# 1. 单词出现频率
# 2. 单词长度
# 3. 单词字典序
# 对于单词出现频率这个因素，我们很容易想到直接使用哈希表计数器Counter()来统计，即
# cnt = Counter(new_lst)
# 而长度因素，可以很容易地使用len()内置函数得到。
#
# 所以我们使用lambda匿名函数来辅助new_lst的排序，即
# new_lst.sort(key = lambda x: (-cnt[x], len(x), x))
# 要注意，由于要求按照单词出现频率降序排列，我们应该以-cnt[x]而不是cnt[x]做为第一个排序依据。
#
# 最后，还需要把new_lst的排序结果再一次使用join()方法合并为字符串并输出。注意合并时要用空格" "隔开每一个单词。
# print(" ".join(new_lst))
#
#
# 代码
# Python

# 题目：2023Q1A-字符串重新排列
# 分值：100
# 作者：许老师-闭着眼睛学数理化
# 算法：哈希表，排序
# 代码看不懂的地方，请直接在群上提问

# # 1、X
# from collections import Counter
#
# lst = input().split()
# n = len(lst)  # 这行没用 MosesMin注释
#
# # 单词内的排序：
# # 对于lst中的每一个单词word：
# # 1. 用list(word)转化为列表
# # 2. 用sorted()内置函数得到按照字典序排序的结果
# # 3. 用join()方法将排序结果重新转化为字符串
# # 再使用列表推导式，可以得到新的列表
# new_lst = ["".join(sorted(list(word))) for word in lst]
#
# # 单词间的排序：
# # 用Counter()统计new_lst中各个单词的出现频率
# cnt = Counter(new_lst)
# # 使用lambda匿名函数，
# # 1. 先按照出现次数即cnt[x]排序，为了实现从大到小排序，需要以-cnt[x]为依据
# # 2. 再按照长度len(x)排序
# # 3. 最后再按照字典序排序
# new_lst.sort(key = lambda x: (-cnt[x], len(x), x))
#
# # 最后使用join()方法，将排序后的列表转化为字符串输出，记得用" "隔开
# print(" ".join(new_lst))


# 2、MosesMin
# from collections import Counter
#
# lst = input().split() # 这样获取到的输入的一个句子 得到的是一个单词列表  MosesMin
# print('lst:' + str(lst))
# # 单词内的排序：
# # 对于lst中的每一个单词word：
# # 1. 用list(word)转化为列表  -- 将单词字符串的各个字母转化为字母列表
# # 2. 用sorted()内置函数得到按照字典序排序的结果 -- 为转换后的字母列表排序
# # 3. 用join()方法将排序结果重新转化为字符串 -- 将排序后的字母列表转化为字符串
# # 再使用列表推导式，可以得到新的列表
# new_lst = ["".join(sorted(list(word))) for word in lst]
# print('new_lst:' + str(new_lst))
#
# # 单词间的排序：
# # 用Counter()统计new_lst中各个单词的出现频率
# cnt = Counter(new_lst)
# # 使用lambda匿名函数，
# # 1. 先按照出现次数即cnt[x]排序，为了实现从大到小排序，需要以-cnt[x]为依据
# # 2. 再按照长度len(x)排序
# # 3. 最后再按照字典序排序
# new_lst.sort(key = lambda x: (-cnt[x], len(x), x))
# # 最后使用join()方法，将排序后的列表转化为字符串输出，记得用" "隔开
# print(" ".join(new_lst))


# MosesMin补充：
# D04-06  字典序是什么？
# 字典序是一种对对象进行排序的方法，通常用于字符串、数字或其他可比较的数据类型。
# 在字典序中，对象按照其在字典中出现的顺序进行排序，即按照字母表或数字表的顺序排列。
# 对于字符串来说，字典序就是按照字母表顺序进行排序；对于数字来说，字典序是按照数值大小进行排序。字典序可以用于比较和排序各种类型的数据。

# lst = input().split()
#
# # 列表推导式写法
# new_lst = ["".join(sorted(list(word))) for word in lst]
# print(new_lst)
# print('---------------------------------#########')
#
# # 复杂写法
# new_lst = list()
# for word in lst:
#     lst_word = list(word)
#     print('lst_word:'+ str(lst_word))
#     sort_word = sorted(lst_word)
#     print('sort_word:' + str(sort_word))
#     str_sort_word = "".join(sort_word)
#     print('str_sort_word:' + str_sort_word)
#     new_lst.append(str_sort_word)
#     print('-----------------------------------------------------------------------')
# print(new_lst)
# print('---------------------------------#########')
#
# lst_word是一个列表，sorted(lst_word)和lst_word.sort()是有区别的；
# sorted(lst_word)会将lst_word排序，并会返回一个排序后的列表；
# lst_word.sort()也会将lst_word排序，但是返回值为空，直接继续使用lst_word即为排序后的结果。


# 时空复杂度
# 时间复杂度：O(NlogN + Σ(MlogM))。单词内、单词间进行排序的时间复杂度
# 空间复杂度：O(N)。
# Σ表示求和，M为每个单词的长度。


# --------------------------------- D04-07 --------------------------------- 0033
# 【哈希表】2023Q2B-选修课
# 题目描述与示例
# 题目描述
# 现有两门选修课，每门选修课都有一部分学生选修，每个学生都有选修课的成绩，
# 需要你找出同时选修了两门选修课的学生，先按照班级进行划分，班级编号小的先输出，
# 每个班级按照两门选修课成绩和的降序排序，成绩相同时按照学生的学号升序排序。
#
# 输入
# 第一行为第一门选修课学生的成绩，第二行为第二门选修课学生的成绩，
# 每行数据中学生之间以英文分号分隔，每个学生的学号和成绩以英文逗号分隔，
# 学生学号的格式为 8 位数字(2 位院系编号+入学年份后 2 位+院系内部 1 位专业编号+所在班级 3 位学号)，
# 学生成绩的取值范围为 [0,100] 之间的整数，两门选修课选修学生数的取值范围为 [1-2000] 之间的整数。
#
# 输出
# 同时选修了两门选修课的学生的学号，如果没有同时选修两门选修课的学生输出 NULL，
# 否则，先按照班级划分，班级编号小的先输出，每个班级先输出班级编号(学号前五位)，
# 然后另起一行输出这个班级同时选修两门选修课的学生学号，
# 学号按照要求排序(按照两门选修课成绩和的降序，成绩和相同时按照学号升序)，学生之间以英文分号分隔。
#
# 示例一
# 输入
# 01202021,75;01201033,95;01202008,80;01203006,90;01203088,100
# 01202008,70;01203088,85;01202111,80;01202021,75;01201100,88
# 输出
# 01202
# 01202008;01202021
# 01203
# 01203088
# 说明
# 同时选修了两门选修课的学生 01202021、01202008、01203088，
# 这三个学生两门选修课的成绩和分别为 150、150、185。
# 01202021、01202008 属于 01202 班的学生，按照成绩和降序，
# 成绩相同时按学号升序输出的结果为 01202008;01202021。
# 01203088 属于 01203 班的学生，按照成绩和降序，成绩相同时按学号升序输出的结果为 01203088。
# 01202 的班级编号小于 01203 的班级编号，需要先输出。
#
# 示例二
# 输入
# 01201022,75;01202033,95;01202018,80;01203006,90;01202066,100
# 01202008,70;01203102,85;01202111,80;01201021,75;01201100,88
# 输出
# NULL
# 说明
# 没有同时选修了两门选修课的学生，输出 NULL。
# 解题思路
# 这题属于典型的哈希表和排序的应用，难度不大。但题干较长，需要仔细读题并理解题目含义。
# 由于分了多层的排序，因此代码也比较长，需要写题时对问题时刻保持清晰的头脑。
#
# 代码
# Python

# 题目：2023Q2B-选修课
# 分值：100
# 作者：许老师-闭着眼睛学数理化
# 算法：哈希表，排序
# 代码看不懂的地方，请直接在群上提问

# from collections import defaultdict
#
# # 定义根据传入的lst构建哈希表的函数
# def buildDict(lst):
#     # 初始化一个空哈希表dic
#     dic = dict()
#     # 遍历lst中的每一个字符串元素item
#     for item in lst:
#         # item中用","隔开学号和成绩
#         num, grade = item.split(",")
#         # 以学号num为key，成绩int(grade)为value，存入哈希表dic中
#         dic[num] = int(grade)
#     # 哈希表dic构建完毕，返回dic
#     return dic
#
# # 分别输入两行字符串，表示两门选修课情况，
# # 对字符串根据";"进行分割，存入两个列表中
# lst1 = input().split(";")
# lst2 = input().split(";")
#
# # 根据两个列表，构建两个字典分别表示选修课1和2的选课情况
# # 字典中的key为学号，value为成绩
# dic1 = buildDict(lst1)
# dic2 = buildDict(lst2)
#
# # 由于要统计两门选修课均选了的学生的成绩情况，使用字典推导式构建一个新字典dic_total
# # dic_total的key为学号，value为两门选修课成绩的和
# dic_total = {num: (dic1[num] + dic2[num]) for num in dic1 if num in dic2}
#
# # 如果dic_total长度为0，说明没有任何一个学生同时选了两门选修课
# # 按照题意直接输出"NULL"
# if len(dic_total) == 0:
#     print("NULL")
# # 否则可以进行后续的排序和输出
# else:
#     # 构建一个新的字典用于储存特定班级所包含的学生
#     # key为5位的班级编号，value为储存若干学号的列表
#     dic_class = defaultdict(list)
#     for num in dic_total:
#         # 学号的前5位为班级编号
#         class_num = num[:5]
#         dic_class[class_num].append(num)
#
#     # 遍历dic_class排序后的key，即为班级编号
#     for class_num in sorted(dic_class.keys()):
#         # 先输出班级
#         print(class_num)
#         # 获得班级class_num的所有学号
#         num_lst = dic_class[class_num]
#         # 对num_lst进行排序
#         # 先按照成绩降序排列，即根据-dic_total[x]升序排列
#         # 成绩相同时再按照学号排列，即根据x排列
#         num_lst.sort(key = lambda x: (-dic_total[x], x))
#         # 输出该班级中排序后的学生学号
#         print(";".join(num_lst))

# 时空复杂度
# 时间复杂度：O(NlogN)。排序所需的时间复杂度。
# 空间复杂度：O(N)。哈希表所占的额外空间。

# --------------------------------- D04-08 --------------------------------- 0034
# 【哈希表】2023Q1A-相同数字的积木游戏
# 题目描述与示例
# 题目
# 小华和小薇一起通过玩积木游戏学习数学。他们有很多积木，每个积木块上都有一个数字，积木块上的数字可能相同。
# 小华随机拿一些积木挨着排成一排，请小薇找到这排积木中数字相同且所处位置最远的 2 块积木块，
# 计算他们的距离。小薇请你帮忙替她解决这个问题。
#
# 输入
# 第一行输入为 N ，表示小华排成一排的积木总数。
# 接下来 N 行每行一个数字，表示小花排成一排的积木上数字。
# 输出
# 相同数字的积木的位置最远距离；如果所有积木数字都不相同，请返回 -1
# 示例一
# 输入
# 5
# 1
# 2
# 3
# 1
# 4
# 输出
# 3
# 示例二
# 输入
# 5
# 1
# 2
# 3
# 1
# 1
# 输出
# 4
# 示例三
# 输入
# 2
# 1
# 2
# 输出
# -1
#
# 解题思路
# 本题一道典型的记录下标的哈希表题目，同时也捎带着一点贪心思想。
#
# 由于我们需要找到相距最远的两个相同数字，那么对于某一个出现次数大于等于2次的数字num，
# 我们必定要选其第一个位置和最后一个位置之间的距离来作为可能的答案。
#
# 故我们用哈希表dic记录每一个数字cur第一次出现的下标。在第i次循环中，当
# - 当前数字cur从未出现过，即不位于哈希表中，则记录dic[cur] = i，即i为cur第一次出现的下标。
# - 当前数字cur曾经出现过，即位于哈希表中，则计算cur与其第一次出现的位置的距离为 i - dic[cur]，将该结果与ans进行比较并更新。
# 上述逻辑整理为代码即为
# for i in range(N):
#     cur = input()
#     if cur not in dic:
#         dic[cur] = i
#     else:
#         ans = max(ans, i-dic[cur])
#
# 代码
# 题目：2023Q1A-相同数字的积木游戏
# 分值：100
# 作者：闭着眼睛学数理化
# 算法：哈希表
# 代码看不懂的地方，请直接在群上提问

# N = int(input())
#
# # 初始化哈希表，记录每一个数字第一次出现的下标
# dic = dict()
# # 初始化答案为-1
# ans = -1
#
# # 循环N次
# for i in range(N):
#     # 输入一个数字cur
#     cur = input()
#     # 如果当前数字cur从未出现过，则记录i
#     # i即为cur第一次出现的下标
#     if cur not in dic:
#         dic[cur] = i
#     # 如果当前数字cur曾经出现过
#     # 那么cur与其第一次出现的位置的距离为 i-dic[cur]
#     # 更新ans
#     else:
#         ans = max(ans, i-dic[cur])
#
# print(ans)


# 时空复杂度
# 时间复杂度：O(N)。需要循环N次。
# 空间复杂度：O(N)。哈希表所占用空间。

# --------------------------------- D04-09 --------------------------------- 0035
# 【哈希集合】2023C-英文输入法
# 题目描述与示例
# 题目
# 主管期望你来实现英文输入法单词联想功能，需求如下：
# 1. 依据用户输入的单词前缀，从已输入的英文语句中联想出用户想输入的单词。
# 2. 按字典序输出联想到的单词序列，如果联想不到，请输出用户输入的单词前缀。
# 注意：
# 1. 英文单词联想时区分大小写
# 2. 缩略形式如"don't" 判定为两个单词"don"和 "t"
# 3. 输出的单词序列不能有重复单词，且只能是英文单词，不能有标点符号
# 输入
# 输入两行。
# 首行输入一段由英文单词word和标点构成的语句str，接下来一行为一个英文单词前缀pre。
# 0 < word.length() <= 20，0 < str.length() <= 10000，0 < pre.length() <= 20
# 输出
# 输出符合要求的单词序列或单词前缀。存在多个时，单词之间以单个空格分割
# 示例一
# 输入
# I love you
# He
# 输出
# He
# 说明
# 用户已输入单词语句"I love you"，可以提炼出"I","love","you"三个单词。接下来用户输入"He" ，
# 从已经输入信息中无法联想到符合要求的单词，所以输出用户输入的单词前缀。
# 示例二
# 输入
# The furthest distance in the world,Is not between life and death,
# ~But when I stand in front or you,Yet you don't know that I love you.

# f
# 输出
# front furthest
# 解题思路
# 首先我们需要处理输入，将输入的字符串s根据标点符号和空格隔开，
# 得到一个由若干单词word组成的单词列表lst。
# 这里稍微有点麻烦，不能再用我们熟悉的split()方法完成，而是改为较为麻烦的遍历写法。
#
# 首先我们初始化lst = [""]，即单词列表中存放了一个空字符串。
# 然后我们遍历字符串s中的字符ch，当
# - ch是字母，则将其加入到lst最后一个元素的末尾，即延长当前单词。如果此时lst[-1]为一个空字符串""，则ch充当了某个单词首位字母的角色。
# - ch不是字母，说明遇到一个标点符号，当前单词的获取已经结束，lst的末尾插入一个新的空字符串""。
#
# 上述思路整理为代码后即为：
# lst = [""]
#
# for ch in s:
#     if ch.isalpha():
#         lst[-1] += ch
#     else:
#         lst.append("")
# 当然这个过程也可用正则表达式以更加简短的代码来完成，但这部分知识已经严重超纲，
# 大部分题目完全用不上，学有余力的同学可以自行研究一下。
#
# 得到lst之后，剩下的工作就相当简单了。由于lst中可能出现重复单词，我们使用哈希集合进行去重操作。
# 又因为最后的输出要求按照字典序排序，因此去重之后再对哈希集合进行调用sorted()内置函数，再转化为列表。
# lst_sorted = list(sorted(set(lst)))
# 对于lst_sorted中的每一个单词word，我们可以使用切片来获得其前pre_length个字符所构成的字符串，
# 并与pre进行比较，就能够得知word是否包含前缀pre了。
# pre_length = len(pre)
# for word in lst_sorted:
#     if word[:pre_length] == pre:
#         ans.append(word)
#
# 总体来说本题难度不大，甚至很难归类为哪一种具体的算法（用到去重功能就姑且认为是哈希集合吧）。
# 难点其实主要在于对输入的处理，初始化lst = [""]实际上是一个颇有技巧的做法。
#
# 当然本题还存在着前缀树的最优解法，但也严重超纲，不要求掌握。
#
# 代码
# 解法一
# Python

# 1、X
# 题目：2023Q1A-英文输入法
# 分值：100
# 作者：许老师-闭着眼睛学数理化
# 算法：哈希集合
# 代码看不懂的地方，请直接在群上提问

# s = input()
# pre = input()
#
# # 初始化列表lst用于存放所有单词
# lst = [""]
#
# # 遍历s中的所有字符ch，如果
# # 1. ch是字母，则加入到lst最后一个元素的末尾，即延长当前单词
# # 2. ch不是字母，说明遇到一个标点符号，结束当前单词的获取，lst的末尾插入一个新的空字符串""
# # 这个过程也可以使用正则表达式来完成，不要求掌握，学有余力的同学可以自学一下
# for ch in s:
#     if ch.isalpha():
#         lst[-1] += ch
#     else:
#         lst.append("")
#
# # 用哈希集合去重lst中可能出现的重复单词
# # 去重后进行排序，排序后在转化为列表lst_sorted
# lst_sorted = list(sorted(set(lst)))
#
# # 初始化答案数组
# ans = list()
#
# # 获得pre的长度，用于切片
# pre_length = len(pre)
# # 遍历lst_sorted中的每一个单词
# for word in lst_sorted:
#     # 如果word前pre_length个字符的切片等于pre
#     # 说明word的前缀是pre，将其加入答案数组ans中
#     if word[:pre_length] == pre:
#         ans.append(word)
#
# # 如果ans长度大于0，说明至少存在一个单词的前缀是pre，输出由所有单词组成的字符串
# # 如果ans长度等于0，说明不存在任何一个单词的前缀是pre，返回pre
# print(" ".join(ans) if len(ans) > 0 else pre)


# 2、MosesMin
# s = input()
# pre = input()
#
# # 初始化列表lst用于存放所有单词
# lst = [""]
#
# # 遍历s中的所有字符ch，如果
# # 1. ch是字母，则加入到lst最后一个元素的末尾，即延长当前单词
# # 2. ch不是字母，说明遇到一个标点符号，结束当前单词的获取，lst的末尾插入一个新的空字符串""
# # 这个过程也可以使用正则表达式来完成，不要求掌握，学有余力的同学可以自学一下
# for ch in s:
#     if ch.isalpha():
#         lst[-1] += ch
#     else:
#         lst.append("")
#
# # 用哈希集合去重lst中可能出现的重复单词
# # 去重后进行排序，排序后在转化为列表lst_sorted
# # MosesMin ，不需要这样写：list(sorted(set(lst))) ，sorted()函数会返回list，所以这里写为sorted(set(lst))即可
# lst_sorted = sorted(set(lst))
#
# # 初始化答案数组
# ans = list()
#
# # 获得pre的长度，用于切片
# pre_length = len(pre)
# # 遍历lst_sorted中的每一个单词
# for word in lst_sorted:
#     # 如果word前pre_length个字符的切片等于pre
#     # 说明word的前缀是pre，将其加入答案数组ans中
#     if word[:pre_length] == pre:
#         ans.append(word)
#
# # 如果ans长度大于0，说明至少存在一个单词的前缀是pre，输出由所有单词组成的字符串
# # 如果ans长度等于0，说明不存在任何一个单词的前缀是pre，返回pre
# print(" ".join(ans) if len(ans) > 0 else pre)


# --------------------------------- D04-10 --------------------------------- 0036
# 【哈希集合】2023Q1A-寻找密码
# 题目描述与示例
# 题目描述
# 小王在进行游戏大闯关，有一个关卡需要输入一个密码才能通过，密码获得的条件如下：
# 在一个密码本中，每一页都有一个由 26 个小写字母组成的若干位密码，从它的末尾开始依次去掉一位得到的新密码也在密码本中存在。
# 请输出符合要求的最长密码，如果由多个符合要求的密码，则返回字典序最大的密码。若没有符合要求的密码，则返回空字符串。
#
# 输入
# 密码本由一个字符串数组组成，不同元素之间使用空格隔开，每一个元素代表密码本每一页的密码。
# 输出
# 一个字符串
# 示例一
# 输入
# h he hel hell hello
# 输出
# hello
# 说明
# "hello" 从末尾依次去掉一位得到的 "hell", "hel", "he", "h"在密码本中都存在。
# 示例二
# 输入
# b eredderd bw bww bwwl bwwlm bwwln
# 输出
# bwwln
#
# 解题思路
# 最朴素的解法是将所有字符串都存在一个哈希表password_set中，然后遍历字符串数组中的每一个密码password，
# 对每一个password都去判断其所有的前缀是否也位于password_set中。如果满足，则把password和ans比较并且更新ans。
#
# 这种做法虽然思路直接简单，但略显笨重，会出现很多重复计算。
#
# 以示例一为例子：
# - 对于单词hell，需要分别考虑前缀h、he、hel
# - 对于单词hello，需要分别考虑前缀h、he、hel、hell
# - 前缀h、he、hel对于单词hello而言，显然是重复计算了。
# - 假设我们已经知道单词hell是一个有效的密码，那么对于单词hello，我们就只需要去考虑hell这个前缀，而不需要再去考虑h、he、hel这三个前缀了。
# - 换句话说，单词hello是否是一个有效的密码，可以由其去掉末尾的前缀hell是否是一个有效的密码来决定。
# 这本质上是一种动态规划的思想。（动态规划更详细的内容在后面会讲到）
#
# 如果用动态规划的语言来描述，即：password是一个有效密码，当且仅当password[:-1]是一个有效密码。
#
# 那么现在问题就变成了：如何能够在判断password是一个有效密码之前，就先判断得到password[:-1]是否有效？
# 这个问题就很简单了。我们只需要对原来的字符串数组password_lst按照字典序进行排序，
# 就可以保证在password进行判断时，password[:-1]已经被判断过了。
#
# 我们可以构建一个用于储存所有有效密码的哈希集合valid_set。
# 然后遍历排序过的字符串数组password_lst中的每一个密码password，
# 如果其去掉末尾的前缀password[:-1]位于valid_set中，说明password也是一个有效密码，需要将其加入valid_set中，同时更新ans。
# for password in password_lst:
#     if password[:-1] in valid_set:
#         valid_set.add(password)
#         ans = password
# 注意valid_set初始化时要包含一个空串""，因为只有一个字符的密码比如"h"，
# 去掉最末尾的字符之后是一个空串""，"h"理应是一个有效的密码，故""应该存在于valid_set中。
# 即：
# valid_set = {""}
#
# 代码
# 解法一
# （哈希集合暴力解法，只能通过部分用例）
# Python
# 题目：2023Q1A-寻找密码
# 分值：100
# 作者：闭着眼睛学数理化
# 算法：哈希表暴力解法
# 代码看不懂的地方，请直接在群上提问

# 将输入字符串分割为字符串数组，并且存入哈希集合中
# password_lst = list(input().split())
# password_set = set(password_lst)
# # 初始化答案为一个空字符串
# ans = str()
#
# # 遍历password_lst中的所有密码单词password
# for password in password_lst:
#     # 如果password的长度比ans小，不可能是答案，直接跳过
#     if len(password) < len(ans):
#         continue
#     # password有可能不符合要求，设置一个标记isValid，初始化为True表示该密码符合要求
#     isValid = True
#     # 遍历password的所有前缀password[:i]，判断前缀是否均位于password_set中
#     for i in range(1, len(password)):
#         # 若某一个前缀不位于哈希集合password_set中，则该password无效，修改isValid为False，且退出循环
#         if password[:i] not in password_set:
#             isValid = False
#             break
#     # isValid为True，说明该password有效，将其与ans比较并更新ans
#     if isValid:
#         if len(password) > len(ans):
#             ans = password
#         else:
#             ans = max(ans, password)
# print(ans)

# 时空复杂度
# 时间复杂度：O(NM)。遍历每个单词、每个字符所需的时间。
# 空间复杂度：O(NM)。
# N为单词数目，M为单词平均长度。

# 解法二
# （哈希集合优化解法，含DP思想，可以通过全部用例）
# Python
# 题目：2023Q1A-寻找密码
# 分值：100
# 作者：闭着眼睛学数理化
# 算法：哈希表优化解法
# 代码看不懂的地方，请直接在群上提问

# password_lst = input().split()
# # 对输入的字符串数组进行升序排序
# password_lst.sort()
#
# # 初始化一个表示有效密码的哈希集合，初始化其中仅包含空字符串
# valid_set = {""}
# # 初始化答案为空字符串
# ans = ""
#
# # 从头到尾遍历升序字符串数组password_lst中的密码password
# for password in password_lst:
#     # 如果password去掉最后一位的结果password[:-1]，位于valid_set哈希集合中
#     # 说明当前的password是一个有效密码，将其加入valid_set，同时更新ans
#     if password[:-1] in valid_set:
#         valid_set.add(password)
#         if len(password) >= len(ans):
#             ans = password
#
# print(ans)

# D05 单调栈
# 什么是单调栈？  即满足单调性的栈结构
# 从栈顶到栈底 元素递增  就是单调递增栈；反之 是单调递减栈

# 什么时候用单调栈？
# 在数组中  寻找某个元素  后面的元素 有多个满足条件的后面的元素 选择其中的一个
# 这类问题  适合用单调栈去解决


# 单调栈问题是个套路问题，无论是简单问题还是中等问题和难度问题，
# 单调栈问题的代码框架基本都是如下这样的：
#       1、初始化栈 条件变量
#       2、for 循环
#       3、for 循环中包含一个while 语句
#           while判断条件通常是 stack是否为空  以及当前for中i 和 stack[-1]之间的大小关系

# D05-01 栈、数组、列表在Python中可以理解为都是同一个东西  初始化的方式包括： = list() 、=  []、[0]*26、[0]*n等

# --------------------------------- D05-01 --------------------------------- 0037
# LC1475.商品折扣后的最终价格
# 一、题目描述
# 给你一个数组 prices ，其中 prices[i] 是商店里第 i 件商品的价格。
# 商店里正在进行促销活动，如果你要买第 i 件商品，那么你可以得到与 prices[j] 相等的折扣，
# 其中 j 是满足 j > i 且 prices[j] <= prices[i] 的 最小下标 ，如果没有满足条件的 j ，你将没有任何折扣。
# 请你返回一个数组，数组中第 i 个元素是折扣后你购买商品 i 最终需要支付的价格。
#
# 示例 1：
# 输入：prices = [8,4,6,2,3]
# 输出：[4,2,4,2,3]
# 解释：
# 商品 0 的价格为 price[0]=8 ，你将得到 prices[1]=4 的折扣，所以最终价格为 8 - 4 = 4 。
# 商品 1 的价格为 price[1]=4 ，你将得到 prices[3]=2 的折扣，所以最终价格为 4 - 2 = 2 。
# 商品 2 的价格为 price[2]=6 ，你将得到 prices[3]=2 的折扣，所以最终价格为 6 - 2 = 4 。
# 商品 3 和 4 都没有折扣。
# 示例 2：
# 输入：prices = [1,2,3,4,5]
# 输出：[1,2,3,4,5]
# 解释：在这个例子中，所有商品都没有折扣。
# 示例 3：
# 输入：prices = [10,1,1,6]
# 输出：[9,0,1,6]
#
# 提示：
# - 1 <= prices.length <= 500
# - 1 <= prices[i] <= 10^3

# MosesMin 本题核心图解思路：我们使用的从后往前遍历 （当然也可以从前往后遍历） 只考虑元素值的情况

# 0
# 输入列表情况：[8,4,6,2,3]
# 待入栈情况：【3】
# 待输出列表情况：[  0, 0, 0, 0, 0]

# 1
# 输入列表情况：[8,4,6,2,3]
# 入栈情况：【3】 3后没有元素 所以待输出位置3
# 待输出列表情况：[  0, 0, 0, 0, 3]

# 2
# 输入列表情况：[8,4,6,2,3]
# 入栈情况： 2要入栈，因为2<栈顶元素3 3弹出    栈变为：【2】
# 待输出列表情况：[  0, 0, 0, 2, 3]

# 3
# 输入列表情况：[8,4,6,2,3]
# 入栈情况：6要入栈 因为6>栈顶元素2  所以2不弹出 【2】，6入栈 栈变为：【6,2】
# 6 - 2 = 4
# 待输出列表情况：[  0, 0, 4, 2, 3]

# 4
# 输入列表情况：[8,4,6,2,3]
# 入栈情况：4要入栈 因为4<栈顶元素6  6弹出  栈变为：【2】  4入栈 栈变为【4,2】
# 4 - 2 = 2
# 待输出列表情况：[  0, 2, 4, 2, 3]
# …………

# 另外  还要理解 while判断条件对应的 图解情况


# 二、题目解析
# 暂时无法在飞书文档外展示此内容
# 三、参考代码
# 代码一
# 单调栈解法
# 题目：LC1475. 商品折扣后的最终价格
# 难度：简单
# 作者：吴师兄学算法
# 算法：单调栈，时间复杂度O(N)
# 代码看不懂的地方，请直接在群上提问

# class Solution:
#     def finalPrices(self, prices: list[int]) -> list[int]:
#
#         # 原数组的长度
#         n = len(prices)
#
#         # 初始结果数组的内容，一开始都是 0
#         ans = [0] * n
#
#         # 设置一个栈
#         stack = []
#
#         # 从后向前去遍历原数组 prices
#         # 从后向前去填充 ans
#         for i in range(n - 1, -1, -1):
#             # 获取当前的原始价格
#             p = prices[i]
#
#             # 不断执行如下的逻辑
#             # 1、栈不为空
#             # 2、栈顶元素大于当前的价格
#             # 使得栈中的元素都小于 p
#             while stack and stack[-1] > p:
#                 # 弹出栈顶元素
#                 stack.pop()
#
#             # 此时，对于 i 这个位置的价格来说
#             # 在它的右侧小于 prices[i] 并且最靠近它的价格是 stack 的栈顶元素
#             # 计算差值，获取答案
#             if stack:
#                 ans[i] = p - stack[-1]
#             else:
#                 ans[i] = p
#
#             # 再把当前的价格也压入栈
#             # 栈是一个单调递减栈
#             stack.append(p)
#
#         # 返回答案
#         return ans

# 代码二
# 暴力解法
# # 题目：LC1475. 商品折扣后的最终价格
# # 难度：简单
# # 作者：闭着眼睛学数理化
# # 算法：直接暴力模拟，时间复杂度O(N^2)
# # 代码看不懂的地方，请直接在群上提问
#
# class Solution:
#     def finalPrices(self, prices: list[int]) -> list[int]:
#         for i in range(len(prices)):                # 第一层循环，遍历整个prices数组
#             for j in range(i+1, len(prices)):       # 第二层循环，遍历索引为i+1以及之后元素
#                 if prices[j] <= prices[i]:          # 找到不大于prices[i]的第一个prices[j]
#                     prices[i] -= prices[j]          # 第i个元素的价格修改为折扣价
#                     break                           # 然后退出循环
#         return prices                               # 返回修改后的prices数组


# D05-02 对应位置的输出 而非输入
# --------------------------------- D05-02 --------------------------------- 0038
# LC739. 每日温度  ★
# 视频讲解。
# https://uha.xet.tech/s/1HttXN
# 一、题目描述
# 根据每日 气温 列表，请重新生成一个列表，对应位置的输入（应该是： 对应位置的输出 MosesMin 20240328）是你需要再等待多久温度才会升高超过该日的天数。
# 如果之后都不会升高，请在该位置用 0 来代替。
#
# 例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，
# 你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。
#
# 提示：气温 列表长度的范围是 [1, 30000]。
# 每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。

# 二、题目解析
# 这道题目最 “难” 的一个点是题目的理解。
# 给定列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，为啥输出就是 [1, 1, 4, 2, 1, 1, 0, 0] ？
# 下面来一个个进行解释。
# 对于输入 73，它需要 经过一天 才能等到温度的升高，也就是在第二天的时候，温度升高到 74 ，所以对应的结果是 1。
# 对于输入 74，它需要 经过一天 才能等到温度的升高，也就是在第三天的时候，温度升高到 75 ，所以对应的结果是 1。
# 对于输入 75，它经过 1 天后发现温度是 71，没有超过它，继续等，一直 等了四天，在第七天才等到温度的升高，温度升高到 76 ，所以对应的结果是 4 。
# 对于输入 71，它经过 1 天后发现温度是 69，没有超过它，继续等，一直 等了两天，在第六天才等到温度的升高，温度升高到 72 ，所以对应的结果是 2 。
# 对于输入 69，它 经过一天 后发现温度是 72，已经超过它，所以对应的结果是 1 。
# 对于输入 72，它 经过一天 后发现温度是 76，已经超过它，所以对应的结果是 1 。
# 对于输入 76，后续 没有温度 可以超过它，所以对应的结果是 0 。
# 对于输入 73，后续 没有温度 可以超过它，所以对应的结果是 0 。
# 也就是说，这道题目就是给你一个值，让你找到右边第一个比它大的数，它们两则的下标差就是输出结果。
# 好了，理解了题意我们来思考如何求解：借助单调递增栈来处理。

# 具体操作如下：
# 遍历整个数组，如果栈不空，且当前数字大于栈顶元素，那么如果直接入栈的话就不是 递增栈 ，
# 所以需要取出栈顶元素，由于当前数字大于栈顶元素的数字，而且一定是第一个大于栈顶元素的数，直接求出下标差就是二者的距离。
# 继续看新的栈顶元素，直到当前数字小于等于栈顶元素停止，再将数字入栈，
# 这样就可以一直保持递增栈，且每个数字和第一个大于它的数的距离也可以算出来。

# MosesMin 本题核心图解思路：索引和元素值一起入栈 例如 [0-73]

# 1
# 输入列表情况：[73, 74, 75, 71, 69, 72, 76, 73]
# 入栈情况：【0-73】
# 待输出列表情况：[0, 0, 0, 0, 0, 0, 0, 0]

# 2
# 输入列表情况：[73, 74, 75, 71, 69, 72, 76, 73]
# 入栈情况：【1-74】 因为74>73 0-73弹出
# 1 - 0 = 1
# 待输出列表情况：[1, 0, 0, 0, 0, 0, 0, 0]

# 3
# 输入列表情况：[73, 74, 75, 71, 69, 72, 76, 73]
# 入栈情况：【2-75】 因为75>74 1-74弹出
# 2 - 1 = 1
# 待输出列表情况：[1, 1, 0, 0, 0, 0, 0, 0]

# 4
# 输入列表情况：[73, 74, 75, 71, 69, 72, 76, 73]
# 入栈情况：【3-71,2-75】 71<75  3-71入栈
# 待输出列表情况：[1, 1, 0, 0, 0, 0, 0, 0]

# 5
# 输入列表情况：[73, 74, 75, 71, 69, 72, 76, 73]
# 入栈情况：【4-69,3-71，2-75】
# 待输出列表情况：[1, 1, 0, 0, 0, 0, 0, 0]

# 6 while的持续过程
# 输入列表情况：[73, 74, 75, 71, 69, 72, 76, 73]
# 入栈情况：【5-72,3-71,2-75】  4-69弹出
# 5-4 =1
# 待输出列表情况：[1, 1, 0, 0, 1, 0, 0, 0]

# 7 while的持续过程
# 输入列表情况：[73, 74, 75, 71, 69, 72, 76, 73]
# 入栈情况：【5-72，2-75】  3-71弹出
# 5-3 =1
# 待输出列表情况：[1, 1, 0, 2, 1, 0, 0, 0]

# …………

# 另外  还要理解 while判断条件对应的 图解情况

# 三、参考代码
# 登录 AlgoMooc 官网获取更多算法图解
# https://www.algomooc.com
# 作者：程序员吴师兄
# 代码有看不懂的地方一定要私聊咨询吴师兄呀
# 每日温度（ LeetCode 739 ）：https://leetcode-cn.com/problems/daily-temperatures
# class Solution:
#     def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
#
#         # 构建一个栈,用来存放每日温度的下标
#         stack = []
#
#         # 获取数组长度
#         length = len(temperatures)
#
#         # 构建一个数组，用来保存输出结果
#         res = [0] * length
#
#         # 从头开始遍历每天的温度
#         for i in range(length):
#             #  拿到当天的温度，不断的和栈顶元素进行比较
#             temperature = temperatures[i]
#
#             # 如果栈顶元素存在并且当天的温度大于栈顶元素
#             # 意味着栈顶元素等到了第一个温度比它更高的那一天
#             # 它们的下标差就是栈顶元素等了多少天等到的更高温度的结果
#             while stack and temperature > temperatures[stack[-1]]:
#                 # 首先获取栈顶元素的值，也就是每日温度的下标值
#                 preIndex = stack.pop()
#
#                 # 它们的下标差就是栈顶元素等了多少天等到的更高温度的结果，保存到输出数组 res 中
#                 res[preIndex] = i - preIndex
#
#             # 再把当天的温度的下标值存放到栈中
#             # 注意：是下标索引值
#             stack.append(i)
#
#         # 最后输出 res 数组即可
#         return res

# 四、复杂度分析
# 时间复杂度：O(n)，其中 n 是温度列表的长度。正向遍历温度列表一遍，对于温度列表中的每个下标，最多有一次进栈和出栈的操作。
# 空间复杂度：O(n)，其中 n 是温度列表的长度。需要维护一个单调栈存储温度列表中的下标。


# --------------------------------- D05-03 --------------------------------- 0039
# D05-03  接雨水 超高频题目★★★★★
# LC42. 接雨水
# 视频地址。
# https://uha.xet.tech/s/2lE6fM
# 一、题目描述
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# [图片]
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
#
# 二、题目解析
# 我们按照行方向去接雨水。
# [图片]
# 接下来我们去寻找凹槽。
# 一个凹槽是由三个柱子围成的。（这里为了描述方便，我们把高度为 0 的柱子也当成存在的柱子）
# [图片]
# 对于这个凹槽来说，它的左侧和底部是由栈中挑选出来的，右侧是由新添加的柱子决定的。
# 什么情况会出现凹槽呢？
# 一旦新添加的柱子高度大于栈顶元素，就有可能形成凹槽！
# [图片]
# 这个时候，栈顶元素是凹槽的底部，如果在栈中存在栈顶元素之前的元素，
# 那么栈顶元素之前的元素就是凹槽的左侧，此时添加的元素是凹槽的右侧。
#
# 这里之所以是说有可能，是因为柱子里面可能是两根高度一样的柱子，
# 即使新添加的柱子高度都大于它们，也是无法构成凹槽，或者说构成了一个面积为 0 的凹槽。
# [图片]
# 如果新添加的柱子高度小于栈顶元素，那么必然无法和当前的栈中元素构成一个凹槽，
# 因为这是一个单调栈，里面的元素越靠近栈顶越小，新添加的柱子高度都小于了栈顶元素，
# 那必然小于里面其它的元素，这种情况下，无法围成一个凹槽，
# 我们就把当前的柱子加入到我们的栈中，让它和里面的柱子一起等待接下来的柱子。
# [图片]
# 如果新添加的柱子高度等于栈顶元素，也是无法形成凹槽的，
# 我们就把当前的柱子加入到我们的栈中，让它和里面的柱子一起等待接下来的柱子。
# 一旦形成了凹槽，我们去计算它的面积。
# 面积由高和宽决定。
# 凹槽的高度是由 min(凹槽左边高度, 凹槽右边高度) - 凹槽底部高度 来计算的。
# [图片]
# 凹槽的宽度是由凹槽右边的下标 - 凹槽左边的下标 - 1（因为只求中间宽度）来计算的。
# [图片]
# 计算完一个凹槽的面积之后，我们就把栈顶元素弹出，
# 察剩下的那些栈中的元素能否和新添加的元素再构成一个新的凹槽。

# MosesMin 本题核心图解思路：入栈时，凹槽元素之后的元素比凹槽元素大 凹槽元素弹出
# [0,1,0,2,1,0,1,3,2,1,2,1]  比如索引为2的0 就是个凹槽元素  遇到索引为3的元素2时  0就要弹出
# 另外  还要理解 while判断条件对应的 图解情况

# 三、参考代码
# 登录 AlgoMooc 官网获取更多算法图解
# https://www.algomooc.com
# 作者：程序员吴师兄
# 代码有看不懂的地方一定要私聊咨询吴师兄呀
# 接雨水（ LeetCode 42 ）:https://leetcode-cn.com/problems/trapping-rain-water/
# class Solution:
#     def trap(self, height: list[int]) -> int:
#         # 构建一个栈，用来存储对应的柱子的下标
#         # stack 存储的是下标而非高度
#         stack = list()
#
#         # 一开始水的面积是 0
#         result = 0
#
#         # 获取数组的长度
#         n = len(height)
#
#         # 从头开始遍历整个数组
#         for i, h in enumerate(height):
#             # 如果栈为空，那么直接把当前索引加入到栈中
#             if not stack:
#                 # 把当前索引加入到栈中
#                 stack.append(i)
#
#             # 否则的话，栈里面是有值的，我们需要去判断此时的元素、栈顶元素、栈顶之前的元素能否形成一个凹槽
#             # 情况一：此时的元素小于栈顶元素，凹槽的右侧不存在，无法形成凹槽
#             elif height[i] < height[stack[-1]]:
#                 # 把当前索引加入到栈中
#                 stack.append(i)
#
#             # 情况二：此时的元素等于栈顶元素，也是无法形成凹槽
#             elif height[i] == height[stack[-1]]:
#
#                 # 把当前索引加入到栈中
#                 stack.append(i)
#
#             # 情况三：此时的的元素大于栈顶元素，有可能形成凹槽
#             # 注意是有可能形成，因为比如栈中的元素是 2 、2 ，此时的元素是 3，那么是无法形成凹槽的
#             else:
#
#                 # 由于栈中有可能存在多个元素，移除栈顶元素之后，剩下的元素和此时的元素也有可能形成凹槽
#                 # 因此，我们需要不断的比较此时的元素和栈顶元素
#                 # 此时的元素依旧大于栈顶元素时，我们去计算此时的凹槽面积
#                 # 借助 while 循环来实现这个操作
#                 while stack and height[i] > height[stack[-1]]:
#
#                     # 1、获取栈顶的下标，bottom 为凹槽的底部位置
#                     bottom = stack[-1]
#
#                     # 将栈顶元素推出，去判断栈顶之前的元素是否存在，即凹槽的左侧是否存在
#                     stack.pop()
#
#                     # 2、如果栈不为空，即栈中有元素，即凹槽的左侧存在
#                     if stack:
#                         # 凹槽左侧的高度 height[stack[-1] 和 凹槽右侧的高度 height[i]
#                         # 这两者的最小值减去凹槽底部的高度就是凹槽的高度
#                         h = min(height[stack[-1]], height[i]) - height[bottom]
#
#                         # 凹槽的宽度等于凹槽右侧的下标值 i 减去凹槽左侧的下标值 stack.top 再减去 1
#                         w = i - stack[-1] - 1
#
#                         # 将计算的结果累加到最终的结果上去
#                         result += h * w
#
#                 # 栈中和此时的元素可以形成栈的情况在上述 while 循环中都已经判断了
#                 # 那么，此时栈中的元素必然不可能大于此时的元素，所以可以把此时的元素添加到栈中
#                 stack.append(i)
#
#         # 最后返回结果即可
#         return result

# MosesMin优化版本：
# class Solution:
#     # D05-03 MosesMin变体1
#     # 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
#     # 输出：6
#     def trap1(self, height: list[int]) -> int:
#         stack = []  # stack = list()
#         ans = 0
#
#         for i,h in enumerate(height):
#             if not stack:
#                 stack.append(i)
#
#             elif h <= height[stack[-1]]:
#                 stack.append(i)
#
#             else:
#                 while stack and height[i] > height[stack[-1]]:
#                     bottom = stack[-1]
#                     stack.pop()
#
#                     if stack:
#                         h = min(height[stack[-1]], height[i]) - height[bottom]
#                         w = i - stack[-1] - 1
#
#                         ans += h * w
#
#                 stack.append(i)
#         return ans
#
#     # D05-03 MosesMin变体2
#     # 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
#     # 输出：6
#     def trap2(self, height: list[int]) -> int:
#         stack = []  # stack = list()
#         ans = 0
#         length = len(height)
#         for i in range(length):
#             if not stack:
#                 stack.append(i)
#
#             elif height[i] <= height[stack[-1]]:
#                 stack.append(i)
#
#             else:
#                 while stack and height[i] > height[stack[-1]]:
#                     bottom = stack[-1]
#                     stack.pop()
#
#                     if stack:
#                         h = min(height[stack[-1]], height[i]) - height[bottom]
#                         w = i - stack[-1] - 1
#
#                         ans += h * w
#
#                 stack.append(i)
#         return ans
#
#     # D05-03 MosesMin变体3--最重要 自己重新理了逻辑架构
#     # 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
#     # 输出：6
#     def trap(self, height: list[int]) -> int:
#         # 一开始水的面积是 0
#         ans = 0
#         # 构建一个栈，用来存储对应的柱子的下标
#         # stack 存储的是下标而非高度
#         stack = []
#         # 获取数组的长度
#         length = len(height)
#         # 从头开始遍历整个数组
#         for i in range(length):
#             # 如果栈为空，那么直接把当前索引加入到栈中
#             if not stack:
#                 stack.append(i)
#             # 如果栈不为空
#             # 则说明，栈里面是有值的，我们需要去判断此时的元素、栈顶元素、栈顶之前的元素能否形成一个凹槽
#             else:
#                 # 情况一、二：此时的元素小于（情况一）或者等于（情况二）栈顶元素，凹槽的右侧不存在，无法形成凹槽
#                 if height[i] <= height[stack[-1]]:
#                     # 把当前索引加入到栈中
#                     stack.append(i)
#                 # 情况三：此时的的元素大于栈顶元素，有可能形成凹槽
#                 # 注意是有可能形成，因为比如栈中的元素是 2 、2 ，此时的元素是 3，那么是无法形成凹槽的
#                 else:
#                     # 由于栈中有可能存在多个元素，移除栈顶元素之后，剩下的元素和此时的元素也有可能形成凹槽
#                     # 因此，我们需要不断的比较此时的元素和栈顶元素
#                     # 此时的元素依旧大于栈顶元素时，我们去计算此时的凹槽面积
#                     # 借助 while 循环来实现这个操作
#                     while stack and height[i] > height[stack[-1]]:
#                         # 1、获取栈顶的下标，bottom 为凹槽的底部位置
#                         bottom = stack[-1]
#                         # 将栈顶元素推出，去判断栈顶之前的元素是否存在，即凹槽的左侧是否存在
#                         stack.pop()
#                         # 2、如果栈不为空，即栈中有元素，即凹槽的左侧存在
#                         if stack:
#                             # 凹槽左侧的高度 height[stack[-1] 和 凹槽右侧的高度 height[i]
#                             # 这两者的最小值减去凹槽底部的高度就是凹槽的高度
#                             h = min(height[stack[-1]], height[i]) - height[bottom]
#                             # 凹槽的宽度等于凹槽右侧的下标值 i 减去凹槽左侧的下标值 stack.top 再减去 1
#                             w = i - stack[-1] - 1
#                             # 将计算的结果累加到最终的结果上去
#                             ans += h * w
#                     # 栈中和此时的元素可以形成栈的情况在上述 while 循环中都已经判断了
#                     # 那么，此时栈中的元素必然不可能大于此时的元素，所以可以把此时的元素添加到栈中
#                     stack.append(i)
#         # 最后返回结果即可
#         return ans


# 四、复杂度分析
# 时间复杂度：O(n)，其中 n 是数组 height 的长度。从 0 到 n−1 的每个下标最多只会入栈和出栈各一次。
# 空间复杂度：O(n)，其中 nn 是数组 height 的长度。空间复杂度主要取决于栈空间，栈的大小不会超过 n。


# --------------------------------- D05-04 --------------------------------- 0040
# LeetCode232、用栈实现队列
# 视频地址。
# https://uha.xet.tech/s/2Mo01r
# 一、题目描述
# 请你仅使用两个栈实现先入先出队列。
# 队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：
# 实现 MyQueue 类：
# - void push(int x)将元素 x 推到队列的末尾
# - int pop() 从队列的开头移除并返回元素
# - int peek() 返回队列开头的元素
# - boolean empty()如果队列为空，返回 True ；否则，返回 False
# 二、题目解析
# 入队操作
# 如果是栈的插入操作，那我们可以把元素都先插入到 stackIn 中，也就实现了队列的 入队操作 。
# 出队操作
# - 当 stackOut 中不为空时，直接操作，此时在 stackOut 中的栈顶元素是最先进入队列的元素，返回该元素即可；
# - 如果 stackOut 为空且 stackIn 不为空，首先需要把 stackIn 中的元素逐个弹出并压入到 stackOut 中，然后返回  stackOut 的栈顶元素即可。
# 三、参考代码
# 登录 AlgoMooc 官网获取更多算法图解
# https://www.algomooc.com
# 作者：程序员吴师兄
# 代码有看不懂的地方一定要私聊咨询吴师兄呀
# 用栈实现队列 （ LeetCode 232 ）:https://leetcode-cn.com/problems/implement-queue-using-stacks/
# class MyQueue:
#     def __init__(self):
#         # 一个栈叫做 stackIn，负责进栈操作，相当于队列 queue 中的入队操作
#         self.stackIn = []
#         # 一个栈叫做 stackOut，负责出栈操作，相当于队列 queue 中的出队操作
#         self.stackOut = []
#
#
#     def push(self, x: int) -> None:
#         # 新添加的元素添加到 stackIn 中
#         self.stackIn.append(x)
#
#
#     def pop(self) -> int:
#         # 如果 stackOut 为空，首先需要将 stackIn 中的所有元素添加到 stackOut 中
#         #注意 stackIn 是栈，栈的性质是先进后出，后进先出，所以是不断的将 stackIn 中的栈顶元素添加进 stackOut 中
#         if not self.stackOut:
#             # 通过 while 循环将 stackIn 中的所有元素都取出
#             while self.stackIn:
#                 # stackOut 不断的添加 stackIn 的栈顶元素
#                 self.stackOut.append(self.stackIn.pop())
#         # 此时，stackIn 已经为空，直接「移除」 stackOut 的栈顶元素
#         return self.stackOut.pop()
#
#
#     def peek(self) -> int:
#         # peek 和 pop 的区别在于是返回栈顶元素而非删除栈顶元素
#         # 如果 stackOut 为空，首先需要将 stackIn 中的所有元素添加到 stackOut 中
#         # 注意 stackIn 是栈，栈的性质是先进后出，后进先出，所以是不断的将 stackIn 中的栈顶元素添加进 stackOut 中
#         if not self.stackOut:
#             # 通过 while 循环将 stackIn 中的所有元素都取出
#             while self.stackIn:
#                 # stackOut 不断的添加 stackIn 的栈顶元素
#                 self.stackOut.append(self.stackIn.pop())
#
#         # peek 和 pop 的区别在于是返回栈顶元素而非删除栈顶元素
#         # 此时，stackIn 已经为空，直接「返回」 stackOut 的栈顶元素
#         return self.stackOut[-1]
#
#
#     def empty(self) -> bool:
#         # 队列是否为空，判断 stackIn 和 stackOut 是否同时不存在元素
#         return not self.stackIn and not self.stackOut


# --------------------------------- D05-05 --------------------------------- 0041
# [] LC225. 用队列实现栈
# 飞书文档中只有题目名  暂无题解链接  MosesMin 20240328
# leetcode官方题解链接如下：
# https://leetcode.cn/problems/implement-stack-using-queues/solutions/432204/yong-dui-lie-shi-xian-zhan-by-leetcode-solution/

# 一、题目描述：
# 请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（push、top、pop和empty）。
#
# 实现MyStack类：
# void push(int x) 将元素x压入栈顶。
# int pop() 移除并返回栈顶元素。
# int top() 返回栈顶元素。
# boolean empty() 如果栈是空的，返回true ；否则，返回false 。
#
#
# 注意：
#
# 你只能使用队列的标准操作 —— 也就是
# push to back、peek / pop from front、size 和 is empty这些操作。
# 你所使用的语言也许不支持队列。 你可以使用list （列表）或者deque（双端队列）来模拟一个队列, 只要是标准的队列操作即可。
#
#
# 示例：
#
# 输入：
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# 输出：
# [null, null, null, 2, 2, false]
#
# 解释：
# MyStack
# myStack = new
# MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // 返回
# 2
# myStack.pop(); // 返回
# 2
# myStack.empty(); // 返回
# False
#
# 提示：
#
# 1 <= x <= 9
# 最多调用100
# 次
# push、pop、top
# 和
# empty
# 每次调用
# pop
# 和
# top
# 都保证栈不为空
#
# 进阶：你能否仅用一个队列来实现栈。

# D05 - 05
# MosesMin补充：队列的特性
# from collections import deque
#
# # 创建一个队列
# queue = deque([1, 2, 3, 4, 5])
#
# # 使用 popleft() 移除并返回队首元素
# first_element = queue.popleft()
# print("移除的队首元素是:", first_element)
# last_element = queue.pop()
# print("移除的队尾元素是:", last_element)
# # 打印移除元素后的队列
# print("移除元素后的队列:", queue)
#
# 输出：
# 移除的队首元素是: 1
# 移除的队尾元素是: 5
# 移除元素后的队列: deque([2, 3, 4])

# 二、题目解析
# https://leetcode.cn/problems/implement-stack-using-queues/solutions/432204/yong-dui-lie-shi-xian-zhan-by-leetcode-solution/
# 三、参考代码
# 方法一：两个队列
# import collections
# class MyStack:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.queue1 = collections.deque()
#         self.queue2 = collections.deque()
#
#
#     def push(self, x: int) -> None:
#         """
#         Push element x onto stack.
#         """
#         self.queue2.append(x)
#         while self.queue1:
#             self.queue2.append(self.queue1.popleft())
#         self.queue1, self.queue2 = self.queue2, self.queue1
#
#
#     def pop(self) -> int:
#         """
#         Removes the element on top of the stack and returns that element.
#         """
#         return self.queue1.popleft()
#
#
#     def top(self) -> int:
#         """
#         Get the top element.
#         """
#         return self.queue1[0]
#
#
#     def empty(self) -> bool:
#         """
#         Returns whether the stack is empty.
#         """
#         return not self.queue1


# 方法二：一个队列
# import collections
# class MyStack:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.queue = collections.deque()
#
#
#     def push(self, x: int) -> None:
#         """
#         Push element x onto stack.
#         """
#         n = len(self.queue)
#         self.queue.append(x)
#         for _ in range(n):
#             self.queue.append(self.queue.popleft())
#
#
#     def pop(self) -> int:
#         """
#         Removes the element on top of the stack and returns that element.
#         """
#         return self.queue.popleft()
#
#
#     def top(self) -> int:
#         """
#         Get the top element.
#         """
#         return self.queue[0]
#
#
#     def empty(self) -> bool:
#         """
#         Returns whether the stack is empty.
#         """
#         return not self.queue


# --------------------------------- D05-06 --------------------------------- 0042
# LC496. 下一个更大元素 I
# https://uha.xet.tech/s/2lwUQi
# 一、题目描述
# nums1 中数字 x 的 下一个更大元素 是指 x 在 nums2 中对应位置 右侧 的 第一个 比 x 大的元素。
# 给你两个 没有重复元素 的数组 nums1 和 nums2 ，下标从 0 开始计数，其中nums1 是 nums2 的子集。
# 对于每个 0 <= i < nums1.length ，找出满足 nums1[i] == nums2[j] 的下标 j ，
# 并且在 nums2 确定 nums2[j] 的 下一个更大元素 。如果不存在下一个更大元素，那么本次查询的答案是 -1 。
# 返回一个长度为 nums1.length 的数组 ans 作为答案，满足 ans[i] 是如上所述的 下一个更大元素 。
# 示例 1：
# 输入：nums1 = [4,1,2], nums2 = [1,3,4,2].
# 输出：[-1,3,-1]
# 解释：nums1 中每个值的下一个更大元素如下所述：
# - 4 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。
# - 1 ，用加粗斜体标识，nums2 = [1,3,4,2]。下一个更大元素是 3 。
# - 2 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。
# 示例 2：
# 输入：nums1 = [2,4], nums2 = [1,2,3,4].
# 输出：[3,-1]
# 解释：nums1 中每个值的下一个更大元素如下所述：
# - 2 ，用加粗斜体标识，nums2 = [1,2,3,4]。下一个更大元素是 3 。
# - 4 ，用加粗斜体标识，nums2 = [1,2,3,4]。不存在下一个更大元素，所以答案是 -1 。
# 提示：
# - 1 <= nums1.length <= nums2.length <= 1000
# - 0 <= nums1[i], nums2[i] <= 104
# - nums1和nums2中所有整数 互不相同
# - nums1 中的所有整数同样出现在 nums2 中
# 二、参考代码
# 1、W
# class Solution:
#     def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
#
#         # 先计算 nums2 • 中每个元素右边的第一个更大的值
#         # 结果存放到一个哈希集合里面
#         # MosesMin注： 上一行注释吴师兄说哈希集合 意思应该是哈希表 哈希表 在python中就是字典 dict(),也可以直接用{}初始化  哈希表的键不能重复  值可以重复
#         # MosesMin注：哈希集合在python中是 set()  哈希集合中元素值不能重复
#         # key 是 nums2 中的元素
#         # value 是这个元素右边的第一个更大的值
#         res = {}
#
#         # 设置一个栈
#         # 这个栈是一个单调递增栈
#         stack = []
#
#         # 从后向前访问 nums 中的元素
#         # 从后往前的写法2： for i in range(len-1,-1,-1)  :表示从索引 len-1 遍历到 0，步长是-1
#         for num in reversed(nums2):
#             # 在访问过程中
#             # 维护单调递增栈的性质
#             # 不断的去拿栈顶元素和当前元素 num 比较
#             # 1、直到找到一个比 num 更大的元素为止
#             # 2、或者栈为空位置
#             while stack and num >= stack[-1]:
#                 # 出栈操作
#                 stack.pop()
#
#             # 1、如果栈不为空，那么此时的栈顶元素就是一个比 num 更大的元素
#             # 存放栈顶元素值到哈希集合 res 中
#             # 2、如果栈为空，说明在 num 的右侧没有任何一个元素比它更大
#             # 存放 -1 到哈希集合 res 中
#             res[num] = stack[-1] if stack else -1
#
#             # 把当前元素加入到栈中
#             stack.append(num)
#
#         # 初始结果数组
#         ans = []
#
#         # 1、由于两个数组都是没有重复元素的数组
#         # 2、nums1 是 nums2 的子集
#         for num in nums1:
#             # 那么就去哈希集合 res 中找出对应元素的值来
#             ans.append(res[num])
#
#         # 返回结果
#         return ans


# 2、MosesMin
# class Solution:
#     # 输入：nums1 = [2,4], nums2 = [1,2,3,4].
#     # 输出：[3,-1]
#     def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
#         res = {}
#         stack = []
#
#         for num in reversed(nums2):
#             while stack and num >= stack[-1]:
#                 stack.pop()
#             res[num] = stack[-1] if stack else -1
#             stack.append(num)
#         ans = []
#
#         for num in nums1:
#             ans.append(res[num])
#         return ans


# --------------------------------- D05-07 --------------------------------- 0043
# 【单调栈】2023C-找朋友
# 题目描述与示例
# 题目描述
# 在学校中，N个小朋友站成一队， 第i个小朋友的身高为height[i]，
# 第i个小朋友可以看到的右边的第一个比自己身高更高的小朋友j，那么j是i的好朋友（j > i）。
# 请重新生成一个列表，对应位置的输出是每个小朋友的好朋友位置，如果没有看到好朋友，请在该位置用0代替。小朋友人数范围是 [0, 40000]。
#
# 输入描述
# 第一行输入N，表示有N个小朋友
# 第二行输入N个小朋友的身高height[i]，都是整数
# 输出描述
# 输出N个小朋友的好朋友的位置
# 示例一
# 输入
# 2
# 100 95
# 输出
# 0 0
# 示例二
# 输入
# 8
# 123 124 125 121 119 122 126 123
# 输出
# 1 2 6 5 5 6 0 0
# 解题思路
# 注意，本题和LC739. 每日温度非常类似。区别在于，
# 本题需要找到的是右边下一个更大元素的索引，而非与当前元素的间隔，显然变得更加简单了。
#
# 我们讲过，类似这种要求寻找左边/右边最近的更大/更小元素的题目，均可以使用单调栈来完成。
#
# 对于单调栈的题目，既可以正序遍历也可以逆序遍历数组来完成，
# 重点在于理解单调栈的原理，同学们只需要选择适合自己理解的方法来完成即可。以下表格总结了两种不同遍历顺序的异同点。
#
# 正序遍历
# 逆序遍历
# 单调栈顺序
# 栈中储存的索引所对应在原数组中的元素大小，从栈底至栈顶单调递减，即更大的数（的下标）位于栈底
#
# 入栈时机
# 栈顶元素反复出栈并修改ans之后，进行入栈。且入栈元素为当前下标i，而非身高h
#
# 修改ans时机
# i为preIndex的下一个更大元素的下标，在出栈过程中，即在while内修改ans[preIndex]
# stack[-1]为i的下一个更大元素的下标，在出栈结束后，即在while外修改ans[i]
# 出栈条件
# h > height[stack[-1]]
# h >= height[stack[-1]]

# D05-07 文档仔细看下  正序和逆序的对别与区别 --MosesMin

# D05-07 map的作用
# lst_str = ["1", "2", "3"]
# print(lst_str)
# # 得到lst_num为[1, 2, 3]
# lst_num = list(map(int, lst_str))
# print(lst_num)

# 输出：
# ['1', '2', '3']
# [1, 2, 3]

# 代码
# 解法一
# Python
# 正序遍历height构建单调栈。

# # 题目：2023Q1A-找朋友
# # 分值：100
# # 作者：许老师-闭着眼睛学数理化
# # 算法：单调栈-正序遍历原数组
# # 代码看不懂的地方，请直接在群上提问
#
#
# # 输入小朋友个数n
# n = int(input())
# # 输入N个小朋友的高度数组
# height = list(map(int, input().split()))
#
# # 构建一个单调栈，用来存放不同小朋友的身高的索引
# # 栈中储存的索引所对应在height中的元素大小，从栈底至栈顶单调递减
# # 即更大的数（的下标）位于栈底
# stack = list()
#
# # 构建列表ans，用来保存输出结果
# # 初始化其中所有的元素均为0
# ans = [0] * n
#
# # 从头开始遍历每一个小朋友的身高
# for i, h in enumerate(height):
#     # 第i个小朋友的身高h，需要不断地与栈顶元素比较
#     # 如果栈顶元素存在并且h【大于】栈顶元素stack[-1]
#     # 意味着栈顶元素找到了右边最近的比他更高的身高h
#     while len(stack) > 0 and h > height[stack[-1]]:
#         # 首先获取栈顶元素的值，也就是上一个比h小的身高的索引值
#         preIndex = stack.pop()
#
#         # i即为preIndex这个索引所对应的，下一个最近身高
#         ans[preIndex] = i
#
#     # 再把当前小朋友身高的下标i存放到栈中
#     # 注意：所储存的是下标i，而不是身高h
#     stack.append(i)
#
# # ans中的int元素转成str后才能合并成字符串
# print(" ".join(map(str, ans)))


# 解法二
# 逆序遍历height构建单调栈。
# # 题目：2023Q1A-找朋友
# # 分值：100
# # 作者：许老师-闭着眼睛学数理化
# # 算法：单调栈-逆序遍历原数组
# # 代码看不懂的地方，请直接在群上提问
#
#
# # 输入小朋友个数n
# n = int(input())
# # 输入N个小朋友的高度数组
# height = list(map(int, input().split()))
#
# # 构建一个单调栈，用来存放不同小朋友的身高的索引
# # 栈中储存的索引所对应在height中的元素大小，从栈底至栈顶单调递增
# # 即更大的数（的下标）位于栈底
# stack = list()
#
# # 构建列表ans，用来保存输出结果
# # 初始化其中所有的元素均为0
# ans = [0] * n
#
# # 逆序遍历每一个小朋友的身高
# for i in range(n-1, -1, -1):
#     h = height[i]
#     # 第i个小朋友的身高h，需要不断地与栈顶元素比较
#     # 如果栈顶元素存在并且h【大于等于】栈顶元素stack[-1]
#     # 说明栈顶元素stack[-1]并不是身高h右边最近的比h更大的元素
#     # 需要将栈顶元素弹出，继续寻找比h大的栈顶元素
#     while len(stack) > 0 and h >= height[stack[-1]]:
#         # 栈顶元素下标对应的身高不大于当前身高h，不是符合要求的更大身高，弹出
#         stack.pop()
#     # 完成弹出后，如果栈顶仍存在元素，说明stack[-1]所对应的身高，是严格比h大的下一个身高
#     if len(stack) > 0:
#         # ans[i]修改为stack[-1]
#         ans[i] = stack[-1]
#
#     # 再把当前小朋友身高的下标i存放到栈中
#     # 注意：所储存的是下标i，而不是身高h
#     stack.append(i)
#
# # ans中的int元素转成str后才能合并成字符串
# print(" ".join(map(str, ans)))


# 时空复杂度
# 时间复杂度：O(N)。不管是正序还是逆序遍历，均仅需一次遍历height数组。
# 空间复杂度：O(N)。单调栈所占用的额外空间。

# MosesMin总结 正序逆序
# # 输入小朋友个数n
# n = int(input())
# # 输入N个小朋友的高度数组
# height = list(map(int,input().split()))
# # 构建列表ans，用来保存输出结果
# # 初始化其中所有的元素均为0
# ans = [0]*n
# # 构建一个单调栈，用来存放不同小朋友的身高的索引
# # 栈中储存的索引所对应在height中的元素大小，从栈底至栈顶单调递增
# # 即更大的数（的下标）位于栈底
# stack = list()
#
# # 顺序
# # 从头开始遍历每一个小朋友的身高
# for i, h in enumerate(height):
#     # 第i个小朋友的身高h，需要不断地与栈顶元素比较
#     # 如果栈顶元素存在并且h【大于】栈顶元素stack[-1]
#     # 意味着栈顶元素找到了右边最近的比他更高的身高h
#     while len(stack) > 0 and h > height[stack[-1]]:
#         # 首先获取栈顶元素的值，也就是上一个比h小的身高的索引值
#         preIndex = stack.pop()
#
#         # i即为preIndex这个索引所对应的，下一个最近身高
#         ans[preIndex] = i
#
#     # 再把当前小朋友身高的下标i存放到栈中
#     # 注意：所储存的是下标i，而不是身高h
#     stack.append(i)
#
# # 逆序
# # 逆序遍历每一个小朋友的身高
# for i in range(n-1, -1, -1):
#     h = height[i]
#     # 第i个小朋友的身高h，需要不断地与栈顶元素比较
#     # 如果栈顶元素存在并且h【大于等于】栈顶元素stack[-1]
#     # 说明栈顶元素stack[-1]并不是身高h右边最近的比h更大的元素
#     # 需要将栈顶元素弹出，继续寻找比h大的栈顶元素
#     while len(stack) > 0 and h >= height[stack[-1]]:
#         # 栈顶元素下标对应的身高不大于当前身高h，不是符合要求的更大身高，弹出
#         stack.pop()
#     # 完成弹出后，如果栈顶仍存在元素，说明stack[-1]所对应的身高，是严格比h大的下一个身高
#     if len(stack) > 0:
#         # ans[i]修改为stack[-1]
#         ans[i] = stack[-1]
#
#     # 再把当前小朋友身高的下标i存放到栈中
#     # 注意：所储存的是下标i，而不是身高h
#     stack.append(i)
# #
# # ans中的int元素转成str后才能合并成字符串
# print(" ".join(map(str, ans)))
# # 与上一行的输出效果相同 MosesMin
# print(" ".join(str(i) for i in ans))

# --------------------------------- D05-08 --------------------------------- 0044
# 【单调栈】2023Q1A-删除重复数字后的最大数字
# 题目描述与示例
# 题目
# 一个长整型数字，消除重复的数字后，得到最大的一个数字。
# 如 12341 ，消除重复的 1，可得到 1234 或 2341，取最大值 2341。
# 如 42234，消除 4 得到 4223 或者 2234 ，再消除 2，得到 423 或 234，取最大值 423。
# 输入
# 输入一个数字，范围 [1, 100000]
# 输出
# 输出经过删除操作后的最大值
# 示例一
# 输入
# 12341
# 输出
# 2341
# 示例二
# 输入
# 42234
# 输出
# 423
# 解题思路
# 注意，本题和LC316. 去除重复字母非常类似。
# 区别在于，本题字符串包含的是数字而不是字母，需要考虑最大数字而不是最小数字。
#
# 为了使得最终结果尽可能大，较大的单个数字自然是尽可能地排在前面。
# 这似乎很直接地就可以使用单调栈的思路来完成：设置一个从栈底往栈顶递减的单调栈。
#
# 使用单调栈，一种朴素美好的设想是：每遇到一个数num，
# 就与栈顶元素stack[-1]进行比较，如果num比stack[-1]大，那么若干比num小的栈顶元素可能会被删除。
#
# 但由于最终删除后的结果必须是，原字符串中的单个数字有且只出现一次，故本题还需要考虑几个问题：
# 1. 如何确保重复出现的数字被删除
# 2. 如何确保每一个数字最终只出现一次
#
# 很容易想到，为了确保最终每一个数字仅出现一次，我们可以对原字符串中每一个数字进行频率统计，
# 而最终的结果字符串中每一个数字出现的频率应该为1。
# 频率统计我们可以用我们熟知的Counter()来完成，即初始化哈希表cnt = Counter(s)。
# 另外，我们还需要知道某一个数字是否在栈中已经出现过了，这可以用一个哈希集合used或者长度为10的列表来记录。
#
# 接着我们从左往右遍历原字符串s，然后考虑每一个字符num的行为。当
# - 如果num没有使用过，即不位于哈希集合used中
#   - num可以直接入栈的情况有
#     - 栈为空
#     - 栈不为空，但num小于栈顶元素stack[-1]
#     - 栈不为空，且num大于栈顶元素stack[-1]，但stack[-1]的计数为1，如果stack[-1]被弹出则最终结果将不包含stack[-1]
#   - 如果上述条件均不满足，num不可以直接入栈，需要反复进行栈顶元素检查并弹出栈顶元素。对于弹出的元素top = stack.pop()，需要做两件事情
#     - top的计数-1，即cnt[top] -= 1。
#     - top要在哈希集合used中移除，因为暂时不在栈中出现了。
#   - num入栈之后，需要将其加入哈希集合used，表示num在栈出现了
# - 如果num已经使用过，即已经位于哈希集合used中
#   - num不能入栈
#   - num的计数-1，即cnt[num] -= 1。
# 将上述思路整理成代码
# for num in num_lst:
#     if num in used:
#         cnt[num] -= 1
#     else:
#         while (len(stack) > 0 and num > stack[-1] and cnt[stack[-1]] > 1):
#             cnt[stack[-1]] -= 1
#             used.remove(stack[-1])
#             stack.pop()
#         stack.append(num)
#         used.add(num)
# 本题基本就完成了。


# D05-08 MosesMin
# stack = [4,3,2,1]
# print("".join(str(i) for i in stack))
# 输出：4321 即先入栈的栈底元素4也先输出  所以构建一个单调递增栈  即从栈顶到栈底逐渐增大 符合要求 # D05-08 MosesMin
# # stack = [4,3,2,1]
# # print("".join(str(i) for i in stack))
# # 输出：4321 即先入栈的栈底元素4也先输出  所以构建一个单调递增栈  即从栈顶到栈底逐渐增大 符合要求


# 代码
# Python
#
# # 题目：2023Q1A-删除重复数字后的最大数字
# # 分值：200
# # 作者：许老师-闭着眼睛学数理化
# # 算法：单调栈
# # 代码看不懂的地方，请直接在群上提问
#
# from collections import Counter
#
# num_lst = list(input()) # 把输入的字符串转化为字符列表，每个元素为一个数字字符
# cnt = Counter(num_lst)  # 计数哈希表，记录每一个数字的出现次数
# stack = list()          # 单调递减栈，更大的数字在栈底
# used = set()            # 查看ch是否使用过
# for num in num_lst:
#     # 如果num位于used中，说明在此之前使用过了，无需入栈
#     if num in used:
#         cnt[num] -= 1   # cnt[ch]的计数-1
#     # 如果ch不位于used中，要把ch加入栈顶
#     else:
#         # 在加入栈底之前，需要进行栈顶元素的检查，
#         # 有可能要弹出若干栈顶元素，弹出的条件为：
#         # 1.栈不为空；
#         # 2.num大于栈顶元素stack[-1]
#         # 3.栈顶元素的计数cnt[stack[-1]]大于1（即后面还有其他相同字符可用）
#         while (len(stack) > 0 and num > stack[-1] and cnt[stack[-1]] > 1):
#             cnt[stack[-1]] -= 1     # 对于栈顶弹出的元素，其计数-1
#             used.remove(stack[-1])  # 同时在used集合中移除
#             stack.pop()             # 栈顶元素弹出
#         # 在进行完栈顶的检查之后，需要做两件事：
#         # 1.把ch加入栈顶；
#         # 2.把ch加入used哈希表，表示已经使用过
#         stack.append(num)
#         used.add(num)
#
# # 最后需要把单调栈中的所有元素用join()方法合并成一个字符串并输出
# print("".join(stack))

# 时空复杂度
# 时间复杂度：O(N)。仅需一次遍历数组。N是输入数字的位数。
# 空间复杂度：O(1)。单调栈和哈希表所占用的额外空间，长度不超过10，故可以认为是常数级别空间。


# --------------------------------- D05-09 --------------------------------- 0045
# 【单调栈】2023C-找最小数
# 题目描述与示例
# 题目描述
# 给一个正整数 NUM1，计算出新正整数 NUM2。NUM2 为 NUM1 中移除 N 位数字后的结果，需要使得 NUM2 的值最小。
# 输入
# 1. 输入的第一行为一个字符串，字符串由 0-9 字符组成，记录正整数 NUM1，NUM1 长度小于 32。
# 2. 输入的第二行为需要移除的数字的个数，小于 NUM1 长度。
# 输出
# 输出一个数字字符串，记录最小值 NUM2。
# 示例一
# 输入
# 2615371
# 4
# 输出
# 131
# 说明
# 移除 2、6、5、7 这四个数字，剩下 1、3、1 按原有顺序排列组成 131 为最小值。
# 示例二
# 输入
# 12345
# 2
# 输出
# 123
# 示例三
# 输入
# 10345
# 2
# 输出
# 034
# 解题思路
# 注意，本题和LC402. 移掉K位数字完全一致。
#
#
# 代码
# Python

# # 题目：2023B-找最小数
# # 分值：200
# # 作者：闭着眼睛学数理化
# # 算法：单调栈
# # 代码看不懂的地方，请直接在群上提问
#
#
# NUM1 = input()
# n = int(input())
# # rest_n 表示剩余的删除次数
# rest_n = n
#
# # 构建一个单调栈，
# # 单调栈从栈底至栈顶单调递增
# # 即大的数字放在栈顶
# stack = list()
#
# # 遍历数字字符串NUM1中的每一个字符ch
# for ch in NUM1:
#     # 出栈的情况：
#     # 1. 栈不为空
#     # 2. ch小于栈顶元素
#     # 3. 剩余的删除次数大于0
#     # 即可以弹出栈顶元素，这样才能使得栈顶元素尽可能小
#     while len(stack) and ch < stack[-1] and rest_n > 0:
#         stack.pop()
#         rest_n -= 1
#     # 对于每一个ch，都应该入栈
#     stack.append(ch)
#
# # 结束循环时，栈中元素不一定恰好为len(NUM1)-n
# # 所以取较小的数前 len(NUM1)-n 个数组合成字符串
# print("".join(stack[:len(NUM1)-n]))

# 时空复杂度
# 时间复杂度：O(M)。仅需一次遍历字符串NUM1。
# 空间复杂度：O(M)。单调栈所占用的额外空间。
# M为字符串NUM1的长度。

# D06 双指针（一） 同向双指针
# 双指针
# 同向双指针（两个指针均从左往右/从右往左移动）

# 指针题目中的指针可以理解为一个索引  指针就是指向一个变量 与C语言中的指针有一些区别
# 同向双指针 两个指针指向同一个索引方向 例如都是从左往右 或者都是从右往左

# --------------------------------- D06-01 --------------------------------- 0046
# LC88. 合并两个有序数组
# 一、题目描述
# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
# 你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。
#
# 二、题目解析
# 设置两个索引 i 和 j 分别指向 nums1 和 nums2 的有效元素的尾部，从它们的尾部开始向前遍历，
# 同时设置索引 cur 指向 nums1 的最末尾，在每次遍历过程中，比较 i 和 j 指向的元素值大小，
# 把大的元素填充到 cur 的位置，填充完毕说明那个元素已经放置在它应该放置的位置，不需要在管它了，
# 把 cur 向前移动，同时把 i 或者 j 向前移动，继续比较 i 和 j 指向的元素值大小，把大的元素填充到 cur 的位置。
#
#
# 三、参考代码

# # 1、W
# # 登录 AlgoMooc 官网获取更多算法图解
# # https:#www.algomooc.com/555.html
# # 作者：程序员吴师兄
# # 代码有看不懂的地方一定要私聊咨询吴师兄呀
# # 合并两个有序数组( LeetCode 88 ):https:#leetcode-cn.com/problems/merge-sorted-array/
# class Solution:
#     def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
#         # 索引从有序数组 nums1 有效元素的末端开始
#         # 数组的下标索引从零开始计数
#         # 索引   0    1     2
#         # 数组 [ 1 ,  2  ,  3 ]
#         i = m - 1
#
#         # 索引从有序数组 nums2 的末端开始
#         j = n - 1
#
#         # 从有序数组 nums1 最末端的位置开始保存元素
#         cur = m + n - 1
#
#         # 通过循环把 num2 的元素都移动到 num1 中
#         while j >= 0:
#
#             # 比较 num1 和 num2 中当前的元素大小
#
#             # 如果 num1 中的索引位置为 i 的元素大于 num2 中索引位置为 j 的元素
#             # 为了防止越界 i 必须是大于等于 0
#             if i >= 0 and nums1[i] > nums2[j]:
#
#                 # 把 num1 中的索引位置为 i 的元素复制到索引为 cur 的位置
#                 # 此时 cur 的元素已经确定下来
#                 nums1[cur] = nums1[i]
#
#                 # 接下来去确定 cur 前面一个元素应该放什么数字
#                 cur -= 1
#                 # 此时，索引 i 需要向前移动
#                 i -= 1
#                 # 否则，如果 num1 中的索引位置为 i 的元素小于或者等于 num2 中索引位置为 j 的元素
#             else:
#
#                 # 把 num2 中的索引位置为 j 的元素复制到索引为 cur 的位置
#                 nums1[cur] = nums2[j]
#                 # 接下来去确定 cur 前面一个元素应该放什么数字
#                 cur -= 1
#                 # 此时，索引 j 需要向前移动
#                 j -= 1

# 2、X
# 题目：LC88. 合并两个有序数组
# 难度：简单
# 作者：许老师-闭着眼睛学数理化
# 算法：双指针
# 代码看不懂的地方，请直接在群上提问


# class Solution:
#     def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
#         # i是nums1的下标（不包含0的部分）
#         # j是nums2的下标
#         i = m - 1
#         j = n - 1
#         # cur是nums1的下标（包含最后的0的部分）
#         cur = m + n - 1
#         # 我们需要把所有nums2中的值放到nums1中，故要求j >= 0
#         # 当j == -1时，说明nums2中所有的元素均已经放到nums1中了
#         # 此时可以退出循环
#         while j >= 0:
#             # 如果i < 0，说明nums1中的值已经用完
#             # 把nums2[j]放到nums1[cur]，cur和j均递减
#             if i < 0:
#                 nums1[cur] = nums2[j]
#                 cur -= 1
#                 j -= 1
#             # i >= 0的情况，nums1中的值还没有用完
#             else:
#                 # nums1[i]大于等于nums2[j]，nums1[i]要放到nums1[cur]
#                 # 然后cur和i均递减
#                 if nums1[i] >= nums2[j]:
#                     nums1[cur] = nums1[i]
#                     cur -= 1
#                     i -= 1
#                 # nums1[i]小于nums2[j]，nums2[j]要放到nums1[cur]
#                 # 然后cur和j均递减
#                 # 以下内容可以合并到i < 0的情况，即变成吴师兄的代码
#                 else:
#                     nums1[cur] = nums2[j]
#                     cur -= 1
#                     j -= 1

# 四、复杂度分析
# 时间复杂度：O(m+n)。指针移动单调递增，最多移动 m+n 次，因此时间复杂度为 O(m+n)。
# 空间复杂度：O(m+n)。

# --------------------------------- D06-02 --------------------------------- 0047

# LC26. 删除有序数组中的重复项
# 视频地址：删除有序数组中的重复项(LeetCode 26)
# 一、题目描述
# 给你一个 升序排列 的数组 nums ，请你 原地 删除重复出现的元素，
# 使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。
#
# 由于在某些语言中不能改变数组的长度，所以必须将结果放在数组nums的第一部分。
# 更规范地说，如果在删除重复项之后有 k 个元素，那么 nums 的前 k 个元素应该保存最终结果。
#
# 将最终结果插入 nums 的前 k 个位置后返回 k 。
# 不要使用额外的空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
#
# 判题标准:
# 系统会用下面的代码来测试你的题解:
# int[] nums = [...]; // 输入数组
# int[] expectedNums = [...]; // 长度正确的期望答案
#
# int k = removeDuplicates(nums); // 调用
#
# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
#
# 如果所有断言都通过，那么您的题解将被 通过。
# 示例 1：
# 输入：nums = [1,1,2]
# 输出：2, nums = [1,2,_]
# 解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。
# 示例 2：
# 输入：nums = [0,0,1,1,1,2,2,3,3,4]
# 输出：5, nums = [0,1,2,3,4]
# 解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。
# 提示：
# - 1 <= nums.length <= 3 * 10^4
# - -10^4 <= nums[i] <= 10^4
# - nums 已按 升序 排列
#
#
# 二、参考代码

# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         # 指针 i 进行数组遍历
#         n = len(nums)
# 
#         # 指针 j 指向即将被赋值的位置
#         j = 0
# 
#         # 开始对数组进行遍历
#         for i in range(n):
# 
#             # 进行筛选
#             if i == 0 or nums[i] != nums[i - 1]:
#                 # 赋值
#                 nums[j] = nums[i]
# 
#                 # j 移动
#                 j += 1
# 
#         # 获取结果
#         return j


# --------------------------------- D06-03 --------------------------------- 0048
# LC80.删除有序数组中的重复项II
# 一、题目描述
# 给你一个有序数组nums ，请你原地删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用O(1)额外空间的条件下完成。
#
# 说明：
# 为什么返回数值是整数，但输出的答案是数组呢？
# 请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
# 你可以想象内部操作如下:
# // nums是以“引用”方式传递的。也就是说，不对实参做任何拷贝
# int len = removeDuplicates(nums);
#
# // 在函数里修改输入数组对于调用者是可见的。
# // 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }
# 示例
# 1：
# 输入：nums = [1, 1, 1, 2, 2, 3]
# 输出：5, nums = [1, 1, 2, 2, 3]
# 解释：函数应返回新长度
# length = 5, 并且原数组的前五个元素被修改为
# 1, 1, 2, 2, 3 。 不需要考虑数组中超出新长度后面的元素。
# 示例
# 2：
# 输入：nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
# 输出：7, nums = [0, 0, 1, 1, 2, 3, 3]
# 解释：函数应返回新长度
# length = 7, 并且原数组的前五个元素被修改为
# 0, 0, 1, 1, 2, 3, 3 。 不需要考虑数组中超出新长度后面的元素。
#
# 提示：
# - 1 <= nums.length <= 3 * 10 ^ 4
# - -104 <= nums[i] <= 10 ^ 4
# - nums
# 已按升序排列
# 二、参考代码

# class Solution(object):
#     def removeDuplicates(self, nums):
#
#         # 指针 slow 指向即将被赋值的位置
#         slow = 0
#
#         # 开始对数组进行遍历
#         for fast in range(len(nums)):
#
#             # 进行筛选
#             if slow < 2 or nums[fast] != nums[slow - 2]:
#                 # 赋值
#                 nums[slow] = nums[fast]
#                 # slow 移动
#                 slow += 1
#
#         # 获取结果
#         return slow


# --------------------------------- D06-04 --------------------------------- 0049
# LC485. 最大连续 1 的个数
# 一、题目描述
# 给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。
# 示例 1：
# 输入：nums = [1,1,0,1,1,1]
# 输出：3
# 解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.
# 示例 2:
# 输入：nums = [1,0,1,1,0,1]
# 输出：2
# 提示：
# - 1 <= nums.length <= 10^5
# - nums[i] 不是 0 就是 1.
# 二、参考代码
# class Solution(object):
#     def findMaxConsecutiveOnes(self, nums):
#
#         # 最后一个 0 所在的索引位置
#         lastZero = -1
#
#         # 结果
#         ans = 0
#
#         # 从左到右访问数组 nums
#         for i, num in enumerate(nums):
#
#             # 1、当前元素为 0 ，更新 lastZero
#             if num == 0:
#                 lastZero = i
#
#             # 2、否则说明当前元素为 1
#             else:
#                 # 通过 lastZero 可以获取当前元素距离最前面的 1 的个数
#                 # 对比之前的 ans ，更新获取最大值
#                 ans = max(ans, i - lastZero)
#
#         # 返回结果
#         return ans

# --------------------------------- D06-05 --------------------------------- 0050
# LC283. 移动零
# 一、题目描述
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。
# 示例 1:
# 输入: nums = [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 示例 2:
# 输入: nums = [0]
# 输出: [0]
# 提示:
# - 1 <= nums.length <= 10^4
# - -2^31 <= nums[i] <= 2^31 - 1
# 进阶：你能尽量减少完成的操作次数吗？
# 二、参考代码
# class Solution:
#     def moveZeroes(self, nums: list[int]) -> None:
#         # 设置一个变量，用来指向经过一系列操作后数组中所有为 0 元素的第一个位置上
#         # 一开始默认在索引为 0 的位置
#         slow = 0
#
#         # 从头到尾遍历数组
#         # 遍历完毕之后，slow 指向了一个为 0 的元素，或者如果数组中不存在 0 ，就和 fast 一样，超过了数组的范围
#         for fast in range(len(nums)) :
#
#             # 在遍历过程中，如果发现访问的元素是非 0 元素
#             # 说明 slow 不在正确的位置上，需要向后移动，寻找合适的位置
#             if nums[fast] != 0:
#
#                 # 这个时候，原先 slow 的值需要被 fast 的值覆盖
#                 nums[slow] = nums[fast]
#
#                 # slow 需要向后移动，寻找合适的位置
#                 slow += 1
#
#         # 接下来，只需要把 slow 极其后面所有的元素都设置为 0 就行
#         for i in range(slow,len(nums)) :
#
#             # 都设置为 0
#             nums[i] = 0

# 四、复杂度分析
# - 时间复杂度：O(n)，其中 n 为序列长度。每个位置至多被遍历两次。
# - 空间复杂度：O(1)。只需要常数的空间存放若干变量。


# --------------------------------- D06-06 --------------------------------- 0051
# LC27.移除元素
# 一、题目描述
# 给你一个数组nums和一个值val，你需要原地移除所有数值等于val的元素，并返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须仅使用O(1)额外空间并原地修改输入数组。
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
#
# 说明:
# 为什么返回数值是整数，但输出的答案是数组呢?
# 请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
# 你可以想象内部操作如下:
#
# // nums是以“引用”方式传递的。也就是说，不对实参作任何拷贝
#
# int len = removeElement(nums, val);
#
# // 在函数里修改输入数组对于调用者是可见的。
# // 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
#
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }
#
# 示例1：
# 输入：nums = [3, 2, 2, 3], val = 3
# 输出：2, nums = [2, 2]
# 解释：函数应该返回新的长度
# 2, 并且nums中的前两个元素均为2。你不需要考虑数组中超出新长度后面的元素。
# 例如，函数返回的新长度为2 ，而nums = [2, 2, 3, 3]或nums = [2, 2, 0, 0]，也会被视作正确答案。
#
# 示例2：
# 输入：nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
# 输出：5, nums = [0, 1, 4, 0, 3]
# 解释：函数应该返回新的长度5, 并且nums中的前五个元素为0, 1, 3, 0, 4。
# 注意这五个元素可为任意顺序。你不需要考虑数组中超出新长度后面的元素。
#
# 提示：
# - 0 <= nums.length <= 100
# - 0 <= nums[i] <= 50
# - 0 <= val <= 100
#
# 二、参考代码
# class Solution:
#     def removeElement(self, nums: list[int], val: int) -> int:
#
#         # 指针 i 进行数组遍历
#         n = len(nums)
#
#         # 指针 j 指向即将被赋值的位置
#         j = 0
#
#         # 开始对数组进行遍历
#         for i in range(n):
#
#             # 进行筛选
#             if nums[i] != val:
#                 # 赋值
#                 nums[j] = nums[i]
#
#                 # j 移动
#                 j += 1
#
#         # 获取结果
#         return j

# --------------------------------- D06-07 --------------------------------- 0052
# 【双指针】2023Q1A-最长的元音字符串
# 题目描述与示例
# 题目
# 定义当一个字符串只有元音字母(a,e,i,o,u,A,E,I,O,U)组成,称为元音字符串，现给定一个字符串，请找出其中最长的元音字符串，并返回其长度，如果找不到请返回0。
# 字符串中任意一个连续字符组成的子序列称为该字符串的子串。
# 输入
# 一个字符串s。字符串长度满足0 < len(s) < 10^5，字符串仅由字符a-z或A-Z组成
# 输出描述
# 一个整数，表示最长的元音字符子串的长度。
# 示例一
# 输入
# asdbuiodevauufgh
# 输出
# 3
# 说明
# 最长的元音字符子串为uio和auu长度都为3，因此输出3
# 解题思路
# 注意，本题和LC485. 最大连续 1 的个数几乎完全一致。唯一的区别在于，本题考虑的是所有元音而不是某种单一的字符，因此需要用一个哈希集合的辅助判断。
#
# 代码
# Java
# import java.util.HashSet;
# import java.util.Scanner;
# public class Main {
#     public static void main(String[] args) {
#         Scanner scanner = new Scanner(System.in );
#         String s = scanner.nextLine();
#
#         // 最后一个非元音所在的索引位置
#         int lastNotVowel = -1;
#
#         // 元音集合
#         HashSet < Character > vowelSet = new HashSet < Character > ();
#         vowelSet.add('a');
#         vowelSet.add('e');
#         vowelSet.add('i');
#         vowelSet.add('o');
#         vowelSet.add('u');
#         vowelSet.add('A');
#         vowelSet.add('E');
#         vowelSet.add('I');
#         vowelSet.add('O');
#         vowelSet.add('U');
#
#         // 答案变量
#         int ans = 0;
#
#         for (int i = 0; i < s.length(); i++) {
#             char ch = s.charAt(i);
#
#             // 当前元素为非元音，更新 lastNotVowel
#             if (!vowelSet.contains(ch)) {
#                 lastNotVowel = i;
#             } else {
#                 // 通过 lastNotVowel 可以获取当前字符 ch 距离最前面的元音个数
#                 // 对比之前的 ans ，更新获取最大值
#                 ans = Math.max(ans, i - lastNotVowel);
#             }
#         }
#
#     // 返回结果
#     System.out.println(ans);
#     }
# }

# Python
# # 题目：2023Q1A-最长的元音字符串
# # 分值：200
# # 作者：闭着眼睛学数理化
# # 算法：同向双指针
# # 代码看不懂的地方，请直接在群上提问
#
# s = input()
#
# # 最后一个非元音所在的索引位置
# lastNotVowel = -1
#
# # 元音集合
# vowelSet = set("aeiouAEIOU")
#
# # 答案变量
# ans = 0
#
# # 从左到右访问数组 nums
# for i, ch in enumerate(s):
#
#     # 当前元素为非元音，更新 lastNotVowel
#     if ch not in vowelSet:
#         lastNotVowel = i
#
#     # 当前元素为元音，更新 ans
#     else:
#         # 通过 lastNotVowel 可以获取当前字符 ch 距离最前面的元音个数
#         # 对比之前的 ans ，更新获取最大值
#         ans = max(ans, i - lastNotVowel)
#
# # 返回结果
# print(ans)

# 时空复杂度
# 时间复杂度：O(N)。仅需一次遍历数组。
# 空间复杂度：O(1)。哈希集合的长度为10，为常数级别空间。

# D07 双指针--相向双指针
# 相向双指针（两个指针从两边往中间移动）：两个指针 一个从左到右移动 一个从右到左移动
# 即：两个指针向内移动 它们的方向是相向的 在移动过程中 这两个指针会产生碰撞的结果 也即所谓的对撞指针
# 相向双指针会考的比较多 而背向双指针（两个指针从中间往两边移动）基本不考  且题目量非常少

# --------------------------------- D07-01 --------------------------------- 0053
# LC9. 回文数
# 一、题目描述
# 给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
# 回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
# - 例如，121 是回文，而 123 不是。
# 示例 1：
# 输入：x = 121
# 输出：true
# 示例 2：
# 输入：x = -121
# 输出：false
# 解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 示例 3：
# 输入：x = 10
# 输出：false
# 解释：从右向左读, 为 01 。因此它不是一个回文数。
# 二、题目解析
#
# 三、参考代码
class Solution:
    def isPalindrome(self, x: int) -> bool:

        # 转换为字符串数组的形式
        xArray = list(str(x))

        # 左边索引的位置在 0
        left = 0

        # 右边索引的位置在 len(xArray) - 1
        right = len(xArray) - 1

        # 两个索引向内移动
        # left 向右移动
        # right 向左移动
        while left <= right:
            # 判断这两个元素值是否相同
            if xArray[left] != xArray[right]:
                # 如果不同，直接返回 False
                return False

            # 否则，left 向右移动
            left += 1

            # right 向左移动
            right -= 1

        return True


# --------------------------------- D07-02 --------------------------------- 0054
# LC125. 验证回文串
# 本题和 LC9. 回文数  的解题思路是一样的。
# 一、题目描述
# 如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 回文串 。
# 字母和数字都属于字母数字字符。
# 给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。
# 示例 1：
# 输入: s = "A man, a plan, a canal: Panama"
# 输出：true
# 解释："amanaplanacanalpanama" 是回文串。
# 示例 2：
# 输入：s = "race a car"
# 输出：false
# 解释："raceacar" 不是回文串。
# 示例 3：
# 输入：s = " "
# 输出：true
# 解释：在移除非字母数字字符之后，s 是一个空字符串 "" 。
# 由于空字符串正着反着读都一样，所以是回文串。
# 提示：
# - 1 <= s.length <= 2 * 10^5
# - s 仅由可打印的 ASCII 字符组成
# 二、题目解析
#
# 三、参考代码

print(123)






# --------------------------------- 疑问： ---------------------------------
# 20240325:
# D04-06
# new_lst.sort(key = lambda x: (-cnt[x], len(x), x)) 最后一个x的作用？ 是根据x排列，字典序的意思。 如D04-07 倒数第二行的注释。


