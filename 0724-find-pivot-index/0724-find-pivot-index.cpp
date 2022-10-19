class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int tsum = 0;
        for(int i=0; i<nums.size(); i++) tsum += nums[i];
        int csum = 0;
        for( int i=0; i<nums.size(); i++ ){
            tsum -= nums[i];
            if( csum == tsum ) return i;
            csum += nums[i];
        }
        return -1;
    }
};