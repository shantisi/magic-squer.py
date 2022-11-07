i=0
a=[]
while i<3:
    j=0
    d=[]
    while j<3:
        magic=int(input("enter no"))
        d.append(magic)
        j=j+1
    a.append(d) 
    i=i+1
i=0
rowsum=[]
colsum=[]
while i<len(a):
    j=0
    sum=0
    while j<len(a):
        sum=sum+a[i][j]
        # print(sum)
        j=j+1
    colsum.append(sum)
    j=0
    sum2=0
    while j<len(a):
        sum2=sum2+a[i][j]
        # print(sum2)
        j=j+1
    rowsum.append(sum2)
    i=i+1 
val=rowsum[0]
i=0
row_col_equal=True
while i<len(rowsum):
    if(rowsum[i]!=val or colsum[i]!=val):
        print("This is not a magic square")
        break
    i=i+1
if row_col_equal:
    row=0
    sum=0
    sum2=0
    while row<len(a):
        col=0
        while j<len(a):
            if row==col:
                sum=sum+a[row][col]
            if row+col==2:
                sum2=sum2+a[row][col]
            j=j+1
        i=i+1
    if sum==sum2:
        print(sum,"magic")

        

