# 3. Create a class to find the three elements that sum to zero from a set of n real numbers.
# Input array: [-25,-10,-7,-3,2,4,8,10]
# Output: [[-10,2,8],[-7,-3,10]]

class Result():
    def three_ele(self,inp):
        list1=[]
        found = False
        for i in range(len(inp)):
            s = set() 
            for j in range(i + 1, len(inp)): 
                x = -(inp[i] + inp[j])
                if x in s: 
                    list1.append((x, inp[i], inp[j]))
                    found = True
                else: 
                    s.add(inp[j]) 
        if found == False: 
            print("No Triplet Found")
        return list1

ans=Result()
a=ans.three_ele( [-25,-10,-7,-3,2,4,8,10])
print (a)