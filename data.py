import csv

def process(raw):
    data = []
    for r in raw:
        point = {}
        point["label"] = (r['income'] == '>50K')

        features = []
        features.append(1.)
        features.append(float(r['age'])/100)
        features.append(float(r['education_num'])/20)
        features.append(r['marital'] == 'Married-civ-spouse')
        #TODO: Add more feature extraction rules here!
        point['features'] = features
        data.append(point)
    return data

def load_csv(filename):
    lines = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            lines.append(line)
    return lines

def load_adult_data():
    return process(load_csv("adult.data"))

#TODO: Possibly use different data for training and validation
def load_adult_train_data():
    return load_adult_data()

def load_adult_valid_data():
    return load_adult_data()

def load_adult_test_data():
    return process(load_csv("adult.test"))

