import seaborn as sns

import matplotlib.pyplot as plt
import pandas as pd

# load data
# data = sns.load_dataset('diamonds')
dataFrame = pd.read_csv("data.csv")

column = dataFrame.columns
print(column)

# datayı matrixe cevirme
matrix = dataFrame.corr()
print(matrix)

# matrix'i plot ile göster
matrix_heatmap = sns.heatmap(
    matrix,
    center=0,
    fmt='.3f',
    square=True,
    annot=True,
    linewidths=.3
)
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
