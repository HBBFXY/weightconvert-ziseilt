WeightStr = input("请输入带有符号的重量值：")
if WeightStr[-2:] == 'kg':
    pd = eval(WeightStr[:-2]) * 2.2046
    print("转换后的重量是{:.3f}pd".format(pd))
elif WeightStr[-2:] == 'pd':
    kg = eval(WeightStr[:-2]) / 2.2046
    print("转换后的重量是{:.3f}kg".format(kg))
else:
    print("输入格式错误")
