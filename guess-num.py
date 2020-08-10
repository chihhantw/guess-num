import random

r = random.randint(1, 100)
count = 0 #計算次數
while True:
	count += 1
	num = input('從1至100的範圍內，請猜數字:')
	num = int(num)
	if num == r:
		print('你猜中了!!!')
		print('這是你猜的第',count,'次')#為了要猜中的時候仍有這行!
		break
	elif num > r:
		print('再小一點')
	elif num < r:
		print('再大一點')
	print('這是你猜的第',count,'次')

