def calculate_salary(people):
    for person, data in people.items():
        name = person
        wage = data[0]
        hours = data[1]
        salary = wage * hours
        print(f'Имя: {name}. Заработная плата: {salary}$')
        
# print(calculate_salary({'Anna': [14, 140], 'Jake': [14,145], 'Mark': [16, 160], 'Christopher': [18, 154]}))