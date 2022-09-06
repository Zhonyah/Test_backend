
"""
Convert Arabic Number to Roman Number.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลขอราบิก เป็นตัวเลขโรมัน
โดยที่ค่าที่รับต้องมีค่ามากกว่า 0 จนถึง 1000



*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""


number = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500,
          900, 1000]  # สร้าง List เก็บตัวเลข Arabic
romanNumber = ['I', 'VI', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C',
               'CD', 'D', 'CM', 'M']  # สร้าง List เก็บตัวเลข Roman

# กำหนดค่า i ให้ทำกับจำนวนสูงสุดของ List เพื่อให้ทำ จากเลขมากที่สุดใน List ก่อน แล้วจึงค่อยทำงานในตัวเลขที่มีค่าน้อยลงมา(ตำแหน่ง List ถัดไป)
i = 12
# รับค่าตาก User บังคับให้เก็บเป็น int
numberInput = int(input("Enter Your Number : "))

# ใช้ if ตรวจสอบ ว่า numberInput ที่ User กรอกมา มีค่ามากกว่า 1000 หรือ น้อยกว่า 0 หรือไม่
if numberInput < 0 or numberInput > 1000:
    print("ใส่ค่าจำนวนเต็มระหว่างs 0 - 1000 เท่านั้น")
else:
    numberRoman = ''  # สร้างตัวแปรไว้เก็บค่า เลข Roman ที่ได้\
    while numberInput != 0:  # ใช้ลูป While ในการเช็ค ถ้า NumberInput มีค่าไม่เท่ากับ 0 ให้ทำการวนซ้ำ

        if number[i] <= numberInput:
            # ใช้ If ในการตรวจสอบว่า ค่าของ Number[i] น้อยกว่าหรือเท่ากับ numberInput หรือไม่ ถ้าเป็นจริงให้ทำคำสั่งใน If แต่ถ้าไม่ให้ไปทำคำสั่งใน Else โดยเริ่มต้น number[i i มีค่าเท่ากับ 12 นั้นเท่ากับ 1000]

            # สั่งให้ numberRoman เก็บค่า List romanNumber[ตำแหน่งที่ i] เช่น 'C' += 'C' ก็จะได้เป็น 'CC'
            numberRoman += romanNumber[i]
            
            # สั่งให้ numberInput ลบค่าตัวเองโดยลบกับ List number[ตำแหน่งที่ i] เช่น 235 -= 100 จะได้ค่า 135 เพื่อเอากลับไปวนลูปต่อ
            numberInput -= number[i]
        else:
            # ถ้าเกิดไม่ตรงเงื่อนไขด้านบนให้ ลบตำแหน่งของ list คือ i ลงมาเรื่อยๆ เพื่อนำ [i] ไปตรวจสอบเงื่อนไขใน Function if
            i = i - 1
    # เมื่อสิ้นสุด Loop ให้แสดงค่าตัวแปร numberRoman ที่เก็บไว้ทั้งหมด
    print(numberRoman)
