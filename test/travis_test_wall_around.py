#!/usr/bin/env python
import unittest, rostest
import rosnode, rospy
import time

class WallTraceTest(unittest.TestCase):
    def set_and_get(self, lf, ls, rs, rf):
        with open("/dev/rtlightsensor0", "w") as f:
            f.write("%d %d %d %d\n" % (rf, rs, ls, lf))

        time.sleep(0.3)

        with open("/dev/rtmotor_raw_l0", "r") as lf, \
             open("/dev/rtmotor_raw_r0", "r") as rf:
            left = int(lf.readline().rstrip())
            right = int(rf.readline().rstrip())

        return left, right

    def test_io(self):
        left, right = self.set_and_get(51, 50, 50, 50) # wall_front = True (left_forward > 50)
        self.assertTrue(left > right > 0, "can't right turn by left_forward sensor")

        left, right = self.set_and_get(50, 50, 50, 51) # wall_front = True (right_forward > 50)
        self.assertTrue(left > right > 0, "can't right turn by right_forward sensor")

        left, right = self.set_and_get(50, 50, 51, 50) # too_right = True
        self.assertTrue(0 < left < right, "can't left turn by right_side sensor. left=" + str(left) + ", right=" + str(right))

        left, right = self.set_and_get(50, 51, 50, 50) # too_left = True
        self.assertTrue(left > right > 0, "can't right turn by left_side sensor")

        left, right = self.set_and_get(50, 50, 50, 50) # without upper
        self.assertTrue(0 < left == right, "can't forward. left=" + str(left) + ", right=" + str(right))

        left, right = self.set_and_get(50, 49, 50, 50) # without upper
        self.assertTrue(0 < left < right, "can't left turn. left=" + str(left) + ", right=" + str(right))

if __name__ == '__main__':
    time.sleep(3)
    rospy.init_node('travis_test_wall_trace')
    rostest.rosrun('pimouse_run_corridor', 'travis_test_wall_trace', WallTraceTest)