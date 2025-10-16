import check50
import check50.c

@check50.check()
def exists():
    """llist_practice.c exists."""
    check50.exists("llist_practice.c")

@check50.check(exists)
def compiles():
    """llist_practice.c compiles."""
    check50.c.compile("llist_practice.c", lcs50=True)


@check50.check(compiles)
def reverse():
    """reverses list correctly"""
    check50.run("./llist_practice").stdout("List: 8 -> 2 -> 3 -> 4 -> 1 -> 5 -> NULL").exit()
