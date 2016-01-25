import csv

def load_csv(filename):
    lines = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            lines.append(line)
    return lines

def load_adult_data():
    return load_csv("adult.data")

#TODO: Possibly use different data for training and validation
def load_adult_train_data():
    return load_adult_data()

def load_adult_valid_data():
    return load_adult_data()

