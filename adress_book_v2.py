import pickle

class PDn:
    def __init__(self, adress_info):
        self.adress_info = adress_info
    def __str__(self):
        return self.adress_info

open_ab = open('adress_book.data', 'rb') # подразумевается наличие файла с данными
ab = pickle.load(open_ab)
open_ab.close

print('Для просмотра наберите "show"')
print('Для удаления контакта из адресной книнги введите "delete"')
print('Для изменения контакта в адресной книге введите "change"')
print('Для поиска в адресной книге введите "search"')
print('Для добавления контакта в адресную книгу введите "add"')
print('Для завершения работы с адресной книгой введите "end"')

def user_info():

    while True:

        user_input = input('Введите требуемое действие: ')

        if user_input == 'show':
            if len(ab) == 0:
                print('Адресная книга пуста.')
            if len(ab) > 0:
                for name, adress in ab.items():
                    print('{0} : "{1}"'.format(name, adress))

        if user_input == 'delete':
            delete_adress = input('Введите имя для удаления: ')         
            del ab[delete_adress]
            print('{0} удален из адресной книги.'.format(delete_adress))       
         
        if user_input == 'add':
            add_name = input('Введите имя : ')
            add_adress = input('Введите адресс : ')
            add_adress = PDn(add_adress)
            ab[add_name] = add_adress
            print('{0} добавлен в адресную книгу'.format(add_name))

        if user_input == 'change':
            change_adress = input('Введите имя для изменения: ')
            new_adress = input('Введите новую адресную информацию: ')
            new_adress = PDn(new_adress)
            ab[change_adress] = new_adress
            print('Изменения {0} сохнанены с новой адресной информацией: {1} '.format(change_adress, new_adress))

        if user_input == 'search':
            search_name = input('Введите имя для поиска: ')
            for name, adress in ab.items():
                if name == search_name:       
                    print('{0} : {1}'.format(name, adress))

        if user_input == 'end':
            print('Работа  с адресной книгой завершена.')
            break

        else:
            pass
user_info()
    
ab_file = open('adress_book.data', 'wb')
pickle.dump(ab, ab_file)
ab_file.close()
