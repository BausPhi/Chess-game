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
        self.assertEqual(3, len(moves))
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

class PossibleMovesBishop(unittest.TestCase):
    def test_bishop_blocked_own_figures_b(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[3][1] = Bishop(color="b", pos=(3, 1))
        field.points[4][2] = Pawn(color="b", pos=(4, 2))
        field.points[2][2] = Pawn(color="b", pos=(2, 2))
        field.points[2][0] = Pawn(color="b", pos=(2, 0))
        field.points[4][0] = Pawn(color="b", pos=(4, 0))
        bishop = field.points[3][1]
        moves = bishop.get_possible_moves(field.points)
        self.assertEqual([], moves)

    def test_bishop_blocked_own_figures_w(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[3][1] = Bishop(color="w", pos=(3, 1))
        field.points[4][2] = Pawn(color="w", pos=(4, 2))
        field.points[2][2] = Pawn(color="w", pos=(2, 2))
        field.points[2][0] = Pawn(color="w", pos=(2, 0))
        field.points[4][0] = Pawn(color="w", pos=(4, 0))
        bishop = field.points[3][1]
        moves = bishop.get_possible_moves(field.points)
        self.assertEqual([], moves)

    def test_bishop_move_blocked_own_figures_b_2(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[3][2] = Bishop(color="b", pos=(3, 2))
        field.points[5][4] = Pawn(color="b", pos=(5, 4))
        field.points[1][4] = Pawn(color="b", pos=(1, 4))
        field.points[5][0] = Pawn(color="b", pos=(5, 0))
        field.points[1][0] = Pawn(color="b", pos=(1, 0))
        bishop = field.points[3][2]
        moves = bishop.get_possible_moves(field.points)
        self.assertEqual(4, len(moves))
        self.assertIn({"start": (3, 2), "end": (4, 3)}, moves)
        self.assertIn({"start": (3, 2), "end": (2, 3)}, moves)
        self.assertIn({"start": (3, 2), "end": (2, 1)}, moves)
        self.assertIn({"start": (3, 2), "end": (4, 1)}, moves)

    def test_bishop_move_blocked_own_figures_w_2(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[3][2] = Bishop(color="w", pos=(3, 2))
        field.points[5][4] = Pawn(color="w", pos=(5, 4))
        field.points[1][4] = Pawn(color="w", pos=(1, 4))
        field.points[5][0] = Pawn(color="w", pos=(5, 0))
        field.points[1][0] = Pawn(color="w", pos=(1, 0))
        bishop = field.points[3][2]
        moves = bishop.get_possible_moves(field.points)
        self.assertEqual(4, len(moves))
        self.assertIn({"start": (3, 2), "end": (4, 3)}, moves)
        self.assertIn({"start": (3, 2), "end": (2, 3)}, moves)
        self.assertIn({"start": (3, 2), "end": (2, 1)}, moves)
        self.assertIn({"start": (3, 2), "end": (4, 1)}, moves)

    def test_bishop_blocked_enemy_figures_b(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[3][1] = Bishop(color="b", pos=(3, 1))
        field.points[4][2] = Pawn(color="w", pos=(4, 2))
        field.points[2][2] = Pawn(color="w", pos=(2, 2))
        field.points[2][0] = Pawn(color="w", pos=(2, 0))
        field.points[4][0] = Pawn(color="w", pos=(4, 0))
        bishop = field.points[3][1]
        moves = bishop.get_possible_moves(field.points)
        self.assertEqual(4, len(moves))
        self.assertIn({"start": (3, 1), "end": (4, 2)}, moves)
        self.assertIn({"start": (3, 1), "end": (2, 2)}, moves)
        self.assertIn({"start": (3, 1), "end": (2, 0)}, moves)
        self.assertIn({"start": (3, 1), "end": (4, 0)}, moves)

    def test_bishop_blocked_enemy_figures_w(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[3][1] = Bishop(color="w", pos=(3, 1))
        field.points[4][2] = Pawn(color="b", pos=(4, 2))
        field.points[2][2] = Pawn(color="b", pos=(2, 2))
        field.points[2][0] = Pawn(color="b", pos=(2, 0))
        field.points[4][0] = Pawn(color="b", pos=(4, 0))
        bishop = field.points[3][1]
        moves = bishop.get_possible_moves(field.points)
        self.assertEqual(4, len(moves))
        self.assertIn({"start": (3, 1), "end": (4, 2)}, moves)
        self.assertIn({"start": (3, 1), "end": (2, 2)}, moves)
        self.assertIn({"start": (3, 1), "end": (2, 0)}, moves)
        self.assertIn({"start": (3, 1), "end": (4, 0)}, moves)

    def test_bishop_not_blocked_b(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[4][4] = Bishop(color="b", pos=(4, 4))
        bishop = field.points[4][4]
        moves = bishop.get_possible_moves(field.points)
        self.assertEqual(13, len(moves))
        self.assertIn({"start": (4, 4), "end": (0, 0)}, moves)
        self.assertIn({"start": (4, 4), "end": (1, 1)}, moves)
        self.assertIn({"start": (4, 4), "end": (2, 2)}, moves)
        self.assertIn({"start": (4, 4), "end": (3, 3)}, moves)
        self.assertIn({"start": (4, 4), "end": (5, 5)}, moves)
        self.assertIn({"start": (4, 4), "end": (6, 6)}, moves)
        self.assertIn({"start": (4, 4), "end": (7, 7)}, moves)
        self.assertIn({"start": (4, 4), "end": (7, 1)}, moves)
        self.assertIn({"start": (4, 4), "end": (6, 2)}, moves)
        self.assertIn({"start": (4, 4), "end": (5, 3)}, moves)
        self.assertIn({"start": (4, 4), "end": (3, 5)}, moves)
        self.assertIn({"start": (4, 4), "end": (2, 6)}, moves)
        self.assertIn({"start": (4, 4), "end": (1, 7)}, moves)

    def test_bishop_not_blocked_w(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[4][4] = Bishop(color="w", pos=(4, 4))
        bishop = field.points[4][4]
        moves = bishop.get_possible_moves(field.points)
        self.assertEqual(13, len(moves))
        self.assertIn({"start": (4, 4), "end": (0, 0)}, moves)
        self.assertIn({"start": (4, 4), "end": (1, 1)}, moves)
        self.assertIn({"start": (4, 4), "end": (2, 2)}, moves)
        self.assertIn({"start": (4, 4), "end": (3, 3)}, moves)
        self.assertIn({"start": (4, 4), "end": (5, 5)}, moves)
        self.assertIn({"start": (4, 4), "end": (6, 6)}, moves)
        self.assertIn({"start": (4, 4), "end": (7, 7)}, moves)
        self.assertIn({"start": (4, 4), "end": (7, 1)}, moves)
        self.assertIn({"start": (4, 4), "end": (6, 2)}, moves)
        self.assertIn({"start": (4, 4), "end": (5, 3)}, moves)
        self.assertIn({"start": (4, 4), "end": (3, 5)}, moves)
        self.assertIn({"start": (4, 4), "end": (2, 6)}, moves)
        self.assertIn({"start": (4, 4), "end": (1, 7)}, moves)

    def test_bishop_left_upper_b(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[0][0] = Bishop(color="b", pos=(0, 0))
        bishop = field.points[0][0]
        moves = bishop.get_possible_moves(field.points)
        self.assertEqual(7, len(moves))
        self.assertIn({"start": (0, 0), "end": (4, 4)}, moves)
        self.assertIn({"start": (0, 0), "end": (1, 1)}, moves)
        self.assertIn({"start": (0, 0), "end": (2, 2)}, moves)
        self.assertIn({"start": (0, 0), "end": (3, 3)}, moves)
        self.assertIn({"start": (0, 0), "end": (5, 5)}, moves)
        self.assertIn({"start": (0, 0), "end": (6, 6)}, moves)
        self.assertIn({"start": (0, 0), "end": (7, 7)}, moves)

    def test_bishop_left_upper_w(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[0][0] = Bishop(color="w", pos=(0, 0))
        bishop = field.points[0][0]
        moves = bishop.get_possible_moves(field.points)
        self.assertEqual(7, len(moves))
        self.assertIn({"start": (0, 0), "end": (4, 4)}, moves)
        self.assertIn({"start": (0, 0), "end": (1, 1)}, moves)
        self.assertIn({"start": (0, 0), "end": (2, 2)}, moves)
        self.assertIn({"start": (0, 0), "end": (3, 3)}, moves)
        self.assertIn({"start": (0, 0), "end": (5, 5)}, moves)
        self.assertIn({"start": (0, 0), "end": (6, 6)}, moves)
        self.assertIn({"start": (0, 0), "end": (7, 7)}, moves)

    def test_bishop_right_lower_b(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[7][7] = Bishop(color="b", pos=(7, 7))
        bishop = field.points[7][7]
        moves = bishop.get_possible_moves(field.points)
        self.assertEqual(7, len(moves))
        self.assertIn({"start": (7, 7), "end": (4, 4)}, moves)
        self.assertIn({"start": (7, 7), "end": (1, 1)}, moves)
        self.assertIn({"start": (7, 7), "end": (2, 2)}, moves)
        self.assertIn({"start": (7, 7), "end": (3, 3)}, moves)
        self.assertIn({"start": (7, 7), "end": (5, 5)}, moves)
        self.assertIn({"start": (7, 7), "end": (6, 6)}, moves)
        self.assertIn({"start": (7, 7), "end": (0, 0)}, moves)

    def test_bishop_right_lower_w(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[7][7] = Bishop(color="w", pos=(7, 7))
        bishop = field.points[7][7]
        moves = bishop.get_possible_moves(field.points)
        self.assertEqual(7, len(moves))
        self.assertIn({"start": (7, 7), "end": (4, 4)}, moves)
        self.assertIn({"start": (7, 7), "end": (1, 1)}, moves)
        self.assertIn({"start": (7, 7), "end": (2, 2)}, moves)
        self.assertIn({"start": (7, 7), "end": (3, 3)}, moves)
        self.assertIn({"start": (7, 7), "end": (5, 5)}, moves)
        self.assertIn({"start": (7, 7), "end": (6, 6)}, moves)
        self.assertIn({"start": (7, 7), "end": (0, 0)}, moves)

class PossibleMovesRook(unittest.TestCase):
    def test_rook_blocked_own_figures_b(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[3][1] = Rook(color="b", pos=(3, 1))
        field.points[3][2] = Pawn(color="b", pos=(3, 2))
        field.points[3][0] = Pawn(color="b", pos=(3, 0))
        field.points[4][1] = Pawn(color="b", pos=(4, 1))
        field.points[2][1] = Pawn(color="b", pos=(2, 1))
        rook = field.points[3][1]
        moves = rook.get_possible_moves(field.points)
        self.assertEqual([], moves)

    def test_rook_blocked_own_figures_w(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[3][1] = Rook(color="w", pos=(3, 1))
        field.points[3][2] = Pawn(color="w", pos=(3, 2))
        field.points[3][0] = Pawn(color="w", pos=(3, 0))
        field.points[4][1] = Pawn(color="w", pos=(4, 1))
        field.points[2][1] = Pawn(color="w", pos=(2, 1))
        rook = field.points[3][1]
        moves = rook.get_possible_moves(field.points)
        self.assertEqual([], moves)

    def test_rook_move_blocked_own_figures_b_2(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[3][2] = Rook(color="b", pos=(3, 2))
        field.points[3][0] = Pawn(color="b", pos=(3, 0))
        field.points[3][4] = Pawn(color="b", pos=(3, 4))
        field.points[5][2] = Pawn(color="b", pos=(5, 2))
        field.points[1][2] = Pawn(color="b", pos=(1, 2))
        rook = field.points[3][2]
        moves = rook.get_possible_moves(field.points)
        self.assertEqual(4, len(moves))
        self.assertIn({"start": (3, 2), "end": (3, 1)}, moves)
        self.assertIn({"start": (3, 2), "end": (3, 3)}, moves)
        self.assertIn({"start": (3, 2), "end": (4, 2)}, moves)
        self.assertIn({"start": (3, 2), "end": (2, 2)}, moves)

    def test_rook_move_blocked_own_figures_w_2(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[3][2] = Rook(color="w", pos=(3, 2))
        field.points[3][0] = Pawn(color="w", pos=(3, 0))
        field.points[3][4] = Pawn(color="w", pos=(3, 4))
        field.points[5][2] = Pawn(color="w", pos=(5, 2))
        field.points[1][2] = Pawn(color="w", pos=(1, 2))
        rook = field.points[3][2]
        moves = rook.get_possible_moves(field.points)
        self.assertEqual(4, len(moves))
        self.assertIn({"start": (3, 2), "end": (3, 1)}, moves)
        self.assertIn({"start": (3, 2), "end": (3, 3)}, moves)
        self.assertIn({"start": (3, 2), "end": (4, 2)}, moves)
        self.assertIn({"start": (3, 2), "end": (2, 2)}, moves)

    def test_rook_blocked_enemy_figures_b(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[3][1] = Rook(color="b", pos=(3, 1))
        field.points[3][2] = Pawn(color="w", pos=(3, 2))
        field.points[3][0] = Pawn(color="w", pos=(3, 0))
        field.points[4][1] = Pawn(color="w", pos=(4, 1))
        field.points[2][1] = Pawn(color="w", pos=(2, 1))
        rook = field.points[3][1]
        moves = rook.get_possible_moves(field.points)
        self.assertEqual(4, len(moves))
        self.assertIn({"start": (3, 1), "end": (3, 2)}, moves)
        self.assertIn({"start": (3, 1), "end": (3, 0)}, moves)
        self.assertIn({"start": (3, 1), "end": (4, 1)}, moves)
        self.assertIn({"start": (3, 1), "end": (2, 1)}, moves)

    def test_rook_blocked_enemy_figures_w(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[3][1] = Rook(color="w", pos=(3, 1))
        field.points[3][2] = Pawn(color="b", pos=(3, 2))
        field.points[3][0] = Pawn(color="b", pos=(3, 0))
        field.points[4][1] = Pawn(color="b", pos=(4, 1))
        field.points[2][1] = Pawn(color="b", pos=(2, 1))
        rook = field.points[3][1]
        moves = rook.get_possible_moves(field.points)
        self.assertEqual(4, len(moves))
        self.assertIn({"start": (3, 1), "end": (3, 2)}, moves)
        self.assertIn({"start": (3, 1), "end": (3, 0)}, moves)
        self.assertIn({"start": (3, 1), "end": (4, 1)}, moves)
        self.assertIn({"start": (3, 1), "end": (2, 1)}, moves)

    def test_rook_not_blocked_b(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[4][4] = Rook(color="b", pos=(4, 4))
        rook = field.points[4][4]
        moves = rook.get_possible_moves(field.points)
        self.assertEqual(14, len(moves))
        self.assertIn({"start": (4, 4), "end": (4, 0)}, moves)
        self.assertIn({"start": (4, 4), "end": (4, 1)}, moves)
        self.assertIn({"start": (4, 4), "end": (4, 2)}, moves)
        self.assertIn({"start": (4, 4), "end": (4, 3)}, moves)
        self.assertIn({"start": (4, 4), "end": (4, 5)}, moves)
        self.assertIn({"start": (4, 4), "end": (4, 6)}, moves)
        self.assertIn({"start": (4, 4), "end": (4, 7)}, moves)
        self.assertIn({"start": (4, 4), "end": (0, 4)}, moves)
        self.assertIn({"start": (4, 4), "end": (1, 4)}, moves)
        self.assertIn({"start": (4, 4), "end": (2, 4)}, moves)
        self.assertIn({"start": (4, 4), "end": (3, 4)}, moves)
        self.assertIn({"start": (4, 4), "end": (5, 4)}, moves)
        self.assertIn({"start": (4, 4), "end": (6, 4)}, moves)
        self.assertIn({"start": (4, 4), "end": (7, 4)}, moves)

    def test_rook_not_blocked_w(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[4][4] = Rook(color="w", pos=(4, 4))
        rook = field.points[4][4]
        moves = rook.get_possible_moves(field.points)
        self.assertEqual(14, len(moves))
        self.assertIn({"start": (4, 4), "end": (4, 0)}, moves)
        self.assertIn({"start": (4, 4), "end": (4, 1)}, moves)
        self.assertIn({"start": (4, 4), "end": (4, 2)}, moves)
        self.assertIn({"start": (4, 4), "end": (4, 3)}, moves)
        self.assertIn({"start": (4, 4), "end": (4, 5)}, moves)
        self.assertIn({"start": (4, 4), "end": (4, 6)}, moves)
        self.assertIn({"start": (4, 4), "end": (4, 7)}, moves)
        self.assertIn({"start": (4, 4), "end": (0, 4)}, moves)
        self.assertIn({"start": (4, 4), "end": (1, 4)}, moves)
        self.assertIn({"start": (4, 4), "end": (2, 4)}, moves)
        self.assertIn({"start": (4, 4), "end": (3, 4)}, moves)
        self.assertIn({"start": (4, 4), "end": (5, 4)}, moves)
        self.assertIn({"start": (4, 4), "end": (6, 4)}, moves)
        self.assertIn({"start": (4, 4), "end": (7, 4)}, moves)

    def test_rook_left_upper_b(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[0][0] = Rook(color="b", pos=(0, 0))
        rook = field.points[0][0]
        moves = rook.get_possible_moves(field.points)
        self.assertEqual(14, len(moves))
        self.assertIn({"start": (0, 0), "end": (0, 1)}, moves)
        self.assertIn({"start": (0, 0), "end": (0, 2)}, moves)
        self.assertIn({"start": (0, 0), "end": (0, 3)}, moves)
        self.assertIn({"start": (0, 0), "end": (0, 4)}, moves)
        self.assertIn({"start": (0, 0), "end": (0, 5)}, moves)
        self.assertIn({"start": (0, 0), "end": (0, 6)}, moves)
        self.assertIn({"start": (0, 0), "end": (0, 7)}, moves)
        self.assertIn({"start": (0, 0), "end": (1, 0)}, moves)
        self.assertIn({"start": (0, 0), "end": (2, 0)}, moves)
        self.assertIn({"start": (0, 0), "end": (3, 0)}, moves)
        self.assertIn({"start": (0, 0), "end": (4, 0)}, moves)
        self.assertIn({"start": (0, 0), "end": (5, 0)}, moves)
        self.assertIn({"start": (0, 0), "end": (6, 0)}, moves)
        self.assertIn({"start": (0, 0), "end": (7, 0)}, moves)

    def test_rook_left_upper_w(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[0][0] = Rook(color="w", pos=(0, 0))
        rook = field.points[0][0]
        moves = rook.get_possible_moves(field.points)
        self.assertEqual(14, len(moves))
        self.assertIn({"start": (0, 0), "end": (0, 1)}, moves)
        self.assertIn({"start": (0, 0), "end": (0, 2)}, moves)
        self.assertIn({"start": (0, 0), "end": (0, 3)}, moves)
        self.assertIn({"start": (0, 0), "end": (0, 4)}, moves)
        self.assertIn({"start": (0, 0), "end": (0, 5)}, moves)
        self.assertIn({"start": (0, 0), "end": (0, 6)}, moves)
        self.assertIn({"start": (0, 0), "end": (0, 7)}, moves)
        self.assertIn({"start": (0, 0), "end": (1, 0)}, moves)
        self.assertIn({"start": (0, 0), "end": (2, 0)}, moves)
        self.assertIn({"start": (0, 0), "end": (3, 0)}, moves)
        self.assertIn({"start": (0, 0), "end": (4, 0)}, moves)
        self.assertIn({"start": (0, 0), "end": (5, 0)}, moves)
        self.assertIn({"start": (0, 0), "end": (6, 0)}, moves)
        self.assertIn({"start": (0, 0), "end": (7, 0)}, moves)

    def test_rook_right_lower_b(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[7][7] = Rook(color="b", pos=(7, 7))
        rook = field.points[7][7]
        moves = rook.get_possible_moves(field.points)
        self.assertEqual(14, len(moves))
        self.assertIn({"start": (7, 7), "end": (7, 6)}, moves)
        self.assertIn({"start": (7, 7), "end": (7, 5)}, moves)
        self.assertIn({"start": (7, 7), "end": (7, 4)}, moves)
        self.assertIn({"start": (7, 7), "end": (7, 3)}, moves)
        self.assertIn({"start": (7, 7), "end": (7, 2)}, moves)
        self.assertIn({"start": (7, 7), "end": (7, 1)}, moves)
        self.assertIn({"start": (7, 7), "end": (7, 0)}, moves)
        self.assertIn({"start": (7, 7), "end": (0, 7)}, moves)
        self.assertIn({"start": (7, 7), "end": (1, 7)}, moves)
        self.assertIn({"start": (7, 7), "end": (2, 7)}, moves)
        self.assertIn({"start": (7, 7), "end": (3, 7)}, moves)
        self.assertIn({"start": (7, 7), "end": (4, 7)}, moves)
        self.assertIn({"start": (7, 7), "end": (5, 7)}, moves)
        self.assertIn({"start": (7, 7), "end": (6, 7)}, moves)

    def test_rook_right_lower_w(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[7][7] = Rook(color="w", pos=(7, 7))
        rook = field.points[7][7]
        moves = rook.get_possible_moves(field.points)
        self.assertEqual(14, len(moves))
        self.assertIn({"start": (7, 7), "end": (7, 6)}, moves)
        self.assertIn({"start": (7, 7), "end": (7, 5)}, moves)
        self.assertIn({"start": (7, 7), "end": (7, 4)}, moves)
        self.assertIn({"start": (7, 7), "end": (7, 3)}, moves)
        self.assertIn({"start": (7, 7), "end": (7, 2)}, moves)
        self.assertIn({"start": (7, 7), "end": (7, 1)}, moves)
        self.assertIn({"start": (7, 7), "end": (7, 0)}, moves)
        self.assertIn({"start": (7, 7), "end": (0, 7)}, moves)
        self.assertIn({"start": (7, 7), "end": (1, 7)}, moves)
        self.assertIn({"start": (7, 7), "end": (2, 7)}, moves)
        self.assertIn({"start": (7, 7), "end": (3, 7)}, moves)
        self.assertIn({"start": (7, 7), "end": (4, 7)}, moves)
        self.assertIn({"start": (7, 7), "end": (5, 7)}, moves)
        self.assertIn({"start": (7, 7), "end": (6, 7)}, moves)
