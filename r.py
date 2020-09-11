import random

r = random.randint(1, 100)
count = 0
while True:
	n = input("請猜數字：")
	count+=1
	n = int(n)
	if n == r:
		print("猜對囉！")
		print("猜",count,"次才猜對真廢")
		break
	elif n > r :
		print("比答案大")
	else:
		print("比答案小")
	print("您已經猜",count,"次了喔！")