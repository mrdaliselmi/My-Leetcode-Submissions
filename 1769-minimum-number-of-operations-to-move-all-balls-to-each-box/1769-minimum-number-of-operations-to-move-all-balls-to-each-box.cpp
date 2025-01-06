class Solution {
public:
    vector<int> minOperations(string boxes) {
        vector<int> ans(boxes.length());
        // for(int i=0;i<boxes.length();i++){
        //     for(int j=0;j<boxes.length();j++){
        //         if (((int)(boxes[j])-48)&&(i!=j)) 
        //             ans[i]+=abs(j-i);
        //     }
        // }
        vector<int> left(boxes.size(), 0);
        vector<int> right(boxes.size(), 0);
        
        int leftCount = 0, rightCount = 0;
        for (int i = 0; i < boxes.size(); i++) {
            if (i != 0) left[i] += leftCount + left[i-1];
            if (boxes[i] == '1') leftCount++;
        }
        for (int i = boxes.size() - 1; i >= 0; i--) {
            if (i != boxes.size() - 1) right[i] += rightCount + right[i+1];
            if (boxes[i] == '1') rightCount++;
        }
        for (int i = 0; i < boxes.size(); i++) {
            ans[i]=left[i] + right[i];
        }
        
        return ans;
    }
};