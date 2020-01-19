def read_file():
    content = []
    with open('./in') as f:
        content = f.read()
        content = [s.replace('"', "") for s in content.strip().split(",")]
        f.close()
        return content


def calc(ary):
    ary = sorted(ary)

    total = 0
    for i in range(0, len(ary)):
        ss = sum([(ord(c) - 64) for c in ary[i]]) * (i + 1)
        total += ss
        if i == 937:
            print(ss)
    return total


assert calc(read_file()) == 871198282
