class Solution {
    public int myAtoi(String s) {
        s = s.trim();
        if (s.isEmpty()) return 0;
        
        int sign = 1;
        int i = 0;
        
        if (s.charAt(i) == '-') {
            sign = -1;
            i++;
        } else if (s.charAt(i) == '+') {
            i++;
        }
        
        int result = 0;
        while (i < s.length()) {
            char c = s.charAt(i);
            if (c < '0' || c > '9') break;
            
            int digit = c - '0';
            if (result > (Integer.MAX_VALUE - digit) / 10) {
                return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            }
            
            result = result * 10 + digit;
            i++;
        }
        
        return result * sign;
    }
}