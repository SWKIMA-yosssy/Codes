import math

#このプログラムは直線回帰限定で利用できる。
#実験データの入力
scores = [
    [1,2,3,4,5]#横軸要素を記入
    ,[8.025, 16.375, 23.575, 31.575, 40.1]#縦軸要素を記入
    ]

#以下は触らなくてよい
length = [len(v) for v in scores][1]
totalx= 0
totaly = 0
Sxy = 0
residual_squarex = 0

for i in range(length):
    totalx += scores[0][i]
for i in range(length):
    totaly += scores[1][i]
averagex = totalx/length
averagey = totaly/length


for x in range(length):
    print('#' + str(x + 1),':', scores[0][x], 'xの残差は', scores[0][x] - averagex)#ユーザーに　'#i : 結果i 残差は di' の形で全データを見せる
    residual_squarex += (scores[0][x] - averagex)**2
    Sxy += (scores[0][x] - averagex)*(scores[1][x] - averagey)
residual_squarex /= length
Sxy /= length

print('共分散Sxyは',Sxy)
print('分散は',residual_squarex)
print('回帰直線はy=',str(Sxy/residual_squarex) + 'x','+',averagey-Sxy/residual_squarex*averagex)
