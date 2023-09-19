class Solution {
public:
    int rob(vector<int>& nums) {
        int first=0,second=0;
        for(int i=0;i<nums.size();i++){
            int temp=std::max(first+nums[i],second);
            first=second;
            second=temp;
        }
        return std::max(first,second);
    }
};