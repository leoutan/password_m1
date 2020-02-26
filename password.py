
i = 0
j = 2 
while i < 3:
	password = input('請輸入密碼： ')
	if password == 'a123456':
		print('登入成功')
		break
	else:
		if i < 2:
			print('密碼錯誤！還有', 2-i, '次機會')
			i = i + 1
		else:
			print('已經猜錯三次囉')
