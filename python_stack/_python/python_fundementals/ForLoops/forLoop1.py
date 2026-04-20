
#1
for x in range (0,151,1):
    print(x)

#2
for x in range (5,101,5):
    print(x)

for x in range (5,101,1):
    if x%5==0:
     print(x)
     

#3
for x in range (1,101,1):
    if x%10==0:
     print("Coding Dojo")
    elif x%5==0:
        print("Coding")
    else :
      print(x)
      
      
#4
sum=0
for x in range (1,500001,2):
    sum=sum+x
print(sum)


sum=0
for x in range (0,500001,1):
    if x%2 != 0:
     sum=sum+x
print(sum)

#5
for x in range (2018,0,-4):
    if x>0:
     print(x)
     
#6
lowNum=2
highNum=9
mult=3
for x in range (lowNum,highNum+1,1):
    if x%mult==0:
        print(x)