

class Solution(object):
    # 1. Merge Strings Alternately
    """You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

    Return the merged string."""

    # def mergeAlternately(self, word1: str, word2: str) -> str:
    #     length = min(len(word1), len(word2))
    #     word = ''
    #     for i in range(length):
    #         word += word1[i]+word2[i]

    #     return word + word1[length:] + word2[length:]

    """For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
    Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2."""

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        pass


solution = Solution()
# solution.mergeAlternately('hola', 'dos')
