import cv2

# 카메라 열기 (0 = 기본 웹캠)
cap = cv2.VideoCapture(0)

# 프레임 크기 가져오기
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# FPS 설정
fps = 20

# 코덱 설정
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# 영상 저장 객체
out = cv2.VideoWriter('output.avi', fourcc, fps, (width, height))

recording = False  # Record 모드 여부
gray_mode = False # Grayscale 모드 여부

while True:

    ret, frame = cap.read()
    if not ret:
        break

    # Record 모드일 때
    if recording:

        # 빨간 원 표시
        cv2.circle(frame, (30, 30), 10, (0, 0, 255), -1)

        # 영상 파일에 저장
        out.write(frame)

    elif gray_mode:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    # 화면 출력
    cv2.imshow("Video Recorder", frame)

    key = cv2.waitKey(1) & 0xFF

    # ESC → 종료
    if key == 27:
        break

    # Space → 모드 전환
    elif key == 32:
        recording = not recording
        if recording:
            print("Recording START")
        else:
            print("Recording STOP")

    elif key ==ord('c'):
        gray_mode = not gray_mode
        if gray_mode:
            print("Grayscale Mode ON")
        else:
            print("Grayscale Mode OFF")

# 자원 해제
cap.release()
out.release()
cv2.destroyAllWindows()
