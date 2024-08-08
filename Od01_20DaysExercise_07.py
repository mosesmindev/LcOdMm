# D07 双指针--相向双指针
# 相向双指针（两个指针从两边往中间移动）：两个指针 一个从左到右移动 一个从右到左移动
# 即：两个指针向内移动 它们的方向是相向的 在移动过程中 这两个指针会产生碰撞的结果 也即所谓的对撞指针
# 相向双指针会考的比较多 而背向双指针（两个指针从中间往两边移动）基本不考  且题目量非常少

# --------------------------------- D07-01 --------------------------------- 00
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
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#
#         # 转换为字符串数组的形式
#         xArray = list(str(x))
#
#         # 左边索引的位置在 0
#         left = 0
#
#         # 右边索引的位置在 len(xArray) - 1
#         right = len(xArray) - 1
#
#         # 两个索引向内移动
#         # left 向右移动
#         # right 向左移动
#         while left <= right:
#             # 判断这两个元素值是否相同
#             if xArray[left] != xArray[right]:
#                 # 如果不同，直接返回 False
#                 return False
#
#             # 否则，left 向右移动
#             left += 1
#
#             # right 向左移动
#             right -= 1
#
#         return True


# --------------------------------- D07-02 --------------------------------- 00
# LC125. 验证回文串
# 本题和 LC9. 回文数  的解题思路是一样的。
# 一、题目描述
# 如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。
# 则可以认为该短语是一个 回文串 。
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

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#
#         # isalnum() 方法检测字符串是否由字母和数字组成
#         # 转换为字符串数组的形式
#         xArray = "".join(ch.lower() for ch in s if ch.isalnum())
#
#         # 左边索引的位置在 0
#         left = 0
#
#         # 右边索引的位置在 len(xArray) - 1
#         right = len(xArray) - 1
#
#         # 两个索引向内移动
#         # left 向右移动
#         # right 向左移动


#         while left <= right:
#             # 判断这两个元素值是否相同
#             if xArray[left] != xArray[right]:
#                 # 如果不同，直接返回 False
#                 return False
#
#             # 否则，left 向右移动
#             left += 1
#
#             # right 向左移动
#             right -= 1
#
#         return True


# --------------------------------- D07-03 --------------------------------- 00
# LC167. 两数之和II- 输入有序数组
# 一、题目描述
# 给你一个下标从 1 开始的整数数组 numbers ，该数组已按 非递减顺序排列 ，
# 请你从数组中找出满足相加之和等于目标数 target 的两个数。
#
# 如果设这两个数分别是 numbers[index1] 和 numbers[index2] ，
# 则 1 <= index1 < index2 <= numbers.length 。
# 以长度为 2 的整数数组 [index1, index2] 的形式返回这两个整数的下标 index1 和 index2。
# 你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。
# 你所设计的解决方案必须只使用常量级的额外空间。
# 示例 1：
#
# 输入：numbers = [2,7,11,15], target = 9
# 输出：[1,2]
# 解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。
# 示例 2：
#
# 输入：numbers = [2,3,4], target = 6
# 输出：[1,3]
# 解释：2 与 4 之和等于目标数 6 。因此 index1 = 1, index2 = 3 。返回 [1, 3] 。
# 示例 3：
#
# 输入：numbers = [-1,0], target = -1
# 输出：[1,2]
# 解释：-1 与 0 之和等于目标数 -1 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。
# 提示：
# - 2 <= numbers.length <= 3 * 10^4
# - -1000 <= numbers[i] <= 1000
# - numbers 按 非递减顺序 排列
# - -1000 <= target <= 1000
# - 仅存在一个有效答案

# 二、题目解析
#
# 三、参考代码

