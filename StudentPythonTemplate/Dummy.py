# If for some reason you have not completed Task 1 or Task 2 but can completed Task 3, feel free to use the following
# dummy functions.
import numpy
import sewar

import Helper
from typing import Callable

classification_scheme = ['Female', 'Male', 'Primate', 'Rodent', 'Food']


def dummyKNN(training_data, data_to_classify, k, measure_func, similarity_flag, most_common_class_func,
             get_neighbour_classes_func, read_func, validate_format_func):
    classified_data = [['Path', 'ActualClass', 'PredictedClass']]
    for i in range(1, len(data_to_classify)):
        # this is only a dummy function, we default classification to Food
        classified_data.append(data_to_classify[i] + ['Food'])
    print("Running dummyKNN")
    return classified_data


def dummyEvaluateKNN(classified_data, confusion_func):
    precision = float(2)
    recall = float(2)
    f_measure = float(2)
    accuracy = float(2)
    return precision, recall, f_measure, accuracy
