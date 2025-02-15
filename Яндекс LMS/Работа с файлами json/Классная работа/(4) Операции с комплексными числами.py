import json


with open('in.json', "r", encoding="utf-8") as f:
    data = list(map(lambda x: (x['Re'], x['Im']), json.loads(f.read())['complex']))
    res = {
        "complex": [
            {
                'Re': data[0][0] + data[1][0],
                'Im': data[0][1] + data[1][1]
            },
            {
                'Re': data[0][0] - data[1][0],
                'Im': data[0][1] - data[1][1]
            },
            {
                'Re': data[0][0] * data[1][0] - data[0][1] * data[1][1],
                'Im': data[0][0] * data[1][1] + data[0][1] * data[1][0]
            },
        ]
    }
    with open('out.json', "w", encoding="utf-8") as out:
        out.write(json.dumps(res))
