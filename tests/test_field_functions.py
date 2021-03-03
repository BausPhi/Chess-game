import unittest
from game.field import *
from game.figures import *

class PawnAtEnd(unittest.TestCase):
    def test_pawn_at_end_white(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[0][0] = Pawn(color="w", pos=(0, 0))
        pawn = field.points[0][0]
        self.assertEqual(pawn, field.pawn_at_end(1))

    def test_pawn_not_at_end_white(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[7][7] = Pawn(color="w", pos=(7, 7))
        pawn = field.points[7][7]
        self.assertEqual(None, field.pawn_at_end(1))

    def test_pawn_not_at_end_black(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[0][0] = Pawn(color="b", pos=(0, 0))
        pawn = field.points[0][0]
        self.assertEqual(None, field.pawn_at_end(2))

    def test_pawn_at_end_black(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[7][7] = Pawn(color="b", pos=(7, 7))
        pawn = field.points[7][7]

        self.assertEqual(pawn, field.pawn_at_end(2))

class CheckMate(unittest.TestCase):
    def test_check_mate_1(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[4][0] = King(color="b", pos=(4, 0))
        field.points[4][1] = Pawn(color="w", pos=(4, 1))
        field.points[3][1] = Pawn(color="w", pos=(3, 1))
        field.points[4][2] = Queen(color="w", pos=(4, 2))
        self.assertEqual(True, field.is_check_mate(1))

    def test_not_check_mate_1(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[4][0] = King(color="b", pos=(4, 0))
        field.points[4][1] = Pawn(color="w", pos=(4, 1))
        field.points[3][2] = Pawn(color="w", pos=(3, 2))
        field.points[4][2] = Queen(color="w", pos=(4, 2))
        self.assertEqual(False, field.is_check_mate(2))

    def test_not_check_mate_2(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[4][0] = King(color="b", pos=(4, 0))
        field.points[4][1] = Pawn(color="w", pos=(4, 1))
        field.points[3][1] = Pawn(color="w", pos=(3, 1))
        field.points[4][2] = Queen(color="w", pos=(4, 2))
        self.assertEqual(False, field.is_check_mate(2))

    def test_not_check_mate_3(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[4][0] = King(color="b", pos=(4, 0))
        field.points[4][1] = Pawn(color="w", pos=(4, 1))
        field.points[3][1] = Pawn(color="w", pos=(3, 1))
        field.points[4][2] = Queen(color="w", pos=(4, 2))
        self.assertEqual(False, field.is_check_mate(2))

    def test_not_check_mate_4(self):
        field = Field(beginning=True, empty=False, field=None)
        field.points[4][1] = Empty(pos=(4, 1))
        field.points[2][3] = Pawn(color="b", pos=(2, 3))
        field.points[4][3] = Pawn(color="b", pos=(4, 3))
        field.points[3][4] = Pawn(color="w", pos=(3, 4))
        field.points[6][3] = Bishop(color="w", pos=(6, 3))
        field.points[3][6] = Empty(pos=(3, 6))
        field.points[2][7] = Empty(pos=(2, 7))
        field.points[3][0] = King(color="b", pos=(3, 0))
        field.points[2][1] = Empty(pos=(2, 1))
        self.assertEqual(False, field.is_check_mate(1))

class Mate(unittest.TestCase):
    def test_mate_1(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[1][1] = King(color="b", pos=(1, 1))
        field.points[0][0] = Pawn(color="b", pos=(0, 0))
        field.points[1][0] = Pawn(color="b", pos=(1, 0))
        field.points[2][0] = Pawn(color="b", pos=(2, 0))
        field.points[0][1] = Pawn(color="b", pos=(0, 1))
        field.points[2][1] = Pawn(color="b", pos=(2, 1))
        field.points[4][4] = Bishop(color="w", pos=(4, 4))
        self.assertEqual(True, field.is_mate(1))

    def test_mate_2(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[4][0] = King(color="b", pos=(4, 0))
        field.points[4][1] = Pawn(color="w", pos=(4, 1))
        field.points[3][1] = Pawn(color="w", pos=(3, 1))
        field.points[4][2] = Queen(color="w", pos=(4, 2))
        self.assertEqual(True, field.is_mate(1))

    def test_mate_3(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[4][0] = King(color="b", pos=(4, 0))
        field.points[4][1] = Pawn(color="w", pos=(4, 1))
        field.points[3][2] = Pawn(color="w", pos=(3, 2))
        field.points[4][2] = Queen(color="w", pos=(4, 2))
        self.assertEqual(False, field.is_mate(1))

    def test_mate_4(self):
        field = Field(beginning=True, empty=False, field=None)
        field.points[2][1] = Empty(pos=(2, 1))
        field.points[4][1] = Empty(pos=(4, 1))
        field.points[2][3] = Pawn(color="b", pos=(2, 3))
        field.points[4][3] = Pawn(color="b", pos=(4, 3))
        field.points[3][4] = Pawn(color="w", pos=(3, 4))
        field.points[6][3] = Bishop(color="w", pos=(6, 3))
        field.points[3][6] = Empty(pos=(3, 6))
        field.points[2][7] = Empty(pos=(2, 7))
        self.assertEqual(True, field.is_mate(1))

    def test_not_mate_1(self):
        field = Field(beginning=True, empty=False, field=None)
        field.points[4][1] = Empty(pos=(4, 1))
        field.points[2][3] = Pawn(color="b", pos=(2, 3))
        field.points[4][3] = Pawn(color="b", pos=(4, 3))
        field.points[3][4] = Pawn(color="w", pos=(3, 4))
        field.points[6][3] = Bishop(color="w", pos=(6, 3))
        field.points[3][6] = Empty(pos=(3, 6))
        field.points[2][7] = Empty(pos=(2, 7))
        field.points[3][0] = Empty(pos=(3, 0))
        field.points[2][1] = King(color="b", pos=(2, 1))
        self.assertEqual(False, field.is_mate(1))

    def test_mate_5(self):
        field = Field(beginning=True, empty=False, field=None)
        field.points[4][1] = Empty(pos=(4, 1))
        field.points[2][3] = Pawn(color="b", pos=(2, 3))
        field.points[4][3] = Pawn(color="b", pos=(4, 3))
        field.points[3][4] = Pawn(color="w", pos=(3, 4))
        field.points[6][3] = Bishop(color="w", pos=(6, 3))
        field.points[3][6] = Empty(pos=(3, 6))
        field.points[2][7] = Empty(pos=(2, 7))
        field.points[3][0] = King(color="b", pos=(3, 0))
        field.points[2][1] = Empty(pos=(2, 1))
        self.assertEqual(True, field.is_mate(1))

'''class Draw(unittest.TestCase):
    def test_draw_1(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[4][0] = King(color="b", pos=(4, 0))
        field.points[4][1] = Pawn(color="w", pos=(4, 1))
        field.points[3][2] = Pawn(color="w", pos=(3, 2))
        field.points[4][2] = Queen(color="w", pos=(4, 2))
        self.assertEqual(True, field.is_draw(1))

    def test_no_draw_1(self):
        field = Field(beginning=False, empty=True, field=None)
        field.points[4][0] = King(color="b", pos=(4, 0))
        field.points[4][1] = Pawn(color="w", pos=(4, 1))
        field.points[3][1] = Pawn(color="w", pos=(3, 1))
        field.points[4][2] = Queen(color="w", pos=(4, 2))
        self.assertEqual(False, field.is_draw(1))

    def test_no_draw_2(self):
        field = Field(beginning=True, empty=False, field=None)
        field.move_figure((3, 6), (3, 5))
        field.print_board()
        self.assertEqual(False, field.is_draw(1))'''
