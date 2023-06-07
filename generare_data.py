import random
import pandas as pd

# 定义国家和月份
countries = ['Country A', 'Country B', 'Country C', 'Country D']
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

# 生成示例数据
data = []
for month in months:
    for country in countries:
        gdp = random.randint(100, 1000)  # 生成100到1000之间的随机整数作为GDP
        data.append({'Month': month, 'Country': country, 'GDP': gdp})

# 将数据保存到CSV文件
df = pd.DataFrame(data)
df.to_csv('gdp_data.csv', index=False)
