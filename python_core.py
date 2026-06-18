#-------------------------------------------------------section -1  (Defining functions)  ----------------------------------------------------

#Q1. Write a function called say_hello() that prints 'Welcome to Python!'
# def say_hello():
#     print("Welcome to Python")
# say_hello()

#Q2. Write a function called add(a, b) that returns the sum of two numbers.
# def add(a,b):
#     return a+b
# print(add(3,2))

#What is the output of a function that has no return statement? Write a function to verify this.
# def greet():
#     print("Hello!")
# set = greet()
# print(set)

#Q4. Write a function area_of_rectangle(length, width) that returns length * width. Call it with values 6 and 4.
# def area_of_rectangle(length,width):
#     print("Area of rectangle : ")
#     return length * width
# print(area_of_rectangle(6,4))

#Explain in your own words: why do we use functions instead of writing code directly?
#Firstly function means a block of code we use the functions for the reuse the code multiple times 



#    -----------------------------------------------  section - 2     (single and multi parameters)  ----------------------------------------------------



#single parameter 
# def fun2(a):
#     print(a)
#     return a
# sum=fun2(20)
# print(sum)

#multiparameter
# def fun2(a,b):
#     print(a+b)
#     return a * b
# demo=fun2(2,10)
# print(demo)

#Q1. Write a function multiply(a, b, c) that returns the product of three numbers

# def multiply(a,b,c):
#     return a*b*c
# product=multiply(10,20,30)
# print(product)

#Q2. Create a function describe_pet(animal, name) that prints: 'My [animal] is named [name].'
# def describe_pet(name="Zuro", animal="dog"):
#     print(f"My {animal} is named as {name}")
# describe_pet()

#Q3.What happens if you call a function with fewer arguments than parameters? Try it and note the error.
# def fun2(name,age):
#     print(f"my name is {name} and my age is {age}")
# fun2("arjun")


#Q4Write a function power(base, exponent) that returns base raised to exponent using the ** operator.
# def power(base,exponent):
#     return base ** exponent
# powell = power(2,3)
# print(powell)

#Q5Create a function full_name(first, middle, last) that returns the full name as a single string.

# def full_name(first,middle,last):
#     return f"{first}{middle}{last}"
# total = full_name("bala " , "venkata " , "durga")
# print(total)




#----------------------------------------------------    section - 3   (positional arguments)------------------------------------------------------

#Q1. Write a function intro(name, city, hobby) that prints a sentence about a person. Call it in two different orders and observe the difference.

# def intro(name,city,hobby):
#     print(f"Hello Good morning, my name is {name} and Ima from {city} adn my hobby is {hobby}")
# intro("Arjun","Vijayawada","Listening music")
# intro("Vijayawada","Arjun","Music")

#Q2. Create subtract(a, b) that returns a - b. What is the difference between subtract(10, 3) and subtract(3, 10)?
# def subtract(a,b):
#     return a - b
# print(subtract(10,3))
# print(subtract(3,10))


#Q3.What does 'positional' mean in 'positional arguments'? Write it in your own words.

#Positional means a certain position for the integer or any string or float that is , and positional arguments means we have giving certain positions in parameters for that when you call the function then you have to give the same type of the arguments meaning based then only it will give the correct output and main thing by calling wrong named arguments compiler does'nt give error but it will be change the meaning for a particular sentence.

#Write a function bio(first_name, last_name, age) and call it correctly using positional arguments.

# def bio(first_name,last_name,age):
#     print(first_name,last_name,age)
# bio("arjun","bommisetty",20)



#Can you pass more positional arguments than there are parameters? What error do you get?

#No we will get type error


#-----------------------------------------------Section-4(Keyword arguments)------------------------------------------

#Call the function send_email(to, subject, body) using keyword arguments in any order

#1) def send_email(to,subject,body):
#     print(f" This email is to {to} and it subjects {subject} , and body is {body}")
# send_email(subject = "coding questions",to = "arjun" , body = "out of the loop")


