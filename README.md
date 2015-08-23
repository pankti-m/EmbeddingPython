# EmbeddingPython
A POC showing how Python can be embedded in C/C++.

An Internet-based article on using multiple programming languages to develop an application aroused my interest and motivated me to try doing so using
C/C++ and Python.

C forms the backbone here and calls into Python to start a calculator program.

To compile on Ubuntu, pass the libpython library.
gcc <c-program> -lpython2.7 -o <executable> 



References:  https://docs.python.org/3/extending/embedding.html
