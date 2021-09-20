import check50
import check50.c

@check50.check()
def exists():
    """Files exist."""
    check50.exists("add2.c")
    check50.exists("sum2.c")

@check50.check(exists)
def compiles():
    """Programs compile."""
    check50.c.compile("add2.c", lcs50=True)
    check50.c.compile("sum2.c", lcs50=True)

@check50.check(compiles)
def add1():
    """adds 2 + 3"""
    check50.run("./add2 2 3").stdout("5\n").exit()

@check50.check(compiles)
def add2():
    """checks number of arguments"""
    check50.run("./add2").stdout("Wrong number of arguments\n").exit()

@check50.check(compiles)
def sum1():
    """Sums 2 + 5 + 7"""
    check50.run("./sum2 2 5 7").stdout("14\n").exit()

@check50.check(compiles)
def sum2():
    """Error with no arguments"""
    check50.run("./sum2").stdout("Wrong number of arguments\n").exit()