def sort_mixed_array(arr):
    letters = sorted([x for x in arr if isinstance(x, str)])
    numbers = sorted([x for x in arr if isinstance(x, int)])
    return letters + numbers

data = [12, 9, 30, "A", "M", 99, 82, "J", "N", "B"]
print(sort_mixed_array(data))
# Output: ['A', 'B', 'J', 'M', 'N', 9, 12, 30, 82, 99]
