import yaml
import csv

def read_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def read_csv(file_path):
    data = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data