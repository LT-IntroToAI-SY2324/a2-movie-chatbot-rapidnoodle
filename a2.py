from typing import List

def match(pattern: List[str], source: List[str]) -> List[str]:
    """Attempts to match the pattern to the source.

    % matches a sequence of zero or more words and _ matches any single word

    Args:
        pattern - a pattern using to % and/or _ to extract words from the source
        source - a phrase represented as a list of words (strings)

    Returns:
        None if the pattern and source do not "match" ELSE A list of matched words
        (words in the source corresponding to _'s or %'s, in the pattern, if any)
    """

    # current index we are looking at in source list
    sind = 0

    # current index we are looking at in pattern list
    pind = 0

    # stores substitutions we will return if matched
    result: List[str] = []

    while True:
        # returned when both indexes reach the end of their lists at the same time
        if sind >= len(source) and pind >= len(pattern):
            return result

        # returns None when the pattern doesnt match the source
        if pind >= len(pattern):
            return None

        # this is complicated, but whenever we reach a %, this is run
        if pattern[pind] == "%":
            # saves the current source index
            oldSind = sind
            
            # if the pattern ends with a "%", append the rest of the source words
            if pind + 1 >= len(pattern):
                sind = len(source)
            
            # sets sind to the index of the first occurance of the next word in the pattern list
            while sind < len(source) and source[sind] != pattern[pind + 1]:
                sind += 1
            
            # appends the result based on the sind index
            element = " ".join(source[oldSind:sind]) if sind > oldSind else ""
            result.append(element)

            # increments pind to prepare for the next iteration
            pind += 1

            # makes sure not to run any code below because this is a special case
            continue
        
        # returns None when the pattern doesnt match the source
        # this is here after the "%" case just in case "%" is the last element in the pattern
        if sind >= len(source):
            return None
        
        # directly indexes source if pattern is "_"
        if pattern[pind] == "_":
            result.append(source[sind])
            sind += 1
            pind += 1
            continue
        
        # if pattern and source match, continue
        # else return None because they dont match
        if source[sind] == pattern[pind]:
            sind += 1
            pind += 1
        else: return None


if __name__ == "__main__":
    assert match(["x", "y", "z"], ["x", "y", "z"]) == [], "test 1 failed"
    assert match(["x", "z", "z"], ["x", "y", "z"]) == None, "test 2 failed"
    assert match(["x", "y"], ["x", "y", "z"]) == None, "test 3 failed"
    assert match(["x", "y", "z", "z"], ["x", "y", "z"]) == None, "test 4 failed"
    assert match(["x", "_", "z"], ["x", "y", "z"]) == ["y"], "test 5 failed"
    assert match(["x", "_", "_"], ["x", "y", "z"]) == ["y", "z"], "test 6 failed"
    assert match(["%"], ["x", "y", "z"]) == ["x y z"], "test 7 failed"
    assert match(["x", "%", "z"], ["x", "y", "z"]) == ["y"], "test 8 failed"
    assert match(["%", "z"], ["x", "y", "z"]) == ["x y"], "test 9 failed"
    assert match(["x", "%", "y"], ["x", "y", "z"]) == None, "test 10 failed"
    assert match(["x", "%", "y", "z"], ["x", "y", "z"]) == [""], "test 11 failed"
    assert match(["x", "y", "z", "%"], ["x", "y", "z"]) == [""], "test 12 failed"
    assert match(["_", "%"], ["x", "y", "z"]) == ["x", "y z"], "test 13 failed"
    assert match(["_", "_", "_", "%"], ["x", "y", "z"]) == [
        "x",
        "y",
        "z",
        "",
    ], "test 14 failed"
    assert match(["x", "%", "z"], ["x", "y", "z", "z", "z"]) == None, "test 15 failed"

    print("All tests passed!")
