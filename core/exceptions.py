class BackgammonError(Exception):
    pass

class InvalidMoveError(BackgammonError):
    pass

class NoCheckerError(BackgammonError):
    pass

class GameOverError(BackgammonError):
    pass
