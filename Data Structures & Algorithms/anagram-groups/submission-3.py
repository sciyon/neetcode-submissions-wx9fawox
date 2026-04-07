class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for word in strs:
            key = "".join(sorted(word))  # sort characters to form key

            if key in d:
                d[key].append(word)
            else:
                d[key] = [word]

        return list(d.values())