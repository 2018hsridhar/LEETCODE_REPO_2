'''
URL := https://leetcode.com/problems/create-a-dataframe-from-list/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

2877. Create a DataFrame from List
'''
import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    # finalDataFrame = pd.DataFrame()
    colNames = ['student_id', 'age']
    # finalDataFrame = pd.DataFrame(columns=['student_id','age'])
    # for student in student_data:
        # dfTemp = pd.DataFrame(student)
        # finalDataFrame = pd.concat([finalDataFrame,dfTemp])
    pdSeriesList = []
    for student in student_data:
        pdSeriesList.append(list(pd.Series(student)))
    # print(pdSeriesList)
    finalDataFrame = pd.DataFrame(pdSeriesList,  columns =  ["student_id", "age"])
    # finalDataFrame = pd.DataFrame(pdSeriesList,  colNames)
    return finalDataFrame

    
