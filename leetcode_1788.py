'''
1788. Maximize the Beauty of the Garden
URL := https://leetcode.com/problems/maximize-the-beauty-of-the-garden/

- Can remove any ( or no ) flowers from the garden
- End result = a valid garden
- Beauty = sum ( remaining flowers) 
Max possible beauty - valid garden
Greedy - add every value ( positive ) and then add negative values ( if no positive values )
Run sum : numPositiveValues, numNegativeValues, to a prefix
If negative - 0 no help, neg valeus no help, keep the ends only

Complexity
N = len(input)
T = O(N)
S = O(N) ( Exp ) O(1) ( Imp ) 
'''
class Solution:
    def maximumBeauty(self, flowers: List[int]) -> int:
        myMaxBeauty = float('-inf')
        posRunSum = 0
        negRunSum = 0
        f = len(flowers)
        positives = [0 for x in range(f)]
        negatives = [0 for x in range(f)]
        # Get left,right positions of each flower
        leftPos = dict()
        rightPos = dict()
        for flowerPtr,flower in enumerate(flowers):
            if(flower not in leftPos):
                leftPos[flower] = flowerPtr
            if(flower not in rightPos):
                rightPos[flower] = flowerPtr
            rightPos[flower] = flowerPtr
            if(flower >= 0):
                posRunSum += flower
            else:
                negRunSum += flower
            positives[flowerPtr] = posRunSum
            negatives[flowerPtr] = negRunSum
        print(positives)
        for flowerVal in leftPos.keys():
            lPos = leftPos[flowerVal]
            rPos = rightPos[flowerVal]
            if(lPos < rPos):
                totalPosMidSum = 0
                totalPosMidSum += positives[rPos]
                # ahhh I see ( negative value by accident here ) 
                # neg value handling needed
                if(flowerVal > 0):
                    totalPosMidSum -= flowerVal
                if(lPos >= 0):
                    posSumLeft = positives[lPos]
                    totalPosMidSum -= posSumLeft
                gardenVal = (flowerVal * 2)
                if(totalPosMidSum > 0):
                    gardenVal += totalPosMidSum
                myMaxBeauty = max(myMaxBeauty, gardenVal)
        return myMaxBeauty

            
        
