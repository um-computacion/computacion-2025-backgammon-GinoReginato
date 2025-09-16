class Rules:
    def __init__(self):
        pass

    def is_valid_move(self, start, end, dice_value, board):
        
        if not board[start]:
            return False

        if len(board[end]) > 1 and board[end][0] != board[start][0]:
            return False

        if abs(end - start) != dice_value:
            return False

        return True