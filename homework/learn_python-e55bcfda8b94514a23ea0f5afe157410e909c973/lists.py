n_list = [1, 2, 3, 54., 'message']
print (n_list)

print (len(n_list))


print(n_list[:2])

n_list[3] = '3 ELEMENT'

sec_list = [1,2,3,4,5]

new_list = n_list + sec_list

print(len(new_list))

#adding items
new_list.append('append element')

new_list.insert(0,'first element')
print(new_list)


#removing items
k=new_list.pop(0)
print(new_list, k)


print(new_list)
y = new_list.remove('append element')
print(new_list)



list_new = [1,25,6]
letter_list = ['apple','jks', 'z']

list_new.sort()
print('New sorted list = ', list_new)


letter_list.sort()
print('letter list = ', letter_list)

new_list.reverse()
print('Reverse list = ', new_list)




ex_list = [1, 'hello', True, 'element', 1245234, False]

ex_list2 = ex_list[:3]
print(ex_list2)