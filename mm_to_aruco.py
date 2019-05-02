import rospy
from std_msgs.msg import String, Header
from rospy.msg import AnyMsg
from geometry_msgs.msg import PoseWithCovarianceStamped, PoseStamped
from marvelmind_nav.msg import hedge_pos

rospy.init_node('mm_to_aruco')

covariance = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
              0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]


def mm_callback(msg):
    # print(msg.header)
    # print(msg.pose)
    # a = msg.pose.pose.position.x
    # print(msg._connection_header)

    pose_stamped = PoseStamped()
    pose_stamped.header.frame_id = 'map'
    pose_stamped.header.stamp = rospy.Time.now()

    pose_stamped.pose.position.x = msg.x_m
    pose_stamped.pose.position.y = msg.y_m
    pose_stamped.pose.position.z = msg.z_m

    pose_stamped.pose.orientation.y = 0.0
    pose_stamped.pose.orientation.x = 0.0
    pose_stamped.pose.orientation.z = 0.0
    pose_stamped.pose.orientation.w = 0.0

    pub.publish(pose_stamped)
    print('---')

pub = rospy.Publisher('/mavros/vision_pose/pose',PoseStamped,queue_size = 10)
rospy.Subscriber('/hedge_pos', hedge_pos, mm_callback)

rospy.spin()
