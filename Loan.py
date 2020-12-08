while True:
	print('''Available Options -> 
1) Monthly Payments
2) Loan Term
3) Rate of Interest
''')
	while True:
		ch1 = int(input('What Would You Like To Do? '))
		print()
		
		if ch1 not in (1, 2, 3):
			print()
			print('Invalid Input')
			print()
			
		elif ch1 == 1:
			p = float(input('Enter The Principal Amount: '))
			print()
			
			while True:
				ch2 = int(input('''The Time Period is in -> 1) Months
2) Years'''))
				if ch2 not in (1, 2):
					print()
					print('Invalid Input')
				else:
					break
				
				
			print()
			t = float(input('Enter The Time Period: '))
			print()
			
			r = float(input('Enter The Rate of Interest: '))
			print()
			
			a = p * 1 + r * t
			
			mp = a // t
			
			if ch2 == 1:
				print('Your {} payments are of Rs. {}'.format(ch2, mp	))
			print()
			
		elif ch1 == 2:
			i = float(input('Enter The Interest Applied : '))
			print()
			
			p = float(input('Enter The Principal Amount : '))
			print()
			
			r = float(input('Enter The Rate of Interest: '))
			print()
			
			t1 = r / 100
			t2 = p * t1
			t3 = i / t2
			
			print(t3)
			print()
			
		elif ch1 == 3:
			print()
			p = float(input('Enter The Principal Amount: '))
			print()
			
			i = float(input('Enter The Interest Applied: '))
			print()
			
			t = float(input(('Enter The Time Period: ')))
			print()
			
			r1 = p * t
			r2 = i / r1
			r3 = r2 * 100
			
			print(r3)
			print()
			
			
			
			
			
			