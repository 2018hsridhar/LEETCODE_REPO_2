# 2881. Create a New Column
# Values of a series as a new col
import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    bonusList = [2*salary for salary in list(employees['salary'])]
    seriesBonus = pd.Series(bonusList)
    addedCol = employees
    addedCol['bonus'] = seriesBonus.values
    return addedCol
    
