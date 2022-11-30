#1
for i in range(1, 7):
    print(i, " ", i**2)
    
#alternatively:

def num(nums):
    for i in nums:
        print(i, " ", i**2)
num([1,2,3,4,5,6,7])

#Number 2:
def my_string(len_my_string):
    if len(len_my_string) == 0:
        print(f"\"\"{len_my_string}, is {len(len_my_string)} characters")
    else:
        print(f"{len_my_string} has {len(len_my_string)} characters")
my_string("")
my_string("jambo")
my_string("power learn project (plp)")

#Number 3

me_string = "Live Happily"
for i in me_string:
    print(i)
if len(me_string) == 0:
    print("Empty String")
else:
    print("i is out of range")

#altenatively
def m_stin(strin):
    for i in strin:
        print(i)
    if len(strin) ==0:
        print("empty string")
    else:
        print("i is out of range")