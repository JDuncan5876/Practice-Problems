/**
 * Given an unsorted integer array, find the first missing positive integer.
 *
 * Classified as Hard on LeetCode, submission beats ~80% of accepted runtimes
 *
 * @author Jared Duncan
 */
public class FirstMissingPositive {
    public int firstMissingPositive(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            if (num > 0 && num <= nums.length) {
                if (nums[num - 1] != num) {
                    int temp = nums[num - 1];
                    nums[num - 1] = nums[i];
                    nums[i] = temp;
                    if (nums[i] > 0 && nums[i] != i + 1) {
                        i--;
                    }
                } else if (num - 1 != i) {
                    nums[i] = -1;
                }
            }
        }

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != i + 1) {
                return i + 1;
            }
        }
        return nums.length + 1;
    }
}