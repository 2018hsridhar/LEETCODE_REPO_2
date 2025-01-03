'''
2271. Maximum White Tiles Covered by a Carpet
URL := https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/description/

'''
class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        maxNumCovered = 0
        numTiles = pow(10,9)
        # sort : guaranted non-overlapping ( and uze in sorted order too ) 
        tiles.sort(key = lambda x : (x[0],x[1]))
        prefixSums = []
        prefixSum = 0
        for [left,right] in tiles:
            tileSize = (right - left + 1)
            prefixSum += tileSize
            prefixSums.append(prefixSum)
        # greedy : go from the left OR go from the right
        # bestTiles case left : (25,35) -> index = 3 => bound @ 32
        # always go right ( exists a best tile)
        for index, tile, in enumerate(tiles):
            [left,right] = tile
            caseLeftBound = (left + carpetLen - 1)
            # print(caseLeftBound)
            bestTileCaseLeft = self.bSearchBestTile(tiles,caseLeftBound)
            numTilesUpper = 0
            mostRecentTile = tiles[bestTileCaseLeft]
            # print(mostRecentTile)
            if(caseLeftBound >= mostRecentTile[1]):
                numTilesUpper += mostRecentTile[1] - mostRecentTile[0] + 1
            elif(caseLeftBound <= mostRecentTile[1]):
                numTilesUpper += caseLeftBound - mostRecentTile[0] + 1
            # all tiles preceding
            leftIdx = bestTileCaseLeft - 1
            if(leftIdx >= 0):
                numTilesUpper += prefixSums[bestTileCaseLeft-1]
            # print(numTilesUpper)
            numTilesLower = 1
            if(index -1 >= 0):
                numTilesLower += prefixSums[index-1]
            numTilesCovered = numTilesUpper - numTilesLower + 1
            maxNumCovered = max(maxNumCovered, numTilesCovered)
        return maxNumCovered

    def bSearchBestTile(self, tiles:List[int], bound:int) -> int:
        bestIndex = -1
        low = 0
        high = len(tiles) - 1
        while(low <= high):
            mid = (int)((low + high) * 0.5)
            [curLow,curHigh] = tiles[mid]
            if(curLow > bound):
                high = mid - 1
            elif(curLow == bound):
                bestIndex = mid
                break
            elif(curLow < bound):
                bestIndex = max(bestIndex,mid)
                low = mid + 1
        return bestIndex
        
