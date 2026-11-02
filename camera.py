import cv2
from datetime import datetime

# Open camera
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Could not open camera")
    exit()

print("Camera started")
print("Press Q or ESC to quit")
print("Press S to save a photo")
print("Press SPACE to take a screenshot")

while True:
    success, frame = camera.read()

    if not success:
        print("Could not read frame")
        break

    # Show camera
    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1) & 0xFF

    # Q = Quit
    if key == ord('q'):
        print("Quitting...")
        break

    # ESC = Quit
    elif key == 27:
        print("Quitting...")
        break

    # S = Save photo
    elif key == ord('s'):
        filename = datetime.now().strftime("photo_%Y%m%d_%H%M%S.jpg")
        cv2.imwrite(filename, frame)
        print(f"Photo saved: {filename}")

    # SPACE = Screenshot
    elif key == 32:
        filename = datetime.now().strftime("screenshot_%Y%m%d_%H%M%S.png")
        cv2.imwrite(filename, frame)
        print(f"Screenshot saved: {filename}")

# Release camera
camera.release()

# Close windows
cv2.destroyAllWindows()

print("Camera closed")