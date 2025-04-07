##########################################################################################
# Task 2 [6 points out of 30] Basic evaluation
# Evaluate your classifier. On your own, implement a method that will create a confusion matrix based on the provided
# classified data. Then implement methods that will return TPs, FPs and FNs based on the confusion matrix.
# From these, implement binary precision, recall and f-measure, and their macro counterparts.
# Finally, implement the multiclass version of accuracy.
# Remember to be mindful of edge cases (the approach for handling them is explained in lecture slides).
# The template contains a range of functions you must implement and use appropriately for this task.
# The template also uses a range of functions implemented by the module leader to support you in this task,
# particularly relating to reading images and csv files accompanying this portfolio.
# You can start working on this task immediately. Please consult at the very least Week 3 materials.
##########################################################################################

import Helper
import Dummy
import numpy as np
from Task_1 import classification_scheme

# This function computes the confusion matrix based on the provided data.
#
# INPUT: classified_data   : a numpy array containing paths to images, actual classes and predicted classes.
#                            Please refer to Task 1 for precise format description. Remember, this data contains
#                            header row!
# OUTPUT: confusion_matrix : a numpy array representing the confusion matrix computed based on the classified_data.
#                            The order of elements MUST be the same as in the classification scheme.
#                            The columns correspond to actual classes and rows to predicted classes.
#                            In other words, confusion_matrix[0] should be understood
#                            as the row of values predicted as Female, and [row[0] for row in confusion_matrix] as the
#                            column of values that were actually Female (independently of if the classified data
#                            contained Female entries or not).

import numpy as np
from Task_1 import classification_scheme

def confusionMatrix(data: np.ndarray, class_list: list[str] = classification_scheme) -> np.ndarray:
    # Flatten and reshape if needed
    data = np.atleast_2d(data)

    if data.shape[1] == 1:
        # Likely a 1D array of CSV rows – split by comma
        data = np.array([row[0].split(',') for row in data])

    if data.shape[1] < 3:
        print("⚠️ Data shape:", data.shape)
        raise ValueError("Input data is malformed: expected at least 3 columns (path, actual, predicted).")

    class_to_index = {label: i for i, label in enumerate(class_list)}
    matrix = np.zeros((len(class_list), len(class_list)), dtype=np.uint32)

    actual_labels = data[1:, 1]
    predicted_labels = data[1:, 2]

    actual_idx = np.vectorize(class_to_index.get)(actual_labels)
    predicted_idx = np.vectorize(class_to_index.get)(predicted_labels)

    for pred_i, actual_i in zip(predicted_idx, actual_idx):
        if pred_i is not None and actual_i is not None:
            matrix[pred_i, actual_i] += 1  # predicted = rows, actual = columns

    return matrix

def computeAccuracy(conf_matrix: np.ndarray) -> float:
    total = conf_matrix.sum()
    if total == 0:
        return 0.0
    return np.trace(conf_matrix) / total

def computePrecision(conf_matrix: np.ndarray, class_list: list[str]) -> dict[str, float]:
    precisions = {}
    for i, label in enumerate(class_list):
        tp = conf_matrix[i, i]
        predicted_total = conf_matrix[:, i].sum()
        precisions[label] = tp / predicted_total if predicted_total > 0 else 0.0
    return precisions

def computeRecall(conf_matrix: np.ndarray, class_list: list[str]) -> dict[str, float]:
    recalls = {}
    for i, label in enumerate(class_list):
        tp = conf_matrix[i, i]
        actual_total = conf_matrix[i, :].sum()
        recalls[label] = tp / actual_total if actual_total > 0 else 0.0
    return recalls


# These functions compute per-class true positives and false positives/negatives based on the provided confusion matrix.
#
# INPUT: confusion_matrix : the numpy array representing the confusion matrix computed based on the classified_data.
#                           The order of elements is the same as  in the classification scheme.
#                           The columns correspond to actual classes and rows to predicted classes.
# OUTPUT: a list of ints representing appropriate true positive, false positive or false
#         negative values per a given class, in the same order as in the classification scheme. For example, tps[1]
#         corresponds to TPs for Male class.


def computeTPs(confusion_matrix: np.ndarray) -> list[int]:
    return [int(confusion_matrix[i][i]) for i in range(len(confusion_matrix))]

def computeFPs(confusion_matrix: np.ndarray) -> list[int]:
    return [
        int(confusion_matrix[i, :].sum() - confusion_matrix[i][i])
        for i in range(len(confusion_matrix))
    ]

