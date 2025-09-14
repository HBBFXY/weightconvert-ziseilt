weight_input = input("请输入重量（例如：10kg 或 5pd）: ").strip().lower()

# 提取数值和单位
if weight_input.endswith('kg'):
    kg = float(weight_input[:-2])
    pd = kg * 2.2046
    print(f"{kg}千克 = {pd:.3f}磅")
elif weight_input.endswith('pd'):
    pd = float(weight_input[:-2])
    kg = pd / 2.2046
    print(f"{pd}磅 = {kg:.3f}千克")
else:
    print("输入格式错误，请使用类似'10kg'或'5pd'的格式")
