class Solution(object):
    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """
        alice = sum([len(a)-2 for a in colors.split("B") if len(a)>2])
        bob = sum([len(b)-2 for b in colors.split("A") if len(b)>2])
        if alice>bob:
            return True
        return False