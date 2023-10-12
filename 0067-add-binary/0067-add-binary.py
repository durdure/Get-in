class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_a = int(a, 2) # string binary a --> integer a
        int_b = int(b, 2) # string binary b --> integer b
        
        summation = int_a + int_b
        
        binary_summation = bin(summation)
        
        bin_str = binary_summation[2:] # remove '0b', not use [:2]
        
        return bin_str