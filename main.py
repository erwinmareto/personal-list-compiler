import pprint
import random

with open("codes.txt") as file:
    contents = file.readlines()

fave = [code for code in contents if "â˜†" in code or "â˜…" in code or "_" in code and type(code[0]) is int]
pprint.pprint(fave)

instant = [code for code in fave if "â˜†â˜…" in code]
print(instant)

basic = [code for code in fave if code not in instant]
print(basic)

unique = []
for numbers in contents:
    try:
        check = int(numbers[0])
        if 7 < len(numbers) <= 11 and numbers not in fave:
            if len(numbers) < 4:
                pass
            else:
                unique.append(numbers)
    except ValueError:
        pass

print(unique)

with open("favorites.txt", "w") as file:
    file.write("GOOD SHIT\n")
    for code in basic:
        if "â˜†" in code:
            file.write(f"{code}\n")
    for code in basic:
        if "â˜…" in code:
            file.write(f"{code}\n")
    file.write("INSTANT NUT\n")
    for code in instant:
        file.write(f"{code}\n")
    file.write("UNIQUE\n")
    for code in unique:
        file.write(f"{code}\n")

with open("instant.txt", "w") as file:
    for code in instant:
        file.write(f"{code}\n")

with open("unique.txt", "w") as file:
    for code in unique:
        file.write(f"{code}\n")

number_u = []
with open("random2.txt", "w") as file:
    for code in range(len(fave)):
        # print(random.randint(1, len(fave)))
        ran_val = random.randint(1, len(fave) - 1)
        if ran_val not in number_u:
            print(fave[ran_val])
            number_u.append(ran_val)
            file.write(f"{fave[ran_val]}\n")
        # else:
        #     print("dupe")
        # file.write(f"{fave[code]}\n")
print(number_u)




