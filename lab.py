
import cv2

img = cv2.imread("sample.jpg")
tmp = cv2.imread("sample_copy.jpg")

if img is None or tmp is None:
    exit()

image = cv2.GaussianBlur(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), (5,5), 0)
template = cv2.GaussianBlur(cv2.cvtColor(tmp, cv2.COLOR_BGR2GRAY), (5,5), 0)

result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
_, _, _, loc = cv2.minMaxLoc(result)

h, w = template.shape
cv2.rectangle(img, loc, (loc[0]+w, loc[1]+h), (0,255,0), 2)

cv2.imshow("Result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

