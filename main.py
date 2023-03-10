import random

generated = []

def generate(index):
    generated.append(random.randint(0, 9))
    # check for the goofy ahh occurences
    # if generated[collumn * row] ==

for collumn in range(9):
    for row in range(9):
        generate(collumn * row)

print(generated)
print(len(generated))