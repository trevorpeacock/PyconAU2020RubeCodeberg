# Entry for PyConlineAU 2020 Rube Codeberg competition

This reads a recursive representation of ascii values of the target message, decodes it, and prints the result.

It uses beautifulsoup4 and lxml packages.

It can be run by calling `make`, or by running `first_program.py` with the above libraries available
```console
$ make
bash -c ". venv/bin/activate && python first_program.py"
Hello World!
```

There is also a test suite to make sure the decoder is working properly
```console
$ make test
bash -c ". venv/bin/activate && python tests.py"
.......
----------------------------------------------------------------------
Ran 7 tests in 0.008s

OK
```

Finally theres a script to generate XML representations
```console
$ make generate
bash -c ". venv/bin/activate && python generate.py"
<character>
...
```