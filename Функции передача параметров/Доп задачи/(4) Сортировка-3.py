def sorting_triple(key, reverse):
    if key == 'len':
        data.sort(key=(lambda x: len(str(x))), reverse=reverse)
    else:
        data.sort(reverse=reverse)

# data = ["one", "two", "three"]
