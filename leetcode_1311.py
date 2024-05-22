'''
URL := https://leetcode.com/problems/get-watched-videos-by-your-friends/description/
1311. Get Watched Videos by Your Friends

Category : Graph Theory, BFS/DFS/LOT, Counting, Ordering, HashMap, Lists and In-Place Sorting

30 mins to rapid solutioning
So many attribute not defined errors

'''
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        uniqueIdsAtLevel = self.getIdsAtLevel(id, level, friends)
        print(uniqueIdsAtLevel)
        vidFreq = self.createVidFreqMap(watchedVideos, uniqueIdsAtLevel)
        # modularize lambda function in-place sort please
        friendVideos = []
        for k, v in vidFreq.items():
            friendVideos.append([k,v])
# https://www.freecodecamp.org/news/lambda-sort-list-in-python/            
        # list comprehension enables filtering ability
        # match list comp : [] style
        friendVideos.sort(key=lambda ndVec: (ndVec[1], ndVec[0]))
        # sort in place : use list later ( iterable of None can cause issues -> preserve in list form only )
        friendVideosFiltered = [x[0] for x in friendVideos]
        return friendVideosFiltered

    # super concise yet expressive type system -> readability bolstering
    def createVidFreqMap(self, watchedVideos: List[List[str]], levelIds:List[int]):
        # Please modularize into own method
        vidFreq = dict()
        for friendId in levelIds:
            curVideos = watchedVideos[friendId]
            for video in curVideos:
                if video not in vidFreq:
                    vidFreq[video] = 0
                vidFreq[video] += 1
        return vidFreq

    # Can we scope down the level of calls for creating our adjacency graph?
    # the tuplet/n-dimensional based in=place stack/queue be harder
    def getIdsAtLevel(self, rootId:int, targetLevel:int, friends: List[List[int]]) -> set:
        # never pass self in param list
        adjList = self.createAdjList(friends)
        # print(adjList)
        uniqueLevelIds = set()
        queue = [[rootId,0]]
        visited = set()
        while(len(queue) > 0):
            parentPair = queue.pop(0)
            parentId = parentPair[0]
            parentLevel = parentPair[1]
            # print("parentId = " + str(parentId))
            # print("parent level = " + str(parentLevel))
            if parentId not in visited:
                visited.add(parentId)
                if(parentLevel == targetLevel):
                    uniqueLevelIds.add(parentId)
                elif(parentLevel < targetLevel):
                    # set method Py3 facilitates quick add :-)
                    children = friends[parentId]
                    for child in children:
                        childLevel = parentLevel + 1
                        # list is append() not add
                        queue.append([child,childLevel])
        # can we immediate listify ( or just use set form anyways -> more guarantees )
        # return list(uniqueLevelIds)
        return uniqueLevelIds

    # Python3 is so fast with the creation of dynamically-typed data structures OMG
    def createAdjList(self, friends: List[List[int]]) -> dict():
        adjList = dict()
        for index, curFriends in enumerate(friends):
            if index not in friends:
                adjList[index] = set()
            for friend in curFriends:
                adjList[index].add(friend)
        return adjList
