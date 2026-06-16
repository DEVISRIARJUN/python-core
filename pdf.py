
# nums = [12 , 15 , 7 , 18 , 20 , 21 , 25]
# k = list(filter(lambda x : (x % 3 ==0) ^ (x % 5 == 0) ,nums))
# print(k)

# nums = [1, 2, 3, 4, 5]
# k = sorted(lambda x,y: x+y, nums)
# print(k)

# a = [1,2,3,4]
# b = [10,20,30,40]
# k = list(map(lambda x,y : x+y, a,b))
# print(k)


# a = [1,2,3]
# b = [10,20,30,40]
# k = list(map(lambda x,y : x+y,a,b))
# print(k)


# nums = [12, 15, 7, 18, 20, 21, 25] 
# k = list(filter(lambda x : (x % 3 == 0) ^ (x % 5 == 0),nums))
# print(k)


# from functools import reduce
# nums = [1, 2, 3, 4] 
# k = reduce(lambda x,y : x+y,nums,10)
# print(k)



# nums = [[1, 2], [3, 4], [5, 6]] 
# result = list(map(lambda x: x.append(10), nums))
# print(result) 
# print(nums) 
# result1 = list(map(lambda x : x + [10],nums))
# print(result1)
# print(nums)


d = {"apple": 100, "banana": 40, "cherry": 150}
k = list(filter(lambda x : x>50 ,d.values()))
print(k)

