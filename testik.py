class SchoolMember:

    def __init__(self, name):
        self.name = name
        print('(Создан SchoolMember: {0})'.format(self.name))
t = SchoolMember('Mrs. Shrividya')
s = SchoolMember('Swaroop')
print(t)
print(s)
