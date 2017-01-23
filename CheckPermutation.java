import java.util.HashMap;
/**
 * Given two strings, write a method to decide if one is a permutation of the other
 * @author Jared Duncan
 */
public class CheckPermutation {
    public static boolean checkPermutation(String str1, String str2) {
        if (str1.length() != str2.length()) {
            return false;
        }
        HashMap<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < str1.length(); i++) {
            char c = str1.charAt(i);
            if (map.containsKey(c)) {
                map.put(c, map.get(c) + 1);
            } else {
                map.put(c, 1);
            }
        }
        for (int i = 0; i < str2.length(); i++) {
            char c = str2.charAt(i);
            Integer value = map.get(c);
            if (value == null || value == 0) {
                return false;
            } else {
                map.put(c, i - 1);
            }
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println(checkPermutation("abc", "cba"));
        System.out.println(checkPermutation("aaaaa", "aaaab"));
        System.out.println(checkPermutation("aaaaa", "aaaa"));
        System.out.println(checkPermutation("", ""));
    }
}