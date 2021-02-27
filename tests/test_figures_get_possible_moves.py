import unittest
from game.field import *
from game.figures import *


class PossibleMovesKing(unittest.TestCase):
    def test_king_moves_possible_up(self):
        field = Field(beginning=True, empty=False, field=None)
        field.points[3][1] = Empty(pos=(3, 1))
        king = field.points[3][0]
        moves = king.get_possible_moves(field.points)
        self.assertEqual([{"start": (3, 0), "end": (3, 1)}], moves)

    def test_king_moves_possible_up_left_right(self):
        field = Field(beginning=True, empty=False, field=None)
        field.points[3][1] = Empty(pos=(3, 1))
        field.points[2][0] = Empty(pos=(2, 0))
        field.points[4][0] = Empty(pos=(4, 0))
        king = field.points[3][0]
        moves = king.get_possible_moves(field.points)
        self.assertEqual(3, len(moves))
        self.assertIn({"start": (3, 0), "end": (3, 1)}, moves)
        self.assertIn({"start": (3, 0), "end": (4, 0)}, moves)
        self.assertIn({"start": (3, 0), "end": (2, 0)}, moves)

    def test_king_moves_enemies_arround_everywhere(self):
        field = Field(beginning=True, empty=False, field=None)
        field.points[3][0] = Pawn(color="w", pos=(3, 0))
        field.points[2][0] = Pawn(color="w", pos=(2, 0))
        field.points[4][0] = Pawn(color="w", pos=(3, 0))
        field.points[2][1] = Pawn(color="w", pos=(2, 1))
        field.points[4][1] = Pawn(color="w", pos=(4, 1))
        field.points[3][2] = Pawn(color="w", pos=(3, 2))
        field.points[2][2] = Pawn(color="w", pos=(2, 2))
        field.points[4][2] = Pawn(color="w", pos=(3, 2))
        field.points[3][1] = King(color="b", pos=(3, 1))
        king = field.points[3][1]
        moves = king.get_possible_moves(field.points)
        self.assertEqual(8, len(moves))
        self.assertIn({"start": (3, 1), "end": (2, 0)}, moves)
        self.assertIn({"start": (3, 1), "end": (3, 0)}, moves)
        self.assertIn({"start": (3, 1), "end": (4, 0)}, moves)
        self.assertIn({"start": (3, 1), "end": (2, 1)}, moves)
        self.assertIn({"start": (3, 1), "end": (4, 1)}, moves)
        self.assertIn({"start": (3, 1), "end": (2, 2)}, moves)
        self.assertIn({"start": (3, 1), "end": (3, 2)}, moves)
        self.assertIn({"start": (3, 1), "end": (4, 2)}, moves)

    def test_king_moves_empty_arround_everywhere(self):
        field = Field(beginning=True, empty=False, field=None)
        field.points[3][0] = Empty(pos=(3, 0))
        field.points[2][0] = Empty(pos=(2, 0))
        field.points[4][0] = Empty(pos=(3, 0))
        field.points[2][1] = Empty(pos=(2, 1))
        field.points[4][1] = Empty(pos=(4, 1))
        field.points[3][2] = Empty(pos=(3, 2))
        field.points[2][2] = Empty(pos=(2, 2))
        field.points[4][2] = Empty(pos=(3, 2))
        field.points[3][1] = King(color="b", pos=(3, 1))
        king = field.points[3][1]
        moves = king.get_possible_moves(field.points)
        self.assertEqual(8, len(moves))
        self.assertIn({"start": (3, 1), "end": (2, 0)}, moves)
        self.assertIn({"start": (3, 1), "end": (3, 0)}, moves)
        self.assertIn({"start": (3, 1), "end": (4, 0)}, moves)
        self.assertIn({"start": (3, 1), "end": (2, 1)}, moves)
        self.assertIn({"start": (3, 1), "end": (4, 1)}, moves)
        self.assertIn({"start": (3, 1), "end": (2, 2)}, moves)
        self.assertIn({"start": (3, 1), "end": (3, 2)}, moves)
        self.assertIn({"start": (3, 1), "end": (4, 2)}, moves)

