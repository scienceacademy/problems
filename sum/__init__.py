import check50
import check50.c

@check50.check()
def exists():
    """sum.c exists."""
    check50.exists("sum.c")

@check50.check(exists)
def compiles():
    """sum.c compiles."""
    check50.c.compile("sum.c", lcs50=True)

@check50.check(compiles)
def veronica():
    """Sums 1-10"""
    check50.run("./sum").stdin("1").stdin("2").stdin("3").stdin("4").stdin("5").stdin("6").stdin("7").stdin("8").stdin("9").stdin("10").stdout("55").exit()

