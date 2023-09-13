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
    sind = 0  # current index we are looking at in source list
    pind = 0  # current index we are looking at in pattern list
    result: List[str] = []  # to store substitutions we will return if matched

    # source: ["x", "y", "z"]
    # pattern: ["x", "_", "z"]

    # michael thinking
    # loops through lists
    
    def getNextIndex():
        x = sind + 1
        y = pind + 1
        while x < len(source) and source[x] != pattern[y]:
            x += 1
            y += 1
        return x

    while sind < len(source) and pind < len(pattern):
        if pattern[pind] == "_":
            result.append(source[sind])
            sind += 1
            pind += 1
            continue

        if pattern[pind] == "%":
            index = getNextIndex()
            result.append(" ".join(source[sind:index]))
            sind += index
            pind += 1
            continue
        
        if source[sind] == pattern[pind]:
            sind += 1
            pind += 1
            continue
        else: return None

    print(result)
    return result

    # keep checking as long as we haven't hit the end of either pattern or source while
    # pind is still a valid index OR sind is still a valid index (valid index means that
    # the index is != to the length of the list)
    while sind != len(source) and pind != len(pattern):
        # your job is to fill out the body of this loop

        # you should delete the following line
        # return ["Not done yet :)"]

        # 1) if we reached the end of the pattern but not source
        if pind == len(pattern) and pind != len(source): return None

        # 2) if the current thing in the pattern is a %
        # WARNING: this condition contains the bulk of the code for the assignment
        # If you get stuck on this one, we encourage you to attempt the other conditions
        #   and come back to this one afterwards
        if pattern[pind] == "%":
            if pind:
                pass
            # value of index after pind should be equal to next one
            # source[x:y] -- x = sind, y = index of start of same
            x = sind
            y = sind
            while y < len(source):
                waitFor = pattern[x + 1]



        # 3) if we reached the end of the source but not the pattern
        if sind == len(source) and pind != len(pattern):
            return None

        # 4) if the current thing in the pattern is an _
        if pattern[pind] == "_":
            result.append(source[sind])

        # 5) if the current thing in the pattern is the same as the current thing in the
        # source
        if (pattern[pind] == source[sind]):
            pind += 1
            sind += 1
        else:
            return None

        # 6) else : this will happen if none of the other conditions are met it
        # indicates the current thing it pattern doesn't match the current thing in
        # source

    return result


if __name__ == "__main__":
    assert match(["x", "y", "z"], ["x", "y", "z"]) == [], "test 1 failed"
    assert match(["x", "z", "z"], ["x", "y", "z"]) == None, "test 2 failed"
    # assert match(["x", "y"], ["x", "y", "z"]) == None, "test 3 failed"
    # assert match(["x", "y", "z", "z"], ["x", "y", "z"]) == None, "test 4 failed"
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
    # this last case is a strange one, but it exposes an issue with the way we've
    # written our match function
    assert match(["x", "%", "z"], ["x", "y", "z", "z", "z"]) == None, "test 15 failed"

    print("All tests passed!")
