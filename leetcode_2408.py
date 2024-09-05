Intuition
Approach
Complexity
Let O:= #-database operations
Let N:= #-rows in the database
Let R:= #-rows to insert across all tables
Let C:= #-cols across each table

Time complexity:
Time=O(1)
Each operation O(1) time complexity.

Space complexity:
Space=O(NRC)(EXP)O(1)(IMP)

Code
'''
URL := https://leetcode.com/problems/design-sql/description/
2408. Design SQL
'''

'''
Rows auto-incremented id ( database insertion guarantee of a row ) 
Last insert row ( even if deleted ) plus one ( never go backwards )
DB History of Record pattern
'''
class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        # Each database has the same list of names for their columns
        self.databases = dict()
        self.databaseIds = dict()
        for name in names:
            self.databases[name] = dict()
            self.databaseIds[name] = 1

    # usually return id of the inserted row into the database table
    # table will exist ( guard check not needed )
    def insertRow(self, name: str, row: List[str]) -> None:
        myDB = self.databases[name]
        curRowId = self.databaseIds[name]
        if(curRowId not in myDB):
            myDB[curRowId] = row
        nextRowId = curRowId + 1
        self.databaseIds[name] = nextRowId

    def deleteRow(self, name: str, rowId: int) -> None:
        del self.databases[name][rowId]

    # note : column Id is an index ( not the actual ID )
    # exert caution
    # should this be a hahsmap : probably not. Sees more an array or list style 
    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        return self.databases[name][rowId][columnId-1]


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# obj.insertRow(name,row)
# obj.deleteRow(name,rowId)
# param_3 = obj.selectCell(name,rowId,columnId)
