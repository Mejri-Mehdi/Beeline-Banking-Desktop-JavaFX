from deepface import DeepFace

result = DeepFace.verify(
    img1_path="faces/user_66.png",
    img2_path="faces/user_67.png"
)

print(result)