'''
URL := https://leetcode.com/problems/brace-expansion/
1087. Brace Expansion

No nestedness ( ask about that ) 
All distinct characters
Small strings only

a,b
c
d,e
f

'''
class Solution:
    def expand(self, s: str) -> List[str]:
        genWords = []
        LEFT = '{'
        RIGHT = '}'
        COMMA = ','
        DELIMS = {LEFT,RIGHT,COMMA}
        records = []
        record = []
        insertRecMode = True
        for letter in s:
            if(letter == LEFT):
                insertRecMode = False
                record = []
            if(letter not in DELIMS):
                record.append(letter)
                if(insertRecMode):
                    records.append(record)
                    record = []
            elif(letter == RIGHT):
                insertRecMode = True
                records.append(record)
                record = []
        rootIndex = 0
        rootWord = ""
        self.makeWords(records, genWords, rootIndex, rootWord)
        genWords.sort()
        return genWords
    
    def makeWords(self, records, genWords, index, word) -> None:
        if(index == len(records)):
            genWords.append(word)
        elif(index < len(records)):
            curRecord = records[index]
            for letter in curRecord:
                childWord = word + letter
                childIndex = index + 1
                self.makeWords(records,genWords,childIndex,childWord)


