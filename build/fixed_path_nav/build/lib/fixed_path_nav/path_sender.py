import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from nav2_msgs.action import NavigateToPose
from rclpy.action import ActionClient
import math

class CircleNavigator(Node):

    def __init__(self):
        super().__init__('circle_navigator')
        self.client = ActionClient(self, NavigateToPose, 'navigate_to_pose')
        self.radius = 2.0
        self.points = 36
        self.index = 0
        self.send_next_goal()

    def send_next_goal(self):
        if not self.client.wait_for_server(timeout_sec=5.0):
            self.get_logger().info("Waiting for Nav2...")
            return

        angle = 2 * math.pi * self.index / self.points

        goal = NavigateToPose.Goal()
        goal.pose.header.frame_id = 'map'
        goal.pose.pose.position.x = self.radius * math.cos(angle)
        goal.pose.pose.position.y = self.radius * math.sin(angle)

        yaw = angle + math.pi/2
        goal.pose.pose.orientation.z = math.sin(yaw/2)
        goal.pose.pose.orientation.w = math.cos(yaw/2)

        self.get_logger().info(f"Going to point {self.index}")

        send_goal_future = self.client.send_goal_async(goal)
        send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info("Goal rejected")
            return

        self.get_logger().info("Goal accepted")
        get_result_future = goal_handle.get_result_async()
        get_result_future.add_done_callback(self.goal_result_callback)

    def goal_result_callback(self, future):
        self.get_logger().info("Reached point")

        self.index += 1
        if self.index >= self.points:
            self.index = 0

        self.send_next_goal()

def main(args=None):
    rclpy.init(args=args)
    node = CircleNavigator()
    rclpy.spin(node)
    rclpy.shutdown()
