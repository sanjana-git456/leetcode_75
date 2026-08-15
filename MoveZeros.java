
public class MoveZeros {

    public char[] zero(char[] x) {
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
}
