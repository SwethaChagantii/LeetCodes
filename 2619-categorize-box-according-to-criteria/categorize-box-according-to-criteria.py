class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        vol = length*width*height
        if (any(value >= 10**4 for value in (length, width, height, mass)) or vol >= 10**9) and mass>= 100:
            return "Both"
        elif any(value >= 10**4 for value in (length,width,height,mass)) or vol >= 10**9:
            return "Bulky"
        elif mass >= 100:
            return "Heavy"
        else:
            return "Neither"
        