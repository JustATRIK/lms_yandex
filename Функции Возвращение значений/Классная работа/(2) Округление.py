def rounding(data):
	res1, res2 = 0, 0
	for i in data:
        res1 += int(i)
    	res2 += int(str(i).split('.')[1])
    return res1, res2
    