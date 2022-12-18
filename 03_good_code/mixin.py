class BaseTokenizer:
    def __init__(self, str_token):
        self.str_token = str_token

    def __iter__(self):
        yield from self.str_token.split("-")

class UpperIterableMixin:
    def __iter__(self):
        return map(str.upper, super().__iter__())

class Tokenizer(UpperIterableMixin, BaseTokenizer):
    pass

# tk = BaseTokenizer("12399asdjas-1n23jkn-zxsndj")
# print(list(tk), tk)

tk = Tokenizer("12399asdjas-1n23jkn-zxsndj")
print(list(tk))
