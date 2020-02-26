from django.test import TestCase

# Create your tests here.

from django.test import TestCase

class SmokeTest(TestCase):
    def test_bad_math(self):
        self.assertEqual(1+1,3)