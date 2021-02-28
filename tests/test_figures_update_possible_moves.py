import unittest
from game.field import *
from game.figures import *


class PossibleMovesKing(unittest.TestCase):
    def test_king_moves_possible_up(self):
        field = Field(beginning=True, empty=False, field=None)
        field.points[3][1] = Empty(pos=(3, 1))
        king = field.points[3][0]
        king.update_possible_moves(field.points)
        self.assertEqual([{"start": (3, 0), "end": (3, 1)}], king.moves)

    def test_king_moves_possible_up_left_right(self):
        field = Field(beginning=True, empty=False, field=None)
        field.points[3][1] = Empty(pos=(3, 1))
        field.points[2][0] = Empty(pos=(2, 0))
        field.points[4][0] = Empty(pos=(4, 0))
        king = field.points[3][0]
        king.update_possible_moves(field.points)
        self.assertEqual(3, len(king.moves))
        self.assertIn({"start": (3, 0), "end": (3, 1)}, king.moves)
        self.assertIn({"start": (3, 0), "end": (4, 0)}, king.moves)
        self.assertIn({"start": (3, 0), "end": (2, 0)}, king.moves)

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
        king.update_possible_moves(field.points)
        self.assertEqual(8, len(king.moves))
        self.assertIn({"start": (3, 1), "end": (2, 0)}, king.moves)
        self.assertIn({"start": (3, 1), "end": (3, 0)}, king.moves)
        self.assertIn({"start": (3, 1), "end": (4, 0)}, king.moves)
        self.assertIn({"start": (3, 1), "end": (2, 1)}, king.moves)
        self.assertIn({"start": (3, 1), "end": (4, 1)}, king.moves)
        self.assertIn({"start": (3, 1), "end": (2, 2)}, king.moves)
        self.assertIn({"start": (3, 1), "end": (3, 2)}, king.moves)
        self.assertIn({"start": (3, 1), "end": (4, 2)}, king.moves)

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
        king.update_possible_moves(field.points)
        self.assertEqual(8, len(king.moves))
        self.assertIn({"start": (3, 1), "end": (2, 0)}, king.moves)
        self.assertIn({"start": (3, 1), "end": (3, 0)}, king.moves)
        self.assertIn({"start": (3, 1), "end": (4, 0)}, king.moves)
        self.assertIn({"start": (3, 1), "end": (2, 1)}, king.moves)
        self.assertIn({"start": (3, 1), "end": (4, 1)}, king.moves)
        self.assertIn({"start": (3, 1), "end": (2, 2)}, king.moves)
        self.assertIn({"start": (3, 1), "end": (3, 2)}, king.moves)
        self.assertIn({"start": (3, 1), "end": (4, 2)}, king.moves)

