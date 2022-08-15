import os
from CellMoudle import Cell


def get_Cells():
    temp_list = ['15' , '25' , '35']

    list_15_idx = []
    list_25_idx = []
    list_35_idx = []



    for temp in temp_list:
        if(temp == '15'):
            list_15_idx = os.listdir(f'Kv1.1\\Temp_{temp}C')    
        if(temp == '25'):
            list_25_idx = os.listdir(f'Kv1.1\\Temp_{temp}C')
        if(temp == '35'):
            list_35_idx = os.listdir(f'Kv1.1\\Temp_{temp}C')





    list_15_Cells = []
    list_25_Cells = []
    list_35_Cells = []

    for cell in list_15_idx:
        Dict = {
        "temprature" : "15",
        "cell_id" : cell
        }
        cell_Obj = Cell(Dict)
        list_15_Cells.append(cell_Obj)
    
    for cell in list_25_idx:
        Dict = {
        "temprature" : "25",
        "cell_id" : cell
        }
        cell_Obj = Cell(Dict)
        list_25_Cells.append(cell_Obj)

    for cell in list_35_idx:
        Dict = {
        "temprature" : "35",
        "cell_id" : cell
        }
        cell_Obj = Cell(Dict)
        list_35_Cells.append(cell_Obj)


    return [list_15_Cells, list_25_Cells , list_35_Cells]