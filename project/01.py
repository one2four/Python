# condig:utf-8

# for i in range(1,5):
# 	for j in range(1,5):
# 		for k in range(1,5):
# 			if (i != j ) and ( i != j ) and ( j != k):
# 				print(i,j,k)

f = [1, 2, 3, 4]

for i in f:
    for j in f:
        for k in f:
            if (i != j) and (j != k) and (i != j):
                print(i, j, k)
