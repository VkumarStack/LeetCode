class Solution:
    def change(self, amount, coins):
        opt = [float('-inf')] * amount + 1