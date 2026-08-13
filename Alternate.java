
public class Alternate {

    public String alt(char[] x, char[] y) {
        int t = Math.min(x.length, y.length);
        StringBuilder l = new StringBuilder();
        for (int i = 0; i < t; i++) {
            l.append(x[i]);
            l.append(y[i]);
        }
        for (int i = t; i < x.length; i++) {
            l.append(x[i]);
        }
        for (int i = t; i < y.length; i++) {
            l.append(y[i]);
        }
        return l.toString();
    }
}
