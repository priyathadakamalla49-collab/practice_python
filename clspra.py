# 1. Write a function to find the second largest number in a list.

# def secnum(a):
#     # a.sort(reverse = True)
#     # return a[1]
#     f = s = 0
#     for i in a:
#         if i > f:
#             s = f
#             f = i
#         elif i > s and i != f:
#             s = i
#     if s == 0:
#         print("No second highest")
#     return s

# a = list(map(int,input("Enter elements:").split()))   
# print(secnum(a))

# 2. Write a function to count uppercase and lowercase letters in a string.

# def countletters(s):
#     count_upper = 0
#     count_lower = 0
#     for i in range(0,len(s)):
#         if s[i].isupper():
#             count_upper += 1
#         elif s[i].islower():
#             count_lower += 1
#         else:
#             continue
#     return f"Uppercase in String:{count_upper},Lowercase in string:{count_lower}"
#     return 

# s = input("Enter String:")
# print(countletters(s))




# 3. Write a function to remove duplicate elements from a list.

def rem_dup(l):
    s = []
    for i in l:
        if i not in s:
            s.append(i)
    return s

l = list(map(int,input("Enter Elements").split()))
print(rem_dup(l))






# 4. Write a function to check if two strings are anagrams.
# 5. Write a function to find all prime numbers in a given range.

# def allprime(r):
#     allp = []
#     for i in range(1,r+1):
#         count = 0
#         for j in range(1,i+1):
#             if i % j == 0:
#                 count += 1
#         if count == 2:
#             allp.append(i)
#     return allp

# r = int(input("ENter range:"))
# print(allprime(r))


# 6. Write a function to return the frequency of each character in a string.
# 7. Write a function to find the longest word in a sentence.
# 8. Write a function to sort a list without using the built-in sort() method.
# 9. Write a function to check whether a number is an Armstrong number.
# 10. Write a function to merge two lists and remove duplicates.