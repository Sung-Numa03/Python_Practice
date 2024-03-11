
"""
Made a variable x with the value of 5 and integer and also _rndText which is a string
"""

y = float(7)
z = str(9)



"""
print(x)
print(y)
print(z)
print(_rndText) #displaying "Hello World!"
"""
def _MyFunction():
    global x 
    x = int(5)
    global _rndText
    _rndText = "Hello World!"
    print(_rndText + " Python is fun")

_MyFunction()

print(_rndText )

for x in "banana":
    print(x)

txt = "The best things in life are free"
if "free" in txt:
    print(txt)

print("===========Loops=============")

print("===========For=============")
fruits = ["Melon", "Grape", "Avocado"]
for k in fruits:
    print(k)
    if "Banana" not in fruits:
        fruits.append("Banana")
    if k == "Banana":
        break
    if "Cherry" not in fruits:
        fruits.append("Cherry")

print(fruits)

print("===========Else In For=============")
for y in range(3, 50, 4):
    print(y)
else:
    print("Done looping")

print("===========While=============")

i = 1
n = 5
secret_word = 6
counter = 1

while True:
    word = input("Enter secret number: ")
    counter = counter + 1
    if word == secret_word:
        print(" You're correct😊")
        break
    if word != secret_word and counter > 7:
        print("you've used all your chances😂")
        break
