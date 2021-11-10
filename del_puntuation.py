text = input('Введите слово')
forbidden = (' ', '!', '.', ',', '?',':', ';', '[', ']', '(', ')', '-')
ForbiddenIndex = 0
text_no_punct = None
while ForbiddenIndex < len(forbidden):
    
    if forbidden[ForbiddenIndex] in text:
        text = text.replace(forbidden[ForbiddenIndex], '')
    ForbiddenIndex += 1
print(text)

