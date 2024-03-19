class Solution {
    public boolean isPowerOfThree(int n) {
        long t = 1;
        while (n > 1 && t < n) {
            t += t << 1;
        }
        return t == n;
    }
}