from main import guess_number
import unittest
class TestSum(unittest.TestCase):
    def test_target_must_be_lowed_limit(self):
        with self.assertRaises(ValueError):
            guess_number(1,2,10)

    def test_target_must_be_upper_limit(self):
        with self.assertRaises(ValueError):
            guess_number(11,2,10)

    def test_invalid_range(self):
        with self.assertRaises(ValueError):
            guess_number(4,10,1)

    def test_simple1(self):
        self.assertEqual (guess_number(6,1,10),(6,3))

    def test_simple2(self):
        n,attempts=guess_number(1,1,100)
        self.assertEqual (n,1)
        self.assertGreaterEqual(attempts,1)

    def test_simple3(self):
        n, attempts = guess_number(50, 1, 100)
        self.assertEqual(n, 50)
        self.assertGreaterEqual(attempts, 1)

    def test_simple4(self):
        n, attempts = guess_number(100, 1, 100)
        self.assertEqual(n, 100)
        self.assertGreaterEqual(attempts, 1)

if __name__ == "__main__":
    unittest.main()
