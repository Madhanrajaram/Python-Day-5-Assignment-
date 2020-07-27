A =[10,20,40,60,70,80]
B = [5,10,15,25,35,45,60]
C=A+B
D=len(C)
j=0
while(j<D-1):
        if(C[j]>C[j+1]):
           a=C[j]
           C[j]=C[j+1]
           C[j+1]=a
           j=-1
        j+=1 
print(f" The Sorted numbers are: {C}")
    