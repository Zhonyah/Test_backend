"""
เขียนโปรแกรมอะไรก็ได้ที่อยาก present Python's skill set เจ๋ง ๆ ของตัวเอง
ข้อนี้ไม่ต้องทำก็ได้ ไม่มีผลลบกับการให้คะแนน แต่ถ้าทำมาเเล้วเจ๋งจริง ก็จะพิจารณาเป็นพิเศษ

"""

import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def command():

    # แปลงเสียงให้เป็น text
    r = sr.Recognizer() 

    # "ดึงข้อมูลจาก Mic มาเก็บไว้ที่ตัวแปร source"
    with sr.Microphone() as source: 


        # ให้โปรแกรมทำการวน Loop ไปเรื่อย ๆ จนกว่าจะมีคำสั่งออกจาก Loop
        while True: 
            print("Alexa: Listening...") 
            # Recognizer จะทำการฟังเสียงที่เก็บไว้ในตัวแปร source และเก็บไว้ใน audio
            audio=r.listen(source) 
            try:    
                query = r.recognize_google(audio,language='th') # Google Web Speech API  รับค่าเสียงจากตัวแปร audio  กำหนดให้แปลงเป็น ภาษาไทย
                print(f"master:{query}")

                #ตรวจสอบเงื่อนไขการตอบกลับ

                if query == "สวัสดี" or query == "สวัสดี alexa" or query == "สวัสดีอเล็กซ่า":
                    speak("Sawaddee Master")

                elif query == "alexa" or query == "อเล็กซ่า":
                    speak("Yes!, Master")

    
                elif query == "Goodbye" or query == "Goodbye alexa" or query == "Good Night":
                    speak("see you again , goodbye Master")
                    break

                elif query == "search by youtube" or query == "Search by YouTube":

                    speak("What do you want to find on Youtube, Master?")
                    print("Alexa: Listening...") 
                    with sr.Microphone() as source2:
                        try:
                            audio2=r.listen(source2) 
                            query2 = r.recognize_google(audio2,language='th')
                            driver = webdriver.Chrome()
                            driver.get('https://www.youtube.com')


                            searchbox = driver.find_element(by=By.XPATH, value=('/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input'))
                            searchbox.send_keys(query2)

                            searchButton = driver.find_element(by=By.XPATH, value=('/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button'))
                            searchButton.click()
                        except:
                            print("Try Again")
                            continue

                elif query == "search by google" or query == "Search by Google":

                    speak("What do you want to find on Google, Master?")
                    print("Alexa: Listening...") 
                    with sr.Microphone() as source2:
                        try:
                            audio2=r.listen(source2) 
                            query2 = r.recognize_google(audio2,language='th')
                            driver = webdriver.Chrome()
                            driver.get('https://www.google.co.th/?hl=th')


                            searchbox = driver.find_element(by=By.XPATH, value=('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'))
                            searchbox.send_keys(query2)

                            searchButton = driver.find_element(by=By.XPATH, value=('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]'))
                            searchButton.click()
                        except:
                            print("Try Again")
                            continue
                elif query == "Thank You" or query == "Thank":

                    speak("You are welcome, Master")

                else :
                    speak("I don't understand Master , Please speak to me again")
                            
            # ถ้าเกิด oogle Web Speech API ไม่สามรถฟังออกหรือไม่ได้ยินเสียง โชว์คำว่า "Try Again" และ ให้ทำการพูดใหม่
            except:
                print("Try Again")
                continue
            

# แปลง text ให้เป็น เสียง
def speak(audio):
    engine.say(audio)   
    engine.runAndWait()
    
            
print(command())