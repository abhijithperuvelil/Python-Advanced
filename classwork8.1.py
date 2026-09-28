# # #write a program to read a text file and displays the number of lines in a file
# f = open("k.txt", "r")
# lines = f.readlines()
# print("Number of lines =", len(lines))
# f.close()
# # #write a program to display the number of words in a file
# f=open("k.txt","r")
# lines=f.read()
# print(lines.split())
# print(len(lines))
# print("Number of Words",len(lines))
#f.close()
# # #write a program to update the second line in a file
# f = open("k.txt", "r")
# s = f.readlines()
# s[1] = "CSS\n"
# f.close()
# f = open("k.txt", "w")
# f.writelines(s)
# f.close()
# # #write a program to display the last 5 lines in a file
# f=open("k.txt","r")
# s=f.readlines()
# print(s[-5:])
# f.close()
# #program to search a particular word in a file
# f=open("k.txt","r")
# w=input("Enter the Word: ")
# s=f.read()
# if w in s:
#     print("Word Found")
# else:
#     print("Not Found")
#
#find the number of letters,digits,and spaces in a file
# f=open("k.txt","r")
# count_digit=0
# count_space=0
# count_alpha=0
# s=f.read()
# for i in s:
#     if i.isdigit():
#         count_digit+=1
#     elif i.isspace():
#         count_space+=1
#     elif i.isalpha():
#         count_alpha+=1
#     else:
#      print("Invalid")
# print("Number of Digits",count_digit)
# print("Number of space",count_space)
# print("Number of Alpha",count_alpha)
#reverse the lines in a file
f=open("k.txt","r")
s=f.readlines()
a=s[::-1]
f.close()
f=open("k.txt","w")
f.writelines(a)
f.close()
# A file totalstudents.txt contains the names of all students in a class,
# and a file passedstudents.txt contains the names of students who passed.txt the exam
# Write a Python program to:
# Read the names from both files.
# # Find the students who did not pass.
# # Write their names to a new file named failed_students.txt, one name per line.
# #
g=open("passed.txt")
f=open("total.txt","r")
s1=f.readlines()
s2=f.readlines()
h=open("failed.txt","w")
for i in s1:
    if i not in s2:
        h.write(i)
f.close()
g.close()
h.close()