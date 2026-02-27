class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        nums1.insert(nums1.end(),nums2.begin(),nums2.end());
        sort(nums1.begin(),nums1.end());
        int n=nums1.size();
        double ans;
        if(n%2==0){
            ans=nums1[(n/2)-1]+nums1[n/2];
            ans/=2;
        }
        else{
            ans=nums1[n/2];
        }
        return ans;
    
    }
};