'''
URL := https://leetcode.com/problems/encode-and-decode-strings/description/
271. Encode and Decode Strings
Encodings and decodings power network communication across distSystems.
Check sameness of strings/data across both machines
But do most TCs even know RLE ( can I assume this ) ???

Working with delimeter harder : how to handle constraints of language set
Solution given : 
    (A) Get the number
    (B) A DELIM of your choice
    (C) The string
    And proceed from there!!!


'''
class Codec:

    
    def encode(self, strs: List[str]) -> str:
        DELIM = ":"
        encoding = ""
        for token in strs:
            tokenLen = (str)(len(token))
            elements = [tokenLen,DELIM,token]
            record = "".join(elements)
            encoding += record
        return encoding

    def decode(self, s: str) -> List[str]:
        EMPTY = ""
        if(len(s) == 2):
            return [EMPTY]
        DELIM = ":"
        decodedStrings = []
        while(len(s) > 0):
            firstHitDelim = s.find(DELIM)
            if(firstHitDelim != -1):
                offset = firstHitDelim + 1
                strLen = (int)(s[0:firstHitDelim])
                s = s[offset:]
                word = s[:strLen]
                wordOffset = len(word)
                s = s[wordOffset:]
                decodedStrings.append(word)
        return decodedStrings


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
