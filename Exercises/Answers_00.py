#00.01.a
import math
def cal_hyp(cat_a, cat_b):
    return math.sqrt(cat_a**2 + cat_b**2)

print(f"1a) {cal_hyp(3, 4)}")  


#00.01.b
def cal_cat(hyp, cat):
    return math.sqrt(hyp**2 - cat**2)  

print(f"1b) {cal_cat(7, 5):.1f}")  


#00.02
def accuracy(target_value:int, real_value:int) -> float:
    return round(real_value/target_value, 2)*100 

print(f"2) {accuracy(365, 300):.0f}%")


#00.03
def accuracy(tp:int, fp:int, tn:int, fn:int) -> int:
    return 100-(tp+tn)/(tp+tn+fp+fn)*100 

print(f"3) {accuracy(2, 2, 11, 985)}%")


#00.04
def slope(point_a:tuple, point_b:tuple) -> tuple:
    k = (point_b[1]-point_a[1]) / (point_b[0]-point_a[0])
    m = point_a[1]-point_a[0]*k
    return (k, m)

print(f"4) {slope((4,4), (0,1))}") 


#00.05
def distance(p1:tuple, p2:tuple) -> int: 
    return round(math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2), 1)

print(f"5) {distance((3, 5), (-2, 4))}")


#00.06
def distance(p1:tuple, p2:tuple) -> int: 
    return round(math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2+(p2[2]-p1[2])**2), 2)

print(f"6) {distance((2, 1, 4), (3, 1, 0))}")