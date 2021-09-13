import check50
import check50.c

@check50.check()
def exists():
    """Files exist."""
    check50.exists("reverse.c")
    check50.exists("palindrome.c")

@check50.check(exists)
def compiles():
    """Programs compile."""
    check50.c.compile("reverse.c", lcs50=True)
    check50.c.compile("palindrome.c", lcs50=True)

@check50.check(compiles)
def reverse():
    """Reverses a string"""
    check50.run("./reverse").stdin("Hello").stdout("olleH\n").exit()


@check50.check(compiles)
def pal1():
    """Checks tacocat"""
    check50.run("./palindrome").stdin("tacocat").stdout("PALINDROME\n").exit()

@check50.check(compiles)
def pal2():
    """Checks not a palindrome"""
    check50.run("./palindrome").stdin("This is not a palindrome").stdout("NOT PALINDROME\n").exit()
