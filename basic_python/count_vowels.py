def count_vowels(string):
    VOWELS = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for vowel in string.lower():
        if vowel in VOWELS:
            count += 1

    return count


print(count_vowels("Hello, World!"))
print(count_vowels("I love Python programming language"))
