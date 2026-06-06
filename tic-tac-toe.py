# /// script
# requires-python = ">=3.9"
# dependencies = ["textual"]
# ///

from textual import on
from textual.app import App
from textual.containers import Horizontal, Vertical, Container, Grid
from textual.widgets import (
    Footer,
    Header,
    Tree,
    Input,
    DataTable,
    Digits,
    Label,
    RichLog,
    Select,
    Button,
)

def tic_tac_toe_board():
    class Board(App):
        CSS_PATH = "tic-tac-toe.tcss"
        BINDINGS = [
    ("up", "move_up", ""),
    ("down", "move_down", ""),
    ("left", "move_left", ""),
    ("right", "move_right", ""),
    ("space", "select", "")
]
        def __init__(self, board_size: int):
            super().__init__()
            self.board_size = board_size
            self.row = 0
            self.col = 0
            self.buttons = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]

        def action_move_up(self):
            self.row = max(0, self.row - 1)
            self.highlight()


        def action_move_down(self):

            self.row = min(self.board_size - 1, self.row + 1)
            self.highlight()


        def action_move_left(self):

            self.col = max(0, self.col - 1)
            self.highlight()


        def action_move_right(self):

            self.col = min(self.board_size - 1, self.col + 1)
            self.highlight()


        def action_select( self):

            button = self.buttons[self.row][self.col]
            button.label = "X"

        def compose(self):
            with Grid(id="board") as grid:
                grid.styles.grid_size_columns = self.board_size
                grid.styles.grid_size_rows = self.board_size

                for r in range(self.board_size):
                    for c in range(self.board_size):
                        btn = Button("", classes="cell")
                        self.buttons[r][c] = btn
                        yield btn


        def on_mount(self):
            board = self.query_one("#board", Grid)
            board.styles.grid_size_columns = self.board_size
            board.styles.grid_size_rows = self.board_size
            self.highlight()

        def highlight(self):
            for row in self.buttons:
                for btn in row:
                    btn.remove_class("selected")

            self.buttons[self.row][self.col].add_class("selected")

    Board(4).run()

tic_tac_toe_board()