arrayNum = input("Введите количество элементов массива")
aray=[]
for x in range(0, int(arrayNum)):
    arrayInput = input("Введите значение элемента ")
    aray.append(arrayInput)

print("Что вы хотите сделать с массивом?")
print("1 -- Максимальные значения")
print("2 -- Dывод элементов по введенным индексам и их произведение")
messageChoice = input("Ваш выбор :")
if messageChoice == "1":
    messageAdd = input("Введите количество максимальных чисел :")
    dataSort = sorted(aray, key=int, reverse=True)
    dataSort = dataSort[:int(messageAdd)]
    print(dataSort)
elif messageChoice == "2":
    whileStop='n'
    messageAdd = ''
    while whileStop != 'y':
        newdata=input("Введите номер элемента")
        print(aray[int(newdata)])
        whileStop=input("Все? [y/n]")




