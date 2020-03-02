
i = 0
j = 2 
pwd = 'a123456'
while True:
	
	if i < 3:
		password = input('請輸入密碼： ')
		if password == pwd:
			print('登入成功')
			break
		else:
			if i < 2:
				print('密碼錯誤！還有', 2-i, '次機會')
			else:
				print('已經猜錯三次囉')
			i = i + 1
	elif i >= 3:
		q = input('請問您是否要更改密碼(y/n): ')
		if q == 'y':
				newpwd = input('請輸入新密碼: ')
				pwd = newpwd
				i = 0
		elif q == 'n':
				print('您的帳號即將被鎖住')
				break

