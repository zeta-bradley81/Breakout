from turtle import Turtle


class BlocksAndBoards(Turtle):
    """bhf = bw = block width
    bwf=BLOCK_WIDTH_FACTOR,
    bhf = BLOCK_HEIGHT_FACTOR,
    bpr= blocks per row
    topy = TOP_Y
    rh = row height
    lx = Left x
     """
    def __init__(self, bhf, bpr, bw, bwf, lx, rh, topy):
        super().__init__()
        self.bhf = bhf
        self.bwf = bwf
        self.bpr = bpr
        self.bw = bw
        self.rh = rh
        self.lx = lx
        self.topy = topy
        self.hideturtle()
        self.pencolor(0, 0, 0)
        self.shapesize(bhf, bwf, outline=2)
        self.penup()
        # This creates a turtle object for each possible block (10 x 15 grid)
        self.block_dictionary = {}
        for r in range(0, 10):
            self.columns = []
            for c in range(0, self.bpr):
                self.columns.append(Turtle('square'))
            self.block_dictionary[r] = self.columns

    def hide_blocks(self):
        for a in range(0, 10):
            for b in range(0, self.bpr):
                self.block_dictionary[a][b].hideturtle()

    def show_blocks(self):
        for a in range(0, 10):
            for b in range(0, self.bpr):
                self.block_dictionary[a][b].showturtle()

    def level_1(self):
        starting_block_count = 0
        sv = 0
        y = self.topy
        level_1_colors = {0: (71, 78, 107), 1: (86, 116, 238), 2: (155, 175, 235), 3: (63, 72, 107), 4: (119, 131, 182)}
        for row_index in range(0, 10):
            if 4 <= row_index <= 9:
                x_pos = self.lx
                this_color = level_1_colors[row_index % 5]
                for col_index in range(0, self.bpr):
                    if 2 < col_index < 12:
                        self.block_dictionary[row_index][col_index].pencolor(0, 0, 0)
                        self.block_dictionary[row_index][col_index].shapesize(self.bhf, self.bwf, outline=2)
                        self.block_dictionary[row_index][col_index].fillcolor(this_color)
                        self.block_dictionary[row_index][col_index].penup()
                        self.block_dictionary[row_index][col_index].setpos(x_pos, y)
                        x_pos += self.bw
                        starting_block_count += 1

                    else:
                        self.block_dictionary[row_index][col_index].penup()
                        self.block_dictionary[row_index][col_index].setpos(1000, 1000)
                        x_pos += self.bw
            else:
                for col_index in range(0, self.bpr):
                    self.block_dictionary[row_index][col_index].penup()
                    self.block_dictionary[row_index][col_index].setpos(1000, 1000)
            y -= self.rh
            sv -= 1
        return starting_block_count

    def level_2(self):
        starting_block_count = 0
        sv = 0
        y = self.topy
        shift_value = 0
        level_2_colors = [(178, 34, 52), (255, 255, 255), (60, 59, 110)]
        for row_index in range(0, 10):
            x_pos = self.lx
            for b in range(0, self.bpr):
                if b <= row_index or b >= abs(row_index - 14):
                    self.block_dictionary[row_index][b].pencolor(0, 0, 0)
                    self.block_dictionary[row_index][b].shapesize(self.bhf, self.bwf, outline=2)
                    self.block_dictionary[row_index][b].fillcolor(level_2_colors[(b + shift_value) % 3])
                    self.block_dictionary[row_index][b].penup()
                    self.block_dictionary[row_index][b].setpos(x_pos, y)
                    x_pos += self.bw
                    starting_block_count += 1
                else:
                    self.block_dictionary[row_index][b].penup()
                    self.block_dictionary[row_index][b].setpos(1000, 1000)
                    x_pos += self.bw
            y -= self.rh
            sv -= 1
        return starting_block_count

    def single_column(self):
        y=self.topy
        for row_index in range(0, 10):
            if row_index <= 8:
                for col_index in range(0, self.bpr):
                    self.block_dictionary[row_index][col_index].goto(1000, 1000)
            else:
                for col_index in range(0, self.bpr):
                    if col_index == 7:
                        self.block_dictionary[row_index][col_index].pencolor(0, 0, 0)
                        self.block_dictionary[row_index][col_index].shapesize(self.bhf, self.bwf, outline=2)
                        self.block_dictionary[row_index][col_index].fillcolor('pink')
                        self.block_dictionary[row_index][col_index].penup()
                        self.block_dictionary[row_index][col_index].setpos(0, y)
                    else:
                      self.block_dictionary[row_index][col_index].goto(1000,1000)

            y -= self.rh
        return 1
