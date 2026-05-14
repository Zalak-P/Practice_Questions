# Problem: https://leetcode.com/problems/car-fleet/
# Trick: Sort cars by position. For each car: calc time = (target - position) / speed
# Once car catches up to another car, the speed of the car will changed to the one in the front, since it's single lane road.

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
    

# At one point this problem does look like Next Greater Element, since we are looking for bigger TIME,
# in the future but it's not.
# WHY? Next Greater Element works like:
# "Current element resolves older waiting elements."
# Example: current_num > stack_top
# So current element immediately answers pending questions.

# Car Fleet is not resolving pending cars like that.
# Instead: Current car must compare itself with the FINAL fleet ahead.
# because fleets can merge and change speeds/times dynamically.