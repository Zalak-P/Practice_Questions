# Problem: https://leetcode.com/problems/car-fleet/
# Trick: Sort cars by start position. For each car: calc time = (target - position) / speed
# We are traversing from right to left. IMP !!!

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = sorted(zip(position, speed), reverse=True)
        
        for pos, spd in cars:
            # Calculate time to reach target
            arrival_time = (target - pos) / spd
            stack.append(arrival_time)

            # If the current car takes less or equal time than the car ahead,
            # it will catch up and join that car's fleet. Pop it from the stack.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

            return len(stack)

# If the trailing car's arrival time is less than or equal to the time of the car ahead of it, it will eventually catch up and merge into the same fleet.


