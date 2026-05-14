# Problem: https://leetcode.com/problems/car-fleet/
# Trick: Sort cars by position. For each car: calc time = (target - position) / speed
# Once the car catch up to another car, then it will drive at the same speed as the car ahead of it.

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = list(zip(position, speed))
        cars.sort(reverse=True) # Reversing because

        result = 0
        prev_time = 0

        for pos, spd in cars:
            current_time = (target - pos) / spd

            # Cannot catch fleet ahead
            if current_time > prev_time:
                result += 1
                prev_time = current_time

        return result
    