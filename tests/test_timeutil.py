from datetime import datetime
from unittest import TestCase

from timeutil import get_time

class TestTimeutil(TestCase):
    def test_get_time_return_correct_time_on_new_year_eve_at_9_am(self):
        time = datetime(2013, 12, 31, 9, 0)
        result = get_time(time)
        self.assertIn("31 December 2013 () at 09:00 AM", result)

    def test_get_time_return_correct_time_on_new_year_eve_at_10_pm(self):
        time = datetime(2013, 12, 31, 22, 0)
        result = get_time(time)
        self.assertIn("31 December 2013 () at 10:00 PM", result)

    def test_get_time_return_correct_date_on_new_year_at_10_pm(self):
        time = datetime(2014, 1, 1, 22, 0)
        result = get_time(time)
        self.assertIn("1 January 2014 () at 10:00 PM", result)
        
    def test_time_from_now_in_bracket_at_10pm(self):
        now = datetime(2013, 8, 24, 11, 40)
        time = datetime(2013, 8, 24, 22, 0)
        result = get_time(time, now)
        self.assertIn("(10 hours 20 minutes from now)", result)
    
    def test_time_from_now_in_bracket_at_11pm(self):
        now = datetime(2013, 8, 24, 11, 40)
        time = datetime(2013, 8, 24, 23, 0)
        result = get_time(time, now)
        self.assertIn("(11 hours 20 minutes from now)", result)
        

