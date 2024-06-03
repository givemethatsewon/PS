class Solution(object):
    def lastStoneWeight(self, stones):
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)

            if y == x:
                pass
            else:
                new_stone = y - x
                heapq.heappush(stones, new_stone)

        if not stones:
            return 0
        else:
            return -stones[0]