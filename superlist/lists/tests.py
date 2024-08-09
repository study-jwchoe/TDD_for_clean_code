from django.test import TestCase


class SmokeTest(TestCase):
    def test_bad_maths(self):
        self.assertEqual(first=1 + 1, second=3)
