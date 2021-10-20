import check50
import check50.c

@check50.check()
def exists():
    """Files exist."""
    check50.exists("concat.c")

@check50.check(exists)
def compiles():
    """Programs compile."""
    check50.c.compile("concat.c", lcs50=True)

@check50.check(compiles)
def add1():
    """adds 'hello' and 'world' """
    check50.run("./concat").stdin("hello").stdin("world").stdout("helloworld\n").exit()

@check50.check(exists)
def frees():
    """Uses free() to free memory"""
    app = open("concat.c").read()
    if 'free(' not in app:
        raise check50.Failure(f"You don't seem to be freeing allocated memory!")