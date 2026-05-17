class Solution {
public:

    string encode(vector<string>& strs) {
        string init = "";
        for(string str: strs) {
            init += str + '\0';
        }

        return init;
    }

    vector<string> decode(string s) {
        vector<string> res;
        string currStr = "";
        for(char ch: s) {
            if(ch == '\0') {
                res.push_back(currStr);
                currStr = "";
            }
            else {
                currStr += ch;
            }
        }
        return res;
    }
};
