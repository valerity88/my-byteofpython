hello = 'Heollo world!!!'
print('Исходная строка: {}'.format(hello))

def replace_def(string):
    string = string
    a = input('Что меняем: ')
    b = input('На что меняем: ')
    i = 0
    j = 0
    string_new = ''
    string_new_1 = None
    while i < len(string):
        while j < len(a):
            if string[i] == a[j]:
                string_new += a[j]
                print(string_new)
                i = i+1
                j = j+1
                if string_new == a:
                    j = 0
                #string_new = string_new
                #print(string_new)
                #string_new_1 = string[0:(i - len(a))] + b + string[i:]
                
            #if string_new != a:
                #i += 1
                #j += 1
                #string_new = ''
                #print('NO')
        i += 1
        print(i)
        print(string_new)
        print(string_new_1)
        
        
        #if string[i] != a[j]:
        #    string_new = ''
        #    i += 1
        #    j = 0
       
    #print(string_new)
   
    
    #for i in string:
    #    string_new += i
    #    if string_new == a:
    #        string_new = b
         
      
    #print('Новая строка: {}'.format(string_new))

while True:    

    replace_def(hello)
