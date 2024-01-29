def max_squares(board):
    square_size = reset_square()
    for idx, col in enumerate(board):
        if col <= 1:
            break
        if col > len(board):
            return -1
        if col > 0:
            if square_size["rows"] == 0:
                init_square(col, square_size)
            else:
                if square_size["cols"] == col:
                    square_size["rows"] += 1
                elif square_size["cols"] != col:
                    square_size = reset_square()
                    init_square(col, square_size)
    return square_size["cols"]
def init_square(col, square_size):
    square_size["rows"] += 1
    square_size["cols"] = col

def reset_square():
    return {"rows": 0, "cols": 0}




