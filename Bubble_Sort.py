def sort(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp


a=[3,21,4,2,6,8,23,9,53,5]
sort(a)
print(a)