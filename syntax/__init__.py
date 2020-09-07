import re

from check50 import *

class Hello(Checks):

    @check()
    def exists(self):
        """syntax.c exists."""
        self.require("syntax.c")

    @check("exists")
    def compiles(self):
        """syntax.c compiles."""
        self.spawn("clang -o syntax syntax.c").exit(0)

    @check("compiles")
    def prints_thisiscs50ap(self):
        """prints "This is CS50AP!\\n" """
        expected = "[Tt]his is CS50AP!?\n"
        actual = self.spawn("./syntax").stdout()
        if not re.match(expected, actual):
            err = Error(Mismatch("This is CS50AP!\n", actual))
            if re.match(expected[:-1], actual):
                err.helpers = "Did you forget a newline (\"\\n\") at the end of your printf string?"
            raise err