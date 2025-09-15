class Rules:
    def __init__(self):
        pass

    def is_valid_move(self, start, end, dice_value, board):
        
        if not board[start]:
            return False
