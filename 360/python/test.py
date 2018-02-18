#!/usr/bin/env python3
import unittest

import scary_sphere

class TestCases(unittest.TestCase):
    def test_correct_answers(self):
        correct_answers = {
            0: 0,
            1: 6,
            45: 34518,
        }
        for test_r, test_answer in correct_answers.items():
            self.assertEqual(scary_sphere.main(test_r), test_answer)


if __name__ == '__main__':
    unittest.main()
