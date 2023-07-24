def get_robbed_money(num_array: list) -> int:
    money, money2 = 0, 0
    for i in range(0, len(num_array) + 1 // 2, 2):
        money += num_array[i]
        if i + 1 != len(num_array):
            money2 += num_array[i + 1]
    if money > money2:
        return money
    return money2


try:
    nums_array = list(map(int, input("Enter money in each house separated by space : ").split()))
    print("The maximum robbed money is : ", get_robbed_money(nums_array))
except ValueError:
    print("Invalid Input. Please enter only integers")
