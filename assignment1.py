x = [1, 2, 3, 4, [10, 20, 30, 40, [100, 200, 300, 400], "riyazulhaque", 5 + 5j], 4000]

# 1)
k = x[4]
print(k[0:2])
# 2)
print(k[6])
# 3)
a = k[4]
print(a[2:4])
# 4)
print(k[3:6])


# program to print the pairs whose sum is even
my = []
for i in range(0, 21):
    for j in range(0, 21):
        if (i + j) % 2 == 0:
            my.append([i, j])

for i in my:
    for j in my:
        if i[0] == j[1] and j[0] == i[1]:
            my.remove(j)
print(my)

# frequency of special characters

special = '!','@','#','$','%','^','&','*'
freq ={}
x = 'hello&!@#world'

freq= dict([(i, x.count(i)) for i in special])
print(freq)

#list of number with a cube of odd numbers from 1-50
x = []
for i in range(1, 50):
    if i % 2 != 0:
        x.append(i * i * i)
print(x)


# all elements multiplied by 3
my = [1, 2, 3, 4, 5, 6]
multiple = []
for i in my:
    multiple.append(i * 3)
print(multiple)
#print(my)



#length of each word
x = "Hello my name is chinmai"
for i in x.split():
    print("Length of", i, "is:", len(i))




#true if only integers
x = [1, 2, 5,'ff']
def torf(lst):
    for i in x:
        try:
            u = int(i)
            re = True
        except:
            re = False
    print(re)



# def flatten(lst):
#    for x in lst:
#        if isinstance(x, list):
#            for x in flatten(x):
#                yield x
#        else:
#            yield x


# print(list(flatten(x)))
