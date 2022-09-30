def alternatingCharacters(s):
    deletions = 0
    pre = s[0]
    for curr in s[1:]:
        if pre == curr:
            deletions += 1
        pre = curr
    return deletions