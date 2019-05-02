import rospy
from clever import srv
from std_srvs.srv import Trigger
import time

rospy.init_node('flight')

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
land = rospy.ServiceProxy('land', Trigger)


print("Programm begin")
#navigate(x=4.71087408066, y=-1.37571883202, z=-0.1856369823225, speed=0.5, frame_id='map', auto_arm=True)
time.sleep(5)
print("Landing")
#res = land()

if res.success:
    print 'Copter is landing'