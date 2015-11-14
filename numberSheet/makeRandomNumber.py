import numpy as np
import pandas as pd
import xlsxwriter

np.random.seed(0)

# 1枚につき9x12=108個の数字
# 5枚なので108x5=540
# 各数字は54個となる
number = []
for i in range(10):
    tmp = [i for j in range(54)]
    number.extend(tmp)
number = np.random.permutation(number)

zero = [0 for i in range(12)]

ct = 0
for paper in range(5):
    row = 9
    col = 12
    rand = np.zeros((row*3,col))
    for i in range(row*3):
        if i%3==0:
            for j in range(col):
                rand[i][j] = number[ct]
                ct+=1;
        else:
            rand[i] = zero


    df = pd.DataFrame(rand)
    filename = 'rand' + str(paper+1) + '.xlsx'
    df.to_excel(filename, sheet_name='Japan_US')

