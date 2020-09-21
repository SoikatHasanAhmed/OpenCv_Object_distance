# OpenCv_Object_distance
Here, we use opencv to find out the distance between the camera and the object by using a single camera/webcam.
By default it will capture the camera. You can change it by giving arg while tuning or changing the parm in the following lines.

```python
parser.add_argument('--webcam', type=bool, default=True)
parser.add_argument('--url', type=str, default='http://192.168.0.4:8080/shot.jpg')
'''
