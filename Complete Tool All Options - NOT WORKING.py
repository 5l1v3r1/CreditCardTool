import random
#these are the import librarys needed for the tool

# ----------------------- FUNCTIONS ------------------------------------------
#bellow these are all the funcitons I wrote for the program to be able to do 
#what is needed in the code, this keeps the working code area tidy


#This function is to calculate the Luhn Algorithm to valudate the credit card 
#by calculating the given numbers against the modolus of 10
def checksum():
	global checked1
	a2 = 0
	a = str(int(creditcard[0]) * 2)
	b = str(int(creditcard[2]) * 2)
	c = str(int(creditcard[4]) * 2)
	d = str(int(creditcard[6]) * 2)
	e = str(int(creditcard[8]) * 2)
	f = str(int(creditcard[10]) * 2)
	g = str(int(creditcard[12]) * 2)
	h = str(int(creditcard[14]) * 2)
	ah = str(a + b + c + d + e + f + g + h)

	for i in range(len(ah)):
		a2 += int(ah[i])
		a1 = int(creditcard[1])
		b1 = int(creditcard[3])
		c1 = int(creditcard[5])
		d1 = int(creditcard[7])
		e1 = int(creditcard[9])
		f1 = int(creditcard[11])
		g1 = int(creditcard[13])
		h1 = int(creditcard[15])
		fin = int(a2 + a1 + b1 + c1 + d1 + e1 + f1 + g1 + h1)
		checksum = int(fin % 10)

	if checksum == 0:
		print("The Credit Card is Valid")
		 
		checked1 = True
	else:
		print("The Credit Card Failed Validation")

#this function is for listing the industry of the card such as Airline if the card begins with either a 1 or 2 
def industrycehcker():
	industry = False
	if len(creditcard) == 16:
		if creditcard[0] in ('1', '2'):
			print("Card From: Airline Industry")
			industry = True
		elif creditcard[0] in ('3'):
			print("Card From: Travel and Entertainment Industry")
			industry = True
		elif creditcard[0] in ('4', '5'):
			print("Card From: Branking and Financial Industry")
			industry = True
		elif creditcard[0] in ('6'):
			print("Card From: Merchandizing and Banking Industry")
			industry = True
		elif creditcard[0] in ('7'):
			print("Card From: Petroleum Industry")
			industry = True
		elif creditcard[0] in ('8'):
			print("Card From: Telecom Industry")
			industry = True
		elif creditcard[0] in ('3'):
			print("Card From: National Assignment i.e. GOV")
			industry = True
		else:
			print("Unknown Industry Identifier")
	elif len(creditcard) == 19:
		if creditcard[0] in ('1', '2'):
			print("Card From: Airline Industry")
			industry = True
		elif creditcard[0] in ('3'):
			print("Card From: Travel and Entertainment Industry")
			industry = True
		elif creditcard[0] in ('4', '5'):
			print("Card From: Branking and Financial Industry")
			industry = True
		elif creditcard[0] in ('6'):
			print("Card From: Merchandizing and Banking Industry")
			industry = True
		elif creditcard[0] in ('7'):
			print("Card From: Petroleum Industry")
			industry = True
		elif creditcard[0] in ('8'):
			print("Card From: Telecom Industry")
			industry = True
		elif creditcard[0] in ('9'):
			print("Card From: National Assignment i.e. GOV")
			industry = True
		else:
			print("Unknown Industry Identifier")

#this function is for check the card type trough the first 2 to 6 numbers matching a set list			
def bankissuercheck():
	if len(creditcard) == 16:
		if creditcard[0] in ('4'):
			print("Card is: Visa")
			validbank = True
		elif creditcard[0:2] in ('34'):
			print("Card is: American Express")
			validbank = True
		elif creditcard[0:2] in ('37'):
			print("Card is: American Express")
			validbank = True
		elif creditcard[0:2] in ('31'):
			print("Card is: China T Union")
			validbank = True
		elif creditcard[0:2] in ('62'):
			print("Card is: China UnionPay")
			validbank = True
		elif creditcard[0:2] in ('36'):
			print("Card is: Dinners Club Internationa")
			validbank = True
		elif creditcard[0:2] in ('55'):
			print("Card is: Diners Club USA MasterCard")
			validbank = True
		elif creditcard[0:2] in ('54'):
			print("Card is: Diners Club USA MasterCard")
			validbank = True
		elif creditcard[0:4] in ('6011'):
			print("Card is: Discover Card")
			validbank = True
		elif creditcard[0:2] in ('64'):
			print("Card is: Discover Card")
			validbank = True
		elif creditcard[0:2] in ('65'):
			print("Card is: Discover Card")
			validbank = True
		elif creditcard[0:2] in ('60'):
			print("Card is: RuPay")
			validbank = True
		elif creditcard[0:4] in ('6521'):
			print("Card is: Discover Card")
			validbank = True
		elif creditcard[0:4] in ('6522'):
			print("Card is: Discover Card")
			validbank = True
		elif creditcard[0:3] in ('636'):
			print("Card is: InterPayment")
			validbank = True
		elif creditcard[0:3] in ('637'):
			print("Card is: InstaPayment")
			validbank = True
		elif creditcard[0:4] in ('3528'):
			print("Card is: JCB")
			validbank = True
		elif creditcard[0:2] in ('3589'):
			print("Card is: JCB")
			validbank = True
		elif creditcard[0:2] in ('50'):
			print("Card is: Maestro")
			validbank = True
		elif creditcard[0:2] in ('56'):
			print("Card is: Maestro")
			validbank = True
		elif creditcard[0:2] in ('58'):
			print("Card is: Maestro")
			validbank = True
		elif creditcard[0:3] in ('639'):
			print("Card is: Maestro")
			validbank = True
		elif creditcard[0:2] in ('67'):
			print("Card is: Maestro")
			validbank = True
		elif creditcard[0:4] in ('5019'):
			print("Card is: Dankort")
			validbank = True
		elif creditcard[0:4] in ('4571'):
			print("Card is: Dankort")
			validbank = True
		elif creditcard[0:4] in ('2200'):
			print("Card is: MIR")
			validbank = True
		elif creditcard[0:4] in ('2204'):
			print("Card is: MIR")
			validbank = True
		elif creditcard[0:6] in ('222100'):
			print("Card is: MasterCard")
			validbank = True
		elif creditcard[0:6] in ('272099'):
			print("Card is: MasterCard")
			validbank = True
		elif creditcard[0:2] in ('51'):
			print("Card is: MasterCard")
			validbank = True
		elif creditcard[0:2] in ('55'):
			print("Card is: Mastercard")
			validbank = True
		elif creditcard[0:4] in ('6334'):
			print("Card is: SOLO")
			validbank = True
		elif creditcard[0:4] in ('6767'):
			print("Card is: SOLO")
			validbank = True
		elif creditcard[0:1] in ('1'):
			print("Card is: UATP")
			validbank = True
		elif creditcard[0:6] in ["459654"]:
			print("Revolut Visa Debit Card")
			validbank = True
		elif creditcard[0:6] in ["539123"]:
			print("Revolut MasterCard Debit Card")
			validbank = True

