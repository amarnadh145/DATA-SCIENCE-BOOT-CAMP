def count_vowels(word):
    count=0
    for i in word:
        if i in ['A','E','I','O','U', 'a','e','i','o','u']:
            count+=1
    return count
word=str(input())
print(count_vowels(word))