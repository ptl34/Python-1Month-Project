# Step 1: Read the file
with open('d:/hyper/Projects/chaki/Week-1/Task-1/input.txt', 'r') as file:
    lines = file.readlines()

# Step 2: Count lines and words
line_count = len(lines)
word_count = sum(len(line.split()) for line in lines)

# Step 3: Write to a new file
with open('d:/hyper/Projects/chaki/Week-1/Task-1/output.txt', 'w') as file:
    file.write(f"Number of lines: {line_count}\n")
    file.write(f"Number of words: {word_count}\n")

print("Done! Result written to output.txt")
