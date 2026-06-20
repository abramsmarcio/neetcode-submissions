class Solution {
    int[] arr;

    public int climbStairs(int n) {
        arr = new int[n + 1];

        for (int i = 0; i <= n; i++) {
            arr[i] = -1;
        }

        return func(n);
    }

    public int func(int i) {
        if (i <= 1)
            return 1;

        if (arr[i] != -1)
            return arr[i];

        int l = func(i - 1);
        int r = func(i - 2);

        return arr[i] = l + r;
    }
}