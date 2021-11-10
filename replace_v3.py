hello = 'Hello world!!!'
print('Исходная строка: {}'.format(hello))

def replace_def(string):

    a = input('Что меняем: ')
    b = input('На что меняем: ')
    string_new = ''
    
    for i in string:
        string_new += i
        if string_new == a:
            string_new = b
         
      
    print('Новая строка: {}'.format(string_new))

while True:    

    replace_def(hello)
