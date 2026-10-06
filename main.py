



name = "KOKO"
num = 10

def func():
    global name
    name = "KOKO"
    print("local var: ", name)
    
func()
print("global var: ", name)

lang = "Python"

for a in lang:
    print(a)
    
x = ("Hello", "World", "Python")
print(len(x))

text = "Python is a popular programming language"
print("popular" in text)

print(len(text))
print(text[7:9])
print(text[10:17])
print(text.capitalize())
print(text.upper())
print(text.lower())


