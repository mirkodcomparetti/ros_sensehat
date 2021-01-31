# ros_sensehat
ROS node for Sense Hat, Raspberry Pi

Dependency is the sense_hat package 2.2.0

The node `hat_publisher.py` publishes the sensors data as

* `/sensehat/humidity`, Float64, queue_size=10
* `/sensehat/temperature`, Float64, queue_size=10
* `/sensehat/pressure`, Float64, queue_size=10
* `/sensehat/accelerometer`, Vector3, queue_size=10
* `/sensehat/gyroscope`, Vector3, queue_size=10
* `/sensehat/magnetometer`, Vector3, queue_size=10
* `/sensehat/compass`, Float64, queue_size=10
* `/sensehat/stick`, String, queue_size=10
