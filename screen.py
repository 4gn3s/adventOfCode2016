class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = [["." for _ in range(width)] for _ in range(height)]
    
    def __repr__(self):
        return "\n".join(["".join([px for px in row]) for row in self.screen])
    
    def rect(self, a, b):
        for row in range(b):
            for col in range(a):
                self.screen[row][col] = "#"
                
    def rotate_row(self, row_index, by):
        self.screen[row_index] = self.screen[row_index][-by:] + self.screen[row_index][:-by]

    def rotate_col(self, col_index, by):
        prev = [self.screen[r][col_index] for r in range(self.height)]
        for r in range(self.height):
            self.screen[r][col_index] = prev[r - by]

def test():
    screen = Screen(8, 6)
    screen.rect(3, 2)
    screen.rotate_col(0, 2)
    screen.rotate_row(0, 1)
    screen.rotate_row(1, 3)
    print(screen)
    
    
test()
