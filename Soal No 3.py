from collections import defaultdict

def count_letters(text):
    result = defaultdict(int)
    for char in text:
        if char.isalpha():
            result[char] += 1
    return dict(sorted(result.items()))

# Contoh penggunaan:
print(count_letters("Hello World"))
# Output: {'H': 1, 'W': 1, 'd': 1, 'e': 1, 'l': 3, 'o': 2, 'r': 1}

print(count_letters("Bismillah"))
# Output: {'B': 1, 'a': 1, 'h': 1, 'i': 2, 'l': 2, 'm': 1, 's': 1}

print(count_letters("MasyaAllah"))
# Output: {'A': 1, 'M': 1, 'a': 3, 'h': 1, 'l': 2, 's': 1, 'y': 1}
