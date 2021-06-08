ar=[5,8,4,6,9,2]
key=0
ans=0
for i in ar:
    if i==key:
        ans=1
        break
if ans==1:
    print("Found")
else:
    print("Not Found")

