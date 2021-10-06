import check50
import check50.c

@check50.check()
def exists():
    """Files exist."""
    check50.exists("rand_range.c")

@check50.check(exists)
def compiles():
    """Program compiles."""
    check50.c.compile("rand_range.c", lcs50=True)

@check50.check(compiles)
def test1():
    """1-6 => 6"""
    check50.run("./rand_range 1 6").stdout("6\n").exit()

@check50.check(compiles)
def test2():
    """15-25 => 22"""
    check50.run("./rand_range 15 25").stdout("22\n").exit()

@check50.check(compiles)
def test3():
    """938-2843 => 2841"""
    check50.run("./rand_range 938 2843").stdout("2841\n").exit()

