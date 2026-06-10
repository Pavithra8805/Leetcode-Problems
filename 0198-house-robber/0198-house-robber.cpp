class Solution {
public:
    int rob(vector<int>& nums) {
        int prev = 0;
        int prev2 =  0;
        for(int num : nums) {
            int current = max(prev, prev2 + num);
            prev2 = prev;
            prev = current;
        }
        return prev;
    }
};