#this is a funciton for checking if the numbers fall into a list bellow to known the issuing country
def countryguess():
	if creditcard[0:4] in ('4319'):
		print("The Card is From Ireland")
	elif creditcard[0:2] in ('34') or creditcard[0:2] in ('37'):
		print("The Card is From America")
	elif creditcard[0:2] in ('31'):
		print("The Card is from China")
	elif creditcard[0:2] in ('62'):
		print("The Card is From China")
	elif creditcard[0:2] in ('36'):
		print("The Card is International")
	elif creditcard[0:3] in range(300, 305):
		print("The Card is International")
	elif creditcard[0:2] in range(54, 55):
		print("The Card is from America")





# ----------------------------- Working Code ------------------------------
#bellow this line is the working code of the program not including the functions
#if there are areas it will most probably be below this line


#this is the main menu area of the program
print("")
print("#######################################################")
print("#		  Made By CyberViking                #")
print("#######################################################")
print("")
print("Options Menu:")
print("Checksum Verifcation - 1 ")
print("Bank Validation - 2 ")
print("Missing last Digit - 3 ")
print("Full Card Generation - 4 ")
print("")
ans = input("Select a Option: ")


#i have decided to remove the option for cards that are longer then 16 for now, as most cards will be upto 16


if ans == '1':
	#this option is to check if a card is valid based on luhn algorithm
	card1 = input("enter the card number: ")
	creditcard = card1.replace(" ", "")
	checksum()


elif ans == '2':
	#This option validates the banks that issued the cards
	checkedsum = False
	industry = False
	validbank = False

	card1 = input("enter the card number: ")
	creditcard = card1.replace(" ", "")

	industrycehcker()
	bankissuercheck()
	countryguess()
	checksum()

	if industry == True and validbank == True and checkedsum == True:
		print("The Given Card is Valid")

	elif industry == True and validbank == True and checkedsum == False:
		print('checkedsum: Failed')

#Having issues here for some reason it wouldnt go to trough the if statements and just jumped straight ot the last else statment
#This section is to the area that will generate tha last missing number of a credit card

elif ans == '3':
	#This option finds the last missing number
	card1 = input("enter the card number: ")
	creditcard = card1.replace(" ", "")
	checked1 = False

	while checked1 == False:
		print("Test 1")
		if len(creditcard) == (15):
			creditcard = creditcard + '0'
			

		elif len(creditcard) == (16):
			creditcard = (creditcard[:15] + str(int(creditcard[15]) + 1))
			print(len(creditcard))
			checksum()
			
			if checked1 == False:
				print("The card is Now Valid")
				print(("This is the Card Number: ") + (str(creditcard)))
				checked1 = True
				print("Test 2")
			else:
				checked1 = False
				print("Test 3")

		if (creditcard[15] == 9 and checked1 == False):
			print('Not a valid Card Number')
			break

		else:
			print("please Enter a Card Number missing the last digit")  # error response
			break



#This seciton will generate a full vaild credit card using the random functions

elif ans == '4':
	checked1 = False
	#this option will generate a full credit card
	while checked1 == False:
		banksidnum = random.randint(100000, 999999)
		month = random.randint(1, 12)
		year = random.randint(19, 30)
		genacardnum = random.randint(1000000000, 9999999999)
		makecvv = random.randint(100, 999)
		creditcard = str(banksidnum) + str(genacardnum)
		checksum()
	if checked1 == True:
		print("")
		print(("Card Number: ") + str(banksidnum) + str(genacardnum))
		print(("CVV number: ") + str(makecvv))
		print(("month of Exipry: ") + str(month))
		print(("Year of Exipry: ") + str(year))
		print("The Card Passess Validation")

else:
	print("!!! please choose a vaild menu option, now exiting !!!")
