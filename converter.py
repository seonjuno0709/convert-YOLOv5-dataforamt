# image size : 2048 x 1536

import glob
import os

# 데이터 셋 경로
# annotation : ETRI에서 제공하는 bounding box 정보 폴더
# images : ETRI에서 제공하는 image
# labels : 새로운 yolo label이 들어갈 폴더
path = os.path.dirname(os.path.realpath(__file__))
annotation_path = os.path.join(path, "annotations")
images_path = os.path.join(path, "images")
labels_path = os.path.join(path, "labels")

# ETRI에서 제공한 기존 .txt bbox 형식을 yolo bbox 형식으로 변환하는 함수
# input parameter data type : integer
# output data type : string list
def txt_to_yolo_bbox(left, top, right, bottom, class_id):
  x_center = (left + right) / 2 / 2048
  y_center = (top + bottom) / 2 / 1536
  width = (right - left) / 2048
  height = (bottom - top) / 1536

  if class_id == 1400:
    new_class_id = 16
  elif class_id == 1401:
    new_class_id = 32
  elif class_id == 1402:
    new_class_id = 2
  elif class_id == 1403:
    new_class_id = 33
  elif class_id == 1404:
    new_class_id = 34
  elif class_id == 1405:
    new_class_id = 17
  else:
    new_class_id = 0
  
  result = [str(new_class_id), str(x_center), str(y_center)
                    , str(width), str(height)]

  return result

# main
files = glob.glob(os.path.join(annotation_path, "*.txt"))

for file in files:
  # 모든 파일 이름 출력
  basename = os.path.basename(file)

  read_file = open(file, "r")
  strings = read_file.readlines()

  #파일의 내용이 비어있는 경우와 내용이 있는 경우
  if strings == []:
    pass
  else:
    write_file = open(labels_path + "\\" + basename, "w")
    for i in strings:
      string = i.split('\t')
      left = int(string[0])
      top = int(string[1])
      right = int(string[2])
      bottom = int(string[3])
      class_id = int(string[4].strip('\n'))

      if class_id == 1400 or class_id == 1401 or class_id == 1402 or class_id == 1403 or class_id == 1404 or class_id == 1405:
        yolo_class_id = txt_to_yolo_bbox(left, top, right, bottom, class_id)[0]
        yolo_x_center = txt_to_yolo_bbox(left, top, right, bottom, class_id)[1]
        yolo_y_center = txt_to_yolo_bbox(left, top, right, bottom, class_id)[2]
        yolo_width = txt_to_yolo_bbox(left, top, right, bottom, class_id)[3]
        yolo_height = txt_to_yolo_bbox(left, top, right, bottom, class_id)[4]
        write_file.write(yolo_class_id + " " + yolo_x_center + " " + yolo_y_center + " " + yolo_width + " " + yolo_height + '\n')
        print(yolo_class_id + " " + yolo_x_center + " " + yolo_y_center + " " + yolo_width + " " + yolo_height)
      else:
        pass
    
    write_file.close()
  read_file.close()

# 내용이 없는 파일을 삭제
del_files = glob.glob(os.path.join(labels_path, "*.txt"))

for del_file in del_files:
  del_read_file = open(del_file, "r")
  
  if del_read_file.readlines() == []:
    del_read_file.close() 
    os.remove(del_file)
