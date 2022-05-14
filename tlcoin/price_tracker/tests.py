from django.test import TestCase

from . import tasks

class RefreshTestCase(TestCase):

    def test_refresh_price(self):
        res = tasks.refresh_price(vs_currency="INR")
        self.assertTrue(res)
