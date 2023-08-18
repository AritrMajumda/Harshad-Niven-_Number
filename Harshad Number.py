n=int(input("enter the number= "))
k=n
s=0
while k>0:
    p=int(k%10)
    s=s+p
    k=int(k/10)
if(n%s==0):
    print(" harshad number ")
else:
    print("not harshad number ")