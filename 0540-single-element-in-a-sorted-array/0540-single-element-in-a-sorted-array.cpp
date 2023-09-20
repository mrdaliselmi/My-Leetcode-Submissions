class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int i=0;
       if (nums.size()>1){
           while((nums[i]==nums[i+1]))
               i+=2;
        return nums[i];}
        return nums[i];
    }
};