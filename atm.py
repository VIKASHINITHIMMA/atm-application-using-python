acc_list=['123','345','567']
pwd_list=['321','345','567']
amt_list=[1000,5000,300]
print ('Good Morning')
acc_no=raw_input('Enter your account no:')
if acc_no not in acc_list:
	print ('invalid account number')
	exit()
pwd=raw_input('Enter your passwod')
for x in range(len(acc_list)):
	if acc_no==acc_list[x]:
		if pwd_list[x]!=pwd:
			print('invalid pin')
			exit()
		else:
			print('Press w to withdraw\nPress d to deposit')
			ch=raw_input()
			amt=int(raw_input('Enter the amount:'))
			if ch=='w':
				if amt>amt_list[x]:
					print('balance is insufficient')
					exit()
				amt_list[x]=amt_list[x]-amt
				print('Withdrawn succesfully')
				print('balance=',amt_list[x])
			elif ch=='d':
				amt_list[x]=amt_list[x]+amt
				print('deposited successfully')
				print('balance=',amt_list[x])
			else:
				print('invalid choice')
exit()

				
		
		

	

