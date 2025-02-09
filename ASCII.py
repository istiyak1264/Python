#website: https://cryptohack.org/challenges/general/
# problem name: ASCII

lists = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
#declaring the flag as empty string
flag = ""
for i in lists:
    #chr() function converts ascii value to character value
    flag += chr(i)
#printing the flag
print(flag)



