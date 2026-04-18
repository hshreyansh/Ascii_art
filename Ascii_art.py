import cv2
import numpy as np

# Clean gradient (dark → light)
ASCII_CHARS = " .:-=+*#%@"

def resize_frame(frame, new_width=140):
    height, width = frame.shape
    ratio = height / width
    new_height = int(new_width * ratio * 0.55)
    return cv2.resize(frame, (new_width, new_height))

def frame_to_ascii(gray):
    frame = resize_frame(gray)

    ascii_data = []
    for row in frame:
        line = ""
        for pixel in row:
            index = int(pixel) * len(ASCII_CHARS) // 256
            line += ASCII_CHARS[index]
        ascii_data.append(line)

    return ascii_data


def ascii_to_image(ascii_data):
    char_h, char_w = 12, 8

    h = len(ascii_data)
    w = len(ascii_data[0])

    img = np.zeros((h * char_h, w * char_w, 3), dtype=np.uint8)

    for i, line in enumerate(ascii_data):
        for j, char in enumerate(line):
            # brightness based on character position
            intensity = int(255 * (ASCII_CHARS.index(char) / (len(ASCII_CHARS)-1)))

            cv2.putText(
                img,
                char,
                (j * char_w, (i + 1) * char_h),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.4,
                (intensity, intensity, intensity),  # white shades
                1,
                cv2.LINE_AA,
            )

    return img


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# lower resolution → smoother
cap.set(3, 320)
cap.set(4, 240)

cv2.namedWindow("ASCII Camera", cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    

    ascii_data = frame_to_ascii(gray)
    ascii_img = ascii_to_image(ascii_data)

    cv2.imshow("ASCII Camera", ascii_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()