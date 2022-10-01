class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        if(n==1) return;
        k = k%n;
        
        
        vector<int> temp;
        for(int i = 0; i<n-k; i++) {
            temp.push_back(nums[i]);
        }
        
        vector<int> res;
        for(int i = n-k; i<n; i++) {
            res.push_back(nums[i]);
        }
        
        for(int i=0; i<res.size(); i++) {
            nums[i] = res[i];
        }
        for(int i=res.size(), j=0; i<n; i++, j++) {
            nums[i] = temp[j];
        }
        
        
    }
};