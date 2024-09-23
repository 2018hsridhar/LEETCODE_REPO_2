Complexity
Time complexity:
O(1)

Space complexity:
O(1)

Code
'''
URL := https://leetcode.com/problems/escape-the-ghosts/description/
789. Escape The Ghosts

Simplify the infinite paths : you can always play "optimally" and move some "1 cell" away from the ghost

'''
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        canEscape = True
        pacman = [0,0]
        pacDistToTarget = self.getDist(pacman,target)
        for ghost in ghosts:
            ghostDistToTarget = self.getDist(ghost,target)
            if(ghostDistToTarget <= pacDistToTarget):
                canEscape = False
                break
        return canEscape

    def getDist(self, piece: List[int], target: List[int]) -> int:
        x1 = piece[0]
        x2 = target[0]
        y1 = piece[1]
        y2 = target[1]
        return abs(x2-x1) + abs(y2-y1)
