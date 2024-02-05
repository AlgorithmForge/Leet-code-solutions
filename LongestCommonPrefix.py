class Solution:
    def loPre(self, strs):
        # Initialize an empty list to store the common prefix characters
        longest_pre = []

        # Check if the input list is not empty
        if strs and len(strs) > 0:
            # Sort the list of strings lexicographically
            strs = sorted(strs)

            # Get the first and last strings after sorting
            first, last = strs[0], strs[-1]

            # Iterate through the characters of the first string
            for i in range(len(first)):
                # Check if the corresponding character in the last string is the same
                if len(last) > i and last[i] == first[i]:
                    # Append the common character to the longest_pre list
                    longest_pre.append(last[i])
                else:
                    # If characters are not the same, return the current common prefix
                    return "".join(longest_pre)

        # Return the common prefix as a string
        return "".join(longest_pre)
