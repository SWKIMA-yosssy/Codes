import math

#実験結果を以下のscoresリストに書き込む
scores = [26, 27, 16]

#以下は触らなくてよい。リストを書き込んだら実行すればOK
length = len(scores)
average = 0
sigmax = 0
residual_square = 0
total = 0

#総和と最確値の算出
for x in scores:
    total = total + x
    
average = total/length

#平均値の標準誤差の算出
for x in range(length):
    print('#' + str(x + 1),':', scores[x], '残差は', scores[x] - average)#ユーザーに　'#i : 結果i 残差は di' の形で全データを見せる
    residual_square = residual_square + (scores[x] - average)**2
    
sigmax_square = residual_square/(length*(length - 1))
sigmax = math.sqrt(sigmax_square)

#結果の表示
print('実験結果の和は', total, 'でした。よって最確値は', average, 'になります。')
print('平均値の標準誤差は', sigmax, 'です。')
print('従って、実験結果は', str(average) + '±' +str(sigmax), 'になります')
