##########################################################################################
# Task 1 [7 points out of 30] My first not-so-pretty image classifier
# Your first task is to implement the kNN classifier on your own. The template contains a range of functions
# you must implement and use appropriately for this task. The template also uses a range of functions implemented
# by the module leader to support you in this task, particularly relating to reading images and csv files accompanying
# this portfolio.
# You can start working on this task immediately. Please consult at the very least Week 2 materials.
##########################################################################################

import os
import Dummy
import Helper
import numpy
from typing import Callable
import Task_4

# Please replace with your student id, including the "c" at the beginning!!!
student_id = 'c22115555'

# This is the classification scheme you should use for kNN
classification_scheme = ['Female', 'Male', 'Primate', 'Rodent', 'Food']


# Given a dictionary of classes and their occurrences, returns a class from the scheme that is most common in that
# dictionary. In case there are multiple candidates, it follows the order of classes in the scheme.
# The function returns empty string if the input dictionary is empty, does not contain any classes from the scheme,
# or if all classes in the scheme have occurrence of 0.
#
# INPUT: nearest_neighbours_classes
#                           : a dictionary that, for each and every class in the scheme, states the occurrence number
#                             of this class (this particular value is calculated elsewhere). You cannot assume
#                             any particular order of elements in the dictionary.
#
# OUTPUT: winner            : a class from classification scheme that is most common in the input variable.
#                             In case there are multiple candidates, it follows the order of classes in the scheme.
#                             Returns empty string if the input dictionary is empty, does not contain any classes
#                             from the scheme, or if all classes in the scheme have occurrence of 0
#

def getMostCommonClass(nearest_neighbours_classes: dict[str, int]) -> str:
    # Filter to only classes in the classification scheme
    valid_classes = {
        cls: nearest_neighbours_classes.get(cls, 0)
        for cls in classification_scheme
    }

    # Find class with highest count (respecting order)
    max_count = max(valid_classes.values(), default=0)
    if max_count == 0:
        return ''

    for cls in classification_scheme:
        if valid_classes[cls] == max_count:
            return cls

    return ''



# The function finds the k nearest neighbours from measures_classes, and returns a dictionary made of classes
# and their occurrences based on these k nearest neighbours.
#
# INPUT:  measure_classes   : a list of tuples that contain two elements each - a distance/similarity value
#                             and class from scheme (in that order). You cannot assume that the input is
#                             pre-sorted in any way.
#         k                 : the value of k neighbours, greater than 0, not guaranteed to be smaller than data size.
#         similarity_flag   : a boolean value stating that the measure used to produce the values above is a distance
#                             (False) or a similarity (True)
# OUTPUT: nearest_neighbours_classes
#                           : a dictionary that, for each class in the scheme, states how often this class
#                             was in the k nearest neighbours
#
def getKNearestNeighboursClass(measure_classes: list[tuple[float, str]], k: int) -> dict[str, int]:
    # Sort by the first element (distance or similarity)
    sorted_measurements = sorted(measure_classes, key=lambda x: x[0])

    # Take the top-k entries
    k_nearest = sorted_measurements[:k]

    # Count class occurrences
    class_counts = {}
    for _, label in k_nearest:
        if label in class_counts:
            class_counts[label] += 1
        else:
            class_counts[label] = 1

    return class_counts


# In this function I expect you to implement the kNN classifier. You are free to define any number of helper functions
# you need for this! You need to use all the other functions in the part of the template above.
#
# INPUT:  training_data       : a numpy array that was read from the training data csv
#         data_to_classify    : a numpy array  that was read from the data to classify csv;
#                             this data is NOT be used for training the classifier, but for running and testing it
#                             (see parse_arguments function)
#         k                   : the value of k neighbours, greater than 0, not guaranteed to be smaller than data size.
#         measure_func        : the function to be invoked to calculate similarity/distance (see Task 4 for
#                               some teacher-defined ones)
#         similarity_flag     : a boolean value stating that the measure above used to produce the values is a distance
#                             (False) or a similarity (True)
#     most_common_class_func  : the function to be invoked to find the most common class among the neighbours
#                             (by default, it is the one from above)
# get_neighbour_classes_func  : the function to be invoked to find the classes of nearest neighbours
#                             (by default, it is the one from above)
#         read_func           : the function to be invoked to find to read and resize images
#                             (by default, it is the Helper function)
#  OUTPUT: classified_data    : a numpy array which expands the data_to_classify with the results on how your
#                             classifier has classified a given image.

def myKnn(
        test_image: list[float],
        train_images: list[list[float]],
        train_labels: list[str],
        k: int,
        distance_function: Callable[[list[float], list[float]], float]
) -> str:
    # Step 1: Calculate distances between test_image and each train_image
    measure_classes = []
    for i in range(len(train_images)):
        dist = distance_function(test_image, train_images[i])
        label = train_labels[i]
        measure_classes.append((dist, label))

    # Step 2: Get top-k nearest classes
    k_classes = getKNearestNeighboursClass(measure_classes, k)

    # Step 3: Return the most common class among the top-k
    return getMostCommonClass(k_classes)

