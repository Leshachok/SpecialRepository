array = [18, 20, 2, 88, 61, 17, 79, 97, 82]
print(array)
var = 0
index = 0
for x in range(len(array)):
    # елемент х беремо за мінімальний
    min = array[x]
    for y in range(x, len(array)):
        # якщо знаходимо менший, то min приймає це значення, запам`ятовуємо значення
        if array[y] < min:
            index = y
            min = array[y]
            var = array[x]
            # після того, як пройшли всі елементи після х, міняємо 	містами х та min (якщо min не є х)
    array[x] = min
    array[index] = var
print("result of 1 sort")
print(array)

array = [18, 20, 2, 88, 61, 17, 79, 97, 82]
print(array)
for x in range(1, len(array)):
    # array[x] будемо порівнювати с попередніми значеннями
    tempVar = array[x]
    j = x - 1
    # якщо попереднє значення більше за наступнє, воно записується  	в наступне
    while j >= 0 and array[j] > tempVar:
        array[j + 1] = array[j]
        j -= 1
        # коли знайшли менше значення, або дійшли до кінця списку, записали запам`ятоване значення tempVar в змінну
        # після меншого за tempVar значення
    array[j + 1] = tempVar
print("result of 2 sort")
print(array)