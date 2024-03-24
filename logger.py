from data_create import name_data, surname_data, phone_data, address_data 

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    
    with open('phonebook.csv', 'a', encoding='utf-8') as f:
        f.write(f'{name};{surname};{phone};{address}\n')        
  

def print_data():
    with open('phonebook.csv', 'r', encoding='utf-8') as f:
        print(f.read())
    print('') 


def correct_data():
    with open('phonebook.csv', 'r', encoding='utf-8') as f:
        data = f.read()
        data_lines = data.split('\n')
        for n, elements in enumerate(data_lines, 1):
            print(n, elements)
    print('')
    
    correct_data_index = int(input('Выберите номер контакта подлежащего изменению: '))-1
    
    data_lines = data.split('\n')
    correct_data_lines = data_lines[correct_data_index]
    elements = correct_data_lines.split(';')
    name = input('Введите ваше имя: ')
    surname = input('Введите вашу фамилию: ')
    phone = input('Введите ваш телефон: ')
    address = input('Введите ваш адрес: ')
    num = elements[0]    
    if len(name) == 0:
        name=elements[1]
    if len(surname) == 0:
        surname=elements[2]
    if len(phone) == 0:
        phone=elements[3]
    if len(address) == 0:
        address = elements[4]  
  
    correct_date = f'{name};{surname};{phone};{address}'            
    data_lines[correct_data_index] = correct_date
    with open('phonebook.csv', 'w', encoding='utf-8') as f:       
        f.write('\n'.join(data_lines))    

    
def delete_data():
    with open('phonebook.csv', 'r', encoding='utf-8') as f:
        data = f.read()
        data_lines = data.split('\n')
        for n, elements in enumerate(data_lines,1):
            print(n, elements)
    print('')

    del_data_index = int(input('Выберите номер контакта подлежащего удалению: '))-1
    
    del_data_lines = data_lines[del_data_index]
    data_lines.pop(del_data_index)
    print(f'Контакт удален...')
    with open('phonebook.csv', 'w', encoding='utf-8') as f:       
        f.write('\n'.join(data_lines))





