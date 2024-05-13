'''
URL := https://leetcode.com/problems/html-entity-parser/description/
1410. HTML Entity Parser

Category : Regex, String Replacement, Tokenization, Single Pass, Linear Scan, String

Complexity:
Let N := len(text)
Let M := #-tokens in the text
Time := O(N)
Space := O(M) ( E ) O(1) ( I )

https://pynative.com/python-regex-replace-re-sub/

'''
import re

class Solution:
    def entityParser(self, text: str) -> str:
        finalStr = ''
        # target_str = "Jessa knows testing and machine learning"
        # patterns = ["&quot", "&apos", "&amp", "&gt", "&lt", "&frasl"]
        # replacements = []
        # origString = text
        # for pattern, replacement in zip(patterns, replacements):
            # tempString = re.sub(r+pattern,replacement, origString)
            # origString = tempString 
        # can't iterate over a list of regex, patterns
        # izip() vs zip() -> no third list creation ( woah efficiency ) 
        removeDoulbeQuotes = re.sub(r"&quot;", "\"", text)
        removeSingleQuote = re.sub(r"&apos;", "\'", removeDoulbeQuotes)
        removeGT = re.sub(r"&gt;", ">", removeSingleQuote)
        removeLT = re.sub(r"&lt;", "<", removeGT)
        removeSlash = re.sub(r"&frasl;", "/", removeLT)
        removeAmp = re.sub(r"&amp;", "&", removeSlash)
        finalStr = removeAmp
        return finalStr
