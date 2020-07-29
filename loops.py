title = "Green Lantern Corp"
# STOP = 10
# This next variable will increment
counter = 0

# Step 1
# while counter < STOP:
#     print(counter)
#     counter += 1

# Step 2
# while counter < len(title):
#     print(counter)
#     counter += 1

# Step 3
# while counter < len(title):
#     print(title[counter])
#     counter += 1

# Step 4
while counter < len(title):
    if(counter % 2) == 0:
        print(title[counter])
    counter += 1
