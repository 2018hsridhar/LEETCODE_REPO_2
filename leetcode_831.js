'''
URL := https://leetcode.com/problems/masking-personal-information/description/
Masking of PII problems ( e-mail and phone numbers )
831. Masking Personal Information

Phone #'s can be 13 digits ( 10 digits local number )
<country_code><local_number>

Gaaah @ Regexp builders ( this the way to go though )
https://regexr.com/


Time consumed
(A) Learning pythonic syntax
(B) Learning regexps
'''
import re

class Solution:
    def maskPII(self, s: str) -> str:
        maskedPII = ""
        isEmail = (s.find('@') != -1)
        if isEmail == True :
            # Python syntax : no `true` -> `True` caps convention
            # https://stackoverflow.com/questions/5615648/how-can-i-call-a-function-within-a-class
            # Member function syntax style here for call hierarchy
            maskedPII = self.maskEmail(s)
        else :
            maskedPII = self.maskPhone(s)
        return maskedPII

    # To pass `self` here or not ( IDK )
    def maskEmail(self, s:str) -> str:
        atIdx = s.find('@')
        name = s[0:atIdx]
        domain = s[atIdx + 1:]
        newName = name.lower()
        newDomain = domain.lower()
        firstLetter = newName[0]
        lastLetter = newName[len(newName) - 1]
        asteriskName = "".join([firstLetter, "*****", lastLetter])
        # Join method : one arg -> array only
        maskedEmail = "".join([asteriskName,'@',newDomain])
        return maskedEmail

    def maskPhone(self, s:str) -> str:
        # https://www.programiz.com/python-programming/set#:~:text=Create%20a%20Set%20in%20Python,or%20dictionaries%20as%20its%20elements.
        # seperationChars = {'+','-','(',')',' '}
        regex = "[+)(\- ]"
        removedSepChars = re.sub(regex,"",s)
        # Country codes will have a given length too
        # Is Regexp overcomplicated this problem?
        # countryCode = s[0:4] # includes characters 0,1,2
        # Get the first 3 digits only ( following ten in the back already selected for )
        # can easily do procedurally ( how to do via regexp )?
        # Get index of 10th digit ( from the right )
        # Iterator -> list conversion
        # Joins on lists -> the pythonic way ( to process text )
        digString = "".join(list(filter(lambda i: i.isdigit(), removedSepChars)))
        lastFourDigits = digString[len(digString) - 4: len(digString)]
        countryCode = digString[:-10]
        zeroDigRegexp = "^\d{0}.*$"
        oneDigRegexp = "^\d{1}.*$"
        twoDigRegexp = "^\d{2}.*$"
        threeDigRegexp = "^\d{3}.*$"
        prefixMask = ""
        if(re.match(threeDigRegexp,countryCode)) :
            prefixMask = "+***-***-***"
        elif(re.match(twoDigRegexp,countryCode)) :
            prefixMask = "+**-***-***"
        elif(re.match(oneDigRegexp,countryCode)) :
            prefixMask = "+*-***-***"
        elif(re.match(zeroDigRegexp,countryCode)) :
            prefixMask = "***-***"
        # better way to concat pythonic strings?
        maskedNumber = "".join([prefixMask,"-",lastFourDigits])
        return maskedNumber
