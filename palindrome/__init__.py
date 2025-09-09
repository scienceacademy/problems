import check50
import check50.c


@check50.check()
def exists():
    """palindrome.c exists"""
    check50.exists("palindrome.c")


@check50.check(exists)
def compiles():
    """palindrome.c compiles"""
    check50.c.compile("palindrome.c", lcs50=True)


@check50.check(compiles)
def test0():
    """Check for palindrome"""
    check50.run("./palindrome").stdin("racecar").stdout("PALINDROME").exit(0)


@check50.check(compiles)
def test1():
    """Check for not palindrome"""
    check50.run("./palindrome").stdin("jellyfish").stdout("NOT PALINDROME").exit(0)
