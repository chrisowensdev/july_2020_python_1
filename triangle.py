height = int(input("Enter a height? "))
count = 0
stars = 1
width_size = height * 2 - 1

while count < height:
    star = '*' * stars
    count += 1
    stars += 2
    print(star.center(width_size))
