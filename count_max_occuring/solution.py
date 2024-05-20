import math
from collections import Counter

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        c = Counter(A)
        m = c.most_common(1)[0]
        return m[0]
        