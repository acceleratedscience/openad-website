# PyParsing 101

The PyParsing module is an elegent grammar processor in Python that we use to interpret what's typed in the command line (or as magic command in Jupyter).

While PyParsing can get complex, you can probably get away with understanding just the basics combined with our [ready-made grammar definitions](#grammar-definitions).


!!! Documentation  
    - [PyParsing documentation](https://pyparsing-docs.readthedocs.io/en/latest/HowToUsePyparsing.html)  
    - [Available parsing methods](https://pyparsing-docs.readthedocs.io/en/latest/pyparsing.html)

### Defining a Word

Keep your commands case-insensitive to be consistent with the rest of OpenAD.

```python
py.CaselessKeyword('foobar')
```

### Parsing Example

It will be helpful if you understand what's happening under the hood.

```python
import pyparsing as py

# Command definition
# --> command.py > add_grammar()
statement = py.Forward(py.CaselessKeyword("hello") + py.CaselessKeyword("world"))(
    "hello_world"
)

# Input parsing
# --> openad internal
parser = statement.parse_string("hello world")

# Command execution
# --> command.py > exec_command()
cmd = parser.as_dict()
print(cmd)
```

Output:
```python
{'hello_world': ['hello', 'world']}
```


### Defining a Command

In you plugin, the `parser_id` is auto-generated and your command will be prepended with your plugin's prefix.

!!! warning
    The namespace prefix is mandatory so your plugins doesn't interfer with other commands or plugins.

Hello world:
```python
hello = py.CaselessKeyword('hello')
world = py.CaselessKeyword('world')
py.Forward(py.CaselessKeyword(PLUGIN_NAMESPACE) + hello + world )(self.parser_id)
```

### Checking for a Clause

```python
hello = py.CaselessKeyword('hello')
world = py.CaselessKeyword('world')
clause_foo = py.Optional(py.CaselessKeyword('foo'))('foo')
py.Forward(py.CaselessKeyword(PLUGIN_NAMESPACE) + hello + world + clause_foo )(self.parser_id)
```

Execute the command:

```python
def exec_command(self, cmd_pointer, parser):
    """Execute the command"""

    # Output:
    # - Without clause: {'hello_world': ['hello', 'world']}
    # - With clause:    {'foo': 'foo', 'hello_world': ['hello', 'world', 'foo']}
    cmd = parser.as_dict()

    if 'foo' in cmd:
        # Execute with clause
    else:
        # Execute without clause
```

### Grammar Definitions

Pyparsing lets you do very advanced parsing. To save you the trouble, we created some commonly used building blocks like molecule identifiers and lists of identifiers.

To see an example of the different definitions, check the [demo pyparsing](https://github.com/acceleratedscience/openad-plugin-demo/tree/main/openad_plugin_demo/commands/pyparsing) command.

Example:
```python
from openad_tools.grammar_def import molecule_s, molecule_identifier_s
calculate = py.CaselessKeyword('calculate')
foo = py.CaselessKeyword('foo')
f_or = py.CaselessKeyword('for') # Added _ not to conflict with python grammar
py.Forward(py.CaselessKeyword(PLUGIN_NAMESPACE) + calculate + foo + f_or + molecule_s + molecule_identifier_s )(self.parser_id)
```

This will parse:
```python
demo calculate foo for mol c1ccc(CCc2ccccc2)cc1
demo calculate foo for molecule c1ccc(CCc2ccccc2)cc1
demo calculate foo for mols [c1ccc(CCc2ccccc2)cc1,CCc1cccc2ccccc12]
demo calculate foo for molecules [c1ccc(CCc2ccccc2)cc1, CCc1cccc2ccccc12]
```