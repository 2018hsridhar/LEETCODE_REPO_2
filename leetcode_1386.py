Intuition and Approach
Only three seating arrangements are possible, so check for those cases. The cases are
'''
Seating arrangements :
arrangeTwo = 2345
arrangeFour = 4567
arrangeSix = 6789
'''
Build a seating chart using a hashmap and set, and approach the problem greedily/inductively from left to run. Each row can be treated as an independent unit.

Category : Greedy, Linear Scan, Hashmaps, Counting, Case-by-enumerations

Complexity
M:= #-rows
N:= #-cols

Time complexity:
O(MN)

Space complexity:
O(MN)(Explicit)O(1)(Implicit)

Code
'''
1386. Cinema Seat Allocation
URL := https://leetcode.com/problems/cinema-seat-allocation/description/
'''
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seatingChart = self.makeSeatingChart(reservedSeats)
        maxFourPersonGroups = self.getNumberFourGroups(n,seatingChart)
        return maxFourPersonGroups

    def getNumberFourGroups(self, n:int, seatingChart: dict()) -> int:
        numberFourGroups = 0
        '''
        Seating arrangements :
            arrangeTwo = 2345
            arrangeFour = 4567
            arrangeSix = 6789
        '''
        arrangeTwo = "2345"
        arrangeFour = "4567"
        arrangeSix = "6789"
        # There's a lot of rows <-- just check the rows that exist
        # for all rows non-existent, we know the value
        numRowsWithAllocations = len(seatingChart.keys())
        numFreeRows = n - numRowsWithAllocations
        familiesInFreeRows = (numFreeRows * 2)
        numberFourGroups += familiesInFreeRows
        for row, curArrangement in seatingChart.items():
            familiesInRow = 0
            curArrangement = seatingChart[row]
            twoStatus = True
            fourStatus = True
            sixStatus = True
            for seat in curArrangement:
                if(arrangeTwo.find(seat) != -1):
                    twoStatus = False
                if(arrangeFour.find(seat) != -1):
                    fourStatus = False
                if(arrangeSix.find(seat) != -1):
                    sixStatus = False
            if(twoStatus and sixStatus):
                familiesInRow = 2
            elif(twoStatus or fourStatus or sixStatus):
                familiesInRow = 1
            numberFourGroups += familiesInRow
        return numberFourGroups

    def makeSeatingChart(self, reservedSeats: List[List[int]]) -> dict():
        seatingChart = dict()
        for [seatRow,seatCol] in reservedSeats:
            if(seatRow not in seatingChart):
                seatingChart[seatRow] = set()
            seatingChart[seatRow].add((str)(seatCol))
        return seatingChart
