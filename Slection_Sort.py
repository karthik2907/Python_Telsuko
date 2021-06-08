def sort(a):
    for i in range(len(a)-1):
        minpo=i
        for j in range(i,len(a)):
            if a[j]<minpo:
                minpo=j

        temp=a[i]
        a[i]=a[i+1]
        a[i+1]=temp
        print(a)


a=[3,21,4,2,6,8,23,9,53,5]
sort(a)
print(a)

