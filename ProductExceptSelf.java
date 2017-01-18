/**
 * Given an array of n integers where n > 1, nums, return an array output such
 * that output[i] is equal to the product of all the elements of nums except nums[i].
 *
 * @author Jared Duncan
 */
public class ProductExceptSelf {
    public int[] productExceptSelf(int[] nums) {
        int product = 1;
        int zeroCount = 0;
        int zeroIndex = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                if (++zeroCount == 2) {
                    return new int[nums.length];
                } else {
                    zeroIndex = i;
                }
            } else {
                product *= nums[i];
            }
        }
        int[] output = new int[nums.length];
        if (zeroCount == 1) {
            output[zeroIndex] = product;
        } else {
            for (int i = 0; i < nums.length; i++) {
                output[i] = product / nums[i];
            }
        }
        return output;
    }
}