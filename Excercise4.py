person = {

    "f_name": "matt",
    "l_name": "Saul",
    "age": "19",
    "hometown": "Aiken, SC",
    "current city": "Anderson",
    "username": "msaul113",
}
print(person)
print(person["f_name"])
print(person["l_name"])
print(person["age"])
print(person["hometown"])
print(person["current city"])
print(person["username"])
print(f"Hello my name is {person['f_name' ]} {person['l_name']}, I'm {person['age']} years old. I'm from {person['hometown']}, but I currently live in {person['current city']}. My username is {person['username']}.")

definitions = {
    "python": "Python is a high-level general-purpose programming language.",
    "variable": "Variable is a element, feature, or factor that is liable to vary or change.",
    "list": "List is a number of connected items or names written or printed consecutively, typically one below the other.",
    "method": "A method is a function that is availible for a given object because of the objects type.",
    "if statement": "Dictionary is a set of words or other text strings made for use in applications such as spelling checkers.",
    "dictionary": "Dictionary is a set of words or other text strings made for use in applications such as spell checkers.",
    "function": "Function is a relationship or expression involving one or more variables.",
}
print('\n')
print(definitions["python"])
print('\n')
print(definitions['variable'])
print('\n')
print(definitions["list"])
print('\n')
print(definitions["method"])
print('\n')
print(definitions["if statement"])
print('\n')
print(definitions["dictionary"])
print('\n')
print(definitions["function"])





sc_counties_dict = {'anderson county':'anderson' ,
               'pickens county':'pickens',
               'oconnee county':'walhalla',
               'greenville county':'greenville',
               'Spartanburg county':'Spartanburg',
               'york county':'york'}

sc_counties_list = ['anderson county','pickens county','laurens county','polk county','sumter county','newberry county','oconee county','greenville county','aiken county','spartanburg county','york county']

for county in sc_counties_list:
    if county in sc_counties_dict:
        print(f'{county} is in our dictionary. The capital is {sc_counties_dict[county].title()}')
    else:
        print(f'{county.title()} is not in our dictionary. We will add this county shortly. Thanks!')
        print('')

anderson_cities = ['belton', 'anderson', 'pendelton', 'powdersville']

for city in anderson_cities:
    if city in sc_counties_dict.values() and sc_counties_list:
       print(f'{city.title()} is te capital of Anderson County')
    else:
        print(f'{city.title()} is the capital of any county')

anderson_county_dict = {'belton': 4366, 'anderson': 24721, 'pendelton': 4361, 'piedmont': 3278, 'powdersville':5463}
pickens_county_dict = {'six mile': 4366, 'easley': 24721, 'pickens': 4421, 'sunset': 3298, 'pumpkintown':5463}
greenville_county_dict = {'greenville': 4366, 'fountain inn': 24721, 'simpsonville': 4721, 'taylors': 3298, 'mauldin':5463}
spartanburg_county_dict = {'duncan': 4366, 'lyman': 24721, 'boiling springs': 4301, 'spartanburg': 3298, 'cowpens':5463}
aiken_county_dict = {'aiken': 4366, 'graniteville': 24721, 'windsor': 4381, 'new ellington': 3298, 'warrenville':5463}

sc_counties_listofdicts = anderson_county_dict, pickens_county_dict, greenville_county_dict, spartanburg_county_dict,
print(sc_counties_listofdicts)

for county in sc_counties_listofdicts:
    for city, population in county.items():
     print(f'In {city.title()}, the current population is {population}')




name = input("Enter your name: ")
print("Hello " + name + " welcome to Anderson University.")

i3 = 120
i5 = 220
i7 = 600
i9 = 1200

pocket = int(input("What does your budget look like: "))

if pocket >= i9:
    print('You can afford our i3, i5, i7, and i9 processor option. ')
elif pocket >= i7:
    print('You can afford our i3, i5, and i7 processor option. ')
elif pocket >= i5:
    print('You can afford our i3 and i5 processor option. ')
elif pocket >= i3:
    print('You can afford our i3 processor option. ')
else:
    print("You can't afford any processor options today. Whenever your ready to exit type out. ")

active = True
while active:
    if pocket == 'out':
        active = False
    else:
        print('Thank for stopping by come and see us again. ')
        active = False
