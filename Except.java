
import java.util.*;

public class Except {

    public ArrayList<Integer> exc(int[] x) {
        ArrayList<Integer> al = new ArrayList<>();
        for (int i = 0; i < x.length; i++) {
            int p = 1;
            for (int j = 0; j < x.length; j++) {
                if (j != i) {
                    p *= x[j];
                }
            }
            al.add(p);
        }
        return al;
    }

    public static void main(String[] args) {
        Except e = new Except();
        int[] arr = {1, 2, 3, 4};
        System.out.println(e.exc(arr));
    }
}
