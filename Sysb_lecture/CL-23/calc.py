# def calc(n1,n2,opr):
#     if opr == '+':
#         return n1+n2
#     elif opr == '-':
#         return n1-n2
#     elif opr == '*':
#         return n1*n2
#     elif opr == '/':
#         return n1/n2
#     else:
#         return "invalid"
    
# num1, num2 = map(int, input("input 2 number: ").split())
# sign = input("enter the operation + - * / : ")
# result = calc(num1,num2,sign)
# print(result)


# print("Use **kwargs to print student details")

# def std(**info):
#     print(info)

# std(name="rafi", age="25", addrs="dhaka")

print("Write a lambda that squares, cubes, and doubles numbers")

# def sqr(n):
#     return n**2

sqr = lambda n : n ** 2
cube = lambda n : n ** 3 
double = lambda n : n * 2
print(double(5))
print(cube(3)) 
print(sqr(3)) 