#include <unordered_map>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> map;
        vector<int> ans;
        int comp;
        for(int i=0;i<nums.size();i++){
            comp=target-nums[i];
            if (map.find(comp)==map.end())
                map[nums[i]]=i;
            else return {i,map[comp]};
        }
        return ans;
};
};