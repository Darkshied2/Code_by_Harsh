class Solution {
public:
    int triangularSum(vector<int>& nums) {
        int n=nums.size()-1;
        while(n--){
            int k=0;
            for(int i=nums.size()-1;i>k;i--){
                nums[i]=(nums[i]+nums[i-1])%10;

            }
            k+=1;
        }
        return nums[nums.size()-1];
    }
};
