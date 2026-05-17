class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<string, vector<string>> similars;
        for(int i = 0; i < strs.size(); i++) {
            string curr = strs[i];
            std::sort(curr.begin(), curr.end());
            similars[curr].push_back(strs[i]);
        }
        
        vector<vector<string>> ret;
        for(auto it = similars.begin(); it != similars.end(); it++) {
            vector<string> currIdxs = it->second;
            ret.push_back(currIdxs);
        }
        return ret;
    }
};
