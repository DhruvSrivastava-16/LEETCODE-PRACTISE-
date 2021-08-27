class Solution {
public:
    string longestPalindrome(string s) {
        string ans;
        int len = s.size(),ansl=0,ansr=0;
        for(int i=0;i<len;i++) {
            
            //Palindromes of odd length
            int l = i,r = i;
            while(l>=0 && r<len && s[l] == s[r]) l--,r++;
              l++,r--;
            
            if(r-l>ansr-ansl)ansl = l,ansr = r;
            
            //Palindromes of even length
            l = i,r = i+1;
            while(l>=0 && r<len && s[l] == s[r])l--,r++;
            l++,r--;
            
            if(r-l>ansr-ansl)ansl = l,ansr = r;
            
        }for(int i=ansl;i<=ansr;i++) ans+=s[i];
        return ans;
    }
};