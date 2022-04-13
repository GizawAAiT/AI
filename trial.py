
class num:
    def __init__(self,a,b,c=110):
        self.a=a
        self.b=b
        self.c=c
def add (w,*r):
    sum=w
    nn=num(3,4)
    sum+=nn.a
    sum+=nn.b
    sum+=nn.c
    for a in r:
        sum+=a
    return sum
print(add(3,2,2,2))