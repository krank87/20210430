

year = int(input("請輸入西元年"))

data = [
    "rat",
    "ox",
    "tiger",
    "rabbit",
    "dragon",
    "snake",
    "horse",
    "sheep",
    "monkey",
    "rooster",
    "dog",
    "pig",

]
index = (year-2008)%12


print(data[index])
