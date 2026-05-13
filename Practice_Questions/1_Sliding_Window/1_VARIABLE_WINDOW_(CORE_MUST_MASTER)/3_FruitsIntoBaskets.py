#Problem: https://takeuforward.org/data-structure/fruit-into-baskets

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        left = right = result = 0
        hashmap = {}
        
        while right < len(fruits):
            hashmap[fruits[right]] = hashmap.get(fruits[right], 0) + 1

            while len(hashmap) > 2:
                hashmap[fruits[left]] -= 1
                if hashmap[fruits[left]] == 0:
                    del hashmap[fruits[left]]                 # 🔹 shrink → release character
                left += 1

            result = max(result, right - left + 1)
            right += 1

        return result
