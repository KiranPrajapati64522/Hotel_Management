table={}
available_rooms={'Siyaji hotel':[201,204,304],'Lemon tree':[101,104,105],'Cosmopolitan':[509,501,504],'Wow hotel':[104,105,107],'The leela palace':[202,203,401,401],'Golden hotel':[301,302,303,401,405],'Clyford suites':[105,106,106,107],'Taj lands ends':[101,103,104,105],'Four seasons':[202,203,404,405],'Hotel leela':[301,304,109,108],'The lalit':[101,102,103],'Sun-n-sand':[201,101,202,203,204],'Eros hotel':[401,402,403],'Wood castle':[101,102,105,108],'Lemon tree premier':[501,502,503,504],'Anujshree':[601,602,604,606],'Imperial grand':[102,103,501,504,506],'Shriram ujjain':[401,403,404],'Kalpana palace':[101,104,109,107],'Hyatt pune':[601,602,701],'Orchid hotel':[303,309,310],'Sayaji hotel':[609,608],'Grand tulip':[201,102,103],'Shekhawat palace':[408,409,601],'Novotel Yes':[603,501,502],'Om palace':[102,103,104,501]}		
print("---------------------------- Welcome to the Hotel System ---------------------")

class Hotel():	
	def __init__(self):
		self.table={}
		
		
	def cityAvailable(self):
		print('----------------- Here you Search the Hotel and Its Details --------------------')
		try: 
			city=input("Enter the city name :")
			city2=city.capitalize()
			print("Location \t Hotel Name \t Room Available \t Address \t PricePer Room")
		
			f=open("object1.txt","r")
			all=f.readlines()
			for data in all:
				d=data.split("\t",1)
				if (d[0]==city2):
					print(data)
			f.close()
		except ValueError:
			print("NOT AVAILABLE")
	
		
