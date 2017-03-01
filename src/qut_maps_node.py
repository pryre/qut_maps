#!/usr/bin/env python
# license removed for brevity
import rospy
from nav_msgs.msg import OccupancyGrid

def mapper():
	pub = rospy.Publisher('/qut_maps/output_grid', OccupancyGrid, queue_size=10, latch=1)
	rospy.init_node('qut_maps_node', anonymous=True)

	map_width = 100
	map_height = 100
	map_grid_size = 0.05	#m/cell

	rate = rospy.Rate(1)	#1hz

	grid_out = OccupancyGrid()
	grid_out.header.frame_id = "map"
	grid_out.header.stamp = rospy.Time.now()
	grid_out.info.map_load_time = rospy.Time.now()
	grid_out.info.resolution = map_grid_size
	grid_out.info.width = map_width
	grid_out.info.height = map_height
	grid_out.info.origin.position.x = -( map_width * map_grid_size ) / 2
	grid_out.info.origin.position.y = -( map_height * map_grid_size ) / 2
	grid_out.info.origin.position.z = 0
	grid_out.info.origin.orientation.w = 1
	grid_out.info.origin.orientation.x = 0
	grid_out.info.origin.orientation.y = 0
	grid_out.info.origin.orientation.z = 0

	flipper = 0

	for j in range(0, map_height):
		for i in range(0, map_width):
			grid_out.data.append(flipper)

			if flipper == 0:
				flipper = 100
			else:
				flipper = 0

		if flipper == 0:
			flipper = 100
		else:
			flipper = 0

	rospy.loginfo("Sending map")
	pub.publish(grid_out)

	rospy.spin()

if __name__ == '__main__':
	try:
		mapper()
	except rospy.ROSInterruptException:
		pass
