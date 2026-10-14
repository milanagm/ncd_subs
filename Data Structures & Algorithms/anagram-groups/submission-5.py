class Solution:
    def groupAnagrams (self, strs: List[str]) -> List[List[str]]:
            map = defaultdict(list)

            for word in strs:
                s_w = "".join(sorted(word)) 
                map[s_w].append(word)

            return list(map.values())