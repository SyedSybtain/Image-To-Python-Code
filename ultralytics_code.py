fromultralyticsimportYoLo
from ultralytics.solutions import ai_gym
import cv2
model=YoL0("yolov8n-pose.pt")
cap=cv2.VideoCapture("path/to/video/file.mp4")
assertcap.isOpened()，"Errorreadingvideo file"
gym_object=ai_gym.AIGym()#initAI GYMmodule
gym_object.set_args(line_thickness=2,
view_img=True,
pose_type="pushup",
kpts_to_check=[6,8,10])
frame_count=0
while cap.isOpened():
success,imθ=cap.read()
if not success:
break
frame_count +=1
results=model.track（im0,verbose=False）
im0=gym_object.start_counting（imo,results,frame_count)
video_writer.write（imo)
cv2.destroyAllWindows()
video_writer.release()