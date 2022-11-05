# return masked string
def maskify(cc):
    length = len(cc)
    num_hash = length - 4
    first_hash = ""
    for hash in range(num_hash):
        first_hash += "#"
    rev_string = first_hash + cc[-4:]
    return rev_string
    # print(length)
    # print(length - 4)
    # print(first_hash)
    # print(len(first_hash))

# loop through each letter

# identify the last four strings and protect them
# slice these - from the back to the last four

# go thru the first portion and replace the letters/numbers with #
# count the number of letters are present


# other solutions
def maskify2(cc):
    return "#"*(len(cc)-4) + cc[-4:]


string = "645564654654561111"

print(maskify(string))
