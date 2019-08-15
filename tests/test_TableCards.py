import os
import unittest
from TableCards import TableCards


class TableCardsTests(unittest.TestCase):


    def test_define_recto_shift_x(self):
        t = TableCards(None,None,None)
        index = 0
        shift = t.define_recto_shift_x(index)
        self.assertEqual(shift, 0)

        index = 1
        shift = t.define_recto_shift_x(index)
        self.assertEqual(shift,35)

        index = 2
        shift = t.define_recto_shift_x(index)
        self.assertEqual(shift,70)

        index = 6
        shift = t.define_recto_shift_x(index)
        self.assertEqual(shift,35)

        index = 8
        shift = t.define_recto_shift_x(index)
        self.assertEqual(shift,105)

    def test_define_recto_shift_y(self):
        t = TableCards(None,None,None)
        index = 0
        shift = t.define_recto_shift_y(index)
        self.assertEqual(shift, 0)

        index = 1
        shift = t.define_recto_shift_y(index)
        self.assertEqual(shift,0)

        index = 2
        shift = t.define_recto_shift_y(index)
        self.assertEqual(shift,0)

        index = 6
        shift = t.define_recto_shift_y(index)
        self.assertEqual(shift,38)

        index = 8
        shift = t.define_recto_shift_y(index)
        self.assertEqual(shift,38)

    def test_define_verso_shift_x(self):
        t = TableCards(None,None,None)
        index = 0
        shift = t.define_verso_shift_x(index)
        self.assertEqual(shift, 18)

        index = 1
        shift = t.define_verso_shift_x(index)
        self.assertEqual(shift,53)

        index = 2
        shift = t.define_verso_shift_x(index)
        self.assertEqual(shift,88)

        index = 6
        shift = t.define_verso_shift_x(index)
        self.assertEqual(shift,53)

        index = 8
        shift = t.define_verso_shift_x(index)
        self.assertEqual(shift,123)

        index = 22
        shift = t.define_verso_shift_x(index)
        self.assertEqual(shift,88)


    def test_define_verso_shift_y(self):
        t = TableCards(None,None,None)
        index = 0
        shift = t.define_verso_shift_y(index)
        self.assertEqual(shift, 0)

        index = 1
        shift = t.define_verso_shift_y(index)
        self.assertEqual(shift,0)

        index = 2
        shift = t.define_verso_shift_y(index)
        self.assertEqual(shift,0)

        index = 6
        shift = t.define_verso_shift_y(index)
        self.assertEqual(shift,38)

        index = 8
        shift = t.define_verso_shift_y(index)
        self.assertEqual(shift,38)

        index = 22
        shift = t.define_verso_shift_y(index)
        self.assertEqual(shift,152)

if __name__ == "__main__":
    unittest.main()