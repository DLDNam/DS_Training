danh_sach = [1, 3, 5, 2, 4, 6, 8, 7, 9]
max = None

for i in danh_sach:
    if i % 2 == 0:
        if max is None or i > max:
            max = i

if max is not None:
    print(max)
else:
    print("Không có số chẵn trong danh sách")