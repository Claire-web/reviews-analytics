data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count = count + 1 # count += 1
        if count % 1000 == 0:
            print(len(data))
print('檔案讀取完畢,總共有', len(data), '筆資料')

#print(data[0])
#print('--------')
#print(data[1])
#print('--------')
#print(data[2])

sum_len = 0
for d in data: #每個d是一個字串
    sum_len = sum_len + len(d)
    print(sum_len)
print('留言平均長度為', sum_len / len(data))