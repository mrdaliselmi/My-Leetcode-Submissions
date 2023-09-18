class Solution {
public:
    int mirrorReflection(int p, int q) {
        while (!(q%2) && !(p%2)){
            q/=2;
            p/=2;
        }
        if (q%2 && p%2) return 1;
        if (!(q%2) && p%2) return 0;
        if (q%2 && !(p%2)) return 2;
        return NULL;
    }
};