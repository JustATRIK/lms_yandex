data, y = [x.strip().split(',') for x in open('top_youtube_channels_data.csv').readlines()], input()
data = list(filter(lambda x: x[-1] == y, data))
top = data[:3]
print(", ".join(map(lambda x: x[1], top)))
print(sum(map(lambda x: int(x[2]), top)))
print("; ".join(set(map(lambda x: x[-2], data))))
