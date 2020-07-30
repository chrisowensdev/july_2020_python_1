list1 = [2, 4, 5]
list2 = [2, 3, 6]
multiplied_list = []
product = []
count = 0
while count < len(list1):
    product.append(list1[count] * list2[count])
    count += 1

print(str(list1) + ' X ' + str(list2) + ' = ' + str(product))
