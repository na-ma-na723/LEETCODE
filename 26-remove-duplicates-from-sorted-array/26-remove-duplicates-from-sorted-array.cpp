class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i=0, n=nums.size();
        if( n==1 ) return 1;
        vector<int> res;
        
        while( i < n ) {
            res.push_back(nums[i]);
            int temp = nums[i];
            i++;
            while( i<n && nums[i] == temp ) i++;
        }
        
        for(int i=0; i<res.size(); i++) {
            nums[i] = res[i];
        }
        
        return res.size();
    }
};