from itertools import permutations

def is_valid_solution(a, b, c, d, e, f, g, h, i, j):
    return (a * 1000 + b * 100 + c * 10 + d) + (e * 1000 + f * 100 + g * 10 + h) == (i * 10000 + j * 1000 + a * 100 + b * 10 + c)

def solve_cryptarithmetic():
    digits = range(10)
    for perm in permutations(digits, 10):
        a, b, c, d, e, f, g, h, i, j = perm
        if is_valid_solution(a, b, c, d, e, f, g, h, i, j):
            print(f"Solution: {a}{b}{c}{d} + {e}{f}{g}{h} = {i}{j}{a}{b}{c}")

solve_cryptarithmetic()
