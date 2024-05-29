class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> answer = new ArrayList<>();
        Arrays.sort(nums);
        for (int z = 0; z < nums.length - 2; z++) {
            while (z > 0 && z < nums.length - 2 && nums[z - 1] == nums[z])
                z += 1;
            int i = z + 1;
            int j = nums.length - 1;
            while (i < j) {
                if (nums[z] + nums[i] + nums[j] == 0) {
                    List<Integer> sum = Arrays.asList(new Integer[]{nums[z], nums[i], nums[j]});
                    answer.add(sum);
                }
                if (nums[z] + nums[i] + nums[j] < 0) {
                    i += 1;
                    while (i < nums.length && nums[i - 1] == nums[i])
                        i += 1;
                }
                else {
                    j -= 1;
                    while (j >= 0 && nums[j + 1] == nums[j])
                        j -= 1;
                }
            }
        }
        return answer;
    }
}