hello = 'Hello world!!!'
print('Исходная строка: {}'.format(hello))

def replace_def(string):

    a = input('Что меняем: ')
    b = input('На что меняем: ')
    string_new = ''
    for x in a:
        print(x)
        for y in b:
            print(y)
            x = y
            string_new += x
        
    print('Новая строка: {}'.format(string_new))
    
replace_def(hello)
