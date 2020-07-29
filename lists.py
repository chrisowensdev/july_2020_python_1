power_rangers = ["Jason", "Trini", "Billy", "Zack", "Kim", "Tommy"]

count = 0
# print("WHILE LOOP")
# while count < len(power_rangers):
#     print(power_rangers[count])
#     count += 1


# FOR EVERY [needle] IN A [haystack]
# for ranger in power_rangers:
#     print(ranger)
#     if ranger == "Billy":
#         break


if "Tommy" in power_rangers:
    power_rangers.remove("Tommy")
    print(power_rangers)
else:
    print("IT'S MOPRHIN TIME!")
