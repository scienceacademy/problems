from cs50 import SQL

import check50
import sqlparse

@check50.check()
def exists():
    """SQL files exists"""
    for i in range(1, 8):
        check50.exists(f"{i}.sql")
    check50.include("songs.db")

@check50.check(exists)
def test1():
    """1.sql produces correct result"""
    solution = {"Seven (feat. Latto) (Explicit Ver.)", "LALA", "vampire", "Cruel Summer", "WHERE SHE GOES", "Sprinter", "Ella Baila Sola", "Columbia", "fukumean", "La Bebe - Remix"}
    check_single_col(run_query("1.sql"),
        solution,
        ordered=False)

@check50.check(exists)
def test2():
    """2.sql produces correct result"""
    solution = ["White Christmas", "It's the Most Wonderful Time of the Year", "Lift Me Up - From Black Panther: Wakanda Forever - Music From and Inspired By", "Dawn FM", "Starry Eyes", "I'm Tired - From "'Euphoria'" An Original HBO Series", "traitor", "Happier Than Ever", "Notion", "Down Under (feat. Colin Hay)"]
    check_single_col(run_query("2.sql"),
        solution,
        ordered=True)

@check50.check(exists)
def test3():
    """3.sql produces correct result"""
    check_single_col(run_query("3.sql"),
        ["Te Bote - Remix", "SICKO MODE", "Walk It Talk It", "Him & I (with Halsey)", "Perfect"],
        ordered=True)

@check50.check(exists)
def test4():
    """4.sql produces correct result"""
    check_single_col(run_query("4.sql"),
            {"Dura", "Me Niego", "Feel It Still", "1, 2, 3 (feat. Jason Derulo & De La Ghetto)", "Criminal"},
        ordered=False)

@check50.check(exists)
def test5():
    """5.sql produces correct result"""
    check_single_cell(run_query("5.sql"), "0.65906", floating=True)

@check50.check(exists)
def test6():
    """6.sql produces correct result"""
    check_single_col(run_query("6.sql"),
        {"rockstar (feat. 21 Savage)", "Psycho (feat. Ty Dolla $ign)", "Better Now", "I Fall Apart", "Candy Paint", "Congratulations"},
        ordered=False)

@check50.check(exists)
def test7():
    """7.sql produces correct result"""
    check_single_cell(run_query("7.sql"), "0.6375", floating=True)

@check50.check(exists)
def test8():
    """8.sql produces correct result"""
    check_single_col(run_query("8.sql"),
{"rockstar (feat. 21 Savage)",  "Psycho (feat. Ty Dolla $ign)", "Girls Like You (feat. Cardi B)", "Look Alive (feat. Drake)", "These Days (feat. Jess Glynne, Macklemore & Dan Caplen)", "Meant to Be (feat. Florida Georgia Line)", "Taste (feat. Offset)", "Solo (feat. Demi Lovato)", "River (feat. Ed Sheeran)", "Finesse (Remix) [feat. Cardi B]", "Freaky Friday (feat. Chris Brown)", "FEFE (feat. Nicki Minaj & Murda Beatz)", "Body (feat. brando)", "Fuck Love (feat. Trippie Redd)", "Dejala que vuelva (feat. Manuel Turizo)", "1, 2, 3 (feat. Jason Derulo & De La Ghetto)", "Corazon (feat. Nego do Borel)", "I Miss You (feat. Julia Michaels)"},
        ordered=False)

def run_query(filename):
    try:
        with open(filename) as f:
            query = f.read().strip()
            query = sqlparse.format(query, strip_comments=True).strip()
        db = SQL("sqlite:///songs.db")
        result = db.execute(query + " LIMIT 10")
        return result
    except Exception as e:
        raise check50.Failure(f"Error when executing query: {str(e)}")

def check_single_col(actual, expected, ordered=False):
    """
    Checks for queries that return just a single column, ensures correct results.
    """

    # Make sure query returned results
    if actual is None or actual == []:
        raise check50.Failure("Query did not return results")

    # Make sure there is only a single column
    row_counts = {len(list(row.values())) for row in actual}
    if row_counts != {1}:
        raise check50.Failure("Query should only return a single column")

    # Get data from column
    try:
        result = [str(list(row.values())[0]) for row in actual]
        result = result if ordered else set(result)
    except IndexError:
        return None

    # Check column data against expected values
    expected = [str(value) for value in expected]
    if not ordered:
        expected = set(expected)
    if result != expected:
        raise check50.Mismatch("\n".join(expected), "\n".join(list(result)))

def check_single_cell(actual, expected, floating=False):
    if floating:
        if len(actual) != 1 or len(actual[0]) != 1:
            raise check50.Failure("Query should only return a single column and single cell")
        if abs(float(list(actual[0].values())[0]) - float(expected)) > 0.01:
            raise check50.Mismatch("\n".join(expected), str(actual))
        return
    return check_single_col(actual, [expected], ordered=True)

def check_double_col(actual, expected, ordered=False):
    """
    Checks for queries that return just a single column, ensures correct results.
    """

    # Make sure query returned results
    if actual is None or actual == []:
        raise check50.Failure("Query did not return results")

    # Make sure there is only a single column
    row_counts = {len(list(row.values())) for row in actual}
    if row_counts != {2}:
        raise check50.Failure("Query should only return a single column")

    # Get data from column
    try:
        result = []
        for row in actual:
            values = list(row.values())
            result.append({str(values[0]), str(values[1])})
        result = result if ordered else set(result)
    except IndexError:
        return None

    # Check column data against expected values
    if result != expected:
        raise check50.Mismatch("\n".join([str(entry) for entry in list(expected)]),
                              "\n".join([str(entry) for entry in list(result)]))

