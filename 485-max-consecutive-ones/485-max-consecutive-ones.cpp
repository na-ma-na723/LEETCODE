class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int count = 0, i = 0, maxCount = 0; 
        
        while( i<nums.size() ) {
            while( i<nums.size() && nums[i] == 1 ) {
                count++;
                i++;
            }
            if( count > maxCount ) maxCount = count;
            count = 0;
            i++;
        }
        
        return maxCount;
    }
};