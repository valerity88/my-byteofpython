hello = 'Hello world!!!'
print('Исходная строка: {}'.format(hello))

def replace_def(string):

    a = input('Что меняем: ')
    b = input('На что меняем: ')
    string_new = ''
    
    for i in string:
        if i == a:
            i = b
        string_new += i
        
    print('Новая строка: {}'.format(string_new))
    
replace_def(hello)
