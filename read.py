data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count = count + 1 # count += 1
        if count % 1000 == 0:
            print(len(data))
print('檔案讀取完畢,總共有', len(data), '筆資料')

sum_len = 0
for d in data: #每個d是一個字串
    sum_len = sum_len + len(d) # sum_len(d) += 1
print('留言平均長度為', sum_len / len(data))


new = []
for d in data:   #把清單內的東西一筆一筆拿出來
	if len(d) < 100:  #如果長度小於100
		new.append(d) #就裝入新清單
print('一共有', len(new), '筆留言長度小於100')  #印出留言長度小於100的筆數
print(new[0])
print('----------------')
print(new[1])

good = []
for d in data:   #把清單內的東西一筆一筆拿出來
	if 'good' in d:  #如果good這個自有在d裡面
		good.append(d) #就裝入good清單
print('一共有', len(good), '筆留言提到good')  #印出留言含good的筆數
print(good[0])
print('----------------')
print(good[1])