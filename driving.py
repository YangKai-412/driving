country = input('請問你是哪國人： ')
if country == '台灣':
	age = input('請輸入年齡： ')
	age = int(age)
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你還不能考駕照')
elif country == '美國':
	age = input('請輸入年齡： ')
	age = int(age)
	if age >= 16:
		print('你可以考駕照')
	else:
		print('你還不能考駕照')
else:
	print('錯誤！請輸入台灣或美國！')

