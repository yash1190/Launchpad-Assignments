a = [1,1,2,3,4,64,35,93,35,87,4,3]
b = []
for i in a:
	if i not in b:
		b.append(i)
print(b)