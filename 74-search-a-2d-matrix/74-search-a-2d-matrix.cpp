bool binSearch(vector<int> nums, int target, int n) {
    int l = 0, r = n-1;
    while(l<=r) {
        int mid = (l + r)/2;
        if( target == nums[mid] )return true;
        else if( target > nums[mid] ) l = mid + 1;
        else if( target < nums[mid] ) r = mid - 1;
    }
    return false;
}

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int size = matrix[0].size();
        for (int i = 0; i < matrix.size(); i++) {
            if( target >= matrix[i][0] && target <= matrix[i][size-1]  ) {
                return binSearch( matrix[i], target, size );
            }
        }
        return false;
    }
};