def getClassesOfKNearestNeighbours(measures_classes: list[tuple[float, str]], k: int, similarity_flag: bool) -> dict[str, int]:
    # Sort based on distance (asc) or similarity (desc)
    sorted_measures = sorted(measures_classes, key=lambda x: x[0], reverse=similarity_flag)

    # Take the top-k
    k_nearest = sorted_measures[:k]

    # Count all classes from the scheme, initialize with 0
    class_counts = {cls: 0 for cls in classification_scheme}
    for _, label in k_nearest:
        if label in class_counts:
            class_counts[label] += 1

    return class_counts

import os

import os

import os

def kNN(training_data: numpy.typing.NDArray, data_to_classify: numpy.typing.NDArray, k: int, measure_func: Callable,
        similarity_flag: bool, most_common_class_func=getMostCommonClass,
        get_neighbour_classes_func=getClassesOfKNearestNeighbours,
        read_func=Helper.readAndResize) -> numpy.typing.NDArray:

    output_rows = [['Path', 'ActualClass', 'PredictedClass']]
    dist_cache = {}        # (test_path, train_path): distance
    image_cache = {}       # train_path: image
    train_label_lookup = {}  # train_path: class

    #  Preload all valid training images + labels
    for train_row in training_data[1:]:  # skip header
        train_path = str(train_row[0]).strip()
        train_label = str(train_row[1]).strip()

        if not os.path.isfile(train_path):
            print(f"[WARN] Train image not found: {train_path}")
            continue

        train_img = read_func(train_path)
        if train_img is None:
            print(f"[WARN] Could not read train image: {train_path}")
            continue

        image_cache[train_path] = train_img
        train_label_lookup[train_path] = train_label

    #  Iterate over test data
    for test_row in data_to_classify[1:]:  # skip header
        test_path = str(test_row[0]).strip()
        actual_class = str(test_row[1]).strip()

        if not os.path.isfile(test_path):
            print(f"[WARN] Test image not found: {test_path}")
            continue

        test_img = read_func(test_path)
        if test_img is None:
            print(f"[WARN] Could not read test image: {test_path}")
            continue

        measures_classes = []

        #  Compare to each preloaded training image
        for train_path, train_img in image_cache.items():
            cache_key = (test_path, train_path)
            if cache_key in dist_cache:
                dist = dist_cache[cache_key]
            else:
                # Match image dtypes if needed
                if test_img.dtype != train_img.dtype:
                    test_img = test_img.astype('uint8')
                    train_img = train_img.astype('uint8')

                dist = measure_func(test_img, train_img)
                dist_cache[cache_key] = dist

            # Look up label directly
            train_class = train_label_lookup.get(train_path)
            if train_class is not None:
                measures_classes.append((dist, train_class))

        if not measures_classes:
            continue

        class_counts = get_neighbour_classes_func(measures_classes, k, similarity_flag)
        predicted_class = most_common_class_func(class_counts)

        output_rows.append([test_path, actual_class, predicted_class])

    return numpy.array(output_rows, dtype=str)



##########################################################################################
# Do not modify things below this line - it's mostly reading and writing #
# Be aware that error handling below is...limited.                                       #
##########################################################################################


# This function reads the necessary arguments from input (see parse_arguments function in Helper file),
# and based on them executes
# the kNN classifier. If the "unseen" mode is on, the results are written to a file.

def main():
    opts = Helper.parseArguments()
    if not opts:
        print("Missing input. Read the README file.")
        exit(1)
    print(f'Reading data from {opts["training_data"]} and {opts["data_to_classify"]}')
    training_data = Helper.readCSVFile(opts['training_data'])
    data_to_classify = Helper.readCSVFile(opts['data_to_classify'])
    unseen = opts['mode']
    if training_data.size == 0 or data_to_classify.size == 0:
        print("Not all of the input data is present, cannot run kNN. Exiting Task 1.")
        return
    if opts['k'] is None or opts['k']<1:
        print("Value of k is missing from input or too small, cannot run kNN. Exiting Task 1.")
        return
    if opts['simflag'] is None:
        print("Similarity flag is missing from input, cannot run kNN. Exiting Task 1.")
        return
    print('Running kNN')
    try:
        result = kNN(training_data, data_to_classify, opts['k'], eval(opts['measure']), opts['simflag'])
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
    if unseen:
        path = os.path.dirname(os.path.realpath(opts['data_to_classify']))
        out = f'{path}/{student_id}_classified_data.csv'
        print(f'Writing data to {out}')
        Helper.writeCSVFile(out, result)


if __name__ == '__main__':
    main()
