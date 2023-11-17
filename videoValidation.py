import cv2
import urllib.request
#from fastapi import FastAPI, HTTPException
#from fastapi.responses import JSONResponse
#import os

#app = FastAPI()

# def validate_video_url(video_url):
#    try:
       # Download the video into a temporary file
#        temp_file_path, _ = urllib.request.urlretrieve(video_url)

        # Check if the video file is successfully opened using OpenCV
#        cap = cv2.VideoCapture(temp_file_path)
#         if not cap.isOpened():
#            os.remove(temp_file_path)  # Remove the temporary file
#            raise HTTPException(
#                status_code=400,
#                detail="Error: Could not open video file.",
#            )

        # Example: Check if video resolution is greater than 0
#        if video_meta['size'][0] <= 0 or video_meta['size'][1] <= 0:
#            os.remove(temp_file_path)  # Remove the temporary file
#            raise HTTPException(
#                status_code=400,
#                detail="Error: Invalid video resolution.",
#            )

        # Release the video capture object and close the temporary file
#        cap.release()
#        video_reader.close()
#        os.remove(temp_file_path)  # Remove the temporary file
#        return JSONResponse(content={"message": "Video is valid. Process further."})

#    except Exception as e:
#        return HTTPException(
#            status_code=400,
#            detail=f"Error: {e}",
#        )

#@app.get("/validate-video")
#async def validate_video(video_url: str):
#    return validate_video_url(video_url)


def validate_video_url(video_url):
    try:
        cap = cv2.VideoCapture(video_url)

        if not cap.isOpened():
            print("Error: Could not open video file.")
            return False
        
        cap.release()

        print("Video validation successful.")
        return True

    except Exception as e:
        print(f"Error: {e}")
        return False

video_url = "https://shramin.blob.core.windows.net/files/video/1677213624593-60cf0548-73f5-4353-bf79-a223ce2f5d24-videoResume.mp4"
validation_result = validate_video_url(video_url)

if validation_result:
    print("Video is verified.")
else:
    print("Video validation failed. Please provide a valid video URL.")
