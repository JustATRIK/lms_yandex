def print_cow():
    new = cow.copy()
    for i in range(len(cow)):
        if new[i] == cow:
            new[i] = cow.copy()
    print(new)

# cow = ['About', 'the', 'white', None, 'bull', None]
# cow[-1] = cow
# cow[3] = cow
