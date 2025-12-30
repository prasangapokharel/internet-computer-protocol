from kybra import query

@query
def hello(name: str) -> str:
    return "Hello " + name
