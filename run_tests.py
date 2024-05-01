import unittest
import xmlrunner

def run_tests():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    test_runner = xmlrunner.XMLTestRunner(output='test-reports')
    test_runner.run(test_suite)

if __name__ == '__main__':
    run_tests()