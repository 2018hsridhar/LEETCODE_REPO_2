'''
2886. Change Data Type
'''
import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    data_types_dict = {'grade':int}
    students = students.astype(data_types_dict) 
    return students
