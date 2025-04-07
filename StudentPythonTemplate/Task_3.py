# In this file please complete the following task:
#
# Task 3 [7 points out of 30] Cross validation
# On your own, evaluate your classifier using the k-fold cross-validation technique covered in the lectures
# (use the training data only). You need to implement the data partitioning and the training and testing data per
# round preparation functions on your own. Output the average precisions, recalls, F-measures and accuracies resulting
# from cross-validation by implementing the relevant function and incorporating what you have implemented in Task 1
# and Task 2 appropriately.
#
# You can rely on the dummy functions if you have not attempted these tasks, and during marking the code will be
# invoked against teacher-implemented versions of these tasks. When invoking functions from Tasks 1 and 2, rely only on
# those that were already defined in the template.
#
# You can start working on this task immediately. Please consult at the very least Week 3 materials.


import os

import Helper
import Task_1
import Task_2
import Dummy
import numpy
import Task_4
from typing import Callable


# This function takes in the data for cross evaluation and the number of partitions to split the data into.
# The input data contains the header row. The resulting partitions do not.

# INPUT: training_data     : a numpy array containing paths to images and actual classes (at the very least, but other
#                            columns can be ignored)
#                            Please refer to Task 1 for precise format description. Remember, this data contains
#                            header row!
#        f                 : the number of partitions to split the data into, value is greater than 0,
#                            not guaranteed to be smaller than data size.
# OUTPUT: partition_list   : a list of numpy arrays, where each array represents a partition, so a subset of entries
#                           of the original dataset s.t. all partitions are disjoint, roughly same size (can differ by
#                            at most 1), and the union of all partitions equals the original dataset minus header row.
#                           THE PARTITIONS DO NOT CONTAIN HEADER ROWS.

def partitionData(training_data: numpy.typing.NDArray, f: int) -> list[numpy.typing.NDArray]:
    # Have fun! Below is just a dummy for returns, feel free to edit
    partition_list = []
    return partition_list


# This function transforms partitions into training and testing data for each cross-validation round (there are
# as many rounds as there are partitions); in other words, we prepare the folds.
# Please remember that the training and testing data for each round must include a header at this point.

# INPUT: partition_list     : a list of numpy arrays, where each array represents a partition (see partitionData function)
#        f                  : the number of folds to use in cross-validation, which is the same as the number of
#                             partitions the data was supposed to be split to, and the number of rounds in cross-validation.
#                             Value is greater than 0.
# OUTPUT: folds             : a list of 3-tuple s.t. the first element is the round number, second is the numpy array
#                             representing the training data for that round, and third is the numpy array representing
#                             the testing data for that round
#                             The round numbers START WITH 0
#                             You must make sure that the training and testing data are ready for use
#                             (e.g. contain the right headers already)


def preparingDataForCrossValidation(partition_list: list[numpy.typing.NDArray], f: int) \
        -> list[tuple[int, numpy.typing.NDArray, numpy.typing.NDArray]]:
    # This is just for error handling, if for some magical reason f and number of partitions are not the same,
    # then something must have gone wrong in the other functions and you should investigate it
    if len(partition_list) != f:
        print("Something went really wrong! Why is the number of partitions different from f??")
        return []
    # Defining the header here for your convenience
    header = numpy.array([["Path", "ActualClass"]])
    folds = []
    # Implement your code here
    return folds


# This function takes the classified data from each cross validation round and calculates the average precision, recall,
# accuracy and f-measure for them.
# Invoke either the Task 2 evaluation function or the dummy function here, do not code from scratch!
#
# INPUT: classified_data_list
#                           : a list of numpy arrays representing classified data computed for each cross validation round
#        evaluation_func    : the function to be invoked for the evaluation (by default, it is the one from
#                             Task_2, but you can use dummy)
# OUTPUT: avg_precision, avg_recall, avg_f_measure, avg_accuracy
#                           : average evaluation measures. You are expected to evaluate every classified data in the
#                             list and average out these values in the usual way.

def evaluateResults(classified_data_list: list[numpy.typing.NDArray], evaluation_func=Task_2.evaluateKNN) \
        -> tuple[float, float, float, float]:
    avg_precision = float(0)
    avg_recall = float(0)
    avg_f_measure = float(0)
    avg_accuracy = float(0)
    # There are multiple ways to count average measures during cross-validation. For the purpose of this portfolio,
    # it's fine to just compute the values for each round and average them out in the usual way.

    return avg_precision, avg_recall, avg_f_measure, avg_accuracy


