/**
 * Given a positive integer, return its corresponding column title as appear
 * in an Excel sheet.
 *
 * @author Jared Duncan
 */
public class ConvertToTitle {
    public String convertToTitle(int n) {
        StringBuilder outBuilder = new StringBuilder();
        while (n > 0) {
            outBuilder.append((char) ((n - 1) % 26 + 'A'));
            n = (n - 1) / 26;
        }
        return outBuilder.reverse().toString();
    }
}