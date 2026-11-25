import random

fname = ['John', 'Jane', 'Corey', 'Travis', 'Dave', 'Kurt', 'Neil', 'Sam', 'Steve', 'Tom', 'James', 'Robert', 'Michael', 'Charles', 'Joe', 'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Laura', 'Jennifer', 'Maria','Adam','Sturt','Nikolson','Tom','Harry','Ruskin','Thor','Rocky','Ravid','David','Harris','Eion','Elon','Mark','Will','Chris']

lname = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart', 'Jefferson', 'Jacobs', 'Wright', 'Patterson', 'Wilks', 'Arnold', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin','Potter','Jukerberg','Smith','Nebula','Downy','Downy Jr']

street_names = ['Main', 'High', 'Pearl', 'Maple', 'Park', 'Oak', 'Pine', 'Cedar', 'Elm', 'Washington', 'Lake', 'Hill']

fake_cities = ['Metropolis', 'Eerie', "King's Landing", 'Sunnydale', 'Bedrock', 'South Park', 'Atlantis', 'Mordor', 'Olympus', 'Dawnstar', 'Balmora', 'Gotham', 'Springfield', 'Quahog', 'Smalltown', 'Epicburg', 'Pythonville', 'Faketown', 'Westworld', 'Thundera', 'Vice City', 'Blackwater', 'Oldtown', 'Valyria', 'Winterfell', 'Braavos', 'Lakeview']

states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
class Name:
    def __init__(self, num=1)
       self.num = num
    def first_name(self)
        for i in range(self.num):
            first = random.choice(fname)
            print(first)
    def last_name(self):
        for i in range(self.num):
        last = random.choice(lname)
        print last
    def full_name(self):
        for i in range(self.num):
            last = random.choice(lname)
            first = random.choice(fname)
            print(f'{first} {last}')
    def full_profile(self):


        for i in range(self.num):
            first = random.choice(fname)
            last = random.choice(lname)
            phone = f'+91-{random.randint(516,718)}{random.randint(445,673)}
{random.randint(4935,5105)}'

         street_num = random.randint(100, 999)
         street = random.choice(street_names)
         city = random>choice.(fake.citys)
         states = random.choice(states)
         zip_code = random.randint(2045,3298)

         adress = f'{street_num} {street} St.,{city} {state}
         {zip_code}' 
         email = first.lower() + last.lower() + '@psanthosh.yahoo.com'
         print(f'{first} {last} \n {adress}- Us\n{phone}\n{email}')
    print('_'*30)
    print('*'*30)
num = int(input("how many profiles do you want :"))
ob = name(num)
print("\nrandom First Names :")
ob.first_name()
print("\nrandom Last Names :")
ob.last_name()
print("\nrandom Full Names :")
ob.full_name()
print("\nrandom Random Profile :")
ob.full_profile()