#include<unordered_set>
class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        unordered_set<char> set;
        for(int i=0;i<jewels.length();i++){
            set.insert(jewels[i]);
        }
        int ans=0;
        for(int i=0;i<stones.length();i++){
            if(set.find(stones[i])!=set.end()) ans++;
        }
        return ans;
    }
};