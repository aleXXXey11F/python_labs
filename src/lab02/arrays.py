nums=[1.0, 1, 2.5, 2.5, 0]
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
print(unique_sorted(nums))
try:    
    min,max= min_max(nums)  
    print(f"min={min} max={max}")
except ValueError as e:
    print(f"Ошибка: {e}")