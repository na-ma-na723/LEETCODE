class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int cs = 0, ms = -9999999;
        for(int i=0; i<nums.size(); i++) {
            cs = cs+ nums[i];
            if( ms<cs ) ms = cs;
            if( cs<0 ) cs = 0;
        }
        return ms;
    }
};