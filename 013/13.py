
def read_file():
    fp = open('./in', 'r')
    content = []
    for line in iter(fp):
        line = line.strip("\n")
        content.append(line)
    fp.close()
    return content


def sum_up_large_int(n):
    content = read_file()
    ss = content[0]
    for i in range(1, len(content)):
        ss = sum_two_string(ss, content[i])
    return ss[:n]

def sum_two_string(a, b):
    if len(a) > len(b):
       b = ("0" * (len(a) - len(b))) + b
    carry = 0
    tt = ""
    for i in range(len(a) - 1, -1, -1):
        total = int(a[i]) + int(b[i]) + int(carry)
        print(total)
        s = total % 10
        carry = total // 10
        tt += str(s)
    if carry > 0:
        tt += str(carry)
    return tt[::-1]

print(sum_up_large_int())
