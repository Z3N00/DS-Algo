"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

"""
def romanToInt(s: str):

    roman = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, \
                 'C': 100, 'D' : 500, 'M' : 1000}
    sum = 0
    penalty = 0
    for i in range(len(s)):
        if i+1 != len(s) and roman[s[i]] < roman[s[i+1]]:
            print(f'current sum = {sum} penalizing {roman[s[i]]}')
            penalty += roman[s[i]]
            
        else:
            print(f'current sum = {sum} adding {roman[s[i]]}')
            sum += roman[s[i]]
        
    print(sum, penalty)  
    
    return sum - penalty


# print(romanToInt("MCMXCIV"))
romanToInt("MCMXCIV")

