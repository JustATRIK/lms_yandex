def placeholder(*lines, **holders):
    d = {}
    for line in lines:
        line1 = line.replace('.', '').replace('!', '').replace(',', ' ').replace('?', '')
        line1 = line1.split()
        for holder in holders.values():
            holder1 = holder.split()
            if len(holder1) != len(line1):
                continue
            for i in range(len(holder1)):
                if '|_' in holder1[i]:
                    if not line1[i][0].isupper():
                        break
                    holder1[i] = holder1[i].replace('|', '')
                holder1[i] = holder1[i].replace('_', line1[i])
            if ' '.join(holder1) == line:
                d.setdefault(holder, []).append(line)
    return d
 