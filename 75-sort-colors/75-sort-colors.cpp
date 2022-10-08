class Solution {
public:
    void sortColors(vector<int>& nums) {
        int freq[3];
        for(int i =0; i<3; i++) freq[i] = 0;
        for(int i=0; i<nums.size(); i++) freq[nums[i]]++;
        int i;
        for(i=0; i<freq[0]; i++) nums[i]=0;
        for( ; i<freq[0]+freq[1]; i++) nums[i]=1;
        for( ; i<freq[0]+freq[1]+freq[2]; i++) nums[i]=2;   
        
        // return nums;
    }
};