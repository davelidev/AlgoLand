import unittest

from fall_probability import solution


class FallProbabilityTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution(0, 0, 1, 1), 0)

    def test_many(self):
        self.assertTrue(solution(0, 0, 2, 2), 0.25)
        self.assertTrue(solution(1, 1, 2, 2), 0.25)
        self.assertTrue(solution(1, 0, 2, 2), 0.25)
        self.assertTrue(solution(1, 1, 3, 1), 1)


if __name__ == '__main__':
    unittest.main()