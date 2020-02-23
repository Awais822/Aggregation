import re
patterns = [(r'\'d',' would'),
            (r'\'s',' is'),
            (r'don\'t','do not')
            ,(r'didn\'t','did not'),(r'\'m',' am')
            ,(r'you\'re',' you are')
            ,(r'\'ve',' have')
            ,(r'\'ll',' will ')]

class RegexReplacer(object):
    def __init__(self):
        self.pattern = patterns
    def ReplaceMethod(self,text):
        for (to_replace,replace_by) in self.pattern:
            regex = re.compile(to_replace)
            text = regex.sub(replace_by,text)
        return text