import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd

# 读取数据
data = pd.read_csv('gdp_data.csv')  # 假设数据保存在gdp_data.csv文件中

# 对数据进行排序，按照GDP降序排列
sorted_data = data.sort_values('GDP', ascending=False)

# 提取国家和月份列
countries = sorted_data['Country'].unique()
months = sorted_data['Month'].unique()

# 创建画布和子图
fig, ax = plt.subplots()

# 初始化条形图对象
bars = ax.bar(countries, sorted_data.loc[sorted_data['Month'] == months[0]]['GDP'])

# 更新函数，用于在动画中更新数据和图形
def update(frame):
    # 获取当前月份的数据
    current_data = sorted_data.loc[sorted_data['Month'] == months[frame]]
    
    # 更新条形图的高度
    for i, bar in enumerate(bars):
        bar.set_height(current_data.iloc[i]['GDP'])
    
    # 设置标题和x轴标签
    ax.set_title('GDP by Country - {}'.format(months[frame]))
    ax.set_xlabel('Country')
    
    # 调整x轴标签的显示
    plt.xticks(rotation=90)
    
# 创建动画对象
ani = animation.FuncAnimation(fig, update, frames=len(months), interval=1000)

# 显示动画
plt.show()
