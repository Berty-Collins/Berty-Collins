##########################################################################################
# Random helper functions. DO NOT MODIFY.
# Be aware that error handling below is...limited.                                       #
##########################################################################################

import cv2
import numpy
import csv
import argparse


# This function does reading and resizing of an image located in a give path on your drive.
# DO NOT REMOVE ANY COLOURS. DO NOT MODIFY PATHS. DO NOT FLATTEN IMAGES.
#
# INPUT:  imagePath         : path to image. DO NOT MODIFY - take from the file as-is. Things like appending "..\"
#                             to the file path within the code are not permitted.
#         width, height     : width and height dimensions to which you are asked to resize your image
#
# OUTPUT: image             : numpy array representing the read and resized image in RGB format
#                             (empty if the image is not found at a given path).
#                             Removing colour channels (e.g. transforming array to grayscale) or flattening the image
#                             ARE NOT PERMITTED.
#

def readAndResize(image_path: str, width=60, height=30) -> numpy.typing.NDArray:
    try:
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)
        image = numpy.asarray(image)
    except:
        print("Image cannot be read at " + str(image_path))
        image = numpy.asarray([])
    return image


# Straightforward function to read the data contained in the file "filename"
def readCSVFile(filename: str) -> numpy.typing.NDArray:
    import csv
    import numpy

    lines = []
    try:
        with open(filename, newline='') as infile:
            # Read first line to check if it's tab-separated
            first_line = infile.readline()
            delimiter = '\t' if '\t' in first_line else ','
            infile.seek(0)  # Go back to the start of the file

            reader = csv.reader(infile, delimiter=delimiter)
            for line in reader:
                lines.append(line)
    except FileNotFoundError as ferror:
        print(ferror)
        print("The data you wanted to read was not at the location passed to the function. Please make sure to "
              "provide a correct path to file.")
    except TypeError as terror:
        print(terror)
        print("Please provide a proper path to file, the input is missing.")

    return numpy.array(lines)


# Straightforward function to write the data contained in "lines" to a file "filename"
def writeCSVFile(filename: str, lines: numpy.typing.NDArray):
    with open(filename, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(lines)


# Straightforward function to transform string to boolean value
def strtobool(value: str) -> bool:
    value = value.lower()
    if value in ("y", "yes", "on", "1", "true", "t"):
        return True
    return False


# This function simply parses the arguments passed to main. It looks for the following:
#       -k              : the value of k neighbours
#       -f              : the number of folds to be used for cross-validation
#       -measure        : function to compute a given similarity/distance measure
#       -simflag        : flag telling us whether the above measure is a distance (False) or similarity (True)
#       -u              : flag for how to understand the data. If -u is used, it means data is "unseen" and
#                         the classification will be written to the file. If -u is not used, it means the data is
#                         for training purposes and no writing to files will happen.
#       training_data   : csv file to be used for training the classifier, contains two columns: "Path" that denotes
#                         the path to a given image file, and "ActualClass" that gives the true class of the image
#                         according to the classification scheme defined at the start of this file.
#       data_to_classify: csv file formatted the same way as training_data; it will NOT be used for training
#                         the classifier, but for running and testing it
#       classified      : csv file extending training data format with 'PredictedClass' column
#       mcc, gnc, rrf, vf,cf,sf,al
#                       : staff variables, do not use
#
def parseArguments() -> dict:
    parser = argparse.ArgumentParser(description='Processes files ')
    parser.add_argument('-k', type=int)
    parser.add_argument('-f', type=int)
    parser.add_argument('-m', '--measure')
    parser.add_argument('-s', '--simflag', type=lambda x: bool(strtobool(x)))
    parser.add_argument('-u', '--unseen', action='store_true')
    parser.add_argument('-train', type=str)
    parser.add_argument('-test', type=str)
    parser.add_argument('-classified', type=str)
    parser.add_argument('-imga', type=str)
    parser.add_argument('-imgb', type=str)
    params = parser.parse_args()

    opt = {'k': params.k,
           'f': params.f,
           'measure': params.measure,
           'simflag': params.simflag,
           'mode': params.unseen,
           'training_data': params.train,
           'data_to_classify': params.test,
           'classified_data': params.classified,
           'image_a': params.imga,
           'image_b': params.imgb,
           }
    return opt
