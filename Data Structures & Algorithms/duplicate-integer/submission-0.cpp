class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
    for(size_t i = 0; i < nums.size(); ++i){
        for(size_t j = i + 1; j < nums.size(); ++j){
            if(nums.at(i) == nums.at(j)){
                return true;
            }
           
            }
    }
    return false;
    }

};
