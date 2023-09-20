class Solution {
public:
    int minPartitions(string n) {
        int res=0;
        for(int i=0;i<n.length();i++){
            int d=((int)n[i])-48;
            res=max(res,d);
        }
    return res;
    }
};