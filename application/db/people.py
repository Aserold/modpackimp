#имя, долларов в час, количество часов отработано
people_wage = {
    'Anna': [14, 140], 
    'Jake': [14,145],
    'Mark': [16, 160],
    'Christopher': [18, 154]
}


def get_employees(data):
    for name, data in data.items():
        wage_per_hour = data[0]
        hours_worked = data[1]
        print(f"Имя: {name}, Заработок в час: {wage_per_hour} долларов, Количество отработанных часов: {hours_worked} часов")
        
# print(get_employees(people_wage))