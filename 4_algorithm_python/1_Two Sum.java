import java.util.ArrayList;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        int[] list = new int[2];
        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            if (map.containsKey(diff)) {
                list[0] = map.get(diff);
                list[1] = i;
                break;
            } else
                map.put(nums[i], i);
        }
        return list;
    }
}