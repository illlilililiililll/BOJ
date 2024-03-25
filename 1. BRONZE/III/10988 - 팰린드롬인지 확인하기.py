def palindrome(word):
    if len(word) <= 0:
        return '1'
    if word[0] == word[-1]:
        return palindrome(word[1:-1])
    else:
        return '0'
    
word = input()
print(palindrome(word))