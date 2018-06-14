This is adaptation Java example comand line argument parser from [Robin Martin](https://github.com/unclebob) ["Clean code"](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship-ebook/dp/B001GSTOAM) book on python.

Written for the study how to write clean code.

Agreements:

```python
    Methods: 

        def methodname(): # public
        def _methodname(): # protected
        def __methodname(): # private
```

Usage cli:

Example

```bash
    $ python -i argscli.py x* -x stringParam
```

```python
    >>> args.getString('x')
    'stringParam'
```

Run tests:

```bash
    $ python -m unittest tests.ArgsTest
    $ python -m unittest tests.ArgsExceptionTest
```
