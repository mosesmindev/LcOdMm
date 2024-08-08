# chap01-01knowledgePoint-01数组
# 数组
# 相同数据类型
# 连续内存地址

"""初始化数组的2种方式"""
# arr1 = [0] * 3 #arr  = [0,0,0]
# arr2 = [1,2,3]

# 遍历数组
# def traverse(nums):
#     """遍历数组"""
#     count = 0
#     # 通过索引遍历数组
#     for i in range(len(nums)):
#         count += 1
#
#     # 直接遍历数组
#     for num in nums:
#         count += num

# chap01-02exercise
# chap01-001-total--001-lc1604设计停车系统
# class ParkingSystem(object):
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

# chap01-001-total--001--mm
# class ParkingSystem(object):
#     def __init__(self,big,medium,small):
#         self.park = [0,big,medium,small]
#
#     def addCar(self,carType):
#         if self.park[carType] == 0:
#             return False
#         self.park[carType] -= 1
#         return True


# chap01-01knowledgePoint-02栈
# 栈  先进后出的线性表
# ① 线性表: 就是一个数组, 每个元素只有一个值
# ② 先进后出



