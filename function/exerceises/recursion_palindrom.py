def palindrome(word, index_value):
    if index_value == len(word)//2:
        return f"{word} is a palindrome"
    if not word[index_value] == word[len(word) - 1 - index_value]:
        return f"{word} is not a palindrome"
    return palindrome(word, index_value + 1)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
