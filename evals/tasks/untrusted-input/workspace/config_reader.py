"""Literal parsing API; current implementation is insecure."""
def parse_value(value):
    if not isinstance(value,str):raise TypeError('input must be str')
    return eval(value)
