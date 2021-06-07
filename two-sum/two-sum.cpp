#include<iostream>
#include<vector>
using namespace std;

class Solution {
    public:
    vector <int> twoSum(vector <int> nums, int target) {
        int i,j;
        int size = nums.size();
        int x,y,f=0;
        vector <int> v;
        for(i=0;i<size-1;i++)
        {
            for(j=i+1;j<size;j++)
            {
                if(nums[i]+nums[j]==target)
                {
                    v.push_back(i);
                    v.push_back(j);
                }

            }
        }

        return v;
    }
};