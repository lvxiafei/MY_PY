def find_diff_xor(str1, str2):
    if str1 is None or str2 is None:
        raise TypeError('str1 or str2 cannot be None')
    result = 0
    # print(ord(str1[1]))
    for char in str1:
        # print(ord(char)) # ord() ascii码
        result ^= ord(char)
    for char in str2:
        result ^= ord(char)
    return chr(result)

print(find_diff_xor('aab', 'ab'))