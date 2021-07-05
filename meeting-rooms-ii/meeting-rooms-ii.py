class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans_rooms = 0

        h = []
        heapq.heapify(h)

        heapq.heappush(h,intervals[0][1])

        for i in intervals[1:]:
            if h[0] <= i[0]:
                heapq.heappop(h)

            heapq.heappush(h,i[1])

        return len(h)

        