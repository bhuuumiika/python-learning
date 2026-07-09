Python Programs
Program 1
i=1
for i in range(21):
    print(i)
Program 2
j=20
while(j>0):
    print(j)
    j-=1
Program 3
N=100
sum=0
for k in range(1,N+1):
    sum+=k
print(sum)
Program 4
num=int(input())
def fact(a):
    if a==1:
        return 1
    else:
        return a*fact(a-1)
fact(num)
Program 5
fact1=1
while(num>0):
    fact1*=num
    num-=1
print(fact1)
Program 6
even=0
for i in range(1,101):
    if i%2==0:
        even+=1
print(even)
Program 7
string="string"
for s in string:
    print(s)
Program 8
set={1,2,3,4,5}
tuple=list(set)
for i in range(5):
    print(tuple[i])
print(type(tuple))
Program 9
num=int(input())
if num%2==0:
    print("even")
Program 10
def area(radius):
    return 3.14*radius**2
area(10)
Program 11
def largest(num1,num2):
    if(num1>num2):
        return num1
    else:
        return num2

num1,num2=map(int,input().split())
largest(num1,num2)
Program 12
def avg(a,b,c,d,e,f):
    sum=a+b+c+d+e+f
    return sum/5

avg(10,20,30,40,50,60)
Program 13
tup_le=("mango","apple","orange","grapes")
for i in tup_le:
    print(i)
#Program 14
print(tup_le[0],tup_le[-1])
print(len(tup_le))
set = {"mango","apple","orange","grapes"}
set.add("banana")
print(set)
set.remove("banana")
print(set)
dict1 = {"name":"John","age":30,"city":"New York"}
print(dict1["name"])
dict1.append({"course":"CSE"})

#TASK 1

students_name = input("Enter the name of the student: ")
dict2 = {}
for i in range (5):
    dict2[i] = int(input("Enter the marks of the student: "))
    