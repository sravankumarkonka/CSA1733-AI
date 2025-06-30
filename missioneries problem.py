# Missionaries and Cannibals Problem

def is_safe(m, c):
    return (m == 0 or m >= c)

def solve_missionaries_cannibals(m, c, b, m_goal, c_goal, boat, path):
    if m == 0 and c == 0:
        print(path)
        return

    if is_safe(m, c) and is_safe(m_goal, c_goal):
        if boat == 'left':
            if m > 0:
                solve_missionaries_cannibals(m - 1, c, 'right', m_goal + 1, c_goal, 'left', path + ['M'])
            if c > 0:
                solve_missionaries_cannibals(m, c - 1, 'right', m_goal, c_goal + 1, 'left', path + ['C'])
            if m > 1:
                solve_missionaries_cannibals(m - 2, c, 'right', m_goal + 2, c_goal, 'left', path + ['MM'])
            if c > 1:
                solve_missionaries_cannibals(m, c - 2, 'right', m_goal, c_goal + 2, 'left', path + ['CC'])
            if m > 0 and c > 0:
                solve_missionaries_cannibals(m - 1, c - 1, 'right', m_goal + 1, c_goal + 1, 'left', path + ['MC'])
        else:
            if m_goal > 0:
                solve_missionaries_cannibals(m + 1, c, 'left', m_goal - 1, c_goal, 'right', path + ['M'])
            if c_goal > 0:
                solve_missionaries_cannibals(m, c + 1, 'left', m_goal, c_goal - 1, 'right', path + ['C'])
            if m_goal > 1:
                solve_missionaries_cannibals(m + 2, c, 'left', m_goal - 2, c_goal, 'right', path + ['MM'])
            if c_goal > 1:
                solve_missionaries_cannibals(m, c + 2, 'left', m_goal, c_goal - 2, 'right', path + ['CC'])
            if m_goal > 0 and c_goal > 0:
                solve_missionaries_cannibals(m + 1, c + 1, 'left', m_goal - 1, c_goal - 1, 'right', path + ['MC'])

# Initial conditions
missionaries = 3
cannibals = 3
solve_missionaries_cannibals(missionaries, cannibals, 'left', 0, 0, 'right', [])
