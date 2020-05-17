import unittest
from abbreviation_generator import isCamelCase,camelCaseSplit

class TestKeywords(unittest.TestCase):
    def test_isCamelCase(self):
        self.assertTrue(isCamelCase("janeDoe"))
        self.assertTrue(isCamelCase("imCamelCase"))
        self.assertTrue(isCamelCase("has$InWord"))
        self.assertFalse(isCamelCase("ImPascalCase"))
        self.assertFalse(isCamelCase("has_underscore"))
        self.assertFalse(isCamelCase("camel"))
        self.assertFalse(isCamelCase("Super"))
        self.assertFalse(isCamelCase("123StartsWithDigits"))
        self.assertFalse(isCamelCase("has OneSpace"))
        self.assertFalse(isCamelCase("has  TwoSpaces"))
        self.assertFalse(isCamelCase("%camelCase"))
        self.assertFalse(isCamelCase(" hasLeadingSpace"))
        with self.assertRaises(TypeError):
            isCamelCase(12345)

    def test_camelCaseSplit(self):
        self.assertEqual(camelCaseSplit("theDarkKnightRises"),["the","Dark","Knight","Rises"])
        self.assertEqual(camelCaseSplit("helloW"),["hello","W"])
        self.assertEqual(camelCaseSplit("helloIWorld"),["hello","I","World"])
        with self.assertRaises(TypeError):
            camelCaseSplit(1234)


if (__name__ == "__main__"):
    unittest.main()
            