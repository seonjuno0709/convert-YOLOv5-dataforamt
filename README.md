### ETRI 데이터를 YOLOv5에서 사용하기 위해 데이터 포맷 변경
**ETRI Data :**

<https://nanum.etri.re.kr/share/kimjy/etri_traffic_light?lang=ko_KR>

annotation 된 정보는 bounding-box left, top, right, bottom, class_id를 나타냄

(Data Set은 직접 ETRI에 신청해 받기)

**YOLOv5 Data Format :**

YOLOv5 데이터 포맷은 class_id, x_center, y_center, width, height 순서로 나타냄

---

**code는 python으로 작성하였음**

![캡처](https://user-images.githubusercontent.com/76555222/210407695-1b89c4d7-c8cb-45ba-84b7-8e7f50e21a83.PNG)
