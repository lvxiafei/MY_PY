from collections import defaultdict


def is_permutation(str1, str2):
    if str1 is None or str2 is None:
        return False
    if len(str1) != len(str2):
         return False
    unique_counts1 = defaultdict(int)
    print(unique_counts1)
    unique_counts2 = defaultdict(int)
    for char in str1:
        unique_counts1[char] += 1  # 默认为0
    for char in str2:
        unique_counts2[char] += 1
    print(unique_counts1)
    return unique_counts1 == unique_counts2

print(is_permutation('Nib', 'bin'))