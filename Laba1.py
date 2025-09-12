from main import summa
import unittest
class TestSum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(summa([3, 3], 6), [0, 1])

    def test_simple2(self):
        self.assertEqual(summa([2, 7, 11, 15], 9), [0, 1])

    def test_simple3(self):
        self.assertEqual(summa([2, 7, 8, 11, 15], 9, 10), None) #неверноe кол-во аргументов

    def test_simple4(self):
        self.assertEqual(summa({2, 7, 11, 15}, 9), None)#не является списком

    def test_simple5(self):
        self.assertEqual(summa(16, 9), None)#нет списка

    def test_simple6(self):
        self.assertEqual(summa([2], 9), None)#в списке тольео один элемент

    def test_simple7(self):
        self.assertEqual(summa([2,4,7,9], 9.4), None)#аргумент нецелое число

    def test_simple8(self):
        self.assertEqual(summa([1.6, 7.4], 9),  None) #в массиве не натуральное число

    def test_simple9(self):
        self.assertEqual(summa([1,3,7,9], 9),  None) #нету вариантов

if __name__ == "__main__":
    unittest.main()
