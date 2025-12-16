# input [56,54,100,35,83,81,100,66,93,81,79,67,100,50,74,59,100,61,37,60]

# score = [56,54,100,35,83,81,100,66,93,81,79,67,100,50,74,59,100,61,37,60]

# centum=0
# for mark in score:
#     if mark==100:
#        centum+=1

# print(centum)

# for mark in score:

#     mark = int(input("Enter the mark :"))

    
#     if mark>=90:
#      print("Grade A")
#     elif mark>=80:
#        print("Grade B")
#     elif mark>=60:
#        print("Grade C")
#     else:
#        print("Grade D")


# # count_90=0
# count_80=0
# count_60=0
# count_59=0
# for mark in score:    
#     if mark>=90:
#      count_90+=1
# print("Number of 90s : ",count_90)
#         if mark>=80 and mark<=90:
#                 count_80+=1
# print("Number of 80s : ",count_80)

#     if mark>=60 and mark<=80:
#                 count_60+=1
# print("Number of 60s : ",count_60)

# numbers = [1,2,3]
# reverselist=[]
# for numbers in range(3,0,-1):
#     reverselist.append(numbers)
# print(reverselist)

# numbers=[1,2,3,4,5]
# doublenumbers=[]
# for num in numbers:    
#     num=num*2    
#     doublenumbers.append(num)
# print(doublenumbers)

num=[1,2,3,4,5]
n = 3
for y in range(n):
    last = num[-1]    
    for x in range(len(num)-1,0,-1):
       num[x]= num[x-1]
    num[0]=last

print(num)
