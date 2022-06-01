import translator
import unittest


class TestEnglishToFrench(unittest.TestCase):
    def setUp(self):
        self.translator = translator.Translator()

    def test_null_input(self):
        self.assertEqual(self.translator.english_to_french(None), None)

    def test_translate_common_phrases(self):
        self.assertEqual(self.translator.english_to_french("Hello"), "Bonjour")
        self.assertEqual(self.translator.english_to_french(
            "Nice to meet you"), "Ravi de vous rencontrer")
        self.assertEqual(self.translator.english_to_french(
            "Goodbye"), "Au revoir")
        self.assertEqual(self.translator.english_to_french("Thanks"), "Merci")
        self.assertEqual(self.translator.english_to_french(
            "Good night"), "Bonne nuit")

    def test_translate_to_itself(self):
        self.assertNotEqual(
            self.translator.english_to_french("Hello"), "Hello")
        self.assertNotEqual(
            self.translator.english_to_french("Thanks"), "Thanks")


class TestFrenchToEnglish(unittest.TestCase):
    def setUp(self):
        self.translator = translator.Translator()

    def test_null_input(self):
        self.assertEqual(self.translator.french_to_english(None), None)

    def test_translate_common_phrases(self):
        self.assertEqual(self.translator.french_to_english("Bonjour"), "Hello")
        self.assertEqual(self.translator.french_to_english(
            "Ravi de vous rencontrer"), "Nice to meet you")
        self.assertEqual(self.translator.french_to_english(
            "Au revoir"), "Goodbye")
        self.assertEqual(
            self.translator.french_to_english("Merci"), "Thank you")
        self.assertEqual(self.translator.french_to_english(
            "Bonne nuit"), "Good night")

    def test_translate_to_itself(self):
        self.assertNotEqual(
            self.translator.french_to_english("Bonjour"), "Bonjour")
        self.assertNotEqual(
            self.translator.french_to_english("Merci"), "Merci")


if __name__ == "__main__":
    unittest.main()
