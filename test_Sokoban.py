from io import StringIO
from Sokoban import Input, State, Game
from tud_test_base import set_keyboard_input, get_display_output

"""
To your information - tests named approval fail with running
all the tests but if you test them one after other - tests pass.
The same situation is with State tests named move_left, move_right.
"""

matrix_to_be_modified = [
         ['x', 'x', 'x', 'x', 'x', 'x'],
         ['x', '_', 'P', 'S', 'O', 'x'],
         ['x', '_', '_', '_', '_', 'x'],
         ['x', '_', '_', '_', '_', 'x'],
         ['x', '_', '_', '_', '_', 'x'],
         ['x', '_', '_', '_', '_', 'x'],
         ['x', '_', '_', '_', '_', 'x'],
         ['x', '_', '_', '_', '_', 'x'],
         ['x', '_', '_', '_', '_', 'x'],
         ['x', '_', '_', '_', '_', 'x'],
         ['x', 'x', 'x', 'x', 'x', 'x']
         ]


# Class Input:

def test_input_move_up_return(monkeypatch):
    input = Input()
    player_input = StringIO('w')
    monkeypatch.setattr('sys.stdin', player_input)
    assert input.get_action() == 'move_up'


def test_input_move_down_return(monkeypatch):
    input = Input()
    player_input = StringIO('s')
    monkeypatch.setattr('sys.stdin', player_input)
    assert input.get_action() == 'move_down'


def test_input_move_left_return(monkeypatch):
    input = Input()
    player_input = StringIO('a')
    monkeypatch.setattr('sys.stdin', player_input)
    assert input.get_action() == 'move_left'


def test_input_move_right_return(monkeypatch):
    input = Input()
    player_input = StringIO('d')
    monkeypatch.setattr('sys.stdin', player_input)
    assert input.get_action() == 'move_right'


def test_input_r_as_return(monkeypatch):
    input = Input()
    player_input = StringIO('r')
    monkeypatch.setattr('sys.stdin', player_input)
    assert input.get_action() == 'restart'


def test_input_move_output():
    set_keyboard_input(['w'])
    input = Input()
    input.get_action()
    output = get_display_output()
    assert output == ["Enter the move: "]


def test_input_move_up_in(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "w")
    i = input("Enter the move: ")
    assert i == "w"


def test_input_approval_yes(monkeypatch):
    input = Input()
    player_input = StringIO('Y')
    monkeypatch.setattr('sys.stdin', player_input)
    assert input.approval() == 'Y'


def test_input_approval_no(monkeypatch):
    input = Input()
    player_input = StringIO('n')
    monkeypatch.setattr('sys.stdin', player_input)
    assert input.approval() == 'n'


def test_input_next_level_yes(monkeypatch):
    input = Input()
    player_input = StringIO('Y')
    monkeypatch.setattr('sys.stdin', player_input)
    assert input.next_level_approval() == 'Y'


def test_input_next_level_no(monkeypatch):
    input = Input()
    player_input = StringIO('n')
    monkeypatch.setattr('sys.stdin', player_input)
    assert input.next_level_approval() == 'n'


# Class State:


def test_state_matrix_get_current_level():
    matrix = State(matrix_to_be_modified)
    assert matrix.current_level() == [
         ['x', 'x', 'x', 'x', 'x', 'x'],
         ['x', '_', 'P', 'S', 'O', 'x'],
         ['x', '_', '_', '_', '_', 'x'],
         ['x', '_', '_', '_', '_', 'x'],
         ['x', '_', '_', '_', '_', 'x'],
         ['x', '_', '_', '_', '_', 'x'],
         ['x', '_', '_', '_', '_', 'x'],
         ['x', '_', '_', '_', '_', 'x'],
         ['x', '_', '_', '_', '_', 'x'],
         ['x', '_', '_', '_', '_', 'x'],
         ['x', 'x', 'x', 'x', 'x', 'x']
         ]


def test_state_player_position():
    matrix = State(matrix_to_be_modified)
    assert matrix.player_position() == (1, 2)


def test_state_move_up():
    matrix = State(matrix_to_be_modified)
    matrix.move('move_up')
    assert matrix.player_position() == (1, 2)


def test_state_move_down():
    matrix = State(matrix_to_be_modified)
    matrix.move('move_down')
    matrix.player_position() == (2, 2)


def test_state_move_left():
    matrix = State(matrix_to_be_modified)
    matrix.move('move_left')
    assert matrix.player_position() == (1, 1)


def test_state_move_right():
    matrix = State(matrix_to_be_modified)
    matrix.move('move_right')
    assert matrix.player_position() == (1, 3)


def test_state_player_cannot_move_S_right():
    mock_matrix = [
         ['x', 'x', 'x', 'x', 'x', 'x'],
         ['x', '_', 'P', 'S', 'S', 'x'],
         ['x', '_', '_', '_', '_', 'x'],
         ['x', 'x', 'x', 'x', 'x', 'x']
         ]
    matrix = State(mock_matrix)
    matrix.move('move_right')
    assert matrix.player_position() == (1, 2)


def test_state_player_cannot_move_S_left():
    mock_matrix = [
         ['x', 'x', 'x', 'x', 'x', 'x'],
         ['x', 'S', 'S', 'P', '_', 'x'],
         ['x', '_', '_', '_', '_', 'x'],
         ['x', 'x', 'x', 'x', 'x', 'x']
         ]
    matrix = State(mock_matrix)
    matrix.move('move_left')
    assert matrix.player_position() == (1, 3)


def test_state_player_cannot_move_S_up():
    mock_matrix = [
         ['x', 'x', 'x', 'x', 'x', 'x'],
         ['x', '_', '_', 'S', 'S', 'x'],
         ['x', '_', '_', 'P', '_', 'x'],
         ['x', 'x', 'x', 'x', 'x', 'x']
         ]
    matrix = State(mock_matrix)
    matrix.move('move_up')
    assert matrix.player_position() == (2, 3)


def test_state_player_cannot_move_S_down():
    mock_matrix = [
         ['x', 'x', 'x', 'x', 'x', 'x'],
         ['x', '_', '_', 'P', 'S', 'x'],
         ['x', '_', '_', 'S', '_', 'x'],
         ['x', 'x', 'x', 'x', 'x', 'x']
         ]
    matrix = State(mock_matrix)
    matrix.move('move_down')
    assert matrix.player_position() == (1, 3)


def test_state_is_finished_Flase():
    matrix = State(matrix_to_be_modified)
    assert matrix.is_finished() is False


def test_state_is_finished_True():
    mock_matrix = [
         ['x', 'x', 'x', 'x', 'x', 'x'],
         ['x', '_', 'P', 'S', '_', 'x'],
         ['x', '_', '_', '_', '_', 'x'],
         ['x', 'x', 'x', 'x', 'x', 'x']
         ]
    matrix = State(mock_matrix)
    assert matrix.is_finished() is True


# Class Game:

def test_game_how_may_levels():
    game = Game()
    assert game.how_many_levels() == 8
