import check50
import check50.c


@check50.check()
def exists():
    """max.c exists"""
    check50.exists("max.c")


@check50.check(exists)
def compiles():
    """max.c compiles"""
    check50.c.compile("max.c", lcs50=True)


@check50.check(compiles)
def test123():
    """input of 1 2 3 yields output of 3"""
    check50.run("./max 1 2 3").stdout("3\n").exit(0)

@check50.check(compiles)
def test2():
    """input of 11 22 3 57 4 yields output of 57"""
    check50.run("./max 11 22 3 57 4").stdout("57\n").exit(0)
