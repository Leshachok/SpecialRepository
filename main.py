array = [18, 20, 2, 88, 61, 17, 79, 97, 82]
print(array)
var = 0
index = 0
for x in range(len(array)):
    min = array[x]
    for y in range(x, len(array)):
        if (array[y] < min):
            index = y
            min = array[y]
            var = array[x]
    array[x] = min
    array[index] = var
print("result of 1 sort")
print(array)

array = [18, 20, 2, 88, 61, 17, 79, 97, 82]
print(array)
for x in range(len(array)):
    tempVar = array[x]
    j = x - 1
    while j >= 0 and array[j] > tempVar:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = tempVar
print("result of 2 sort")
print(array)
