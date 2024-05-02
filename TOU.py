# import numpy as np
# import matplotlib as mpl
# import matplotlib.pyplot as plt
#
#
# def my_function(x):
#     return x**2 + 2*x + 1
#
#
# x = np.linspace(-10, 10, 400)
# y = my_function(x)
#
# plt.title('y = x^2 + 2x + 1')
# plt.xlabel('x')
# plt.ylabel('y')
#
# plt.plot(x, y)
# plt.show()

from pandas import DataFrame

data1 = {
    'ID': ['1', '2', '3', '4', '5'],
    'Sex': ['F', 'F', 'M', 'M', 'F'],
    'Money': [1200, 2500, 1500, 500, 800],
    'Name': ['Take', 'Sato', 'Oka', 'Sawada', 'Motoki']
}

df_data1 = DataFrame(data1)

data2 = {
    'Japanese': [80, 90, 80, 65, 90, 90],
    'Math': [85, 100, 90, 70, 75, 80],
    'English': [85, 95, 90, 75, 85, 85],
    'Science': [90, 85, 95, 80, 70]  # 【A】 Added 'Science' column
}

df_data2 = DataFrame(data2)

# Data Merging
df_merge_data = df_data1.merge(df_data2)

# Extract and display people who have more than 1000 Money
rich_people = df_merge_data[df_merge_data['Money'] > 1000]  # 【B】
print(rich_people)