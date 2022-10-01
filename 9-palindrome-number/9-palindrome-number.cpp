class Solution {
public:
    bool isPalindrome(int x) {
        long int res = 0, temp = x;
        
        if( x < 0 ) return false;
        x = abs(x);
        
        while( x > 0 ) {
            int r = x%10;
            res = res*10 + r;
            x /= 10;
        }
        
        if(res == temp ) return true;
        
        return false;
    }
};