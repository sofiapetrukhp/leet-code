"13. Roman to Integer"

class Solution:
    def romanToInt(self, s: str) -> int:
        
        dicionario = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        resultado = 0

        for i in range(len(s) - 1):
            if dicionario[s[i]] < dicionario[s[i + 1]]:
                resultado -= dicionario[s[i]]
            else:
                resultado += dicionario[s[i]]
        resultado += dicionario[s[-1]]
        return resultado
