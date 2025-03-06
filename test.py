import os

hello = 123
print(hello)

def test(foo=123):
    """
    Hello
    """
    if hello == foo:
        return True

inp = None
default_path = os.path.expanduser("~/.ipython/profile_default/startup")****
if not os.path.exists(default_path):
    os.mkdir(default_path)