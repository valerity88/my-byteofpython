hello = 'Hellolo world and good luck!!!'
print('Исходная строка: {}'.format(hello))

def replace_def(string):
    string = string
    a = input('Что меняем: ')
    b = input('На что меняем: ')
    i = 0
    j = 0
    string_new = ''
    
    while i < len(string) and j < len(a):
        if string[i] != a[j]:
            string_new = ''
            j = 0
        if string[i] == a[j]:
            string_new += a[j]
            #print(string_new)
            j += 1
            
        if string_new == a:
            string_new = ''
            string = string[0:(i - (len(a))+1)] + b + string[(i+1):]
            #print('ok')
            j = 0
        i += 1   
 
        #print(i)
        #print(j)
        #print(string_new)
        #print(string)
    print('Новая строка: {}'.format(string))

while True:    

    replace_def(hello)
