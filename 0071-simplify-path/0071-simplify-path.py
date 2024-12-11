class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        directories = path.split('/')
        res = []
        for directory in directories:
            if directory == '.' or directory == '':
                continue
            elif directory == '..':
                if len(res):
                    res.pop()
            else:
                res.append(directory)
        return '/'+('/'.join(res))