# In this task you are expected to perform and evaluate cross-validation on a given dataset.
# You are expected to partition the input dataset into f partitions, then arrange them into training and testing
# data for each cross validation round, and then run kNN for each round using this data and k, measure_func, and
# similarity_flag that are provided at input (see Task 1 for kNN input for more details).
# The results for each round are collected into a list and then evaluated.
#
# You are then asked to produce an output dataset which extends the original input training_data by adding
# "PredictedClass" and "FoldNumber" columns, which for each entry state what class it got predicted when it
# landed in a testing fold and what the number of that fold was (everything is in string format).
# This output dataset is then extended by two extra rows which add the average measures at the end.
#
# You are expected to invoke the Task 1 kNN classifier or the Dummy classifier here, do not implement these things
# from scratch! You must use the other relevant function defined in this file.
#
# INPUT: training_data      : a numpy array that was read from the training data csv (see parse_arguments function)
#        f                  : the number of folds, greater than 0, not guaranteed to be smaller than data size.
#        k                  : the value of k neighbours, greater than 0, not guaranteed to be smaller than data size.
#        measure_func       : the function to be invoked to calculate similarity/distance (see Task 4 for
#                               some teacher-defined ones)
#        similarity_flag    : a boolean value stating that the measure above used to produce the values is a distance
#                             (False) or a similarity (True)
#        knn_func           : the function to be invoked for the classification (by default, it is the one from
#                             Task_1, but you can use dummy)
#        partition_func     : the function used to partition the input dataset (by default, it is the one above)
#        prep_func          : the function used to transform the partitions into appropriate folds
#                            (by default, it is the one above)
#        eval_func          : the function used to evaluate cross validation (by default, it is the one above)
# OUTPUT: output_dataset    : a numpy array which extends the original input training_data by adding "PredictedClass"
#                             and "FoldNumber" columns, which for each entry state what class it got predicted when it
#                             landed in a testing fold and what the number of that fold was (everything is in string
#                             format). This output dataset is then extended by two extra rows which add the average
#                             measures at the end (see the h and v variables).
def crossEvaluateKNN(training_data: numpy.typing.NDArray, f: int, k: int, measure_func: Callable,
                     similarity_flag: bool, knn_func=Task_1.kNN,
                     partition_func=partitionData, prep_func=preparingDataForCrossValidation,
                     eval_func=evaluateResults) -> numpy.typing.NDArray:
    # This adds the header
    output_dataset = numpy.array([['Path', 'ActualClass', 'PredictedClass', 'FoldNumber']])
    avg_precision = -1.0;
    avg_recall = -1.0;
    avg_fMeasure = -1.0;
    avg_accuracy = -1.0;
    classified_list = []

    # Have fun with the computations!

    # The measures are now added to the end.
    h = ['avg_precision', 'avg_recall', 'avg_f_measure', 'avg_accuracy']
    v = [avg_precision, avg_recall, avg_fMeasure, avg_accuracy]

    output_dataset = numpy.append(output_dataset, [h], axis=0)
    output_dataset = numpy.append(output_dataset, [v], axis=0)

    return output_dataset


##########################################################################################
# You should not need to modify things below this line - it's mostly reading and writing #
# Be aware that error handling below is...limited.                                       #
##########################################################################################


# This function reads the necessary arguments (see parse_arguments function in Task_1_5),
# and based on them evaluates the kNN classifier using the cross-validation technique. The results
# are written into an appropriate csv file.
def main():
    opts = Helper.parseArguments()
    if not opts:
        print("Missing input. Read the README file.")
        exit(1)
    print(f'Reading data from {opts["training_data"]}')
    training_data = Helper.readCSVFile(opts['training_data'])
    if training_data.size == 0:
        print("Input data is empty, cannot run cross-validation. Exiting Task 3.")
        return
    if opts['f'] is None or opts['f'] < 1:
        print("Value of f is missing from input or too small, cannot run cross validation. Exiting Task 3.")
        return
    if opts['k'] is None or opts['k'] < 1:
        print("Value of k is missing from input or too small, cannot run cross validation. Exiting Task 3.")
        return
    if opts['simflag'] is None:
        print("Similarity flag is missing from input, cannot run cross validation. Exiting Task 3.")
        return
    print('Running cross validation')
    try:
        result = crossEvaluateKNN(training_data, opts['f'], opts['k'], eval(opts['measure']), opts['simflag'])
    except NameError as nerror:
        print(nerror)
        print("Wrong measure function name was passed to the function, please double check the function name. "
              "For example, try 'Task_4.computePSNRSimilarity' and make sure you have not deleted any imports "
              "from the template.")
        return
    except TypeError as terror:
        print("Measure function is incorrect or missing, please double check the input. "
              "For example, try 'Task_4.computePSNRSimilarity' and make sure you have not deleted any imports "
              "from the template.")
        return
    path = os.path.dirname(os.path.realpath(opts['training_data']))
    out = f'{path}/{Task_1.student_id}_cross_validation.csv'
    print(f'Writing data to {out}')
    Helper.writeCSVFile(out, result)


if __name__ == '__main__':
    main()
