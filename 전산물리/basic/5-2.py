cabinet = {3:"유재석", 100:"김태호"}
print((cabinet[3]))
print(cabinet[100])

print(cabinet.get(3))

print(cabinet[3])
print("hi")

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])
# 새손님
print(cabinet)
cabinet["A-3"] = "김종국" #유재석이 빠지고 김종국이 들어감
cabinet["C-20"] = "조세호"
print(cabinet)