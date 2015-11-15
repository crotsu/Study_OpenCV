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
    rand = np.zeros((row,col))
    for i in range(row):
        for j in range(col):
            rand[i][j] = number[ct]
            ct+=1;
    
    # 左上の一番最初の数字を，質問用紙の識別子にするために，強制的に値を入れ替える．
    if paper==1:
        tmp = rand[0][0]
        rand[0][0] = rand[0][11]
        rand[0][11] = tmp

    if paper==2:
        tmp = rand[0][0]
        rand[0][0] = rand[1][4]
        rand[1][4] = tmp

    if paper==3:
        tmp = rand[0][0]
        rand[0][0] = rand[1][0]
        rand[1][0] = tmp

    if paper==4:
        tmp = rand[0][0]
        rand[0][0] = rand[1][11]
        rand[1][11] = tmp

    # ファイル出力
    df = pd.DataFrame(np.int32(rand))
    filename = 'rand' + str(paper+1)
    df.to_excel(filename+'.xlsx', sheet_name='Japan_US')
    df.to_csv(filename+'.csv', index=False, header=None)

