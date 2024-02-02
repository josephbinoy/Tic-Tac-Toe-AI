import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel

from ai import *

class TicTacToeGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.board = [' '] * 9
        self.buttons = []
        self.initUI()

    def initUI(self):
        grid_layout = QGridLayout()

        button_size = 100 

        for i in range(9):
            button = QPushButton('', self)
            button.setFixedSize(button_size, button_size)
            button.clicked.connect(lambda _, i=i: self.on_button_click(i))
            font = button.font()
            font.setPointSize(30)
            button.setFont(font)
            self.buttons.append(button)
            grid_layout.addWidget(button, i // 3, i % 3)

        self.result_label = QLabel('', self)
        grid_layout.addWidget(self.result_label, 3, 0, 1, 3)

        self.setLayout(grid_layout)
        self.setWindowTitle('Tic-Tac-Toe')
        self.setGeometry(100, 100, 3 * button_size, 4 * button_size)
        self.show()

    def on_button_click(self, index):
        # Check if the cell is empty
        if self.board[index] == ' ':
            # Update the board with the player's move ('O')
            self.board[index] = 'O'
            self.buttons[index].setText('O')
            self.buttons[index].setEnabled(False)

            # Check for a winner
            result = self.check_winner()
            if result == 'You win!' or result == 'Computer wins!' or result == 'Draw':
                self.display_winner(result)
                self.disable_buttons()
            else:
                # Computer's move
                move = getComputerMove(self.board)
                self.board[move] = 'X'
                self.buttons[move].setText('X')
                self.buttons[move].setEnabled(False)

                # Check for a winner again
                result = self.check_winner()
                if result == 'You win!' or result == 'Computer wins!' or result == 'Draw':
                    self.display_winner(result)
                    self.disable_buttons()

    def disable_buttons(self):
        for button in self.buttons:
            button.setEnabled(False)

    def display_winner(self, winner_text):
        self.result_label.setText(winner_text)

    def check_winner(self):
        # Define the winning combinations
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]  # diagonals
        ]

        for combination in winning_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != ' ':
                return 'You win!' if self.board[combination[0]] == 'O' else 'Computer wins!'

        if ' ' not in self.board:
            return 'Draw'  # The game is a draw

        return False  # The game is still ongoing

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TicTacToeGUI()
    sys.exit(app.exec_())
