# Getting started

This is just a demo page.

Anonymouse code block:

    inp = None
    default_path = os.path.expanduser("~/.ipython/profile_default/startup")
    if not os.path.exists(default_path):
        os.mkdir(default_path)
    if len(sys.argv) == 1:
        destination = os.path.expanduser("~/.ipython/profile_default/startup/openad_magic.py")
        destination_old = os.path.expanduser(f"~/.ipython/profile_default/startup/openad.py")
    else:
        inp = sys.argv[1]
        destination = os.path.expanduser(f"~/.ipython/profile_{inp}/startup/openad_magic.py")
        destination_old = os.path.expanduser(f"~/.ipython/profile_{inp}/startup/openad.py")

Code block python:

```python
inp = None
default_path = os.path.expanduser("~/.ipython/profile_default/startup")
if not os.path.exists(default_path):
    os.mkdir(default_path)
if len(sys.argv) == 1:
    destination = os.path.expanduser("~/.ipython/profile_default/startup/openad_magic.py")
    destination_old = os.path.expanduser(f"~/.ipython/profile_default/startup/openad.py")
else:
    inp = sys.argv[1]
    destination = os.path.expanduser(f"~/.ipython/profile_{inp}/startup/openad_magic.py")
    destination_old = os.path.expanduser(f"~/.ipython/profile_{inp}/startup/openad.py")
```
