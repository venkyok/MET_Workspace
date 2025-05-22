def one_to_three():
    for i in range(1,4):
        print(i)

def three_to_seven():
    for i in range(3,8):
        print(i)

def seven_to_ten():
    for i in range(7,11):
        print(i)

# three_to_seven()
# one_to_three()
# seven_to_ten()


def new_fun(lang,name):
    if lang =='en':
        print(f'hello {name}')
    elif lang =='fr':
        print(f'bonjour {name}')
    else:
        print(f'hola {name}')

# new_fun('en','joy')

data =[
    {
        "name":'joy',
        'age':25

    },
    {
        'name':'hoi',
        'age':30

    }

]


def extract_name(details):
    age_1 = details[0]['age']
    age_2 = details[1]['age']

    return [age_1,age_2]

ans = extract_name(data)
    
print(ans)