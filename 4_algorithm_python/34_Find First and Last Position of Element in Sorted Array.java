class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] answer = new int[] { -1, -1 };
        int i = 0;
        int j = nums.length - 1;
        if (nums.length == 0)
            return answer;
        if (nums.length == 1 && nums[0] == target)
            return new int[] { 0, 0 };
        while (i <= j) {
            int mid = (i + j) / 2;
            if (nums[mid] < target)
                i = mid + 1;
            else if (nums[mid] > target)
                j = mid - 1;
            else {
                int temp = mid;
                while (mid > 0 && nums[mid] == nums[mid - 1])
                    mid -= 1;
                answer[0] = mid;
                while (temp < nums.length - 1 && nums[temp] == nums[temp + 1])
                    temp += 1;
                answer[1] = temp;
                break;
            }
        }
        return answer;
    }
}