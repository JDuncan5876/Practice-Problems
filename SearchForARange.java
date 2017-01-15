/**
 * Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.
 *
 * Your algorithm's runtime complexity must be in the order of O(log n).
 *
 * If the target is not found in the array, return [-1, -1].
 *
 * @author Jared Duncan
 */
public class SearchForARange {
    public int[] searchRange(int[] nums, int target) {
        int[] result = new int[2];
        if (nums.length == 0) {
            result[0] = -1;
            result[1] = -1;
            return result;
        }
        int start = 0;
        int end = nums.length;
        int mid = (start + end) / 2;
        while (nums[mid] != target) {
            if (target < nums[mid]) {
                end = mid;
            } else {
                start = mid + 1;
            }
            if (start >= end) {
                result[0] = -1;
                result[1] = -1;
                return result;
            }
            mid = (start + end) / 2;
        }

        int i = mid;
        int j = mid;
        do {
            i--;
        } while (i >= 0 && nums[i] == target);
        do {
            j++;
        } while (j < nums.length && nums[j] == target);
        result[0] = ++i;
        result[1] = --j;
        return result;
    }
}