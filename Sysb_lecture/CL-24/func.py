def sum_avg(*nums):
    # add = sum(nums)
    # avrg = add / len(nums)
    # return add, avrg

    print(f"sum: {sum(nums)} \navg: {sum(nums)/len(nums)}")

my_tupl = map(int, input("Enter numbers: ").split())
sum_avg(*my_tupl)