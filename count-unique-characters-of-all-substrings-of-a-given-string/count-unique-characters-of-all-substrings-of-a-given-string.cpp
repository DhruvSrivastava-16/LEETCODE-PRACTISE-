class Solution {
public:
	const int M = 1000000007;
    int uniqueLetterString(string s) {
		int n = s.length();
        
		vector<long long> L(n, -1), R(n, -1);
		vector<long long> lastL(26, -1), lastR(26, n);
		for (int i = 0; i < n; i++){
			L[i] = i - lastL[s[i] - 'A'];
			lastL[s[i] - 'A'] = i;
		}     
		for (int i = n-1; i >= 0; i--){
			R[i] = lastR[s[i] - 'A'] - i;
			lastR[s[i] - 'A'] = i;
		}   
		int ans = 0; 

		for (int i = 0; i < n; i++){
			ans = (ans + (L[i] * R[i]) % M) % M;
		}
		return ans;
    }
};