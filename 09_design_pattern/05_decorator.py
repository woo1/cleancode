class DictQuery:
    def __init__(self, **kwargs):
        self._raw_query = kwargs

    def render(self)->dict:
        return self._raw_query

class QueryEnhancer:
    def __init__(self, query: DictQuery):
        self.decorated = query

    def render(self):
        return self.decorated.render()

class RemoveEmpty(QueryEnhancer):
    def render(self):
        org = super().render()
        return {k:v for k, v in org.items() if v}

class CaseInsensitive(QueryEnhancer):
    def render(self):
        org = super().render()
        return {k:v.lower() for k, v in org.items()}

if __name__ == '__main__':
    org = DictQuery(key="value", empty="", none=None, upper="UPPPERCASE", title="Title")
    empty_query = RemoveEmpty(org)
    new_query = CaseInsensitive(empty_query)
    print(org.render())
    print(empty_query.render())
    print(new_query.render())
