import check50
import check50.c

@check50.check()
def exists():
    """shuffle.c exists."""
    check50.exists("shuffle.c")

@check50.check(exists)
def compiles():
    """shuffle.c compiles."""
    check50.c.compile("shuffle.c", lcs50=True)

@check50.check(compiles)
def one():
    """ Works with seed 1234 """
    expected = "5 6 8 7 1 9 0 3 2 4\n"
    actual = check50.run("./shuffle 1234").stdout()
    if expected != actual:
        help = "Common mistake - read the pseudocode carefully."
        raise check50.Mismatch(expected, actual, help=help)
