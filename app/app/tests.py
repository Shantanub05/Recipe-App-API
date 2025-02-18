from django.test import SimpleTestCase

from app import calc # type: ignore






class CalTest(SimpleTestCase):
    def test_add_numbers(self):
        res = calc.add(5,6)

        self.assertEqual(res,11)

    def test_sub_numbers(self):
        res = calc.sub(7,3)
        self.assertEqual(res,4)