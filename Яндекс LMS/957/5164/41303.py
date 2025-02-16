def epic_hero(arr, knight):
    if len(arr) == 0 or arr[0] >= knight:
        return [knight] + arr
    return [arr[0]] + epic_hero(arr[1:], knight)
