
import csv
import pandas as pd

def create_ls():
    ls = []
    for i in range (0,18):
        ls.append(i)
    return ls


def adjust_csv_to_DataFrame(path):
    ls = create_ls()
    df = pd.read_csv(path, names=ls)

    # for no Rajnish Data
    # df = pd.read_csv(path)
    return df


