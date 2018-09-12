'''
Hw1.def
mohamad
9/12/2018
'''
def sum_ten_random_1_10_interval():
    sum_num = 0
    for count in range (10):
        randnums = random.randrange(1,10)
        sum_num = sum_num + randnums
        print(randnums, end='')
    print(sum_num)
main()
