dic = {0: 1, 2: 3, 4: 5}

# 遍历key方法1
for k in dic:
    print(k)

for v in dic.values():
    print(v)
'''
# 遍历key方法2
for k in dic.keys():
    print(k)
# 获得哈希表中所有键key组成的一个列表
keys = list(dic.keys())

# 遍历values
for v in dic.values():
    print(v)
# 获得哈希表中所有值value组成的一个列表
values = list(dic.values())

# 遍历key和values
for k, v in dic.items():
    print(k, v)  
# 获得哈希表中所有键值对(key, value)组成的一个二元列表
pairs = list(dic.items())
'''


# 编写一个表示小狗的类Dog作为例子。
class Dog():
    # 初始化小狗的两个属性，name和age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 模拟小狗被命令时蹲下
    def sit(self):
        print(self.name + " is sitting now.")
    # 模拟小狗被命令时打滚
    def roll_over(self):
        print(self.name + " rolled over.")

# 创建实例对象
dog1 = Dog("dahuang", 6)  # dog1表示一只名字为大黄，6岁的狗
dog2 = Dog("xiaohei", 5)  # dog2表示一只名字为小黑，5岁的狗

# 访问实例对象的属性
print(dog1.name)  # 输出“dahuang”
print(dog2.age) # 输出5

# 访问类的方法
dog1.sit()  # 输出“dahuang is sitting now.”
dog2.roll_over()  # 输出“xiaohei rolled over.”