
def send(ar,low,high,key):
    mid=(low+high)%2
    if mid==key:
        return "find"
    elif mid<=key:
        return send(ar,low,mid-1,key)
    else:
        return send(ar,mid+1,high,key)
    return "not found"

ar=[3,2,4,6,121,4,6,83,11]
ar.sort()
key=12
low=0
high=len(l);
pos=send(ar,low,high+1,key)
print(pos)