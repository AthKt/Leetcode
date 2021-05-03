class Solution:
    def defangIPaddr(self, address: str) -> str:
        counter = ""
        for i in address:
            if i == ".":
                counter += "[.]"
            else:
                counter += i
        return counter

solution = Solution()
address = "1.1.1.1"
print(solution.defangIPaddr(address))

# Extra Solution
# class Solution:
#    def defangIPaddr(self, address: str) -> str:
#        return address.replace(".", "[.]")