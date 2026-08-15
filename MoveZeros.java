
import java.util.*;

public class MoveZeros {

    public int[] zero(int[] x) {
        int write = 0;
        for (int i = 0; i < x.length; i++) {
            if (x[i] != 0) {
                x[write] = x[i];
                write += 1;
            }
        }
        for (int i = write; i < x.length; i++) {
            x[i] = 0;
        }
        return x;
    }

    public static void main(String[] args) {
        MoveZeros mz = new MoveZeros();
        int[] arr = {1, 0, 0, 4, 6, 0, 7};
        int[] result = mz.zero(arr);
        System.out.println(Arrays.toString(result));
    }
}