class HotelSystem():	
	def __init__(self):
		self.table={}
		
	def check_in(self):
		try:
			while True:	
				print('----------------------------------------------------------')
				print("Available cities for hotel are: Indore,Mumbai,Ujjain,Delhi,Pune,Banglore,Ahemdabad")
				city=input("Enter the city name in which you booking for the hotel:")
				city2=city.upper()
				if city2=='INDORE':
					print("Choose the Hotel Names:\n1.Siyaji hotel  \n2.Lemon tree \n3.Cosmopolitan \n4.Wow Hotel ")
					i=input("Enter the Hotel Name : ")
					i2=i.capitalize()
					print("Location \t Hotel Name \t Room Available \t Address \t PricePer Room")
				
				elif city2=='MUMBAI':
					print("Choose the Hotel Names:\n1.Taj Lands ends \n2.Four seasons \n3.The Lalit \n4.Hotel Leela \n5.Sun-N-sand ")
					i=input("Enter the Hotel Name : ")
					i2=i.capitalize()
					print("Location \t Hotel Name \t Room Available \t Address \t PricePer Room")
				elif city2=='BANGLORE':
					print("Choose the Hotel Names:\n1.The Leela Palace \n2.Golden Hotel \n3.Clyford Suites ")
					i=input("Enter the Hotel Name : ")
					i2=i.capitalize()
					print("Location \t Hotel Name \t Room Available \t Address \t PricePer Room")
				elif city2=='AHEMDABAD':
					print("Choose the Hotel Names:\n1.Shekhawat Palace \n2.Novotel \n3.Om Palace ")
					i=input("Enter the Hotel Name : ")
					i2=i.capitalize()
					print("Location \t Hotel Name \t Room Available \t Address \t PricePer Room")
				elif city2=='DELHI':
					print("Choose the Hotel Names:\n1.Eros hotel \n2.Wood castle \n3.Lemon Tree Premier ")
					i=input("Enter the Hotel Name : ")
					i2=i.capitalize()
					print("Location \t Hotel Name \t Room Available \t Address \t PricePer Room")
				elif  city2=='UJJAIN':
					print("Choose the Hotel Names:\n1.Anujshree \n2.Imperial Grand \n3.Shrirram Ujjain \n4.Kalpana Palace ")
					i=input("Enter the Hotel Name : ")
					i2=i.capitalize()
					print("Location \t Hotel Name \t Room Available \t Address \t PricePer Room")
				elif city2=='PUNE':
					print("Choose the Hotel Names:\n1.Hyatt Pune \n2.Orchid hotel \n3.Sayaji hotel \n4.Grand tulip ")
					i=input("Enter the Hotel Name : ")
					i2=i.capitalize()
					print("Location \t Hotel Name \t Room Available \t Address \t PricePer Room")
				else:
					print("NOT AVAILABLE HOTEL FOR THIS CITY")
					break;
				
					
				f=open("object1.txt","r")
				all=f.readlines()
				for data in all:
					d=data.split("\t",2)
					if (d[1]==i2):
						print(data)
			
				f.close()
			
				print(f"************* Welcome to the Hotel ({i2}) in ({city2}) ****************")
				print("Now you fill the details for Booking")
				name=str(input("Enter your name: "))
				name1=name.capitalize()
				
				address=str(input("Enter your address: "))
				phone=int(input("Enter your phone number: "))
				d,m,y=map(int,input("Enter check-in-date in date,month,year: ").split('/'))
				date=(y,m,d)
				days=int(input("Enter the days to stay in Hotel: "))
				if i2=='Siyaji hotel':
					if available_rooms['Siyaji hotel']:
						room_no=available_rooms['Siyaji hotel'].pop(0)
						total_charges=600*days
					else:
						print("Not Available")
						return
				if i2=='Lemon tree':
					if available_rooms['Lemon tree']:
						room_no=available_rooms['Lemon tree'].pop(0)
						total_charges=700*days
					else:
						print("Not Available")
						return
				if i2=='Cosmopolitan':
					if available_rooms['Cosmopolitan']:
						room_no=available_rooms['Cosmopolitan'].pop(0)
						total_charges=600*days
					else:
						print("Not Available")
						return
				if i2=='Wow hotel':
					if available_rooms['Wow hotel']:
						room_no=available_rooms['Wow hotel'].pop(0)
						total_charges=500*days
					else:
						print("Not Available")
						return
				if i2=='The leela palace':
					if available_rooms['The leela palace']:
						room_no=available_rooms['The leela palace'].pop(0)
						total_charges=3100*days
					else:
						print("Not Available")
						return
				if i2=='Golden hotel':
					if available_rooms['Golden hotel']:
						room_no=available_rooms['Golden hotel'].pop(0)
						total_charges=3723*days
					else:
						print("Not Available")
						return
				if i2=='Clyford suites':
					if available_rooms['Clyford suites']:
						room_no=available_rooms['Clyford suites'].pop(0)
						total_charges=3100*days
					else:
						print("Not Available")
						return
				if i2=='Taj lands ends':
					if available_rooms['Taj lands ends']:
						room_no=available_rooms['Taj lands ends'].pop(0)
						total_charges=4200*days
					else:
						print("Not Available")
						return
				if i2=='Four seasons':
					if available_rooms['Four seasons']:
						room_no=available_rooms['Four seasons'].pop(0)
						total_charges=4000*days
					else:
						print("Not Available")
						return
				if i2=='Hotel leela':
					if available_rooms['Hotel leela']:
						room_no=available_rooms['Hotel leela'].pop(0)
						total_charges=3750*days
					else:
						print("Not Available")
						return
				if i2=='The lalit':
					if available_rooms['The lalit']:
						room_no=available_rooms['The lalit'].pop(0)
						total_charges=3800*days
					else:
						print("Not Available")
						return
				if i2=='Sun-n-sand':
					if available_rooms['Sun-n-sand']:
						room_no=available_rooms['Sun-n-sand'].pop(0)
						total_charges=3700*days
					else:
						print("Not Available")
						return
				if i2=='Eros hotel':
					if available_rooms['Eros hotel']:
						room_no=available_rooms['Eros hotel'].pop(0)
						total_charges=3969*days
					else:
						print("Not Available")
						return
				if i2=='Wood castle':
					if available_rooms['Wood castle']:
						room_no=available_rooms['Wood castle'].pop(0)
						total_charges=3132*days
					else:
						print("Not Available")
						return
				if i2=='Lemon tree premier':
					if available_rooms['Lemon tree premier']:
						room_no=available_rooms['Lemon tree premier'].pop(0)
						total_charges=3900*days
					else:
						print("Not Available")
						return
				if i2=='Anujshree':
					if available_rooms['Anujshree']:
						room_no=available_rooms['Anujshree'].pop(0)
						total_charges=3000*days
					else:
						print("Not Available")
						return
				if i2=='Imperial grand':
					if available_rooms['Imperial grand']:
						room_no=available_rooms['Imperial grand'].pop(0)
						total_charges=3500*days
					else:
						print("Not Available")
						return
				if i2=='Shriram ujjain':
					if available_rooms['Shriram ujjain']:
						room_no=available_rooms['Shriram ujjain'].pop(0)
						total_charges=2999*days
					else:
						print("Not Available")
						return
				if i2=='Kalpana palace':
					if available_rooms['Kalpana palace']:
						room_no=available_rooms['Kalpana palace'].pop(0)
						total_charges=3100*days
					else:
						print("Not Available")
						return
				if i2=='Hyatt pune':
					if available_rooms['Hyatt pune']:
						room_no=available_rooms['Hyatt pune'].pop(0)
						total_charges=5450*days
					else:
						print("Not Available")
						return
				if i2=='Orchid hotel':
					if available_rooms['Orchid hotel']:
						room_no=available_rooms['Orchid hotel'].pop(0)
						total_charges=5400*days
					else:
						print("Not Available")
						return
				if i2=='Sayaji hotel':
					if available_rooms['Sayaji hotel']:
						room_no=available_rooms['Sayaji hotel'].pop(0)
						total_charges=5098*days
					else:
						print("Not Available")
						return
				if i2=='Grand tulip':
					if available_rooms['Grand tulip']:
						room_no=available_rooms['Grand tulip'].pop(0)
						total_charges=3156*days
					else:
						print("Not Available")
						return
				if i2=='Shekhawat palace':
					if available_rooms['Shekhawat palace']:
						room_no=available_rooms['Shekhawat palace'].pop(0)
						total_charges=3400*days
					else:
						print("Not Available")
						return
				if i2=='Novotel Yes':
					if available_rooms['Novotel Yes']:
						room_no=available_rooms['Novotel Yes'].pop(0)
						total_charges=4000*days
					else:
						print("Not Available")
						return
				if i2=='Om palace':
					if available_rooms['Om palace']:
						room_no=available_rooms['Om palace'].pop(0)
						total_charges=3707*days
					else:
						print("Not Available")
						return
				
				print()	
				print(f"Check_in {name} , {address} on {date} in room no.:{room_no} for {days}days and your total charges is {total_charges}")
				print("Thank U for Booking in our Hotel.....")
				break;
				
					
					
		except ValueError:
				print("You enter the wrong detail plz enter the correct details ")
				self.check_in()
		
