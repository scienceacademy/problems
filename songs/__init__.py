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
    solution = ["White Christmas", "It's the Most Wonderful Time of the Year", "Lift Me Up - From Black Panther: Wakanda Forever - Music From and Inspired By", "Dawn FM", "Starry Eyes", "I'm Tired - From \"Euphoria\" An Original HBO Series", "traitor", "Happier Than Ever", "Notion", "Down Under (feat. Colin Hay)"]
    check_single_col(run_query("2.sql"),
        solution,
        ordered=True)

@check50.check(exists)
def test3():
    """3.sql produces correct result"""
    check_single_col(run_query("3.sql"),
        ["Agudo M��gi", "White Christmas", "The Christmas Song (Merry Christmas To You) - Remastered 1999", "Let It Snow! Let It Snow! Let It Snow!", "A Holly Jolly Christmas - Single Version", "Jingle Bell Rock", "Jingle Bells - Remastered 1999", "Rockin' Around The Christmas Tree", "It's Beginning to Look a Lot Like Christmas (with Mitchell Ayres & His Orchestra)", "Run Rudolph Run - Single Version"],
        ordered=True)

@check50.check(exists)
def test4():
    """4.sql produces correct result"""
    check_single_col(run_query("4.sql"),
            {"Seven (feat. Latto) (Explicit Ver.)", "SABOR FRESA", "Calm Down (with Selena Gomez)", "TQM", "BABY HELLO", "Cold Heart - PNAU Remix", "VAGABUNDO", "QUEMA", "Mi Bello Angel", "PRC"},
        ordered=False)

@check50.check(exists)
def test5():
    """5.sql produces correct result"""
    check_single_cell(run_query("5.sql"), "64.27415", floating=True)

@check50.check(exists)
def test6():
    """6.sql produces correct result"""
    check_single_col(run_query("6.sql"),
        {"Circles", "Chemical", "Overdrive"},
        ordered=False)

@check50.check(exists)
def test7():
    """7.sql produces correct result"""
    check_single_cell(run_query("7.sql"), "Blinding Lights")

@check50.check(exists)
def test8():
    """8.sql produces correct result"""
    check_double_col(run_query("8.sql"),
        [{"G", "7"},
        {"", "5"},
        {"F", "4"},
        {"E", "4"},
        {"D", "4"},
        {"G#", "3"},
        {"F#", "3"},
        {"A", "2"},
        {"B", "1"},
        {"A#", "1"}],
        ordered=True)

def run_query(filename):
    try:
        with open(filename) as f:
            query = f.read().strip()
            query = sqlparse.format(query, strip_comments=True).strip()
            if "LIMIT" not in query:
                query = query.replace(";", " LIMIT 10;")
        db = SQL("sqlite:///songs.db")
        result = db.execute(query)
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

