#1..WAP to check whether an element exists within a tuple
t=tuple(eval(input()))
n=int(input())
for i in t:
    if i==n:
        print("element found")
        break
else:
    print("not found")
#2..WAP to find repeated elements in tuple
t=tuple(eval(input()))
s=()
for i in t:
    if i not in s:
        if t.count(i)>1:
            print(i)
        s+=(i,)
#3..WAP to remove an element from a tuple
t=tuple(eval(input()))
n=int(input())
t1=()
for i in t:
    if i==n:
        continue
    else:
        t1+=(i,)
print(t1)
#4..WAP to reverse a tuple
t=tuple(eval(input()))
print(t[::-1])
#5..WAP to print maximum element in a tuple
t=tuple(eval(input()))
a=sorted(t)
print(a[-1])
#6..WAP to print sum of elements of a tuple
t=tuple(eval(input()))
s=0
for i in t:
    s+=i
print(s)

