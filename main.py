from render import Render
from processor import Processor
import cv2
import time


def main(save=False, ratio_aspect=(16, 9), reduced_resolution=96, output_resolution=(1080, 1920), chars="$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`\\'.   ", font=cv2.FONT_HERSHEY_PLAIN, scale=1, thickness=1, color=(255, 255, 255)):
    # Open the default camera
    cam = cv2.VideoCapture(0)

    # Get the default frame width and height
    # Capture-Property-Frame-Width
    frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
                       )  # Capture-Property-Frame-Height

    # Define the codec(coder/decoder) and create VideoWriter object
    # Four Character Code for codec is `mp4v`
    codec = cv2.VideoWriter_fourcc(*'mp4v')
    if save:
        out = cv2.VideoWriter('output.mp4', codec, 20,
                              (frame_width, frame_height))

    prev_time = time.time()

    proc = Processor(96, aspect_ratio=ratio_aspect, chars=chars)
    rend = Render(output_resolution, font=font, scale=scale,
                  thickness=thickness, color=color)

    while True:
        ret, frame = cam.read()
        ascii_array = proc.ascii_array(frame)
        frame = rend.ascii_frame(ascii_array)

        if not ret:
            break

        curr_time = time.time()
        fps = 1 / (curr_time - prev_time)
        prev_time = curr_time

        text = f"FPS: {int(fps)}"
        cv2.putText(frame, text, (10, 40), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 255, 255), 2, cv2.LINE_AA)

        # Write the frame to the output file
        if save:
            out.write(frame)

        # Display the captured frame
        cv2.imshow('Camera', frame)

        prev_time = time.time()

        # Press 'q' to exit the loop
        if cv2.waitKey(1) == ord('q'):
            break

    # Release the capture and writer objects
    cam.release()
    if save:
        out.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
