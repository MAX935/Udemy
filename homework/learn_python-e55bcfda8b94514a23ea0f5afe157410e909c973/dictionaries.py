car_prices = {'Mercedes': 10000, 'Toyota': 7000, 'BMW': 12000}
print(car_prices)
print(car_prices['BMW'])




car_prices['Lada'] = 6000
print(car_prices['Lada'])



del car_prices['Toyota']
print(car_prices)



car_prices.clear()
print(car_prices)


person = {

'first name' : 'Jack',
'last name' : 'Jones',
'car' : 'BMW',
'color' : 'black',
'hobbies' : ['football', 'swimming', 'golf'],
'children' : {'son': 'White son', 'dauther': 'black dauther'}

}

print(person['car'])
print (person['children'])




temp = person['hobbies'][0]
print(temp)



xt = person['children']['son']
print(xt)


print(person.items())




dict2 = {
'key':'first',
'last':'nefirst'
}

print(dict2['last'])