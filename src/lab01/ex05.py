fio_input = input("ФИО: ").strip()
fio_parts = fio_input.split()
initials = "".join([part[0].upper() for part in fio_parts if part])
length = len(fio_parts[0]) + len(fio_parts[1]) + len(fio_parts[2])

print(f"Инициалы: {initials}.")
print(f"Длина (символов): {length}.")
