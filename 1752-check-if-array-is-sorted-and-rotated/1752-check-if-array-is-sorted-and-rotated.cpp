class Solution {
public:
    bool check(vector<int>& nums) {
        int n = nums.size(), i;
        for(i=1 ;i<n; i++) {
            if( !(nums[i] >= nums[i-1]) ) break;
        }
        
        if( i==n ) return true;
        i++;
        
        while( i<n ) {
            if( !(nums[i] >= nums[i-1]) ) return false;
            i++;
        }
        if( nums[0] < nums[n-1] ) return false;
        return true;
    }
};