import cv2

source="old_image.jpg"
destination="new_image.jpg"
scale_percent=50

src=cv2.imread(source,cv2.IMREAD_UNCHANGED)

if src is None:
    print("Image not found!")
    exit()

new_width=int(src.shape[1] * scale_percent/100)
new_height=int(src.shape[0] * scale_percent/100)

output = cv2.resize(src,(new_width,new_height))
cv2.imwrite(destination,output)
print("Image resized and saved to",destination)