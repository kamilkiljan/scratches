def gen_postal_codes(sc, ec):
    """
    Return list of postal codes in range between
    given postal codes in format 'XX-XXX'.
    Params:
    - sc: start code (non-inclusive)
    - ec: end code (non-inclusive)
    """
    sn = int(sc[:2])*1000+int(sc[3:])
    en = int(ec[:2])*1000+int(ec[3:])
    return ['{0}-{1}'.format(str(x).zfill(5)[:2],
                             str(x).zfill(5)[2:]) for x in range(sn+1, en)]


def find_missing_numbers(nums, n_limit):
    """
    Return list of integers in range 1 to n_limit
    not present in the nums list.
    Params:
    - nums: list of numbers
    - n_limit: limit value (inclusive)
    """
    nums = set(nums)
    return_list = []
    for x in range(1, n_limit+1):
        if x not in nums:
            return_list.append(x)
    return return_list


def gen_decimals_in_range_with_steps(start=2, stop=5.5, step=0.5):
    """
    Generate list of decimals in selected range
    with defined step between them.
    Params:
    start - start of range
    stop - end of range (inclusive)
    step - incremented value
    """
    from decimal import Decimal
    return_list = []
    i = 0
    while start + i * step <= stop:
        return_list.append(Decimal(start + i * step))
        i += 1
    return return_list
