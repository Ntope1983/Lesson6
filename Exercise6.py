# multidimensional arrays
List2x=[[1,2,3,4],[5,6,7,8],[8,9,10,11]]
print(List2x)
List2x.insert(0,[0,0,0,0])
print(List2x)
for rows in List2x:
    rows.append(1)
print(List2x)