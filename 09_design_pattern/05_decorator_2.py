from collections import Iterable
from typing import Callable, Dict

class DictQuery:
    def __init__(self, **kwargs):
        self._raw_query = kwargs

    def render(self)->dict:
        return self._raw_query

class QueryEnhancer:
    def __init__(self, query: DictQuery, *decorators) -> None:
        self._decorated = query
        self._decorators = decorators

    def render(self):
        current_result = self._decorated.render()
        for deco in self._decorators:
            current_result = deco(current_result)
        return current_result

def remove_empty(data:dict):
    return {k: v for k, v in data.items() if v}

def case_insensitive(data:dict):
    return {k: v.lower() for k, v in data.items() if v}

class CaseInsensitive(QueryEnhancer):
    def render(self):
        org = super().render()
        return {k:v.lower() for k, v in org.items()}

if __name__ == '__main__':
    query = DictQuery(key="value", empty="", none=None, upper="UPPPERCASE", title="Title")
    new_query = QueryEnhancer(query, remove_empty, case_insensitive)
    print(query.render())
    print(new_query.render())
