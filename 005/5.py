from prime.prime_factor import prime_factor

def convert_to_dict(cur_list):
    cur_dict = {}
    for i in cur_list:
        if str(i) in cur_dict:
            cur_dict[str(i)] = cur_dict[str(i)] + 1
        else:
            cur_dict[str(i)] = 1
    return cur_dict


# we compare those 2 list,
# A is the final factors we want for calculate real answer
# B is the factors of certian number
# e.g. A: {1: 1, 2: 2, 3: 1, 5: 1}, B{2: 1, 3: 1}
# make sure A has larger or equal factor count for B

def compare_factors(final, current):
    for key, value in current.items():
        if key in final:
            if final[key] < value:
                final[key] = value
        if key not in final:
            final[key] = value
    return final


def get_product_from_all_factors(final):
    product = 1
    for key, value in final.items():
        product = product * (int(key) ** value)
    return product



def get_smallest_multiple(n):
    final_factors = {}
    for i in range(1, n+1):
        cur_factor_list = prime_factor(i)
        cur_factor_dict = convert_to_dict(cur_factor_list)
        compare_factors(final_factors, cur_factor_dict)
    return get_product_from_all_factors(all_factor_dict)

print(get_smallest_multiple(20))