#2)Write a function create_profile(username, email, age) and call it using keyword arguments.
# def create_profile(username,email,age):
#     print(username,email,age)
# create_profile(username="arjun",age=18,email="arjun56@gmail.com")

#3)What is the error if you place a positional argument after a keyword argument? Test it.

# def intro(name, city, hobby):
#     print(name, city, hobby)
# intro(name="Arjun", "Vijayawada", "Music")

#4)Rewrite this call using keyword arguments: book_ticket('Alice', 'Delhi', 'Mumbai', 2)

# def book_tickets(name,city1,city2,number):
#     print(name , city1 , city2 , number)
# book_tickets(name ="arjun",city1 = "vijayawada", city2 = "hyderabad",number = 3)


#arbitary keyword arguments
# def fun2(**kwargs):
#     for key,value in kwargs.items():
#         print(key ,":", value)
# fun2(name = "arjun",character = "cool" ,age = 20 , status = "unmarried")


#--------------------------------------------------- Section-5 (Default parameters) -------------------------------------------------------------
# def default(name,message="good morning"):
#     print(f"{message},{name}")
# default("Arjun")
# default("Raju","Good afternoon")

#Q1. Write a function power(base, exponent=2) that returns base^exponent. Test with one and two arguments.
# def fun(base,exponent=2):
#     return base**exponent
# print(fun(6))
# print(fun(7,4))
# print(fun(9,4))

    
#Create a function connect(host, port=3306, protocol='TCP') and call it with various combinations.

# def connect(host,port=3306,protocol="TCP"):
#     print(f"{host},{port},{protocol}")
# connect("server")
# connect(host="google",port=5032,protocol="SAP")
# connect(host="cohost",port=8746,protocol="UDP")

#What is the SyntaxError in: def func(name='Guest', age)? Fix it.
# def func(name="Guest",age):
#     pass

#it means first it takes only default argument then after non default argument if we try to give non default argument in first it gives the syntax error
    


#Write a function discount_price(price, discount=10) that returns the discounted price. Test with and without the discount argument
# def discount_price(price,discount=10):
#     return price - (price * discount/100)
# print(discount_price(30))
# print(discount_price(50,25))

#Why would you use a default parameter instead of just hardcoding a value inside the function? Explain with an example.

#By using the default parameter when you write multiple satatemnets it gives the every time same default answer in multiple code line based on your printing statements in that after that by calling the function it takes the default value what you have given again you doesnot give in callinf function
# def default(name,age=20):
#     print(f"my name is {name} and my age is {age}")
# default("arjun")
# default("deva")



#-----------------------------------------------   section-6  (Arbitary parameters)   ---------------------------------------------------

#Postional agruments
# def add_all(*args):
#     sum = 0
#     for num in args:
#         sum = sum + num
#     return sum
# print(add_all(10,20,30,40,50))
# print(add_all(4,6,8,10,15))
# print(add_all(5,17,8,9,0))

#Keyword arguments
# def data(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key} : {value}")
# data(name="sukanya",age=21,address="vijYwada")


#Q1. Write a function multiply_all(*args) that returns the product of all numbers passed.

# def multiply_all(*args):
#     product = 1
#     for num in args:
#         product = product * num
#     return product
# print(multiply_all(1,2,3,4))


#Create a function display_tags(**kwargs) that prints each keyword-value pair on its own line.
# def display_tags(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key} : {value}")
# display_tags(name="arjun",time="5:29",month="june")


#Write a function describe_person(name, *hobbies) where name is a regular param and hobbies are collected into a tuple
# def describe_person(name,*hobbies):
#     print(name,hobbies)
# describe_person("arjun","playing","dancing","singing")

#What is the output of: def f(*args): print(type(args)) → f(1, 2, 3)? Explain why.
# def f(*args):
#     print(type(args))
# f(1,2,3)

#Write a function mixed(a, b, *args, **kwargs) and call it with at least 6 arguments. Print each part.

