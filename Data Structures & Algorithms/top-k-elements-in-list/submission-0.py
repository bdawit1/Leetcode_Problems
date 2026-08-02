class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Standard count with a hash map
        count = {}                              

        for i in nums:                         
            count[i] = count.get(i, 0) + 1      

        result = []                             # list that will return results

        # Step 2: Loop k times to grab the highest element
        for i in range(k):                      # repeat k times, once for each number we need to collect
            highest_num = None                  # track the most frequent number found so far this pass 
            highest_freq = -1                   # track its frequency; start at -1 so any real count beats it

            # Find the single most frequent number left in the map
            for num, freq in count.items():     # look at every number and its count still in the dict
                if freq > highest_freq:         # is this number more frequent than the best so far?
                    highest_freq = freq         # yes -> remember this new highest frequency
                    highest_num = num           # and remember which number it belongs to

            # Add it to our results and delete it so we find the NEXT highest next turn
            result.append(highest_num)          # save this pass's winner into the results
            count.pop(highest_num)              # remove it from the dict so it can't win again next pass

        return result                           # hand back the k most frequent numbers