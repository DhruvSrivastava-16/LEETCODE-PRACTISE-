
class Solution {
    public String reorganizeString(String S) {
        if (S == null || S.length() == 0) {
            return "";
        }
 
        // step 1: do the word count
        int[] counts = new int[26];
        for (int i = 0 ; i < S.length(); i++) {
            char c = S.charAt(i);
            counts[c - 'a'] += 1;
        }
 
        // step2: sort the word count 
        PriorityQueue<Pair> pq = new PriorityQueue<>(new MyPairComparator());
         
        for (int i = 0; i < 26; i++) {
            if (counts[i] == 0) {
                continue;
            }
            Pair pair = new Pair((char)(i + 'a'), counts[i]);
            pq.offer(pair);
        }
 
        if (pq.peek().count > (S.length() + 1) / 2) {
            return "";
        }
 
        StringBuilder ans = new StringBuilder();
        while (!pq.isEmpty()) {
            Pair top = pq.poll();
            if (ans.length() > 0 && top.c == ans.charAt(ans.length() - 1)) {
                Pair secondTop = pq.poll();
                pq.offer(top);
                top = secondTop;
            }
 
            ans.append(top.c);
            top.count -= 1;
 
            if (top.count > 0) {
                pq.offer(top);
            }
        }
 
        return ans.toString();
    }
}
 
class Pair {
    char c;
    int count;
    public Pair(char c, int count) {
        this.c = c;
        this.count = count;
    }
}
 
class MyPairComparator implements Comparator<Pair> {
    @Override
    public int compare(Pair a, Pair b) {
        return b.count - a.count;
    }
}