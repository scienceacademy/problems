import check50
import check50.c

@check50.check()
def exists():
    """syntax.c exists."""
    check50.exists("syntax.c")


@check50.check(exists)
def compiles():
    """syntax.c compiles."""
    check50.c.compile("syntax.c", lcs50=True)

@check50.check(compiles)
def prints():
    """prints the correct string"""
    check50.run("./syntax").stdin("").stdout("This is CS50AP!").exit()
