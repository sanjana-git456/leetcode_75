
import java.util.*;

public class Except {

    public int[] exc(int[] x) {
        ArrayList<Integer> al = new ArrayList<>();
        for (int i = 0; i < x.length; i++) {
            int fix = x[i];
            int p = 1;
            for (int j = 0; j < x.length; j++) {
                if (x[j] != fix) {
                    p *= x[j];
                }
            }
        }
        return p;
    }
}
