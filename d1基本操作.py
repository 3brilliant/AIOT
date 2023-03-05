print(r"http\\hello world")   #print输出中用r或者R表示转义字符没有意义
#print(r"\\lajkjal\")    用r或者R末尾不能是 单斜杠\  可以是双斜杠
print("jin\btian")    #\b  转义字符表示后退
print("jin\rtian")    #\r  转义字符为enter清空前面的
'''
8bit（位） = 1byte（字节）
256byte = 1Kb  (千)        2的8次方等于256
1024Kb = 1Mb  （兆）
1024Mb = 1Gb   （吉）
1024Gb = 1T   （太）
'''

print(chr(0b1000001))    #表示二进制的字符  (ASCII)
print(ord("A"))      #表示字符的十进制数字
print(bin(65))   #结果为 0b1000001 相当于将ord("A")转换成二进制数

import keyword
print(keyword.kwlist)   #展示关键字

name = "罗欢"
print(name)       #name中存放的就是值“罗欢”的地址
print("标识",id(name))   #地址
print("类型",type(name))   #类型
print("值",name)    #value值