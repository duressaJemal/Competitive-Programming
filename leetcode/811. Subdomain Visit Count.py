# Link: https://leetcode.com/problems/subdomain-visit-count/
#Q: 811. Subdomain Visit Count

# Time: O(N * M) where M = lenght of subdomain
# Space: O(M)

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        
        output = []
        count = defaultdict(int)
        
        for string in cpdomains:
            rep, domain = string.split()
            domain = domain.split(".")
            rep = int(rep)
            
            prev = ""
            for i in range(len(domain) - 1, -1, -1):
                if prev:
                    current = domain[i] + "." + prev
                    count[current] += rep
                    prev = current
                    
                else:
                    count[domain[i]] += rep
                    prev = domain[i]
            
        for key, value in count.items():
            output.append(str(value) + " " + key)
        
        return output
