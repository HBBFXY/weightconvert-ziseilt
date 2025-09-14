def weight_converter():
    # 获取用户输入
    user_input = input("请输入重量和单位（例如：10kg或10pd）: ").strip().lower()
    
    # 检查输入是否有效
    if not user_input[:-2].replace('.', '').isdigit() or user_input[-2:] not in ['kg', 'pd']:
        print("输入格式错误，请按照示例输入（如10kg或10pd）")
        return
    
    # 提取数值和单位
    try:
        value = float(user_input[:-2])
        unit = user_input[-2:]
    except ValueError:
        print("输入格式错误，请确保数字部分有效")
        return
    
    # 进行转换
    if unit == 'kg':
        # 千克转磅
        result = value * 2.2046
        print(f"{value:.3f}kg = {result:.3f}pd")
    elif unit == 'pd':
        # 磅转千克
        result = value / 2.2046
        print(f"{value:.3f}pd = {result:.3f}kg")

# 运行程序
if __name__ == "__main__":
    weight_converter()
