import java.util.HashSet;
/**
 * Implement an algorithm to determine if a string has all unique characters.
 * @author Jared Duncan
 */
public class IsUnique {
    public static boolean isUnique(String str) {
        HashSet<Character> set = new HashSet<>();
        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            if (set.contains(c)) {
                return false;
            } else {
                set.add(c);
            }
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println(isUnique("abcdefghijklmnopqrstuvwxyz"));
        System.out.println(isUnique("aa"));
        System.out.println(isUnique("Hello World!"));
        System.out.println(isUnique("!@#$%^&*("));
    }
}