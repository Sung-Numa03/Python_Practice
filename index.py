
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