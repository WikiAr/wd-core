import sys
from pathlib import Path
core_dir = Path(__file__).parent.parent
sys.path.append(core_dir)
# ---
import unittest
from np.si3g import mainwithcat2

class TestSi3g(unittest.TestCase):

    def test_mainwithcat2(self):
        # Test the mainwithcat2 function here
        # As this function does not return any value and mostly prints the output, 
        # we can test it by providing some mock inputs and check if it runs without any errors.
        try:
            mainwithcat2()
        except Exception as e:
            self.fail(f"mainwithcat2() raised exception {e}")

if __name__ == '__main__':
    unittest.main()
