word = input()

middle_index = len(word) // 2

if len(word) % 2 != 0:
    print(word[middle_index])
else:
    print(word[middle_index - 1 : middle_index + 1])