'''
URL := https://leetcode.com/problems/regular-expression-matching/
10. Regular Expression Matching

'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        return self.solve(s, p, 0, 0, memo)

    def solve(self, s: str, p: str, s_index: int, p_index: int, memo: dict) -> bool:
        WILDCARD = '*'
        PERIOD = '.'
        key = f"{s_index}-{p_index}"

        if key in memo:
            return memo[key]

        can_solve = False

        # Guard conditions
        if s_index > len(s) or p_index > len(p):
            can_solve = False

        elif s_index == len(s):
            next_p = p_index + 1
            if p_index == len(p):
                can_solve = (s_index == len(s))
            elif p_index < len(p):
                # Remaining pattern must be zero or more "x*" pairs
                while p_index + 1 < len(p) and p[p_index + 1] == WILDCARD:
                    p_index += 2
                can_solve = p_index == len(p)
                memo[key] = can_solve

        elif s_index < len(s) and p_index < len(p):
            char_s = s[s_index]
            char_p = p[p_index]
            next_p = p_index + 1

            # Case 1: Next character in pattern is '*'
            if next_p < len(p) and p[next_p] == WILDCARD:
                if char_p == PERIOD or char_s == char_p:
                    # Try multiple wildcard expansion possibilities
                    child_one = self.solve(s, p, s_index + 1, p_index, memo)
                    child_three = self.solve(s, p, s_index, p_index + 2, memo)
                    can_solve = child_one or child_three
                else:
                    # Zero-match case (skip wildcard)
                    can_solve = self.solve(s, p, s_index, p_index + 2, memo)

            # Case 2: Regular match or '.'
            if char_s == char_p or char_p == PERIOD:
                if self.solve(s, p, s_index + 1, p_index + 1, memo):
                    can_solve = True

        memo[key] = can_solve
        return can_solve
