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


save_path = "C:/Users/user/Desktop/My project/Computer Vision/Mode_Switching_Camera/Capture" # 캡처 파일 저장 경로
# 영상 저장 객체
out = cv2.VideoWriter(save_path+"/output.avi", fourcc, fps, (width, height))

recording = False  # Record 모드 여부
gray_mode = False # Grayscale 모드 여부
capture_count = 0  # 파일 이름용

while True:

    ret, frame = cap.read()
    display_frame = frame.copy()
    if not ret:
        break

    if gray_mode:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        display_frame = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    # Record 모드일 때
    if recording:

        # 빨간 원 표시
        cv2.circle(display_frame, (30, 30), 10, (0, 0, 255), -1)
        # 영상 파일에 저장
        out.write(display_frame)

    elif not recording:
        # 녹화 중이 아닐 때는 "Camera" 텍스트 표시
        cv2.putText(display_frame, "Camera", (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1, (0, 0, 0), 4)   # 검은색 (두껍게)

        cv2.putText(frame, "Camera", (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1, (255, 255, 255), 2)  # 흰색 (얇게)
        
    # 화면 출력
    cv2.imshow("Video Recorder", display_frame)

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
    # C → 그레이스케일 모드 전환
    elif key ==ord('c'):
        gray_mode = not gray_mode
        if gray_mode:
            print("Grayscale Mode ON")
        else:
            print("Grayscale Mode OFF")
    # S → 화면 캡처
    elif key == ord('s'):
        if recording:
            print("Cannot capture while recording!")
            continue
        else:
            filename = f"capture_{capture_count}.png"
            cv2.imwrite(save_path + "/" + filename, display_frame)
            print(f"{filename} saved")
            capture_count += 1


# 자원 해제

cap.release()
out.release()
cv2.destroyAllWindows()
