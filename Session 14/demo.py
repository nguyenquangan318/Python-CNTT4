total = 10

def sum(first_num = 0, second_num = 0):
    '''Hàm tính tổng 2 số

    Args:
        first_num (int, optional): _description_. Defaults to 0.
        second_num (int, optional): _description_. Defaults to 0.

    Returns:
        int: Tổng đã tính được
    '''
    total = first_num + second_num
    print(f'Tổng của 2 số là: {total}')
    return total

return_value = sum(3,4)
print(total)