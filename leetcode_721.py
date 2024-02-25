'''
URL := https://leetcode.com/problems/accounts-merge/description/
721. Accounts Merge

# records : [ name, e1,...,en] emails
Merge accounts / records
accounts with common e-mails?
people can have same name ( do not use name )

people can have multiple accounts -> can we compactify and store on space?

Return : 
    across accounts : any order
    in account : [ name, emails(sorted ASC DICT ) ]

'''
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToAccounts = self.getAccountsForEmails(accounts)
        adjList = self.createAdjListFromEmailAccounts(emailToAccounts)
        mergedAccounts = []
        # gaaah evn though 2d mergedAccount, start 1-D only!
        # [[]] seen as ["[]"] not as []
        visited = set()
        # Sets and Maps -> both key-base structures :-)
        # dfs list returns a list of IDs ( id list generalizes better for the merge op)
        for srcNode in range(len(accounts)):
            mergeIdList = set()
            if(srcNode not in visited):
                # gaaah name definition errs
                self.dfs(mergeIdList,srcNode,adjList, visited)
                self.merge(mergeIdList,accounts,mergedAccounts)
        return mergedAccounts

# None for readability
# Recursive DFS so fast to write up
# self is an implicitly given positional arg in python ( not explicilty mpassed )
    def merge(self,mergeIdList:set(), accounts:List[List[str]], mergedAccounts: List[List[str]]) -> None:
        name = ""
        # unique name guaranteed
        allEmails = set()
        for accountId in mergeIdList:
            if name == "":
                name = accounts[accountId][0]
            accountEmails = accounts[accountId][1:]
            # .update() over for loop .add() for adding multiple elements to a set in Pythonic synta
            allEmails.update(accountEmails)
        # Join to arrays here ( slice and join ops )
        # conv : set -> array
        # woah PY operator overloading join arrays
        # sorted defined multiple iterables :-)
        mergeList = [name] + sorted(allEmails)
        mergedAccounts.append(mergeList)

    def dfs(self,mergeIdList: set, parentNode:int, adjList:dict, visited:set) -> None:
        if(parentNode not in visited):
            visited.add(parentNode)
            mergeIdList.add(parentNode)
            childAccounts = adjList[parentNode]
            for childAccount in childAccounts:
                self.dfs(mergeIdList,childAccount,adjList,visited)

    def getAccountsForEmails(self, accounts: List[List[str]]) -> dict:
        emailsToAccounts = dict()
        for accountIdx in range(len(accounts)):
            account = accounts[accountIdx]
            for j in range(1,len(account),1):
                email = account[j]
                if email not in emailsToAccounts:
                    emailsToAccounts[email] = []
                emailsToAccounts[email].append(accountIdx)
        # print(emailsToAccounts)
        return emailsToAccounts

# PY calls them position args -> interesting
# Functions as attributes of objects style
# How to reduce overhead of data structure conversion codes?
    def createAdjListFromEmailAccounts(self, emailToAccounts:dict):
        adjList = dict()
        for accountsList in emailToAccounts.values():
            # Good compilers catch `NameErrors`
            for i in range(len(accountsList)):
                src = accountsList[i]
                if(src not in adjList):
                    adjList[src] = []
                for j in range(i+1,len(accountsList),1):
                    dst = accountsList[j]
                    if(dst not in adjList):
                        adjList[dst] = []
                    adjList[src].append(dst)
                    adjList[dst].append(src)
        return adjList

        
