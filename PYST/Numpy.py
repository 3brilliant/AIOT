# 数据分析第一个库Numpy
# 导入包
import numpy as np
'''
一维数组
'''
# 创建一个数组
arr = np.array([1,2,3,4])
print(arr)

# 将数组当中的数据取出来,根据索引
print(arr[[2,3]])

# 数组可以数进行比较，找出大于3的数,用布尔值进行返回
print(arr > 3)


# 将返回的布尔值进行赋值并进行输出
cond = arr >3
print(arr[cond])

# 创建一维数组
# 全是一的数组，shape表示创建一的个数
np.ones(shape=10)

# 全是零的数组
np.zeros(shape=10)
np.zeros(10)

# 创建定义的数组,fill_value表示自定义值
np.full(shape=10,fill_value=4)

# 创建随机整数,size表示个数，dtype表示uint8,uint32等类型，默认是int
np.random.randint(0,100,size=10,dtype=int)
# 创建没有上限的整数数组
np.random.randint(2,size=10)

# 创建正态分布（平均值为0,标准差为1）的数组,个数为10个
np.random.randn(10)

# 创建等差数列,表示将1~10分为10等份
np.linspace(1,10,10)

# 创建等比数列，base表示比值，num表示分成几分，默认是50份，1~5表示2的1~5次方
np.logspace(1,5,num=5,base=2)
# 设置不显示科学计数法
np.set_printoptions(suppress=True)

