# Mode Switching Camera

OpenCV와 Python을 이용하여 웹캠 영상을 확인하고 녹화할 수 있는 Video Recorder 프로그램입니다.  
Preview 모드와 Record 모드를 전환할 수 있으며, 필터 및 캡처 기능을 제공합니다.

## 주요 기능

- 웹캠을 통한 실시간 영상 출력
- Preview / Record 모드 전환
- 녹화 중 화면에 녹화 상태 표시 (빨간색 원)
- Preview 모드에서 상태 텍스트 표시 ("Camera")
- 녹화된 영상 파일 저장
- 화면 캡처 기능
- 흑백(Grayscale) 필터 적용 및 해제

## 조작 방법

| 키 | 기능 |
|---|---|
| Space | Preview / Record 모드 전환 |
| C | 흑백 필터 적용 / 해제 |
| S | 화면 캡처 |
| ESC | 프로그램 종료 |

## 프로그램 동작

- 프로그램 실행 시 웹캠 영상이 실시간으로 출력됩니다.
- Preview 모드에서는 좌측 상단에 **"Camera"** 텍스트가 표시됩니다.
- Record 모드에서는 좌측 상단에 **빨간색 원**이 표시되며 영상이 저장됩니다.
- 녹화 중에는 캡처 기능이 비활성화되며, 시도 시 안내 메시지가 출력됩니다.

## 출력 파일

- 녹화 영상: `output.avi`
- 캡처 이미지: `capture_*.png`

## 추가 기능

- **흑백 필터 토글**
  - `C` 키를 눌러 컬러 / 흑백 전환 가능
- **캡처 기능**
  - `S` 키를 눌러 현재 화면 저장
- **녹화 중 캡처 제한**
  - 녹화 상태에서 캡처 시도 시 경고 메시지 출력
- **텍스트 가독성 개선**
  - Outline 텍스트를 사용하여 모든 배경에서 가독성 확보

## 사용 기술

- `cv2.VideoCapture` : 웹캠 입력
- `cv2.VideoWriter` : 영상 저장
- `cv2.waitKey()` : 키 입력 처리

# Mode Switching Camera

This is a simple video recorder program built with OpenCV and Python.  
It allows users to preview webcam input, record video, apply filters, and capture images.

## Features

- Real-time webcam video display
- Preview / Record mode switching
- Recording indicator (red circle)
- Status text display in Preview mode ("Camera")
- Save recorded video to file
- Screen capture functionality
- Grayscale filter toggle

## Controls

| Key | Function |
|---|---|
| Space | Toggle Preview / Record mode |
| C | Toggle grayscale filter |
| S | Capture current frame |
| ESC | Exit program |

## Behavior

- The webcam feed is displayed in real time.
- In Preview mode, **"Camera"** text is shown at the top-left corner.
- In Record mode, a **red circle** indicates recording status.
- Capture is disabled during recording, and a warning message is displayed if attempted.

## Output Files

- Recorded video: `output.avi`
- Captured images: `capture_*.png`

## Additional Features

- **Grayscale filter toggle**
  - Press `C` to switch between color and grayscale
- **Capture function**
  - Press `S` to save the current frame
- **Capture restriction during recording**
  - Displays a warning message if capture is attempted during recording
- **Improved text visibility**
  - Outline text ensures readability on any background

## Technologies Used

- `cv2.VideoCapture` : webcam input
- `cv2.VideoWriter` : video saving
- `cv2.waitKey()` : keyboard input handling

## Screenshot

![grayscale_capture](https://github.com/park2722/Mode_Switching_Camera/blob/main/Capture/capture_0.png)  
![vanilla_capture](https://github.com/park2722/Mode_Switching_Camera/blob/main/Capture/capture_1.png)  
