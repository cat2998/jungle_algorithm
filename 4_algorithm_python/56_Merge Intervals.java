class Solution {
    public int[][] merge(int[][] intervals) {
        ArrayList<int[]> list = new ArrayList<int[]>();
        Arrays.sort(intervals, new Comparator<int[]> () {
            @Override
            public int compare(int[] a, int[] b) {
                if (a[0] == b[0])
                    return a[1] - b[1];
                return a[0] - b[0];
            }
        });
        int i = 0;
        while (i < intervals.length) {
            int start = intervals[i][0];
            int end = intervals[i][1];
            i += 1;
            while (i < intervals.length && end >= intervals[i][0]) {
                end = Math.max(end, intervals[i][1]);
                i += 1;
            }
            list.add(new int[]{start, end});
        }
        int[][] answer = new int[list.size()][];
        for (int j = 0; j < list.size(); j++)
            answer[j] = list.get(j);

        return answer;
    }
}