class Hello:
    _word = "hello world"

    def __init__(self):
        self._word = "hello world"

    def pr_word2(self):
        print(self._word)

    @classmethod
    def pr_word(cls):
        print(cls._word)


word = Hello()
word.pr_word()
word.pr_word2()