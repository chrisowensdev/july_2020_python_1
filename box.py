# 1. Ask user width
width = int(input("Width? "))

# 2. Ask user height
height = int(input("Height? "))
horizontal_border = "*" * width

middle_array = []
count = 0
while count <= width:
    if count == 0 or count == width - 1:
        middle_array.append('*')
    else:
        middle_array.append(' ')
    count += 1
middle_string = ''.join(middle_array)

height_count = 0
while height_count <= height:
    if height_count == 0 or height_count == height:
        print(horizontal_border)
    else:
        print(middle_string)
    height_count += 1
