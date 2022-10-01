class Solution {
public:
    int reverse(int x) {
        long int res = 0;
        bool isNeg = false;
        if( x < 0 ) isNeg = true;
        x = abs(x);
        
        while( x > 0 ) {
            int r = x%10;
            res = res*10 + r;
            x /= 10;
        }
        
        if( isNeg ) res*=(-1);
        
        if(res < INT_MIN || res > INT_MAX) return 0;
        
        return res;
        
        
    }
};