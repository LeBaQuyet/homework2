string_maps = {
    "1": "abc",
    "2": "def",
    "3": "ghi",
    "4": "jkl",
    "5": "mno",
    "6": "pqrs",
    "7": "tuv",
    "8": "wxy",
    "9": "z"
}
s = input("Nhập 2 chữ số từ 1 đến 9: ")
# Kiểm tra độ dài và tính hợp lệ
if len(s) == 2 and s[0] in string_maps and s[1] in string_maps:
    for c1 in string_maps[s[0]]:
        for c2 in string_maps[s[1]]:
            print(c1 + c2)
else:
    print("Dữ liệu không hợp lệ!")
