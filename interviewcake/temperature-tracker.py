import unittest


class TempTracker(object):

    # Implement methods to track the max, min, mean, and mode
    def __init__(self):
        
        self.max_temperature = -float('inf')
        self.min_temperature = float('inf')
        self.temperature_count = 0
        self.temperature_sum = 0
        self.occurrences = [0] * 110  # Fahrenheit temperatures
        self.max_occurrences = 0
        self.mean = 0
        self.mode = None

    def insert(self, temperature):
        
        if temperature < 0 or temperature > 100:
            raise Exception("Invalid temperature: ", temperature)
        
        # update max and min
        if temperature > self.max_temperature:
            self.max_temperature = temperature
        if temperature < self.min_temperature:
            self.min_temperature = temperature
        
        # update mean
        self.temperature_count += 1
        self.temperature_sum += temperature
        self.mean = self.temperature_sum / self.temperature_count
        
        # update mode
        self.occurrences[temperature] += 1
        if self.occurrences[temperature] > self.max_occurrences:
            self.max_occurrences = self.occurrences[temperature]
            self.mode = temperature
        
        

    def get_max(self):
        return self.max_temperature

    def get_min(self):
        return self.min_temperature

    def get_mean(self):
        return self.mean

    def get_mode(self):
        return self.mode


















# Tests

class Test(unittest.TestCase):

    def test_tracker_usage(self):
        tracker = TempTracker()

        tracker.insert(50)
        msg = 'failed on first temp recorded'
        self.assertEqual(tracker.get_max(), 50, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 50.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 50, msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on higher temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 65.0, msg='mean ' + msg)
        self.assertIn(tracker.get_mode(), [50, 80], msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on third temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 70.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)

        tracker.insert(30)
        msg = 'failed on lower temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 30, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 60.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)


unittest.main(verbosity=2)