public class Solution {
    private Dictionary<char, int> romanSymbolDictionary = new Dictionary<char, int>() {
        { 'I', 1 },
        { 'V', 5 },
        { 'X', 10 },
        { 'L', 50 },
        { 'C', 100 },
        { 'D', 500 },
        { 'M', 1000 }
    };
    
    private string Reverse(string s) {
        return new string(s.ToCharArray().Reverse().ToArray());
    }
    
    public int RomanToInt(string s) {
        int returnValue = 0;
        string reverseS = Reverse(s);
        char prevChar = (char)0;
        
        foreach (char c in reverseS) {
            
            if (
                prevChar != (char)0
                && (
                    ((prevChar == 'V' || prevChar == 'X') && c == 'I')
                    || ((prevChar == 'L' || prevChar == 'C') && c == 'X')
                    || ((prevChar == 'D' || prevChar == 'M') && c == 'C')
                )
            ) {
                returnValue -= romanSymbolDictionary[c];
                
            } else {
                returnValue += romanSymbolDictionary[c];
            }
            
            prevChar = c;
        }
        
        return returnValue;
    }
}