def get_digits():
    fp = open('./input.txt', "r")
    content = ""
    for line in iter(fp):
        print(line)
        content += line
    fp.close()
    return "".join(content.split("\n"))


def get_product(str):
    m = 1
    for i in range(0, len(str)):
        m *= int(str[i])
    return m


def max_product_in_a_series(n, data):
    return max([get_product(data[i:i+n]) for i in range(len(data) - n + 1) ])


print(max_product_in_a_series(13, get_digits()))