# class Solution:
#     def twoSum(self, numbers: list[int], target: int) -> list[int]:
#         # 初始结果数组
#         res = [0, 0]
#         # 定义左侧指针left，指向数组中第一个元素
#         # 默认从数组的索引为 0 的位置开始
#         left = 0
#         # 定义右侧指针 right，指向数组中最后一个元素
#         right = len(numbers) - 1
#
#         # 两个索引向内移动
#         # left 向右移动
#         # right 向左移动
#         # 因为题目要求：不可以 重复使用相同的元素，所以left 不能 等于 right  --MosesMin
#         while left < right:
#             # 1、如果左侧指针与右侧指针所指向的元素和等于目标值，则返回结果
#             if numbers[left] + numbers[right] == target:
#                 # 题目说明下标从 1 开始，就操作一下
#                 res[0] = left + 1
#                 res[1] = right + 1
#                 # 返回结果
#                 return res
#
#             # 2、如果左侧指针与右侧指针所指向的元素和小于目标值
#             elif numbers[left] + numbers[right] < target:
#                 # 因为数组是升序排列的，为了让两数之和变大一些
#                 # 因此应将左侧指针向右移动一位
#                 left += 1
#
#             # 3、如果左侧指针与右侧指针所指向的元素和大于目标值
#             elif numbers[left] + numbers[right] > target:
#                 # 因为数组是升序排列的，为了让两数之和变小一些
#                 # 因此应将右侧指针向左移动一位
#                 right -= 1
#         # 返回结果
#         return res

# --------------------------------- D07-04 --------------------------------- 00
# LC11. 盛水最多的容器
# 视频链接：吴师兄学算法
# 一、题目描述
# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
# 在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 二、题目解析
# 一开始，我们先去考虑相距最远的两个柱子所能容纳水的面积。
# [图片]
# 接下来去思考，我们去移动哪根柱子会更加合适?
# 这里我们需要注意一点：无论移动哪根柱子，柱子之间的宽度都是变小的。
# 移动右边那根更高的柱子？
# [图片]
# [图片]
# 由于水面高度是由最短的柱子决定的，所以移动右边那根更高的柱子的时候，
# 水面高度一定是不会增加，甚至有可能遇到更短的柱子而变小，而宽度有一定再减少，所以水的面积也一定减少。
# 移动左边那根更短的柱子？

# 这时候，水的高度是不确定的，那么面积也是不确定的，有可能比之前更大，也有可能更小或者相等。
# 所以，我们可以得出一个结论：移动两根柱子之间更短的那根柱子，才有可能在宽度一定变小的情况下，
# 找到一个更高的水面，从而使得面积有可能更大。

# 那接下来这道题目的解法也就有了：
# 1、设置两个索引，分别指向容器的两侧，即索引 left 指向最左边的柱子，索引 right 指向最右边的柱子。
# [图片]
# 2、记录下此时的水的面积，可以定义为 res
# 3、观察需要向内移动哪根柱子
# - 1）如果移动较高的柱子，由于水的宽度在变小，而水的高度一定不会增加，
# 所以最终水的面积不会超过之前记录的水的面积 res
# - 2）所以，只能移动较短的柱子，然后计算此时水的面积，再与之前记录的水的面积 res 进行比较，
# 保存那个更大的值

# 4、再去判断应该向内移动哪根柱子
# 5、直到 left 和 right 相遇为止

# https://www.algomooc.com/587.html
# 作者：程序员吴师兄
# 代码有看不懂的地方一定要私聊咨询吴师兄呀
# 盛最多水的容器 ( LeetCode 11) :
# https://leetcode-cn.com/problems/container-with-most-water/
# class Solution:
#     def maxArea(self, height: list[int]) -> int:
#         # 设置两个索引，分别指向容器的两侧
#         # 索引 left 指向最左边的柱子
#         left = 0
#         # 索引 right 指向最右边的柱子
#         right = len(height) - 1
#         # 设置一个变量用来保存当下水的最大面积
#         res = 0
#
#         # 移动 left 和 right，直到 left 和 right 相遇为止
#         while left < right:
#             # 水的宽度是 right - left
#             width = right - left
#             # 水的高度由两根柱子最短的那根决定
#             h = min(height[left], height[right])
#             # 计算此时水的面积
#             area = width * h
#
#             # 如果此时水的面积大于了我们之前保存的那个值，我们需要更新一下
#             if area >= res:
#                 # 更新 res 的值为 area，确保 res 一直都是最大的值
#                 res = area
#
#             # 接下来去观察需要移动哪根柱子：必定是最短的那根柱子
#             # 如果左边的柱子更短，那么向内移动左边的柱子，因为只有这样，才有可能找到一个更高的水面
#             # 在宽度一定变小的情况下，水的面积才有可能增大
#             if height[left] < height[right]:
#                 # 向内移动左边的柱子
#                 left += 1
#
#             # 如果右边的柱子更短，那么向内移动右边的柱子，因为只有这样，才有可能找到一个更高的水面
#             # 在宽度一定变小的情况下，水的面积才有可能增大
#             else:
#                 # 向内移动右边的柱子
#                 right -= 1
#
#         # 最后返回最大的面积 res 即可
#         return res