class HotelManagementDepartment():
	
		
	def add_hotel(self):
		ct=input("city: ")
		ct1=ct.capitalize()
		name=input("Hotel Name: ")
		name1=name.capitalize()
		address=input("Room Available: ")
		city=input("Full Address of Hotel:")
		price=input("PricePer Room: ")
		f=open("object1.txt","a")
		f.write(ct1+"\t")
		f.write(name1+"\t")
		f.write(address+"\t")
		f.write(city+"\t")
		f.write(price+"\n")
		print("Record Added")
		f.close()

	def delete_hotel(self):
		i=input("Enter the city name to remove from file: ")
		i1=i.capitalize()
		i=input("Enter the Hotel name to remove from file: ")
		i1=i.capitalize()
		f=open("object1.txt","r")
		all=f.readlines()
		f=open("object1.txt","w")
		for data in all:
			d=data.split("\t",2)
			if (d[1]!=i1):
				f.writelines(data)
		print("Record delete")
		f.close()

	

	def search_hotel(self):
		i=input("Enter the city name to be searched from file: ")
		i1=i.capitalize()
		f=open("object1.txt","r")
		all=f.readlines()
		for data in all:
			d=data.split("\t",1)
			if (d[0]==i1):
				print(data)
		f.close()

	def show_hotel(self):
		f=open("object1.txt","r")
		print("City  \t Hotel Name \t Room Available \t Full_Address \t PricePer_Room")
		print(f.read())
		f.close()

		
	def add_employee(self):
		em=input("Employee Id: ")
		name=input("Employee Name: ")
		name1=name.capitalize()
		address=input("Employee Address: ")
		contact=input("Contact Number: ")
		f=open("object.txt","a")
		f.write(em+"\t")
		f.write(name1+"\t")
		f.write(address+"\t")
		f.write(contact+"\n")
		print("Record Added")
		f.close()

	def delete_employee(self):
		i=input("Enter the Employee Id to remove from file: ")
		i=input("Enter the name to delete: ")
		f=open("object.txt","r")
		all=f.readlines()
		f=open("object.txt","w")
		for data in all:
			d=data.split("\t",2)
			if (d[1]!=i):
				f.writelines(data)
		print("Record delete")
		f.close()

	def update_employee(self):
		i=input("Enter the Employee Id to be updated from file: ")
		f=open("object.txt","r")
		all=f.readlines()
		f=open("object.txt","w")
		for data in all:
			d=data.split("\t",1)
			if (d[0]==i):
				name=input("New Name: ")
				address=input("New Address: ")
				contact=input("New Contact No.: ")
				f.writelines(d[0]+"\t"+name+"\t"+address+"\t"+contact+"\n")
			else:
				f.writelines(data)
				print("Record updated")
		f.close()

	def search_employee(self):
		i=input("Enter the Employee Id to be searched from file: ")
		f=open("object.txt","r")
		all=f.readlines()
		for data in all:
			d=data.split("\t",1)
			if (d[0]==i):
				print(data)
		f.close()

	def show_employee(self):
		f=open("object.txt","r")
		print("ID \t Name \t Address \t Contact no")
		print(f.read())
		f.close()


	