def computeFNs(confusion_matrix: np.ndarray) -> list[int]:
    return [
        int(confusion_matrix[:, i].sum() - confusion_matrix[i][i])
        for i in range(len(confusion_matrix))
    ]

# These functions compute the binary measures based on the provided values. Not all measures use all of the values.
#
# INPUT: tp, fp, fn : the values of true positives, false positive and negatives
# OUTPUT: appropriate evaluation measure created using the binary approach.

def computeBinaryPrecision(tp: int, fp: int, fn: int) -> float:
    return tp / (tp + fp) if (tp + fp) > 0 else 0.0

def computeBinaryRecall(tp: int, fp: int, fn: int) -> float:
    return tp / (tp + fn) if (tp + fn) > 0 else 0.0

def computeBinaryFMeasure(tp: int, fp: int, fn: int) -> float:
    precision = computeBinaryPrecision(tp, fp, fn)
    recall = computeBinaryRecall(tp, fp, fn)
    if precision + recall == 0:
        return 0.0
    return 2 * (precision * recall) / (precision + recall)



# These functions compute the evaluation measures based on the provided values - macro precision, macro recall,
# macro f-measure, and accuracy (multiclass version). Not all measures use of all the values.
# You are expected to use appropriate binary counterparts when needed (binary recall for macro recall, binary precision
# for macro precision, binary f-measure for macro f-measure).
#
# INPUT: tps, fps, fns, data_size
#                       : the per-class true positives, false positive and negatives, and number of classified entries
#                         in the classified data (aka, don't count the header!)
# OUTPUT: appropriate evaluation measures created using the macro-average approach.

def computeMacroPrecision(tps: list[int], fps: list[int], fns: list[int], data_size: int) -> float:
    precisions = [computeBinaryPrecision(tp, fp, fn) for tp, fp, fn in zip(tps, fps, fns)]
    return sum(precisions) / len(precisions) if precisions else 0.0

def computeMacroRecall(tps: list[int], fps: list[int], fns: list[int], data_size: int) -> float:
    recalls = [computeBinaryRecall(tp, fp, fn) for tp, fp, fn in zip(tps, fps, fns)]
    return sum(recalls) / len(recalls) if recalls else 0.0

def computeMacroFMeasure(tps: list[int], fps: list[int], fns: list[int], data_size: int) -> float:
    f_measures = [computeBinaryFMeasure(tp, fp, fn) for tp, fp, fn in zip(tps, fps, fns)]
    return sum(f_measures) / len(f_measures) if f_measures else 0.0

def computeAccuracy(tps: list[int], fps: list[int], fns: list[int], data_size: int) -> float:
    total_tp = sum(tps)
    return total_tp / data_size if data_size > 0 else 0.0



# In this function you are expected to compute precision, recall, f-measure and accuracy of your classifier using
# the macro average approach.

# INPUT: classified_data   : a numpy array containing paths to images, actual classes and predicted classes.
#                            Please refer to Task 1 for precise format description.
#       confusion_func     : function to be invoked to compute the confusion matrix
#
# OUTPUT: computed measures
def evaluateKNN(classified_data: np.ndarray, confusion_func=confusionMatrix) -> tuple[float, float, float, float]:
    conf_matrix = confusion_func(classified_data, classification_scheme)
    tps = computeTPs(conf_matrix)
    fps = computeFPs(conf_matrix)
    fns = computeFNs(conf_matrix)
    data_size = len(classified_data) - 1  # exclude header

    precision = computeMacroPrecision(tps, fps, fns, data_size)
    recall = computeMacroRecall(tps, fps, fns, data_size)
    f_measure = computeMacroFMeasure(tps, fps, fns, data_size)
    accuracy = computeAccuracy(tps, fps, fns, data_size)

    return precision, recall, f_measure, accuracy



##########################################################################################
# You should not need to modify things below this line - it's mostly reading and writing #
# Be aware that error handling below is...limited.                                       #
##########################################################################################


# This function reads the necessary arguments (see parse_arguments function in Task_1_5),
# and based on them evaluates the kNN classifier.
def main():
    opts = Helper.parseArguments()
    if not opts:
        print("Missing input. Read the README file.")
        exit(1)
    print(f'Reading data from {opts["classified_data"]}')
    classified_data = Helper.readCSVFile(opts['classified_data'])
    if classified_data.size == 0:
        print("Classified data is empty, cannot run evaluation. Exiting Task 2.")
        return
    print('Evaluating kNN')
    result = evaluateKNN(classified_data)
    print('Result: precision {}; recall {}; f-measure {}; accuracy {}'.format(*result))


if __name__ == '__main__':
    main()
