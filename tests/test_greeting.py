import unittest

from epicidiom import greeting


class GreetingTests(unittest.TestCase):
    def test_greeting_uses_name(self) -> None:
        self.assertEqual(greeting("April"), "Hello, April!")

    def test_greeting_falls_back_to_world(self) -> None:
        self.assertEqual(greeting("   "), "Hello, world!")


if __name__ == "__main__":
    unittest.main()
