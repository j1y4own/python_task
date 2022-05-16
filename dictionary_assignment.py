jiyun = {'name' : 'jiyunjeon', 'age' : '24', 'birth' : '990814', 'sex' : 'female', 'number' : '010-8758-8347'}
hyunsoo = {'name' : 'hyunsoooh', 'age' : '29', 'birth' : '940923', 'sex' : 'male', 'number': '010-4444-7777'}
seeun =  {'name' : 'seeunjo', 'age' : '24', 'birth' : '990805', 'sex' : 'female', 'number': '010-6686-2779'}

name = [1, 2, 3]
age = [1, 2, 3]
birth = [1, 2, 3]
sex = [1, 2, 3]
number = [1, 2, 3]

name[0:3] = [jiyun['name'], hyunsoo['name'], seeun['name']]
age[0:3] = [jiyun['age'], hyunsoo['age'], seeun['age']]
birth[0:3] = [jiyun['birth'], hyunsoo['birth'], seeun['birth']]
sex[0:3] = [jiyun['sex'], hyunsoo['sex'], seeun['sex']]
number = [jiyun['number'], hyunsoo['number'], seeun['number']]

print(name)
print(age)
print(birth)
print(sex)
print(number)