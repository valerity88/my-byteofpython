def reserve(text):
    forbidden = (' ', '!', '.', ',', '?',':', ';', '[', ']', '(', ')', '-')
    ForbiddenIndex = 0
    text = text.lower()
    while ForbiddenIndex < len(forbidden):
    
        if forbidden[ForbiddenIndex] in text:
            text = text.replace(forbidden[ForbiddenIndex], '')
        ForbiddenIndex += 1
    return text[::-1]

def is_palindrome(text):
    forbidden = (' ', '!', '.', ',', '?',':', ';', '[', ']', '(', ')', '-')
    ForbiddenIndex = 0
    text = text.lower()
    while ForbiddenIndex < len(forbidden):
    
        if forbidden[ForbiddenIndex] in text:
            text = text.replace(forbidden[ForbiddenIndex], '')
        ForbiddenIndex += 1
    return text == reserve(text)

something = input('Введите текст: ')
print(is_palindrome(something))
print(reserve(something))

if (is_palindrome(something)):
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")
