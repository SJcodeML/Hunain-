a=hash("hello")
print(a)

# b=hash([1, 2])
# print(b)

str_a = "hello"
str_b = "hello"
print(str_a is str_b)


a = [10, 20, 30]
b = a
a.append(40)
a = [1, 2] 
print(a is b)
print(b is a )