class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        rst = []
        length = 0
        path = []
        for word in words:
            if len(path) + len(word) + length > maxWidth:
                spaces = maxWidth - length
                string = ''
                if len(path) == 1:
                    string = path[0] + ' ' * (spaces)
                else:
                    space = spaces // (len(path) - 1)
                    extra = spaces % (len(path) - 1)
                    for i in range(len(path)-1):
                        string += path[i]
                        if i < extra:
                            string += ' ' * (space + 1)
                        else:
                            string += ' ' * space
                    string += path[-1]
                rst.append(string)
                path = []
                length = 0
            path.append(word)
            length += len(word)

        laststring = ' '.join(path)
        space = maxWidth - len(laststring)
        laststring = laststring + ' ' * space
        rst.append(laststring)
        return rst

                        
                    
        