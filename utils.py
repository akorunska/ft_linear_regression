import sys
import csv

dataset_filename = "./data.csv"
thetas_storage_filename = "./thetas.json"
learning_rate = 0.2

def estimate_price(mileage, theta0, theta1):
    return float(theta0 + (theta1 * mileage));

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
    for d in dataset:
        km.append(d.km)
        price.append(d.price)
    return km, price


def read_dataset():
    dataset = []
    with open(dataset_filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for d in reader:
            dataset.append(DataItem(d))
    return dataset

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    sys.exit(1)