class abcd(Hotel,HotelSystem,HotelManagementDepartment):
	def __init__(self):
	
	
		while True:
			print()
			print("1. For Customer")
			print("2. For Hotel Management Department")
			print("3. Exit")
			choice=input("Enter the choice(1-3): ")
			if choice==str(1):
				while True:
					print()
					print("1. Search for Hotel")
					print("2. Booking for room")
					print("3. Exit")
					choice=input("Enter the choice(1-3): ")
					if choice==str(1):
						self.cityAvailable()
					elif choice==str(2):
						self.check_in()
					elif choice==str(3):
						break
					else:
						print("Invalid Number, Please enter the correct option")
			elif choice==str(2):
				while True:
					print("1. Hotel Portal")
					print("2. Employee Portal")
					print("3. Exit")
					choice=input("Enter the choice(1-3): ")
					if choice==str(1):
						while True:	
							print()
							print("Welcome to the Hotel Portal")
							print("1. Add new Location of Hotel ")
							print("2. Delete Hotel details")
							print("3. Search Hotel")
							print("4. Show all Hotel")			
							print("5. Exit")
							ch=input("Enter the choice(1-5): ")
							if ch==str(1):
								self.add_hotel()
							elif ch==str(2):
								self.delete_hotel()
							elif ch==str(3):
								self.search_hotel()
							elif ch==str(4):
								self.show_hotel()
							elif ch==str(5):
								break
							else:
								print("Invalid Number ,Please Choose the correct option")
					elif choice==str(2):
						while True:
							print()
							print("Welcome to the Employee Portal")
							print("1. Add new Employee ")
							print("2. Delete Employee details")
							print("3. Update the Employee")
							print("4. Search Employee")
							print("5. Show all Employees")
							print("6. Exit")
							ch=input("Enter the choice(1-6): ")
							if ch==str(1):
								self.add_employee()
							elif ch==str(2):
								self.delete_employee()
							elif ch==str(3):
								self.update_employee()
							elif ch==str(4):
								self.search_employee()
							elif ch==str(5):
								self.show_employee()
							elif ch==str(6):
								break
							else:
								print("Invalid Number ,Please Choose the correct option")
					elif choice==str(3):
						break;
						
					else:
						print("Invalid Choice , please enter the correct option")
						
			elif choice==str(3):
				break
			else:
		 		print("Invalid Choice , please enter the correct option")
h=abcd()






