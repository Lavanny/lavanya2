
## Indexing

# a = 'HelloWorld'
#
# print(a[::-1])

## Lambda functions
double = lambda x,y : x+y
# print(double(5,2))

## Tuples

a = (1, 2, 3, 4)
## immutable
# a[1] = 5

# for i in range(len(a)):
#     print(a[i])


# for x,y in enumerate(a):
#     print(x, y)

## Packing and Unpacking

# x, y = (1,2)
# print(x)
#
# print(5 in a)

# a = (100,)
# print(type(a))
# print(a)

### Dictionaries

d = {
    'Anne': 123,
    'Bill': 456,
    'Cathy': 789
}

# d['Don'] = 1234
# # print(d)
# # x= d.pop('Cathy')
# # print(d)
#
# # e = dict([('Anne',1234), (3,4)])
# # print(e)
#
# d = {x:x**2 for x in range(1,4)}
# print(d)

phonebook = {
    'Anne': 123,
    'Bill': 456,
    'Cathy': 789
}

# print(phonebook.keys())
# print(phonebook.values())
# print(phonebook.items())
#
# for (x, y) in phonebook.items():
#     print(x, y)

# person = {
#     'name':'A',
#     'age': 21,
#     'phone': 1234,
#     'address':{
#         'city':'New Delhi',
#         'state': 'Delhi',
#         'country': 'India',
#     }
#
# }
#
# print(person['address']['country'])

phonebook = {
    'Anne': 123,
    'Bill': 456,
    'Cathy': 789
}
print(phonebook.get('Don'))
