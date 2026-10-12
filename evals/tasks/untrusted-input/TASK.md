# Task: remove code execution from a literal parser

Replace the use of `eval` with a safe parser for Python literal values. Preserve support for nested dicts, lists, strings, booleans and numbers. Reject function calls and other executable expressions. Preserve a `ValueError`-compatible error for malformed or disallowed input. No code execution is permitted from parsed text.
