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
