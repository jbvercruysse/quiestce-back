import os
import unittest
from DrawCards import DrawCards


class DrawCardsTests(unittest.TestCase):


    def test_define_recto_shift_x(self):
        t = DrawCards(None,None,None)
        index = 0
        shift = t.define_recto_shift_x(index)
        self.assertEqual(shift, 0)

        index = 1
        shift = t.define_recto_shift_x(index)
        self.assertEqual(shift,48)

        index = 2
        shift = t.define_recto_shift_x(index)
        self.assertEqual(shift,96)

        index = 6
        shift = t.define_recto_shift_x(index)
        self.assertEqual(shift,96)

        index = 8
        shift = t.define_recto_shift_x(index)
        self.assertEqual(shift,0)

        index = 22
        shift = t.define_recto_shift_x(index)
        self.assertEqual(shift, 96)

        index = 23
        shift = t.define_recto_shift_x(index)
        self.assertEqual(shift, 144)


    def test_define_recto_shift_y(self):
        t = DrawCards(None,None,None)
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
        self.assertEqual(shift,79)

        index = 8
        shift = t.define_recto_shift_y(index)
        self.assertEqual(shift,158)

        index = 23
        shift = t.define_recto_shift_y(index)
        self.assertEqual(shift, 158)

    def test_define_verso_shift_x(self):
        t = DrawCards(None,None,None)
        index = 0
        shift = t.define_verso_shift_x(index)
        self.assertEqual(shift, 0)

        index = 1
        shift = t.define_verso_shift_x(index)
        self.assertEqual(shift,48)

        index = 2
        shift = t.define_verso_shift_x(index)
        self.assertEqual(shift,96)

        index = 6
        shift = t.define_verso_shift_x(index)
        self.assertEqual(shift,96)

        index = 8
        shift = t.define_verso_shift_x(index)
        self.assertEqual(shift,0)

        index = 22
        shift = t.define_verso_shift_x(index)
        self.assertEqual(shift,96)


    def test_define_verso_shift_y(self):
        t = DrawCards(None,None,None)
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
        self.assertEqual(shift,79)

        index = 8
        shift = t.define_verso_shift_y(index)
        self.assertEqual(shift,158)

        index = 22
        shift = t.define_verso_shift_y(index)
        self.assertEqual(shift,158)

if __name__ == "__main__":
    unittest.main()