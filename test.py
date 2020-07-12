from markdown2 import markdown
s = markdown("```python\nprint('hello world')```", extras=['fenced-code-blocks'])
print(s)