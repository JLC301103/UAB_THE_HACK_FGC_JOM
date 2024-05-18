import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('yolov8n-seg.pt')

# Replace with your phone's IP address and port
url = "http://10.151.234.203:8080/video"

# Open video stream
cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("Error: Could not open video stream")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame")
        break
    
    # Run YOLOv8 model on the frame
    results = model(frame)

    # Assuming results is a list, iterate through each result
    if isinstance(results, list):
        for result in results:
            # Plot the results
            annotated_frame = result.plot()
            # Display the frame
            cv2.imshow('YOLOv8 Segmentation', annotated_frame)
    else:
        annotated_frame = results.plot()
        cv2.imshow('YOLOv8 Segmentation', annotated_frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close display windows
cap.release()
cv2.destroyAllWindows()


