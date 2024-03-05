def isMatch(s: str, p: str) -> bool:
    # Initialize the DP table
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    print(f'Initialization of the 2d array \n {dp}')
    dp[0][0] = True  # Empty string matches empty pattern
    print(f'Adding True to the top left of the 2d array \n {dp}')

    # Fill the first row for patterns like a*, a*b*, a*b*c* etc.
    print(f'length of p is {len(p)}')
    for j in range(2, len(p) + 1):
        if p[j-1] == '*':
            print(f'blah blah {j}')
            dp[0][j] = dp[0][j-2]
    print(f'Filling in the 2d array with star values \n {dp}')

    # Fill the DP table
    for i in range(1, len(s) + 1):
        print(f'i = {i}')
        for j in range(1, len(p) + 1):
            print(f'j = {j}')
            print(f'value at i = {i}, j = {j}, {dp[i][j]}')
            if p[j-1] == s[i-1] or p[j-1] == '.':
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':
                # Check zero occurrence
                dp[i][j] = dp[i][j-2]
                # Check one or more occurrence if character before * matches s[i-1]
                if p[j-2] == s[i-1] or p[j-2] == '.':
                    dp[i][j] = dp[i][j] or dp[i-1][j]
    
    print(f'Final 2d array \n {dp}')

    return dp[len(s)][len(p)]

result = isMatch(s = "aa", p ="a*")
print(result)