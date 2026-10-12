"""Deduplicate while preserving insertion order and equality semantics."""
def unique_stable(values):
    output=[]
    for value in values:
        if value not in output:
            output.append(value)
    return output
