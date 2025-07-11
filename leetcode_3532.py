'''
3532. Path Existence Queries in a Graph I
URL :+ https://leetcode.com/problems/path-existence-queries-in-a-graph-i/description/
Sorted, non-decreasing ( never decreases ; the same or increases ) order
Sorted -> grouping -> get nodes by indices ( in each group )
For each group, determine group membership

Self-referential property is easy
10 minutes -> almost passed -> close -> check
'''
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        answer = [False for idx in range(len(queries))]
        guid = 0
        grouping = dict()
        # Compare and test difference
        for index in range(len(nums) - 1):
            # Always add current grouping
            if(guid not in grouping):
                    grouping[guid] = set()
            curNode = nums[index]
            nextNode = nums[index+1]
            diff = abs(nextNode - curNode)
            if(diff <= maxDiff):
                    grouping[guid].add(index)
                    grouping[guid].add(index+1)
            else:
                grouping[guid].add(index)
                nextGuid = guid + 1
                guid = nextGuid
                # Add next node ( instantiation )
                grouping[nextGuid] = set()
                grouping[nextGuid].add(index+1)
        # reverse hashmap : value->keys now
        # and check lat member ( 1 off case )
        if(guid not in grouping):
            grouping[guid] = set()
        grouping[guid].add(len(nums)-1)
        membership = dict()
        for group,nodes in grouping.items():
            for node in nodes:
                if(node not in membership):
                    membership[node] = group
        # print(membership)
        for index,[qSrc,qDst] in enumerate(queries):
            gSrc = membership[qSrc]
            gDst = membership[qDst]
            hasAPath = (gSrc == gDst)
            answer[index] =hasAPath
        return answer


        
