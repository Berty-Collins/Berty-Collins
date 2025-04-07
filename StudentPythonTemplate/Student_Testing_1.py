import unittest
import sys
import cv2
from io import StringIO
import copy
import logging

import Task_4
from Task_1 import *
import Dummy

sys.tracebacklimit = 6

training_data = Helper.readCSVFile("../training_data.csv")
testing_data = Helper.readCSVFile("../testing_data.csv")


class Task_1_Testing(unittest.TestCase):
    #
    # This function contains one unit test for getClassesOfKNearestNeighbours.
    # The function simply checks one possible behaviour, and there are many more possible. More than that
    # is also supporting markers. Feel free to expand on these tests for your own purposes. This area is not marked
    # or checked.
    #
    def test1_getClassesOfKNearestNeighbours_distance_behaviour(self):
        # Setting up the variables - value of k, the input measure_classes, and the output we expect for a distance approach
        k = 3
        measure_classes = [(0.5, 'Female'), (0.2, 'Male'), (1, 'Male'), (3, 'Primate'), (2.0, 'Female')]
        outputIfDist = {'Female': 1, 'Male': 2, 'Primate': 0, 'Rodent': 0, 'Food': 0}
        student_output = getClassesOfKNearestNeighbours(copy.deepcopy(measure_classes), k, False)
        result = student_output == outputIfDist
        result_message = 'Produced output is not equal to the expected one. Expected ' + str(
            outputIfDist) + " and got " + str(student_output)
        self.assertEqual(result, True, result_message)

    # This function contains one unit test for getMostCommonClass.
    # The function simply checks one possible behaviour, and there are many more possible. More than that
    # is also supporting markers. Feel free to expand on these tests for your own purposes. This area is not marked
    # or checked.
    #
    def test2_getMostCommonClass(self):
        input1 = {'Female': 2, 'Male': 5, 'Primate': 1, 'Rodent': 3, 'Food': 0}
        answer1 = 'Male'
        student_output = getMostCommonClass(copy.deepcopy(input1))
        result = student_output == answer1
        result_message = 'Produced output is not equal to the expected one. Expected ' + str(
            answer1) + " and got " + str(student_output)
        self.assertEqual(result, True, result_message)

    # This function contains one unit test checking if kNN output is in the right format (no guarantee
    # that the content is right itself!)
    # The function simply checks one possible behaviour, and there are many more possible. More than that
    # is also supporting markers. Feel free to expand on these tests for your own purposes. This area is not marked
    # or checked.
    #
    def test3_kNNOutputFormat(self):
        output = kNN(copy.deepcopy(training_data), copy.deepcopy(testing_data), 3, Task_4.computePSNRSimilarity,
                     True)
        result = validateDataFormat(output)
        self.assertEqual(result, True,
                         "kNN function output is not formatted well")


# This function checks if the classified data from kNN has the right format (not content, just format!)
# It checks if the required columns are present, and if entries are paths and classes
def validateDataFormat(data_to_validate):
    formatCorrect = True
    if not set(["Path", "ActualClass", "PredictedClass"]).issubset(set(data_to_validate[0])):
        return False
    for row in data_to_validate[1:]:
        isFile = os.path.isfile(row[0])
        isClass = row[1] in classification_scheme
        isClass = isClass and row[2] in classification_scheme
        if not isFile or not isClass:
            return False
    return formatCorrect


if __name__ == "__main__":
    test_classes_to_run = Task_1_Testing
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(test_classes_to_run)
    runner = unittest.TextTestRunner()
    runner.run(suite)
