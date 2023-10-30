import cv2
import numpy as np
color_ranges = {
    'red': ([0, 0, 100], [80, 80, 255]),
    'green': ([0, 100, 0], [80, 255, 80]),
    'blue': ([100, 0, 0], [255, 80, 80]),
    'yellow': ([0, 100, 100], [80, 255, 255]),
    'orange': ([0, 50, 100], [50, 150, 255]),
    'purple': ([100, 0, 100], [255, 80, 255]),}
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    color_identified = []
    for color, (lower, upper) in color_ranges.items():
        lower = np.array(lower, dtype=np.uint8)
        upper = np.array(upper, dtype=np.uint8)
        mask = cv2.inRange(hsv_frame, lower, upper)
        color_percentage = np.count_nonzero(mask) / (mask.shape[0] * mask.shape[1]) * 100
        if color_percentage > 5:  # Identify if a color covers more than 5% of the frame
            color_identified.append(color)
    if color_identified:
        identified_colors_str = ', '.join(color_identified)
        cv2.putText(frame, f"Identified colors: {identified_colors_str}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Live Color Identification', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()