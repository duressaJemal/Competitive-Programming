class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        counter = Counter(deck)
        values = list(counter.values())
        
        curent_gcd = values[0]
        for val in values:
            curent_gcd = gcd(curent_gcd, val)
        
        return curent_gcd > 1