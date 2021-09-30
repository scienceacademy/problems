import check50
import check50.c

@check50.check()
def exists():
    """factorial.c exists"""
    check50.exists("factorial.c")

@check50.check(exists)
def compiles():
    """factorial.c compiles"""
    check50.c.compile("factorial.c", lcs50=True)

@check50.check(compiles)
def test5():
    """5! is 120"""
    check50.run("./factorial").stdin("5").stdout("120").exit(0)

@check50.check(compiles)
def test10():
    """10! is 3628800"""
    check50.run("./factorial").stdin("10").stdout("3628800").exit(0)
