# coding:utf-8


# for i in range(-1000,1000):
#   for j in range(-1000,1000):
#       if (i+j)*(i-j)==168:
#           print(i,j)
#           x= i*i -100
# print(x)
for i in range(1, 85):
    if 168 % i == 0:
        j = 168 / i
        if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
            m = (i + j) / 2
            n = (i - j) / 2
            x = n * n - 100
            print(x)
