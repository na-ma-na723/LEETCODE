class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int n = nums.size();
        int r = n-1, l = 0;
        if( n == 1 || nums[0] > nums[1]) return 0;
        if(  nums[r] > nums[r-1] ) return r;
        while( l<=r ) {
            int mid = (l+r)/2;
            if( nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1] ) return mid;
            else if( nums[mid] < nums[mid+1] ) l = mid+1;
            else if( nums[mid] < nums[mid-1] ) r = mid-1;
        }
        return 0;
    }
};