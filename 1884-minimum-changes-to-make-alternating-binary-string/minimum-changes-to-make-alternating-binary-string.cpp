class Solution {
public:
    int minOperations(string s) {
        int n = s.length();
        int count1 = 0, count2 = 0;
        for (int i = 0; i < n; i++) {
            if (s[i] != '0' + i % 2) {
                count1++;
            }
        }
        for (int i = 0; i < n; i++) {
            if (s[i] != '1' - i % 2) {
                count2++;
            }
        }
        return std::min(count1, count2);
    }
};