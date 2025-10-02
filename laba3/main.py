import unittest
from bin_tree import bintree
class Test_variant_14(unittest.TestCase):
    def test1(self):
        tree=bintree(4,14)
        self.assertEqual(tree["value"],14)
    def test2(self):
        tree=bintree(2,10)
        self.assertEqual(tree["left"]["value"], 3 - 10)
        self.assertEqual(tree["right"]["value"], 20)
    def test3(self):
        tree=bintree(3,5)
        self.assertEqual(tree["left"]["left"]["value"], 5)
        self.assertEqual(tree["left"]["right"]["value"], -4)
        self.assertEqual(tree["right"]["left"]["value"], -7)
        self.assertEqual(tree["right"]["right"]["value"], 20)
if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)
