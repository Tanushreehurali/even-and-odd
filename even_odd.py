import sys

if len(sys.argv) > 1:
    script_name = sys.argv[0]
    numbers = [int(x) for x in sys.argv[1:]]
    print("User provided input numbers:")
else:
    script_name = sys.argv[0]
    numbers = [10, 15, 22, 33, 40]  # default values
    print("No input given — using default numbers:")


even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1


print("Script Name:", script_name)
print("Numbers:", numbers)
print("Even Count:", even_count)
print("Odd Count:", odd_count)
