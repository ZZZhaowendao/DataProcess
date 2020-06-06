import csv
import matplotlib.pyplot as plt
from datetime import datetime

"""处理CSV格式的数据"""
filename = "death_valley_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    """
    # 获取每个元素的索引及其值
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    """
    # 从文件中获取日期,对应最高温度,最高气温
    dates, highs, lows = [], [], []
    for row in reader:
        # 数据缺失检查
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, "missing date")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    # 每日温差
    temperature_difference = []
    for index in range(0, len(highs)):
        temperature_difference.append(highs[index] - lows[index])
    """根据数据绘制图形"""
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c="red", alpha=0.5)
    plt.plot(dates, lows, c="blue", alpha=0.5)
    plt.fill_between(dates, lows, highs, facecolor="blue", alpha=0.1)
    plt.plot(dates, temperature_difference, c="green")
    plt.title("Daily high and low temperatures - 2014", fontsize=24)
    plt.xlabel("", fontsize=16)
    # 更好地绘制日期标签
    fig.autofmt_xdate()
    plt.ylabel("Temperature(F)", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)

    plt.show()