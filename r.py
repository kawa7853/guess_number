import random

r = random.randint(1, 100)
while True:
	n = input("請猜數字：")
	n = int(n)
	if n == r:
		print("猜對囉！")
		break
	elif n > r :
		print("比答案大")
	else:
		print("比答案小")