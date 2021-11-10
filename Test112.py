class PDn:
    def __init__(self, adress_info):
        self.adress_info = adress_info
    def __str__(self):
        return self.adress_info
         
valerity_adress_info = PDn('1')
zakivalera_adress_info = PDn('2')
it_adress_info = PDn('3')
swaroop_adress_info = PDn('4')
larry_adress_info =  PDn('5')
matsumoto_adress_info = PDn('6')
spammer_adress_info = PDn('7')

ab = {'Valerity' : valerity_adress_info,
      'ZakiValera' : zakivalera_adress_info,
      'IT' : it_adress_info,
      'Larry' : larry_adress_info ,
      'Matsumoto' : matsumoto_adress_info,
      'Spammer' : spammer_adress_info}

print('Для удаления контакта из адресной книнги введите "delete"')

def user_info():
    user_input = input('Введите требуемое действие: ')
    if user_input == 'delete':
        delete_adress = input('Введите имя для удаления: ')               
        for name, adress in ab.items():
            if name == delete_adress:               
                print(adress)
                del adress
        del ab[delete_adress]
                
        print(ab)
        print(valerity_adress_info)

while True:
    user_info()
