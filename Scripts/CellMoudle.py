from asyncio.windows_events import NULL
import csv_to_DataFrame as DF_Generator
import pandas as pd
import csv

class Cell:
    
    def __init__(self, cell_payload_Dict):
        self.information_Dict = cell_payload_Dict
        self.rep2_dataFrame = NULL


    def convert_csv_to_dataFrame(self):
        temprature = self.information_Dict["temprature"]
        cell_id = self.information_Dict["cell_id"]

        path = f'Kv1.1\\Temp_{temprature}C\\{cell_id}\\{cell_id}_Activation_rep2.csv'
        df = DF_Generator.adjust_csv_to_DataFrame(path)
        self.rep2_dataFrame = df

        

    def convert_to_csv(self, data_avarage):

        temprature = self.information_Dict["temprature"]
        cell_id = self.information_Dict["cell_id"]

        path = f'Kv1.1\\{temprature}\\{cell_id}'


        data_avarage.to_csv(f'{path}\\data_{cell_id}_avarage_with_index.csv')
        data_avarage.to_csv(f'{path}\\data_{cell_id}_avarage_no_index.csv', index=False)

    def get_cell_id(self):
        return self.information_Dict["cell_id"]

    def get_temprature(self):
        return self.information_Dict["temprature"]

    def get_df(self):
        return self.rep2_dataFrame