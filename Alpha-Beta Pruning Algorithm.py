

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.value = None

def alpha_beta(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or not node.children:
        return evaluate(node)

    if maximizing_player:
        max_eval = float('-inf')
        for child in node.children:
            eval = alpha_beta(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for child in node.children:
            eval = alpha_beta(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def evaluate(node):
   
    return node.state


if __name__ == "__main__":
    root = Node(100)
   
    result = alpha_beta(root, depth=3, alpha=float('-inf'), beta=float('inf'), maximizing_player=True)
    print("Optimal value:", result)
