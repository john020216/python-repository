def Score():
    
   
   for area in range(1, 8):
       a = float(input("%d 번째 과제점수: "%(area)))

   e1 = int(input("중간고사 점수: "))
   
   for area in range(9, 15):
       a = float(input("%d 번째 과제점수: "%(area)))
       
   e2 = int(input("기말고사 점수: "))
   
   n = a * 0.4
   b = e1 * 0.3
   c = e2 * 0.3
   
   t = n + b + c
   if  100 >= t >= 90:
       grade = "A"
   elif 90 >= t >= 80:
        grade = "B"
   elif 80 >= t >= 70:
        grade = "C"
   elif 70 >= t >= 60:
        grade = "D"
   elif t < 60:
        grade = "F"
    
   print("\n과제점수 = %.2f"%n)
   print("중간점수 = %.2f"%b)
   print("기말점수 = %.2f"%c)
   print("합계 = %.2f"%(n+b+c))
   print("등급 = %s"%grade)

Score()