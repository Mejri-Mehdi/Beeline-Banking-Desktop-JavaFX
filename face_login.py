import sys
from deepface import DeepFace

img1 = sys.argv[1]
img2 = sys.argv[2]

try:
    result = DeepFace.verify(
        img1_path=img1,
        img2_path=img2,
        model_name="Facenet",
        detector_backend="opencv",
        enforce_detection=False
    )

    distance = result["distance"]
    print("DISTANCE =", distance)

    if distance < 0.8:
        print("MATCH")
    else:
        print("NO_MATCH")

except Exception as e:
    print("ERROR:", str(e))