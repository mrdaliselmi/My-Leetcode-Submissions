class HeapItem(object):
    def __init__(self, word, count):
        self.count = count
        self.word = word
    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        freq = Counter(words)
        min_heap = []
        for word, count in freq.items():
            heapq.heappush(min_heap, HeapItem(word,count))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        result = []
        while min_heap:
            result.append(heapq.heappop(min_heap).word)
        result.reverse()
        return result
        