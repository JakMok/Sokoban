import copy
from levels import levels


class Input:
    """
    Class that represents player's input in the Sokoban game.
    :param input: while game is running,
    input is responsible for player's input
    :type input: str
    """

    def __init__(self, input=None):
        self.input = input

    def get_action(self):
        """
        Takes player's move and returns appropriate name of move.
        """
        move = input("Enter the move: ")
        if move in ['w', 's', 'a', 'd', 'r']:
            dict_of_action = {'w': 'move_up', 's': 'move_down',
                              'a': 'move_left', 'd': 'move_right',
                              'r': 'restart'
                              }
            return dict_of_action[move]
        else:
            return self.get_action()

    def approval(self):
        """
        Asks whether to start the game.
        """
        approval = input("Do you want to play? [Y/n] ")
        while approval not in ['Y', 'n']:
            return self.approval()
        return approval

    def next_level_approval(self):
        """
        Asks whether player wants to continue game on higher level.
        """
        approval = input("Great! Do you want to play on higher level? [Y/n] ")
        if approval not in ['Y', 'n']:
            return self.next_level_approval()
        else:
            return approval


class State:
    """
    Class that represents a state in the Sokoban game.
    :param level: level player plays on
    :type level: list
    """

    def __init__(self, level=None):
        self._matrix = level

    def current_level(self):
        """
        Returns current level.
        """
        return self._matrix

    def player_position(self):
        """
        Returns player position in matrix.
        """
        current_level = self._matrix
        for x in range(len(current_level)):
            for y in range(len(current_level[x])):
                if current_level[x][y] == 'P':
                    return x, y

    def move(self, move):
        """
        Modifies matrix according to player's move.
        """
        current_level = self._matrix
        line, index = self.player_position()
        if move == 'move_up':
            line_sign = -1
            index_sign = 0
        elif move == 'move_down':
            line_sign = 1
            index_sign = 0
        elif move == 'move_right':
            line_sign = 0
            index_sign = 1
        elif move == 'move_left':
            line_sign = 0
            index_sign = -1
        if current_level[line + 1*line_sign][index + 1*index_sign] == 'x':
            pass
        elif current_level[line + 1*line_sign][index + 1*index_sign] == 'S':
            if current_level[line + 2*line_sign][index + 2*index_sign] == 'x'\
                or\
                current_level[line + 2*line_sign][index + 2*index_sign] == 'S':
                pass
            else:
                current_level[line][index] = '_'
                current_level[line + 2*line_sign][index + 2*index_sign] = 'S'
                current_level[line + 1*line_sign][index + 1*index_sign] = 'P'
        elif current_level[line + 1*line_sign][index + 1*index_sign] == '_':
            current_level[line][index] = '_'
            current_level[line + 1*line_sign][index + 1*index_sign] = 'P'

    def display_matrix(self, matrix):
        """
        Prints current level in the termianl.
        """
        print(f"{chr(0x1B)}[2J")
        for element in matrix:
            print(element)

    def display_basic_matrix(self):
        """
        Prints basic matrix before player's first move.
        """
        matrix = self.current_level()
        for element in matrix:
            print(element)

    def is_finished(self):
        """
        Returns information whether player has already won.
        """
        numbers_of_O = 0
        for line in self._matrix:
            if 'O' in line:
                numbers_of_O += 1
        if numbers_of_O == 0:
            return True
        else:
            return False


class Game:
    """
    Class that initializes game in the Sokoban game.
    """

    def __init__(self, levels=None):
        self._levels = levels

    def get_levels(self):
        return self._levels

    def info(self):
        """
        Informs player how to move in the Sokoban game.
        """
        mess = "Welcome to Sokoban game!\n\
Player will move with using w, s, a, d keys.\n\
Using 'r' key the game will restart the current level."
        return print(mess)

    def how_many_levels(self):
        """
        Returns the count of levels.
        """
        number_of_levels = len(levels)
        return int(number_of_levels)

    def copied_matrix(self):
        index = self.level_index
        matrix = levels[index]
        copied_matrix = copy.deepcopy(matrix)
        return copied_matrix

    def game(self):
        """
        The mechanism of creating a game.
        """
        input = Input()
        game = Game()
        game.info()
        if input.approval() == 'Y':
            print(f"{chr(0x1B)}[2J")
            self.level_index = 0
            while self.level_index < self.how_many_levels():
                current_level = self.copied_matrix()
                matrix = State(current_level)
                matrix.display_basic_matrix()
                while matrix.is_finished() is False:
                    move = input.get_action()
                    if move == 'restart':
                        current_level = self.copied_matrix()
                        matrix.display_matrix(current_level)
                    else:
                        matrix = State(current_level)
                        matrix.move(move)
                        matrix.display_matrix(current_level)
                if input.next_level_approval() == 'n':
                    return print('Thank you for your time!')
                else:
                    print(f"{chr(0x1B)}[2J")
                    self.level_index += 1
            print(f"{chr(0x1B)}[2J")
            return print("We are so happy that such a player wants to play further\
 but you've already successfully completed the game.")
        else:
            print(f"{chr(0x1B)}[2J")
            return print('Thank you for your time!')


if __name__ == "__main__":
    game = Game()
    game.game()
