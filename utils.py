import sys
import csv
import json

dataset_filename = "data.csv"
thetas_storage_filename = "thetas.json"
learning_rate = 0.05

def estimate_price(mileage, theta0, theta1):
    return float(theta0 + (theta1 * mileage))

def write_thetas_to_file(theta0, theta1):
    try:
        thetas_data = {
            'theta0': theta0,
            'theta1': theta1
        }
        with open(thetas_storage_filename, 'w', encoding='utf-8') as f:
            json.dump(thetas_data, f, ensure_ascii=False, indent=4)
    except:
        eprint("Error when writing ", thetas_storage_filename)

def read_thetas_from_file():
    try:
        with open(thetas_storage_filename) as json_file:
            data = json.load(json_file)
        return float(data['theta0']), float(data['theta1'])
    except:
        eprint("Error when reading ", thetas_storage_filename)

class DataItem:
    km = 0
    price = 0

    def __init__(self, data_dict):
        self.km = int(data_dict['km'])
        self.price = int(data_dict['price'])
    
    def __str__(self):
        return str(self.__dict__)

def dataset_to_vectors(dataset):
    km = []
    price = []
    try:
        for d in dataset:
            km.append(d.km)
            price.append(d.price)
    except:
        eprint("Dadataset with uncorrect formatting")
    return km, price

def read_dataset():
    dataset = []
    try:
        with open(dataset_filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for d in reader:
                try:
                    dataset.append(DataItem(d))
                except:
                    eprint("Dadataset with uncorrect formatting")
    except:
        eprint("Error when reading dataset")
    return dataset

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    sys.exit(1)


