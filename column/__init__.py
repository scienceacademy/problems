import check50
import check50.c
import re

@check50.check()
def exists():
    """column.c exists"""
    check50.exists("column.c")

@check50.check(exists)
def compiles():
    """column.c compiles"""
    check50.c.compile("column.c", lcs50=True)

@check50.check(compiles)
def encrypt1():
    """encrypts "secretmessage" as "ctsgeeeasrmse" using key "one" """
    check50.run("./column one").stdin("secretmessage").stdout("ciphertext: ctsgeeeasrmse\n").exit(0)


@check50.check(compiles)
def encrypt2():
    """encrypts "This is a secret." as "" using key "hello" """
    check50.run("./column hello").stdin("This is a secret.").stdout("ciphertext: haeTsristseic\n").exit(0)

@check50.check(compiles)
def encrypt3():
    """encrypts "This is a secret." as "" using key "heLlo" """
    check50.run("./column hello").stdin("This is a secret.").stdout("ciphertext: haeTsristseic\n").exit(0)

@check50.check(compiles)
def handles_no_argv():
    """handles lack of key"""
    check50.run("./column").exit(1)

@check50.check(compiles)
def handles_invalid_length():
    """handles invalid key length"""
    check50.run("./column ab").exit(2)

@check50.check(compiles)
def handles_invalid_key_chars():
    """handles invalid characters in key"""
    check50.run("./column abc1").exit(2)

