# Code golf: Make a program that takes 2 intergers (-100 to 100) and gives their highest common factor.
# i.e.
# input: 20
# input: 15
# output: 5
# The only requirements are that the program takes 2 numbers and returns the highest common factor, 
# everything else is fair game. i.e. if you code returns 5 dogs that is still a valide result. 
# Also the program can continue to run after displaying the result.
# "display the result mean that someone could see the result in the terminal" //outdated

# Code golf: Find all possitive interger common factors of 2 numbers (including 1, and possable including one of the inputs).
# i.e.
# input1 18
# input2 12
# 1 2 3 6 
# or 
# input1 20
# input2 10
# 10 
# 5 
# 2 
# 1
# Any order or message works aslong as it is readable and does not contain other numbers, after the two inputs you can not put in more inputs.
# Goal is to use the least amount of chr (a blank line counts as one chr). The program must end when it is done printing numbers.


 # 3 lines, 78 chr, prints all from 1-inf
#a=input().split(",")
#print(a[0], a[1])
 # check is alius would make this better?

 # 4 lines, 80 chr, prints all from 1-inf
"""
c,d=int,input
a,b=c(d()),c(d())
for i in range(1,a+1):
 if a%i==b%i==0:print(i)
 """

"""
c()=int(input())
a,b=int(input()),int(input())
for i in range(1,a+1):
 if a%i==b%i==0:print(i)
 # check is alius would make this better?
 """



 # 3 lines, 78 chr, prints all from 1-inf
a,b=int(input()),int(input())
for i in range(1,a+1):
 if a%i==b%i==0:print(i)
 

 # 3 lines, 76 chr, prints all from 1-inf if first input is lower then second
"""
a,b=int(input()),int(input())
for i in range(1,a):
 if a%i==b%i==0:print(i)
 """

# maybe change to code for x in range...

# I know that using range in a for loop is bad but this is for code golf.
# maybe replace 101 with an input and use an alius


"""
try:
    #x = 2/0
    #x = 2 + "a"
    x = 1
except TypeError as a:
    print(a)
except ZeroDivisionError as a:
    print(a)
else:
    print("d")
finally:
    print("end")
"""

###################################################end of segment
#import math
"""def test1(a, b):
    if (a !=0):
        print("a"*int(100*math.sin(a/b)))
        test1(int(a/1.25), b)
a = int(input())
b = a
test1(a, b)

iii = 0.0
while iii < 10:
    print("e"*(20+int(20*math.sin(iii))))
    iii += 0.01"""