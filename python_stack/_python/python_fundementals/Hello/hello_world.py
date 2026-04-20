# 1
string1='Hello World'
print(string1)
print('Hello World')

#2
name = "Nesma"
print("Hello ", name + "!")
print("Hello " + name + "!")


#3
num = 16
print("Hello", num ,"!")
print("Hello "+ str(num) +" !") 
#print("Hello"+ num +"!")    #error

#4
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}.".format(fave_food1,fave_food2))    
print(f"I love to eat {fave_food1} and {fave_food2}.")    


#ninja 
test = "NesmaAhmadLubbad"
print(test.upper())
print(test.lower())
print(test.count("Nes"))
print(test.split("a"))
print(test.find("m"))
print(test.isalnum())
print(test.isalpha())
print(test.islower())
print(test.isdigit())
print(test.isupper())