# --------------------------------- D07-05 --------------------------------- 00

# LC15. 三数之和
# 一、题目描述
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 *a，b，c ，*使得 a + b + c = 0 ？
# 请你找出所有和为 0 且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
# 二、题目解析
# 三、参考代码
# 登录 AlgoMooc 官网获取更多算法图解
# https://www.algomooc.com
# 作者：程序员吴师兄
# 代码有看不懂的地方一定要私聊咨询吴师兄呀
# 三数之和(15)：https://leetcode-cn.com/problems/3sum/ 
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # 题目存在多组解，每一组解都是一个数组，所以使用二维数组存储所有的解
        ans = []
        # 边界情况判断
        if nums == None or len(nums) < 3:
            return ans
        # 先将数组进行排序操作，从小到大
        nums.sort()
        # 开始遍历整个数组
        # 在遍历的过程中，观察设置的三个位置的元素之后的大小
        # num[i] 为从左到右观察过去的元素
        # left 为从 i 到 len - 1 的元素; right 为从 len - 1 向左移动到 i 的元素
        for i in range(len(nums)):
            # 如果发现 nums[i] > 0 ，由于 nums 是递增序列，left 在 nums[i] 的右侧，
            # right 也在 nums[i] 的右侧
            # 那么 num[i]、nums[left]、nums[right] 都大于 0 
            # 说明这三数之和一定大于 0 ，结束循环
            if nums[i] > 0:
                break
                # 答案中不可以包含重复的三元组，所以需要执行一个去重的操作
            # 不能用set去重，set去重 可能会删除正确答案，比如[-1,-1,2]这种，两个-1都删了 所以不能用set去重 MosesMin
            # 比如这个输入 [-4,-1,-1,0,1,2]
            # i 指向的为第一个 -1 时，left 指向的元素值为 0 ，right 指向的元素值为 1 
            # i 指向的为第二个 -1 时，left 指向的元素值为 0 ，right 指向的元素值为 1 
            # 这两组解都是 [ -1 , 0 , 1]，所以需要去重
            if i > 0 and nums[i] == nums[i - 1]:
                #  continue 关键字用于跳过当前循环中的剩余代码，并继续下一次循环的执行。
                #  这通常用于在循环中遇到特定条件时跳过当前迭代。
                continue
                # left 为从 i 到 len - 1 的元素，向右移动

            left = i + 1
            # right 为从 len - 1 向左移动到 i 的元素，向左移动
            right = len(nums) - 1
            # left 和 right 不断的向内移动
            while left < right:
                # 计算这三者之和
                sum = nums[i] + nums[left] + nums[right]
                # 发现三者之和为 0
                if sum == 0:
                    # 把这个结果记录一下
                    ans.append([nums[i], nums[left], nums[right]])
                    # 答案中不可以包含重复的三元组，所以需要执行一个去重的操作
                    # 比如这个输入 [-2,0,0,2,2]
                    # i 指向的元素值为 -2 ，left 指向的元素值为第一个 0 ，right 指向的元素值为倒数第一个 2 时
                    # 它们的 sum 为 0 ，如果让 ，left 向右移动一下，，right 向左移动一下，它们的 sum 也为 0
                    # 但是这两组解都是 [ -2 , 0 , 2]，所以需要去重
                    while left < right and nums[left] == nums[left + 1]:
                        # left 向右移动
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        # right 向左移动
                        right -= 1
                    # left 向右移动
                    left += 1
                    # right 向左移动
                    right -= 1
                # 如果三者之和小于 0 ，那么说明需要找更大的数
                elif sum < 0:
                    # left 向右移动
                    left += 1
                # 如果三者之和大于 0 ，那么说明需要找更小的数
                elif sum > 0:
                    # right 向左移动
                    right -= 1
        # 返回结果
        return ans


