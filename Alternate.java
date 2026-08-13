import java.util.*;
public class Alternate {
    public char[] alt(char[] x, char[] y) {
        int t = Math.min(x.length, y.length);
        ArrayList<Character> l = new ArrayList<>();
        for (int i = 0; i < t; i++) {
            l.add(x[i]);
            l.add(y[i]);
        }
        for (int i = t; i < x.length; i++) {
            l.add(x[i]);
        }
        for (int i = t; i < y.length; i++) {
            l.add(y[i]);
        }

    }
}
