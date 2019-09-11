solution = [
    ["W", "2"],
    ["A", "0"],
    ["S", "4"],
    ["D", "1"],
    ["I", "5"],
    ["J", "8"],
    ["K", "6"],
    ["L", "3"],
    ["O", "7"],
    ["P", "9"]
]

crypt = [
    "WASD",
    "IJKL",
    "AOPAS"
]


def isCryptSolution(crypt, solution):
    solution_dict = {}

    for letter, number in solution:
        solution_dict[letter] = number

    word_1,  word_2, result = crypt

    word_1_number = ''.join(map(lambda key: solution_dict[key], word_1))
    word_2_number = ''.join(map(lambda key: solution_dict[key], word_2))
    result_number = ''.join(map(lambda key: solution_dict[key], result))

    if len(word_1_number) > 1 and word_1_number[0] == '0' \
            or len(word_2_number) > 1 and word_2_number[0] == '0' \
            or len(result_number) > 1 and result_number[0] == '0':
        return False

    return int(word_1_number) + int(word_2_number) == int(result_number)


print(isCryptSolution(crypt, solution))
