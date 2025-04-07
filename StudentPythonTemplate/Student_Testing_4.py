import copy
import unittest
import sys
import Helper
import Task_4
from Task_4 import *
import Dummy

sys.tracebacklimit = 6
width = 60
height = 30

numpy.seterr(divide='raise')
numpy.seterr(invalid='raise')

#
img_red = Helper.readAndResize("../Extras/red.jpg")
img_black = Helper.readAndResize("../Extras/black.jpg")
img_gray = Helper.readAndResize("../Extras/gray.jpg")

places = 10


class Task_4_Testing(unittest.TestCase):

    # This function contains one unit test for cosine similarity.
    # The function simply checks one possible behaviour, and there are many more possible. More than that
    # is also supporting markers. Feel free to expand on these tests for your own purposes. This area is not marked
    # or checked.
    #

    def test1_computeCosineSimilarity(self):
        measure_function = Task_4.computeCosineSimilarity
        student_output = measure_function(copy.deepcopy(img_red), copy.deepcopy(img_gray))

        # We first check if it returns what it is supposed to, rounded to given decimal places for convenience
        expected_output = 0.5863706746
        val1 = round(float(student_output), places)
        val2 = round(float(expected_output), places)

        result = (val1 == val2)
        result_message = "Computing cosine similarity failed, expected " + str(val2) + " and got " + str(val1)
        self.assertEqual(result, True, result_message)

    def test2_computeRMSEDistance(self):
        measure_function = Task_4.computeRMSEDistance
        student_output = measure_function(copy.deepcopy(img_black), copy.deepcopy(img_red))

        # We first check if it returns what it is supposed to, rounded to given decimal places for convenience
        expected_output = 147.2333748396
        val1 = round(float(student_output), places)
        val2 = round(float(expected_output), places)

        result = (val1 == val2)
        result_message = "Computing cosine similarity failed, expected " + str(val2) + " and got " + str(val1)
        self.assertEqual(result, True, result_message)


if __name__ == "__main__":
    test_classes_to_run = [Task_4_Testing]
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(test_classes_to_run)
    runner = unittest.TextTestRunner()
    runner.run(suite)
