class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
       std::unordered_map<int, int> counts;
       for(int i = 0; i < nums.size(); i++) {
           counts[nums[i]]++;
       }

       vector<vector<int>> freq(nums.size()+1);
       for(auto& entry: counts) {
            freq[entry.second].push_back(entry.first);
       }

       vector<int> res;
       int found = 0;
       for(int i = freq.size()-1; i>=0; i--) {
            for(int n: freq[i]) {
                res.push_back(n);
                if(res.size() == k) return res;
            }
       }

       return res;
       
    }
};
