nums=[[1, 2], "ab"]
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError("Список не может быть пустым")
    else:
        return min(nums), max(nums)
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    dict_nums=dict.fromkeys(nums)
    nums_un=list(dict_nums)
    nums_un.sort()
    return nums_un
def flatten(mat: list[list | tuple]) -> list:
    result = []
    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError("Ожидался список или кортеж")
        result.extend(row)
    return result
try:
    print(flatten(nums))
except TypeError as a:
    print(f"Ошибка: {a}")
print(unique_sorted(nums))
try:    
    min,max= min_max(nums)  
    print(f"min={min} max={max}")
except ValueError as e:
    print(f"Ошибка: {e}")