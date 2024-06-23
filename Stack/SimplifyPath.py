"""
Given an absolute path for a Unix-style file system, which begins with a slash '/', transform this path into its simplified canonical path.

In Unix-style file system context, a single period '.' signifies the current directory, a double period ".." denotes moving up one directory level, and multiple slashes such as "//" are interpreted as a single slash. In this problem, treat sequences of periods not covered by the previous rules (like "...") as valid names for files or directories.

The simplified canonical path should adhere to the following rules:

It must start with a single slash '/'.
Directories within the path should be separated by only one slash '/'.
It should not end with a slash '/', unless it's the root directory.
It should exclude any single or double periods used to denote current or parent directories.
Return the new path.

 

Example 1:

Input: path = "/home/"

Output: "/home"

Explanation:

The trailing slash should be removed.

 
Example 2:

Input: path = "/home//foo/"

Output: "/home/foo"

Explanation:

Multiple consecutive slashes are replaced by a single one.

Example 3:

Input: path = "/home/user/Documents/../Pictures"

Output: "/home/user/Pictures"

Explanation:

A double period ".." refers to the directory up a level.

Example 4:

Input: path = "/../"

Output: "/"

Explanation:

Going one level up from the root directory is not possible.

Example 5:

Input: path = "/.../a/../b/c/../d/./"

Output: "/.../b/d"

Explanation:

"..." is a valid name for a directory in this problem.

 

Constraints:

1 <= path.length <= 3000
path consists of English letters, digits, period '.', slash '/' or '_'.
path is a valid absolute Unix path.
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        if path[0] != '/':
            return ''
        stack = []
        for c in path:
            #print('c - ', c)
            if len(stack) == 0:
                stack.append(c)
            else:
                if c == '/' and stack[-1] == '/':
                    # do not add current '/' to the stack
                    pass
                elif c == '/' and stack[-1] == '.':
                    # if the stack[-3:-2], if applicable, is '/.',
                    # delete the last two elements in the stack
                    if (len(stack) >= 3 and stack[-3] == '/' 
                        and stack[-2] == '.'):
                        # only when len(stack) >= 3, it is possible that
                        # we are looking at /.. in the stack, togehter with
                        # the current value of c, we have '/../' and we need to go up one level
                        del stack[-1]
                        del stack[-1]
                        del stack[-1]
                        while len(stack) > 0 and stack[-1] != '/':
                            del stack[-1]
                    elif len(stack) >= 2 and stack[-2] == '/':
                        # we are looking at '/.' in the stack, so we simply remove the one at the top of the stack
                        del stack[-1]
                    else:
                        stack.append(c)
                else:
                    stack.append(c)
            #print('stack - ', stack)
        if len(stack) > 1 and stack[-1] == '/':
            del stack[-1]
        if len(stack) > 1 and stack[0] != '/':
            stack.insert(0, '/')
        if len(stack) == 0:
            stack.append('/')
        return ''.join(stack)
    

so = Solution()

path = "/home/"
print(so.simplifyPath(path))

path = "/home//foo/"
print(so.simplifyPath(path))

path = "/home/user/Documents/../Pictures"
print(so.simplifyPath(path))

path = "/../"
print(so.simplifyPath(path))

path = "/.../a/../b/c/../d/./"
print(so.simplifyPath(path))