# def mixedargs(a,b,*args,**kwargs):
#     print(a,b,args,kwargs)
# mixedargs(2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,name="arjun",city="vijayawada",college="Amrita sai")




#-------------------------------------------------Section6(Functional refernces)--------------------------------------------------------

# def apply(func,value):
#     return func(value)
# def double(x):
#     return x*2
# def square(x):
#     return x*x
# print(apply(double,5))
# print(apply(square,5))



#Assign the built-in function len to a variable called count. Use it to find the length of a list.

# count = len
# numbers = [1,2,3,4,5,6,7,8]
# print(count(numbers))


#Write a function run_twice(func, value) that calls func on value twice and returns the final result.
# def run_twice(func,value):
#     return func(value) * 2
# run_twice("arjun",2)



#Store the functions upper, lower, and title (string methods) in a dictionary. Let the user choose which one to apply.

# operations = {
#     "upper": str.upper,
#     "lower": str.lower,
#     "title": str.title
# }
# text = input("Enter a string: ")
# choice = input("Choose upper, lower, or title: ")
# if choice in operations:
#     print(operations[choice](text))
# else:
#     print("Invalid choice")


#Write a function that returns another function. Example: make_multiplier(3) should return a function that multiplies any number by 3.

# def multiplier(x):
#     def multiply(y):
#         return x * y
#     return multiply
# times_3 = multiplier(3)
# print(times_3(5))
# print(times_3(10))


#Can you store the same function under multiple names in a dictionary? Test it and explain what happens.




# 
# k = input()
# for i in k:
#     if (lambda z : z not in "AEIOUaeiou")(i):
#         print(i)    

# x=lambda a,b:a+b
# print(x(10,20))

# m = lambda x,y,z : x * y + z
# print(m(10,20,30)) 


# s = lambda x,y,z,a : x + y * z // a
# print(s(10,20,30,40))

# def s(x):
#     print(x*5)
#     return x*5
# print(s(10))

# marks = [35,20,40,18,24,37]
# def check(m):
#     return m >= 25
# print(list(filter(check,marks)))


# marks = [35,20,40,18,24,37]
# print(list(filter(lambda  x : x >= 25 , marks)))

# sal = [35000,20000,40000,18000,37000,43000]
# print(list(map(lambda x : x + 2000 ,sal)))



#-----------------------------------------------------------------Section - 8--------------------------------------------------------------------------

#Q1. Write a lambda function that takes a number and returns its cube.
# s = lambda x : x ** 3
# print(s(10))


#Q2. Create a lambda that takes two numbers and returns the larger one using a conditional expression (x if x > y else y).
# larger = lambda x , y : y if y > x else x
# print(larger(30,28))


#Q3. Convert this regular function into a lambda: def even(n): return n % 2 == 0
# remainder = lambda x : x % 2 == 0
# print(remainder(20))

#Use a lambda with .sort() to sort this list of tuples by the second element:  [(1,'banana'),(2,'apple'),(3,'cherry')]

# fruits = [(1,'banana') , (2,'apple') , (3 ,'cherry')]
# fruits.sort(key = lambda x : x [1] )
# print(fruits)

#reduce ------ > is used for the sum of all numbers in a list and it will do all mathematical operations 
# from functools import reduce
# nums = [1, 2, 3, 4, 5]
# result = reduce(lambda x, y: x * y, nums)
# print(result)


#can lambda function call inside a another function
# def greet(name):
#     return "Hello " + name
# msg = lambda x: greet(x)
# print(msg("Arjun"))



#print vowels using map function
# l = ["Hello","hii","who","are","you"]
# k = []
# def fun(x):
#     if x not in "AEIOUaeiou":
#         return x
#     return ""
# for i in l:
#     s = list(map(fun,i))
#     s = "".join(s)
#     k.append(s)
# print(k)
# def fun2(y):
#     s = 0
#     for i in y:
#         s = s + ord(i)
#     return s
# A = list(map(fun2,k))
# print(A)


# l = [[1,2],[3,4],[5,6]]
# k = [1,2]
# print(k+[20])


