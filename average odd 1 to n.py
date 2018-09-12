'''
lab1.def
mohamad
9/12/2018
'''
def average_odd_1_to_n(n):
    if (n % 2 == 0):
        print("invalid Imput")
        return -1
    sm = 0
    count = 0
    while (n >= 1):
        count = count + 1
        sm = sm + n
        n = n - 2
    return sm // count
What_is_n_string = input("what is n")
what_is_n_int = int(What_is_n_string)
sum = what_is_n_int
print(sum)
