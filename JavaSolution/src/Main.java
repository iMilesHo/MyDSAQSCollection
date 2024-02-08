public class Main {
    public static void main(String[] args) {
        int n = 5;
        int[][] pascal = new int[n][];
        for (int i = 0; i < n; i++) {
            pascal[i] = new int[i + 1]; // since java array is 0-based
            pascal[i][0] = 1;
            for(int j=1; j<i; j++) {
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j];
            }
            pascal[i][i] = 1;
        }
        System.out.println(pascal);
    }
}