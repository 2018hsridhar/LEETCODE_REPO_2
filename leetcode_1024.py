'''
URL := https://leetcode.com/problems/video-stitching/description/
1024. Video Stitching

Complexity
Let N := #-videos
Time := O(NlgN) + O(N) = O(Nlgn)
Space := O(1) ( E ) O(1) ( I ) 

'''
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        minVideos = 0
        # The lambda is each element : use the sorted() function in Python :-)
        # Sliding window two pointer approach more intuitive?
        sortedClips = sorted(clips, key = lambda stitch: (stitch[0], stitch[1] * -1 ))
        lPtr = 0
        rPtr = 0
        n = len(sortedClips)
        curBestRightMost = sortedClips[rPtr][1]
        # catch case : can not even start video procecssing of our clips / stream of clips
        if(sortedClips[0][0] > 0 ):
            return -1
        # always choose the first video ( is within the time )
        minVideos += 1
        while(lPtr < n):
            curClip = sortedClips[lPtr]
            curLeft = curClip[0]
            curRight = curClip[1]
            if(curRight >= time):
                break
            hitARightVideo = False
            while(rPtr < n):
                rightClip = sortedClips[rPtr]
                rightLeft = rightClip[0]
                nextRightMost = rightClip[1]
                if(rightLeft <= curRight):
                    if(nextRightMost >= curBestRightMost):
                        curBestRightMost = nextRightMost
                        hitARightVideo = True
                        lPtr = rPtr
                else:
                    break
                rPtr += 1
            if(hitARightVideo):
                minVideos += 1
            else:
                minVideos = -1
                break
        # do a right most check at the end : ensure this passes time
        # if we could never get right enough => that is problematic.
        if(curBestRightMost < time):
            minVideos = -1
        return minVideos
        
