class TicTacToe:
    def __init__(self):
        self.ttt_dict = {
            'top_left': ' ', 'top_center': ' ', 'top_right': ' ',
            'mid_left': ' ', 'mid_center': ' ', 'mid_right': ' ',
            'btm_left': ' ', 'btm_center': ' ', 'btm_right': ' ',
        }

    # Display the tic-tac-toe board
    def print_board(self):
        print("+---+---+---+")
        print(f"- {self.get_colored_mark('top_left')} | {self.get_colored_mark('top_center')} | {self.get_colored_mark('top_right')} -")
        print("+---+---+---+")
        print(f"- {self.get_colored_mark('mid_left')} | {self.get_colored_mark('mid_center')} | {self.get_colored_mark('mid_right')} -")
        print("+---+---+---+")
        print(f"- {self.get_colored_mark('btm_left')} | {self.get_colored_mark('btm_center')} | {self.get_colored_mark('btm_right')} -")
        print("+---+---+---+")
   
    def get_colored_mark(self, position):
        mark = self.ttt_dict[position]
        if mark == 'X':
            return "\033[1;31mX\033[0m"  # Red color for X
        elif mark == 'O':
            return "\033[1;34mO\033[0m"  # Blue color for O
        else:
            return ' '  # Empty space
   
    def check_win_condition(self):
        win_conditions = [
            # rows
            ('top_left', 'top_center', 'top_right'),
            ('mid_left', 'mid_center', 'mid_right'),
            ('btm_left', 'btm_center', 'btm_right'),
            # columns
            ('top_left', 'mid_left', 'btm_left'),
            ('top_center', 'mid_center', 'btm_center'),
            ('top_right', 'mid_right', 'btm_right'),
            # diagonals
            ('top_left', 'mid_center', 'btm_right'),
            ('top_right', 'mid_center', 'btm_left'),
        ]

        for combination in win_conditions:
            if (self.ttt_dict[combination[0]] == self.ttt_dict[combination[1]] == self.ttt_dict[combination[2]]
                    and self.ttt_dict[combination[0]] != ' '):
                return True
        return False

    # to check the players draw or not
    def check_draw(self):
        for value in self.ttt_dict.values():
            if value == ' ':
                return False
        return True

    def player_move(self, current_player):
        if current_player == "X":
            number = 1
        elif current_player == "O":
            number = 2
        print(f"Hi, this is your turn, Player {number}")
        
        while True:
            choice = input(f"Please enter your move (e.g., 'top_left', 'mid_center'): ").strip()
            
            if choice in self.ttt_dict.keys() and self.ttt_dict[choice] == ' ':
                self.ttt_dict[choice] = current_player
                break
            else:
                print("Invalid choice. Try again.")
        
        if self.check_win_condition():
            self.print_board()
            print(f"Player {current_player} wins!")
            return True
        
        if self.check_draw():
            self.print_board()
            print("It's a draw!")
            return True
    
        return False

    def reset_board(self):
        for key in self.ttt_dict:
            self.ttt_dict[key] = ' '

    def tic_tac_toe(self):
        self.reset_board()
        print("\033[1;32m Please enter as below\n\033[0m")
        print("+----------+------------+-----------+")
        print("-\033[1;35m top_left\033[0m |\033[1;35m top_center\033[0m |\033[1;35m top_right\033[0m -")
        print("+----------+------------+-----------+")
        print("-\033[1;35m mid_left\033[0m |\033[1;35m mid_center\033[0m |\033[1;35m mid_right\033[0m -")
        print("+----------+------------+-----------+")
        print("-\033[1;35m btm_left\033[0m |\033[1;35m btm_center\033[0m |\033[1;35m btm_right\033[0m -")
        print("+----------+------------+-----------+\n")
       
        current_player = 'X'
        
        while True:
            self.print_board()
            
            if self.player_move(current_player):
                break
            
            current_player = 'O' if current_player == 'X' else 'X'

        choice = input("Do you want to play again? (y/n): ").strip().lower()
        if choice == "y":
            self.tic_tac_toe() 
        else:
            print("Thank you for playing!")

# Use .py files for traditional Python scripts that need to be executed or imported as modules in other scripts.
