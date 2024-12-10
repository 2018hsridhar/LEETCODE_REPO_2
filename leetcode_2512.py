'''
URL := https://leetcode.com/problems/reward-top-k-students/description/
2512. Reward Top K Students

Approach : Sorting, Heaps, Priority Queues, Tokenization, Strings

Complexity
N := #-students
T = O(N)
S = O(N) ( Exp ) O(1) ( Imp ) 
'''
class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        topKStudents = []
        positive_tokens = set(positive_feedback)
        negative_tokens = set(negative_feedback)
        studentRanks = []
        delim = " "
        posPoint = 3
        negPoint = 1
        for studentIndex, rpt in enumerate(report):
            studentId = student_id[studentIndex]
            reportTokens = rpt.split(delim)
            studentScore = 0
            for token in reportTokens:
                if(token in positive_tokens):
                    studentScore += posPoint
                elif(token in negative_tokens):
                    studentScore -= negPoint
            record = [studentId, studentScore]
            studentRanks.append(record)
        # non incr : high -> low
        studentRanks.sort(key = lambda x : (-1 * x[1],x[0]))
        # print(studentRanks)
        topKStudents = studentRanks[0:k]
        topKStudents = [student_id for [student_id, score] in topKStudents]
        return topKStudents
        
