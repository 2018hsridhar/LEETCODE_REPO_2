'''
URL := https://leetcode.com/problems/design-spreadsheet/description/
3484. Design Spreadsheet

It's pretty straightforward -> design a Excel-esque spreadsheet
Leverage a hashmap

'''
class Spreadsheet:

    def __init__(self, rows: int):
        self.cellMap = dict()
        self.RESET = 0
        self.LOWER = 'A'
        self.UPPER = 'Z'

    def setCell(self, cell: str, value: int) -> None:
        if(cell not in self.cellMap):
            self.cellMap[cell] = value
        self.cellMap[cell] = value

    def resetCell(self, cell: str) -> None:
        if(cell in self.cellMap):
            self.cellMap[cell] = self.RESET

    def getValue(self, formula: str) -> int:
        expr_body = formula[1:]
        tokens = expr_body.split('+', 1)
        tokenOne = tokens[0]
        tokenTwo = tokens[1]
        # check first character
        valOne = self.get_token_value(tokenOne)
        valTwo = self.get_token_value(tokenTwo)
        targetSum = valOne + valTwo
        return targetSum

    def get_token_value(self, token):
        """
        Returns the value for a token.
        If the token is a cell, looks up its value in cellMap.
        Otherwise, converts the token to an integer.
        """
        if self.isACell(token):
            return self.cellMap.get(token, 0)
        else:
            return int(token)

    def isACell(self,token:str) -> bool:
        firstLet = token[0]
        return (ord(self.LOWER) <= ord(firstLet) and ord(firstLet) <= ord(self.UPPER))


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
