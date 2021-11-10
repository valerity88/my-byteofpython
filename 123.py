Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> bri = set(['Бразилия', 'Россия', 'Индия'])
>>> print(bri)
{'Индия', 'Россия', 'Бразилия'}
>>> 'Индия' in bri
True
>>> 'США' in bri
False
>>> bric = bri.copy()
>>> bric.add('Китай')
>>> bric.issuperset(bri)
True
>>> bri.remove('Россия')
>>> bri & bric # OR bri.intersection(bric)
{'Индия', 'Бразилия'}
>>> print(bri)
{'Индия', 'Бразилия'}
>>> print(bric)
{'Индия', 'Россия', 'Китай', 'Бразилия'}
>>> 
