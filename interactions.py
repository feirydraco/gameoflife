from cell import Cell
from cellgrid import CellGrid
from tkinter import Tk, Frame, Button
import tkinter.messagebox
from random import randint
from popups import popupInput
board_height = 10
board_width = 10

def populate():
    x, y = randint(0, board_height - 2), randint(0, board_width - 2)
    cell = grid.grid[x][y]
    print(x, y)
    if cell.fill == False:
        cell.switch()
        cell.draw()

def clear():
    for i in range(board_height - 1):
        for j in range(board_width - 1):
            cell = grid.grid[i][j]
            if cell.fill == True:
                cell.switch()
                cell.draw()
            cell.fill == False
            
def numOfNeighbors(x, y):
    count = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            cell = grid.grid[i][j]
            if cell.fill == True and ((i >= 0 and j >= 0) and (i < board_height and j < board_width)):
                count += 1
    if grid.grid[x][y].fill == True:
        count -= 1
    return count

def update():
     temp = []
     for i in range(board_height - 2):
         temp.append(['0'] * board_width)

     for i in range(board_height - 2):
         for j in range(board_width - 2):
             cell = grid.grid[i][j]
             if cell.fill == True:
                 temp[i][j] = '1'
     for row in range(board_height - 1):
         "".join(temp[i])

gui = Tk()
gui.title = "Game of Life"
frame = Frame(gui)
frame.pack(side = "bottom")
RandomPopulate = Button(frame, text = "Populate", command = populate)
RandomPopulate.grid(row = 0, column = 0, rowspan = 2, sticky = "W", padx = (0, 0))
Next = Button(frame, text = "Next Generation", repeatdelay = 1, repeatinterval = 1, command = update)
Next.grid(row = 0, column = 1, sticky = "W")
Clear = Button(frame, text = "Clear Memory", command = clear)
Clear.grid(row = 0, column = 100, sticky = "E")
Exit = Button(frame, text = "Exit", command = lambda: gui.destroy())
Exit.grid(row = 0, column = 101, sticky = "E")
grid = CellGrid(gui, board_height, board_width, 20)
grid.pack()

gui.mainloop()