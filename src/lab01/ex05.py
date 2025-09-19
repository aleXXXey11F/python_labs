fio_input = input().strip()
fio_parts = fio_input.split()
initials = ''.join([part[0].upper() for part in fio_parts if part])
length = len(fio_input)

print(f"Инициалы: {initials}.")
print(f"Длина (символов): {length}.")