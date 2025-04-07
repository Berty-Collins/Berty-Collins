import unittest
import numpy
import sys
import copy
import Dummy
import logging

import Task_2
from Task_2 import *
from Task_1 import *

numpy.seterr(divide='raise')
numpy.seterr(invalid='raise')

classified_data = numpy.asarray(Helper.readCSVFile("../Extras/classified_data.csv"))
expected_matrix = numpy.array([[2, 2, 0, 1, 1], [1, 2, 0, 0, 0], [0, 1, 1, 0, 1], [1, 2, 1, 3, 0], [0, 1, 0, 0, 1]])


class Task_2_Testing(unittest.TestCase):

    # This function contains one unit test for confusionMatrix.
    # The function simply checks one possible behaviour, and there are many more possible. More than that
    # is also supporting markers. Feel free to expand on these tests for your own purposes. This area is not marked
    # or checked.
    #
    def test1_confusionMatrix_basic(self):
        expected = copy.deepcopy(expected_matrix)
        student_matrix = Task_2.confusionMatrix(copy.deepcopy(classified_data))
        # Using a helper function for equality checking, given some funky data formats sometimes
        result = arrayEqual(student_matrix, expected)
        result_message = "confusionMatrix construction failed. Got \n" + str(student_matrix) + " and expected \n" + str(
            expected)
        self.assertEqual(result, True, result_message)

    # Here we check if TPs are calculated well
    # This function contains just one test.
    # The function simply checks one possible behaviour, and there are many more possible. More than that
    # is also supporting markers. Feel free to expand on these tests for your own purposes. This area is not marked
    # or checked.
    #
    def test2_computeTPs(self):
        student_result = Task_2.computeTPs(copy.deepcopy(expected_matrix))
        expected = [2, 2, 1, 3, 1]
        #We check with roundEqual since students should be using ints but don't always do ><
        result = roundEqual(student_result, expected)
        result_message = "Computing TPs failed. Expected \n" + str(expected) + " and got \n" + str(student_result)
        self.assertEqual(result, True, result_message)

    # Here we check if FPs are calculated well
    # This function contains just one test.
    # The function simply checks one possible behaviour, and there are many more possible. More than that
    # is also supporting markers. Feel free to expand on these tests for your own purposes. This area is not marked
    # or checked.
    def test3_computeFPs(self):
        student_result = Task_2.computeFPs(copy.deepcopy(expected_matrix))
        expected = [4, 1, 2, 4, 1]
        # We check with roundEqual since students should be using ints but don't always do ><
        result = roundEqual(student_result, expected)
        result_message = "Computing FPs failed. Expected \n" + str(expected) + " and got \n" + str(student_result)
        self.assertEqual(result, True, result_message)

    # Here we check if FNs are calculated well
    # This function contains just one test.
    # The function simply checks one possible behaviour, and there are many more possible. More than that
    # is also supporting markers. Feel free to expand on these tests for your own purposes. This area is not marked
    # or checked.
    def test4_computeFNs(self):
        student_result = Task_2.computeFNs(copy.deepcopy(expected_matrix))
        expected = [2, 6, 1, 1, 2]
        # We check with roundEqual since students should be using ints but don't always do ><
        result = roundEqual(student_result, expected)
        result_message = "Computing FNs failed. Expected \n" + str(expected) + " and got \n" + str(student_result)
        self.assertEqual(result, True, result_message)

    # Here we check if binary precision is calculated well
    # This function contains just one test.
    # The function simply checks one possible behaviour, and there are many more possible. More than that
    # is also supporting markers. Feel free to expand on these tests for your own purposes. This area is not marked
    # or checked.

    def test5_computeBinaryPrecision(self):
        student_result = Task_2.computeBinaryPrecision(2, 6, 1)
        expected = 0.25

        result = roundEqual([student_result], [expected])
        result_message = "Computing binary precision failed. Expected \n" + str(expected) + " and got \n" + str(
            student_result)
        self.assertEqual(result, True, result_message)

    # Here we check if binary recall is calculated well
    # This function contains just one test.
    # The function simply checks one possible behaviour, and there are many more possible. More than that
    # is also supporting markers. Feel free to expand on these tests for your own purposes. This area is not marked
    # or checked.

    def test6_computeBinaryRecall(self):
        student_result = Task_2.computeBinaryRecall(2, 6, 1)
        expected = 0.66666666666667

        result = roundEqual([student_result], [expected])
        result_message = "Computing binary recall failed. Expected \n" + str(expected) + " and got \n" + str(
            student_result)
        self.assertEqual(result, True, result_message)

    # Here we check if binary f-measure is calculated well
    # This function contains just one test.
    # The function simply checks one possible behaviour, and there are many more possible. More than that
    # is also supporting markers. Feel free to expand on these tests for your own purposes. This area is not marked
    # or checked.

    def test7_computeBinaryFMeasure(self):
        student_result = Task_2.computeBinaryFMeasure(2, 6, 1)
        expected = 0.363636364

        result = roundEqual([student_result], [expected])
        result_message = "Computing binary f-measure failed. Expected \n" + str(expected) + " and got \n" + str(
            student_result)
        self.assertEqual(result, True, result_message)

    # Here we check if macro precision is calculated well
    # This function contains just one test.
    # The function simply checks one possible behaviour, and there are many more possible. More than that
    # is also supporting markers. Feel free to expand on these tests for your own purposes. This area is not marked
    # or checked.
    def test8_computeMacroPrecision(self):
        tps = [2, 2, 1, 3, 1]
        fns = [2, 6, 1, 1, 2]
        fps = [4, 1, 2, 4, 1]
        data_size = 21
        student_result = Task_2.computeMacroPrecision(tps, fps, fns, data_size)
        expected = 0.4523809523809524

        result = roundEqual([student_result], [expected])
        result_message = "Computing macro precision failed. Expected \n" + str(expected) + " and got \n" + str(
            student_result)
        self.assertEqual(result, True, result_message)

    # Here we check if macro recall is calculated well
    # This function contains just one test.
    # The function simply checks one possible behaviour, and there are many more possible. More than that
    # is also supporting markers. Feel free to expand on these tests for your own purposes. This area is not marked
    # or checked.

    def test9_computeMacroRecall(self):
        tps = [2, 2, 1, 3, 1]
        fns = [2, 6, 1, 1, 2]
        fps = [4, 1, 2, 4, 1]
        data_size = 21
        student_result = Task_2.computeMacroRecall(tps, fps, fns, data_size)
        expected = 0.4666666666666667

        result = roundEqual([student_result], [expected])
        result_message = "Computing macro recall failed. Expected \n" + str(expected) + " and got \n" + str(
            student_result)
        self.assertEqual(result, True, result_message)

    # Here we check if macro f-measure is calculated well
    # This function contains just one test.
    # The function simply checks one possible behaviour, and there are many more possible. More than that
    # is also supporting markers. Feel free to expand on these tests for your own purposes. This area is not marked
    # or checked.

    def testx10_computeMacroFMeasure(self):
        tps = [2, 2, 1, 3, 1]
        fns = [2, 6, 1, 1, 2]
        fps = [4, 1, 2, 4, 1]
        data_size = 21
        student_result = Task_2.computeMacroFMeasure(tps, fps, fns, data_size)
        expected = 0.42181818181818176

        result = roundEqual([student_result], [expected])
        result_message = "Computing macro f-measure failed. Expected \n" + str(expected) + " and got \n" + str(
            student_result)
        self.assertEqual(result, True, result_message)

    # Here we check if accuracy is calculated well
    # This function contains just one test.
    # The function simply checks one possible behaviour, and there are many more possible. More than that
    # is also supporting markers. Feel free to expand on these tests for your own purposes. This area is not marked
    # or checked.

    def testx11_computeAccuracy(self):
        tps = [2, 2, 1, 3, 1]
        fns = [2, 6, 1, 1, 2]
        fps = [4, 1, 2, 4, 1]
        data_size = 21
        student_result = Task_2.computeAccuracy(tps, fps, fns, data_size)
        expected = 0.42857142857142855

        result = roundEqual([student_result], [expected])
        result_message = "Computing accuracy failed. Expected \n" + str(expected) + " and got \n" + str(
            student_result)
        self.assertEqual(result, True, result_message)


def arrayEqual(data1, data2):
    nums1 = numpy.array(data1).flatten()
    nums2 = numpy.array(data2).flatten()
    return roundEqual(nums1, nums2)


def roundEqual(nums1, nums2):
    if len(nums1) != len(nums2):
        return False
    for i in range(0, len(nums1)):
        v1 = round(float(nums1[i]), 4)
        v2 = round(float(nums2[i]), 4)
        if v1 != v2:
            return False
    return True


if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(Task_2_Testing)
    runner = unittest.TextTestRunner()
    runner.run(suite)
