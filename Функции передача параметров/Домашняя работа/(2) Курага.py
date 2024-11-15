def dried_apricots(data):
    for i in range(len(data)):
        if apricots[i] / 2 >= data[i]:
            apricots[i] = 0
        else:
            apricots[i] = max(apricots[i], data[i])

# apricots = []
