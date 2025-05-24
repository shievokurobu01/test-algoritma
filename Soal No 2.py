def pattern_count(text, pattern):
    if len(pattern) == 0 or len(pattern) > len(text):
        return 0
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count

# Contoh penggunaan:
print(pattern_count("palindrom", "ind"))     # Output: 1
print(pattern_count("abakadabra", "ab"))     # Output: 2
print(pattern_count("hello", ""))            # Output: 0
print(pattern_count("ababab", "aba"))        # Output: 2
print(pattern_count("aaaaaa", "aa"))         # Output: 5
print(pattern_count("hell", "hello"))        # Output: 0