class PossibleMovesPawn(unittest.TestCase):
    def test_pawn_move_blocked_black(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[3][1] = Pawn(color="b", pos=(3, 1))
        field.points[3][2] = Pawn(color="w", pos=(3, 2))
        pawn = field.points[3][1]
        moves = pawn.get_possible_moves(field.points)
        self.assertEqual([], moves)

    def test_pawn_all_moves_possible_black(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[3][1] = Pawn(color="b", pos=(3, 1))
        field.points[4][2] = Pawn(color="w", pos=(4, 2))
        field.points[2][2] = Pawn(color="w", pos=(2, 2))
        pawn = field.points[3][1]
        moves = pawn.get_possible_moves(field.points)
        self.assertEqual(4, len(moves))
        self.assertIn({"start": (3, 1), "end": (3, 2)}, moves)
        self.assertIn({"start": (3, 1), "end": (3, 3)}, moves)
        self.assertIn({"start": (3, 1), "end": (4, 2)}, moves)
        self.assertIn({"start": (3, 1), "end": (2, 2)}, moves)

    def test_pawn_move_blocked_white(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[3][5] = Pawn(color="b", pos=(3, 5))
        field.points[3][6] = Pawn(color="w", pos=(3, 6))
        pawn = field.points[3][6]
        moves = pawn.get_possible_moves(field.points)
        self.assertEqual([], moves)

    def test_pawn_move_all_possible_white(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[2][5] = Pawn(color="b", pos=(2, 5))
        field.points[4][5] = Pawn(color="b", pos=(4, 5))
        field.points[3][6] = Pawn(color="w", pos=(3, 6))
        pawn = field.points[3][6]
        moves = pawn.get_possible_moves(field.points)
        self.assertEqual(4, len(moves))
        self.assertIn({"start": (3, 6), "end": (2, 5)}, moves)
        self.assertIn({"start": (3, 6), "end": (4, 5)}, moves)
        self.assertIn({"start": (3, 6), "end": (3, 5)}, moves)
        self.assertIn({"start": (3, 6), "end": (3, 4)}, moves)

class PossibleMovesKnight(unittest.TestCase):
    def test_knight_move_all_possible(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[4][4] = Knight(color="b", pos=(4, 4))
        knight = field.points[4][4]
        moves = knight.get_possible_moves(field.points)
        self.assertEqual(8, len(moves)
                )
        self.assertIn({"start": (4, 4), "end": (2, 3)}, moves)
        self.assertIn({"start": (4, 4), "end": (2, 5)}, moves)
        self.assertIn({"start": (4, 4), "end": (6, 3)}, moves)
        self.assertIn({"start": (4, 4), "end": (6, 5)}, moves)
        self.assertIn({"start": (4, 4), "end": (3, 2)}, moves)
        self.assertIn({"start": (4, 4), "end": (5, 2)}, moves)
        self.assertIn({"start": (4, 4), "end": (3, 6)}, moves)
        self.assertIn({"start": (4, 4), "end": (5, 6)}, moves)

    def test_knight_move_left_upper_part(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[1][1] = Knight(color="b", pos=(1, 1))
        knight = field.points[1][1]
        moves = knight.get_possible_moves(field.points)
        self.assertEqual(4, len(moves)
                )
        self.assertIn({"start": (1, 1), "end": (3, 0)}, moves)
        self.assertIn({"start": (1, 1), "end": (3, 2)}, moves)
        self.assertIn({"start": (1, 1), "end": (2, 3)}, moves)
        self.assertIn({"start": (1, 1), "end": (0, 3)}, moves)

    def test_knight_move_left_upper_wall(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[0][0] = Knight(color="b", pos=(0, 0))
        knight = field.points[0][0]
        moves = knight.get_possible_moves(field.points)
        self.assertEqual(2, len(moves)
                )
        self.assertIn({"start": (0, 0), "end": (1, 2)}, moves)
        self.assertIn({"start": (0, 0), "end": (2, 1)}, moves)

    def test_knight_move_right_lower_part(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[6][6] = Knight(color="b", pos=(6, 6))
        knight = field.points[6][6]
        moves = knight.get_possible_moves(field.points)
        self.assertEqual(4, len(moves)
                )
        self.assertIn({"start": (6, 6), "end": (4, 7)}, moves)
        self.assertIn({"start": (6, 6), "end": (4, 5)}, moves)
        self.assertIn({"start": (6, 6), "end": (5, 4)}, moves)
        self.assertIn({"start": (6, 6), "end": (7, 4)}, moves)

    def test_knight_move_right_upper_wall(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[7][7] = Knight(color="b", pos=(7, 7))
        knight = field.points[7][7]
        moves = knight.get_possible_moves(field.points)
        self.assertEqual(2, len(moves)
                )
        self.assertIn({"start": (7, 7), "end": (5, 6)}, moves)
        self.assertIn({"start": (7, 7), "end": (6, 5)}, moves)

    def test_knight_move_partially_blocked_by_own_figures(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[2][1] = Knight(color="b", pos=(2, 1))
        field.points[4][0] = Pawn(color="b", pos=(4, 0))
        field.points[0][2] = Pawn(color="b", pos=(0, 2))
        field.points[1][3] = Pawn(color="b", pos=(1, 3))
        knight = field.points[2][1]
        moves = knight.get_possible_moves(field.points)
        self.assertEqual(3, len(moves)
                )
        self.assertIn({"start": (2, 1), "end": (4, 2)}, moves)
        self.assertIn({"start": (2, 1), "end": (3, 3)}, moves)
        self.assertIn({"start": (2, 1), "end": (0, 0)}, moves)

    def test_knight_completely_blocked_by_own_figures(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[2][2] = Knight(color="b", pos=(2, 2))
        field.points[4][1] = Pawn(color="b", pos=(4, 1))
        field.points[0][3] = Pawn(color="b", pos=(0, 3))
        field.points[1][4] = Pawn(color="b", pos=(1, 4))
        field.points[3][0] = Pawn(color="b", pos=(3, 0))
        field.points[3][4] = Pawn(color="b", pos=(3, 4))
        field.points[0][1] = Pawn(color="b", pos=(0, 1))
        field.points[1][0] = Pawn(color="b", pos=(1, 0))
        field.points[4][3] = Pawn(color="b", pos=(4, 3))
        knight = field.points[2][2]
        moves = knight.get_possible_moves(field.points)
        self.assertEqual([], moves)
