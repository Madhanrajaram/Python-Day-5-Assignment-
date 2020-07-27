l1=[0,12,10,4,1,0,56,2,0,1,3,0,56,0,4]
l2=l1.sort()
l5=[]
l3=[]
l4=[]
for each in l1:
  if each==0:
    l3.append(each)
  else:
    l4.append(each)
    
l5=l4+l3
print(l5)