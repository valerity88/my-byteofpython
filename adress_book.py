import pickle
ab = { 'Valerity' : 'valerity@inbox.ru',
       'Zakirov_VI' : 'zakirov_vi@24.rospotrebnadzor.ru',
       'ZakiValera' : 'zakivalera@yandex.ru',
       'IT' : 'it@24.rospotrebnadzor.ru',
       'Swaroop' : 'swaroop@swaroopch.com',
       'Larry' : 'larry@wall.org',
       'Matsumoto' : 'matz@ruby-lang.org',
       'Spammer' : 'spammer@hotmail.com'}
print('Для просмотра наберите "show"')
print('Для удаления контакта из адресной книнги введите "delete"')
print('Для изменения контакта в адресной книге введите "change"')
print('Для поиска в адресной книге введите "search"')
print('Для добавления контакта в адресную книгу введите "add"')
def user_info():
    user_input = input('Введите требуемое действие: ')
    if user_input == 'show':
        for name, adress in ab.items():
            print('{0} : "{1}"'.format(name, adress))
    if user_input == 'delete':
        delete_adress = input('Введите имя для удаления: ')
        del ab[delete_adress]
        print(ab)
    if user_input == 'add':
        add_name = input('Введите имя : ')
        add_adress = input('Введите адресс : ')
        ab[add_name] = add_adress
        print(ab)
    if user_input == 'change':
        change_adress = input('Введите имя для изменения: ')
        new_adress = input('Введите новый адрес: ')
        ab[change_adress] = new_adress
        print(ab)
    if user_input == 'search':
        search_name = input('Введите имя для поиска: ')
        for name, adress in ab.items():
            if name == search_name:       
                print('{0} : {1}'.format(name, adress))
    else:
        pass
while True:
    user_info()
ab_file = open('adress_book.data', 'wb')
pickle.dump(ab, ab_file)
ab_file.close()
