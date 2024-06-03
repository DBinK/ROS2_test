import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class ImageSubscriber(Node):
    def __init__(self):
        super().__init__('image_subscriber')
        self.subscription = self.create_subscription(Image, 'video_frames', self.image_callback, 10)
        self.subscription  # 防止未使用的变量警告
        self.bridge = CvBridge()

    def image_callback(self, msg):
        try:
            #self.get_logger().info(f'收到了了一帧：') 
            cv_image = self.bridge.imgmsg_to_cv2(msg, "passthrough")
            cv_image_bgr8 = cv2.cvtColor(cv_image, cv2.COLOR_RGB2BGR)
            #cv2.imshow('Received Image', cv_image_bgr8)
            cv2.imshow('Received Image', cv_image)
            cv2.waitKey(1)  # 显示图像并等待1毫秒
        except Exception as e:
            print(f"Error displaying image: {e}")

def main(args=None):
    rclpy.init(args=args)
    image_subscriber = ImageSubscriber()
    rclpy.spin(image_subscriber)
    image_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()