from datetime import datetime
from unittest import TestCase

from timeutil import get_time

class TestTimeutil(TestCase):
    def test_get_time_at_9am(self):
        time = datetime(2013, 12, 31, 9, 0)
        result = get_time(time)
        self.assertTrue("31 December 2013 at 09:00 AM" in result)

    def test_get_time_at_10pm(self):
        time = datetime(2013, 12, 31, 22, 0)
        result = get_time(time)
        self.assertTrue("31 December 2013 at 10:00 PM" in result)
        
    def test_bracket_at_10pm(self):
        now = datetime(2013, 8, 24, 11, 40)
        time = datetime(2013, 8, 24, 22, 0)
        result = get_time(time, now)
        self.assertTrue("(10 hours 20 minutes from now)" in result)
    
    def test_bracket_at_11pm(self):
        now = datetime(2013, 8, 24, 11, 40)
        time = datetime(2013, 8, 24, 23, 0)
        result = get_time(time, now)
        self.assertTrue("(11 hours 20 minutes from now)" in result)

