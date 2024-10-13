class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        
        kelvin = celsius + 273.15
        
        multip =   celsius * 1.80 
        
        Fahrenheit = multip + 32.00
        
        ans = [kelvin, Fahrenheit]
        return ans
        