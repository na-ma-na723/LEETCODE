class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int count =0, i=0, n=nums.size();
        vector<int> res;
        while( i<n ) {
            if( nums[i] == 0 ) {
                count++;
            }
            else {
                res.push_back(nums[i]);
            }
            i++;
        }
        
        for(int i=0; i<res.size(); i++) {
            nums[i] = res[i];
        }
        for(int i=res.size(); i<n; i++) {
            nums[i] = 0;
        }
    }
};