class PossibleMovesPawn(unittest.TestCase):
    def test_pawn_move_blocked_black(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[3][1] = Pawn(color="b", pos=(3, 1))
        field.points[3][2] = Pawn(color="w", pos=(3, 2))
        pawn = field.points[3][1]
        pawn.update_possible_moves(field.points)
        self.assertEqual([], pawn.moves)

    def test_pawn_all_moves_possible_black(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[3][1] = Pawn(color="b", pos=(3, 1))
        field.points[4][2] = Pawn(color="w", pos=(4, 2))
        field.points[2][2] = Pawn(color="w", pos=(2, 2))
        pawn = field.points[3][1]
        pawn.update_possible_moves(field.points)
        self.assertEqual(4, len(pawn.moves))
        self.assertIn({"start": (3, 1), "end": (3, 2)}, pawn.moves)
        self.assertIn({"start": (3, 1), "end": (3, 3)}, pawn.moves)
        self.assertIn({"start": (3, 1), "end": (4, 2)}, pawn.moves)
        self.assertIn({"start": (3, 1), "end": (2, 2)}, pawn.moves)

    def test_pawn_move_blocked_white(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[3][5] = Pawn(color="b", pos=(3, 5))
        field.points[3][6] = Pawn(color="w", pos=(3, 6))
        pawn = field.points[3][6]
        pawn.update_possible_moves(field.points)
        self.assertEqual([], pawn.moves)

    def test_pawn_move_all_possible_white(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[2][5] = Pawn(color="b", pos=(2, 5))
        field.points[4][5] = Pawn(color="b", pos=(4, 5))
        field.points[3][6] = Pawn(color="w", pos=(3, 6))
        pawn = field.points[3][6]
        pawn.update_possible_moves(field.points)
        self.assertEqual(4, len(pawn.moves))
        self.assertIn({"start": (3, 6), "end": (2, 5)}, pawn.moves)
        self.assertIn({"start": (3, 6), "end": (4, 5)}, pawn.moves)
        self.assertIn({"start": (3, 6), "end": (3, 5)}, pawn.moves)
        self.assertIn({"start": (3, 6), "end": (3, 4)}, pawn.moves)

class PossibleMovesKnight(unittest.TestCase):
    def test_knight_move_all_possible(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[4][4] = Knight(color="b", pos=(4, 4))
        knight = field.points[4][4]
        knight.update_possible_moves(field.points)
        self.assertEqual(8, len(knight.moves))
        self.assertIn({"start": (4, 4), "end": (2, 3)}, knight.moves)
        self.assertIn({"start": (4, 4), "end": (2, 5)}, knight.moves)
        self.assertIn({"start": (4, 4), "end": (6, 3)}, knight.moves)
        self.assertIn({"start": (4, 4), "end": (6, 5)}, knight.moves)
        self.assertIn({"start": (4, 4), "end": (3, 2)}, knight.moves)
        self.assertIn({"start": (4, 4), "end": (5, 2)}, knight.moves)
        self.assertIn({"start": (4, 4), "end": (3, 6)}, knight.moves)
        self.assertIn({"start": (4, 4), "end": (5, 6)}, knight.moves)

    def test_knight_move_left_upper_part(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[1][1] = Knight(color="b", pos=(1, 1))
        knight = field.points[1][1]
        knight.update_possible_moves(field.points)
        self.assertEqual(4, len(knight.moves))
        self.assertIn({"start": (1, 1), "end": (3, 0)}, knight.moves)
        self.assertIn({"start": (1, 1), "end": (3, 2)}, knight.moves)
        self.assertIn({"start": (1, 1), "end": (2, 3)}, knight.moves)
        self.assertIn({"start": (1, 1), "end": (0, 3)}, knight.moves)

    def test_knight_move_left_upper_wall(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[0][0] = Knight(color="b", pos=(0, 0))
        knight = field.points[0][0]
        knight.update_possible_moves(field.points)
        self.assertEqual(2, len(knight.moves))
        self.assertIn({"start": (0, 0), "end": (1, 2)}, knight.moves)
        self.assertIn({"start": (0, 0), "end": (2, 1)}, knight.moves)

    def test_knight_move_right_lower_part(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[6][6] = Knight(color="b", pos=(6, 6))
        knight = field.points[6][6]
        knight.update_possible_moves(field.points)
        self.assertEqual(4, len(knight.moves))
        self.assertIn({"start": (6, 6), "end": (4, 7)}, knight.moves)
        self.assertIn({"start": (6, 6), "end": (4, 5)}, knight.moves)
        self.assertIn({"start": (6, 6), "end": (5, 4)}, knight.moves)
        self.assertIn({"start": (6, 6), "end": (7, 4)}, knight.moves)

    def test_knight_move_right_upper_wall(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[7][7] = Knight(color="b", pos=(7, 7))
        knight = field.points[7][7]
        knight.update_possible_moves(field.points)
        self.assertEqual(2, len(knight.moves))
        self.assertIn({"start": (7, 7), "end": (5, 6)}, knight.moves)
        self.assertIn({"start": (7, 7), "end": (6, 5)}, knight.moves)

    def test_knight_move_partially_blocked_by_own_figures(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[2][1] = Knight(color="b", pos=(2, 1))
        field.points[4][0] = Pawn(color="b", pos=(4, 0))
        field.points[0][2] = Pawn(color="b", pos=(0, 2))
        field.points[1][3] = Pawn(color="b", pos=(1, 3))
        knight = field.points[2][1]
        knight.update_possible_moves(field.points)
        self.assertEqual(3, len(knight.moves))
        self.assertIn({"start": (2, 1), "end": (4, 2)}, knight.moves)
        self.assertIn({"start": (2, 1), "end": (3, 3)}, knight.moves)
        self.assertIn({"start": (2, 1), "end": (0, 0)}, knight.moves)

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
        knight.update_possible_moves(field.points)
        self.assertEqual([], knight.moves)

class PossibleMovesBishop(unittest.TestCase):
    def test_bishop_move_blocked_own_figures_b(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[3][1] = Bishop(color="b", pos=(3, 1))
        field.points[4][2] = Pawn(color="b", pos=(4, 2))
        field.points[2][2] = Pawn(color="b", pos=(2, 2))
        field.points[2][0] = Pawn(color="b", pos=(2, 0))
        field.points[4][0] = Pawn(color="b", pos=(4, 0))
        bishop = field.points[3][1]
        bishop.update_possible_moves(field.points)
        self.assertEqual([], bishop.moves)

    def test_bishop_move_blocked_own_figures_w(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[3][1] = Bishop(color="w", pos=(3, 1))
        field.points[4][2] = Pawn(color="w", pos=(4, 2))
        field.points[2][2] = Pawn(color="w", pos=(2, 2))
        field.points[2][0] = Pawn(color="w", pos=(2, 0))
        field.points[4][0] = Pawn(color="w", pos=(4, 0))
        bishop = field.points[3][1]
        bishop.update_possible_moves(field.points)
        self.assertEqual([], bishop.moves)

    def test_bishop_move_blocked_enemy_figures_b(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[3][1] = Bishop(color="b", pos=(3, 1))
        field.points[4][2] = Pawn(color="w", pos=(4, 2))
        field.points[2][2] = Pawn(color="w", pos=(2, 2))
        field.points[2][0] = Pawn(color="w", pos=(2, 0))
        field.points[4][0] = Pawn(color="w", pos=(4, 0))
        bishop = field.points[3][1]
        bishop.update_possible_moves(field.points)
        self.assertEqual(4, len(bishop.moves))
        self.assertIn({"start": (3, 1), "end": (4, 2)}, bishop.moves)
        self.assertIn({"start": (3, 1), "end": (2, 2)}, bishop.moves)
        self.assertIn({"start": (3, 1), "end": (2, 0)}, bishop.moves)
        self.assertIn({"start": (3, 1), "end": (4, 0)}, bishop.moves)

    def test_bishop_move_blocked_enemy_figures_w(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[3][1] = Bishop(color="w", pos=(3, 1))
        field.points[4][2] = Pawn(color="b", pos=(4, 2))
        field.points[2][2] = Pawn(color="b", pos=(2, 2))
        field.points[2][0] = Pawn(color="b", pos=(2, 0))
        field.points[4][0] = Pawn(color="b", pos=(4, 0))
        bishop = field.points[3][1]
        bishop.update_possible_moves(field.points)
        self.assertEqual(4, len(bishop.moves))
        self.assertIn({"start": (3, 1), "end": (4, 2)}, bishop.moves)
        self.assertIn({"start": (3, 1), "end": (2, 2)}, bishop.moves)
        self.assertIn({"start": (3, 1), "end": (2, 0)}, bishop.moves)
        self.assertIn({"start": (3, 1), "end": (4, 0)}, bishop.moves)

    def test_bishop_move_not_blocked_b(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[4][4] = Bishop(color="b", pos=(4, 4))
        bishop = field.points[4][4]
        bishop.update_possible_moves(field.points)
        self.assertEqual(13, len(bishop.moves))
        self.assertIn({"start": (4, 4), "end": (0, 0)}, bishop.moves)
        self.assertIn({"start": (4, 4), "end": (1, 1)}, bishop.moves)
        self.assertIn({"start": (4, 4), "end": (2, 2)}, bishop.moves)
        self.assertIn({"start": (4, 4), "end": (3, 3)}, bishop.moves)
        self.assertIn({"start": (4, 4), "end": (5, 5)}, bishop.moves)
        self.assertIn({"start": (4, 4), "end": (6, 6)}, bishop.moves)
        self.assertIn({"start": (4, 4), "end": (7, 7)}, bishop.moves)
        self.assertIn({"start": (4, 4), "end": (7, 1)}, bishop.moves)
        self.assertIn({"start": (4, 4), "end": (6, 2)}, bishop.moves)
        self.assertIn({"start": (4, 4), "end": (5, 3)}, bishop.moves)
        self.assertIn({"start": (4, 4), "end": (3, 5)}, bishop.moves)
        self.assertIn({"start": (4, 4), "end": (2, 6)}, bishop.moves)
        self.assertIn({"start": (4, 4), "end": (1, 7)}, bishop.moves)

    def test_bishop_move_not_blocked_w(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[4][4] = Bishop(color="w", pos=(4, 4))
        bishop = field.points[4][4]
        bishop.update_possible_moves(field.points)
        self.assertEqual(13, len(bishop.moves))
        self.assertIn({"start": (4, 4), "end": (0, 0)}, bishop.moves)
        self.assertIn({"start": (4, 4), "end": (1, 1)}, bishop.moves)
        self.assertIn({"start": (4, 4), "end": (2, 2)}, bishop.moves)
        self.assertIn({"start": (4, 4), "end": (3, 3)}, bishop.moves)
        self.assertIn({"start": (4, 4), "end": (5, 5)}, bishop.moves)
        self.assertIn({"start": (4, 4), "end": (6, 6)}, bishop.moves)
        self.assertIn({"start": (4, 4), "end": (7, 7)}, bishop.moves)
        self.assertIn({"start": (4, 4), "end": (7, 1)}, bishop.moves)
        self.assertIn({"start": (4, 4), "end": (6, 2)}, bishop.moves)
        self.assertIn({"start": (4, 4), "end": (5, 3)}, bishop.moves)
        self.assertIn({"start": (4, 4), "end": (3, 5)}, bishop.moves)
        self.assertIn({"start": (4, 4), "end": (2, 6)}, bishop.moves)
        self.assertIn({"start": (4, 4), "end": (1, 7)}, bishop.moves)

    def test_bishop_move_left_upper_b(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[0][0] = Bishop(color="b", pos=(0, 0))
        bishop = field.points[0][0]
        bishop.update_possible_moves(field.points)
        self.assertEqual(7, len(bishop.moves))
        self.assertIn({"start": (0, 0), "end": (4, 4)}, bishop.moves)
        self.assertIn({"start": (0, 0), "end": (1, 1)}, bishop.moves)
        self.assertIn({"start": (0, 0), "end": (2, 2)}, bishop.moves)
        self.assertIn({"start": (0, 0), "end": (3, 3)}, bishop.moves)
        self.assertIn({"start": (0, 0), "end": (5, 5)}, bishop.moves)
        self.assertIn({"start": (0, 0), "end": (6, 6)}, bishop.moves)
        self.assertIn({"start": (0, 0), "end": (7, 7)}, bishop.moves)

    def test_bishop_move_left_upper_w(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[0][0] = Bishop(color="w", pos=(0, 0))
        bishop = field.points[0][0]
        bishop.update_possible_moves(field.points)
        self.assertEqual(7, len(bishop.moves))
        self.assertIn({"start": (0, 0), "end": (4, 4)}, bishop.moves)
        self.assertIn({"start": (0, 0), "end": (1, 1)}, bishop.moves)
        self.assertIn({"start": (0, 0), "end": (2, 2)}, bishop.moves)
        self.assertIn({"start": (0, 0), "end": (3, 3)}, bishop.moves)
        self.assertIn({"start": (0, 0), "end": (5, 5)}, bishop.moves)
        self.assertIn({"start": (0, 0), "end": (6, 6)}, bishop.moves)
        self.assertIn({"start": (0, 0), "end": (7, 7)}, bishop.moves)

    def test_bishop_move_right_lower_b(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[7][7] = Bishop(color="b", pos=(7, 7))
        bishop = field.points[7][7]
        bishop.update_possible_moves(field.points)
        self.assertEqual(7, len(bishop.moves))
        self.assertIn({"start": (7, 7), "end": (4, 4)}, bishop.moves)
        self.assertIn({"start": (7, 7), "end": (1, 1)}, bishop.moves)
        self.assertIn({"start": (7, 7), "end": (2, 2)}, bishop.moves)
        self.assertIn({"start": (7, 7), "end": (3, 3)}, bishop.moves)
        self.assertIn({"start": (7, 7), "end": (5, 5)}, bishop.moves)
        self.assertIn({"start": (7, 7), "end": (6, 6)}, bishop.moves)
        self.assertIn({"start": (7, 7), "end": (0, 0)}, bishop.moves)

    def test_bishop_move_right_lower_w(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[7][7] = Bishop(color="w", pos=(7, 7))
        bishop = field.points[7][7]
        bishop.update_possible_moves(field.points)
        self.assertEqual(7, len(bishop.moves))
        self.assertIn({"start": (7, 7), "end": (4, 4)}, bishop.moves)
        self.assertIn({"start": (7, 7), "end": (1, 1)}, bishop.moves)
        self.assertIn({"start": (7, 7), "end": (2, 2)}, bishop.moves)
        self.assertIn({"start": (7, 7), "end": (3, 3)}, bishop.moves)
        self.assertIn({"start": (7, 7), "end": (5, 5)}, bishop.moves)
        self.assertIn({"start": (7, 7), "end": (6, 6)}, bishop.moves)
        self.assertIn({"start": (7, 7), "end": (0, 0)}, bishop.moves)
