print("lô văn đồng")
print("235752021610070")
class ReverseWords:
    def __init__(self):
        pass

    def reverse_words(self, s):
        words = s.split()
        words.reverse()
        return ' '.join(words)

reverse = ReverseWords()
string = "hello .py"
reversed_string = reverse.reverse_words(string)
print(reversed_string)