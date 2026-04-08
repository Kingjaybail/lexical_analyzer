public class Test4 {
    public static int add(int a, int b) {
        return a + b;
    }

    public static boolean isEven(int n) {
        return n == 0;
    }

    public static void main(String[] args) {
        int result = add(3, 4);
        boolean check = isEven(result);
    }
}
