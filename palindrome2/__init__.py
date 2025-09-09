import check50
import check50.c


@check50.check()
def exists():
    """palindrome2.c exists"""
    check50.exists("palindrome2.c")


@check50.check(exists)
def compiles():
    """palindrome2.c compiles"""
    check50.c.compile("palindrome2.c", lcs50=True)


@check50.check(compiles)
def test0():
    """Check for palindrome"""
    check50.run("./palindrome2").stdin("was it a cat I saw").stdout("PALINDROME").exit(0)


@check50.check(compiles)
def test1():
    """Check for not palindrome"""
    check50.run("./palindrome2").stdin("jellyfish").stdout("NOT PALINDROME").exit(0)
