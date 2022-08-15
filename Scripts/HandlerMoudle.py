import itertools
import CSV_Lister
import Embaded
import pandas as pd
import matplotlib.pyplot as plt
import os
import csv

def generete_one_list(list):
    new_list = []
    for i in range(0,2):
        for c in list[i]:
            new_list.append(c)
    return new_list

class Handler:

    def __init__(self):
        self.Cell_List = []
        self.One_Cell_List = []
        self.wanted_cells = []

    def generete_one_list(self, list):
        new_list = []
        for i in range(0,2):
            for c in list[i]:
                new_list.append(c)
        return new_list

    def fetch_Cell_List(self):
        Cell_List = CSV_Lister.get_Cells()
        for temp in Cell_List:
            for cell in temp:
                cell.convert_csv_to_dataFrame()
        
        self.Cell_List = Cell_List
        self.One_Cell_List = self.generete_one_list(Cell_List)


    def start_sequence(self):
        idx = 0
        self.send_cell_one_time_to_show_by_index(idx)
        

    def send_cell_one_time_to_show_by_index(self, idx):
        Embaded.showData(self.One_Cell_List[idx], idx, self)
    
    def manage_wanted_list(self, idx, Ans):
        if Ans:
            self.wanted_cells.append(self.One_Cell_List[idx])
        idx+=1
        if(idx < len(self.One_Cell_List)):
            self.send_cell_one_time_to_show_by_index(idx)

    def fetch_csv_for_wanted_list(self):
            with open(f'wantd_cell_list.csv' , 'w') as csv_wanted_cells:
                for cell in self.wanted_cells:
                    ls = ['K', 'Kv1', 'Kv1,1', cell.get_temprature(), cell.get_cell_id()]
                    writer = csv.writer(csv_wanted_cells)
                    writer.writerow(ls) 



handler = Handler()
handler.fetch_Cell_List()
handler.start_sequence()
print(handler.wanted_cells)
handler.fetch_csv_for_wanted_list()