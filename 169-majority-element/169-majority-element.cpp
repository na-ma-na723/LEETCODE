class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map <int, int> m;
        
        
        for (int i = 0; i < nums.size(); i++)
            m[nums[i]]++;
        
        int maxCount = 0, count = m[nums[0]], element;
        
        for (auto i : m) {
            count = i.second;
            if( count > maxCount ) {
                element = i.first;
                maxCount = count;
            }
            
        }
        return element;
    }
};