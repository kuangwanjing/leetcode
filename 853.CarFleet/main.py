class Solution:
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        # main solution here is about deduction:
        # if the Ci can catch up with Ci+1 before target, then Ci-1 can catch up with Ci+1
        # if Ci-1 can cath up with Ci.

        # couple the position and speed to calculate the remaining time to reach the target
        cars = sorted(zip(position, speed))
        times = [float(target-p) / s for p, s in cars]   
        ans = 0
        while len(times) > 1:
            # lead is the time the fleet to take to reach the target
            lead = times.pop()
            # if the following car uses more time to reach at its origin speed, then it will 
            # never catch up the previous fleet
            if lead < times[-1]: ans += 1
            # examine the next car
            else: times[-1] = lead
        # handle the case that only one car is left in the stack.
        return ans + bool(times)
