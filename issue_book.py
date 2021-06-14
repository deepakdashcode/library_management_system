import time
import mysql.connector as c
db=c.connect(host='localhost', user='root', passwd='2580',database='my_library')

def getDateAndTime():
    timedetails = tuple(time.localtime())
    dictionary = {'Year': timedetails[0], 'Month': timedetails[1], 'Date': timedetails[2], 'Hour': timedetails[3],
                  'Minute': timedetails[4], 'Second': timedetails[5]}
    return dictionary

print(getDateAndTime())
def issue(isbn,date_of_issue,time_of_issue):
    #isbn = int(input('Enter the isbn code\n'))
    cur=db.cursor()
    #isbn=int(input('Enter the ISBN\n'))
    sql='select ISBN from books'
    cur.execute(sql)
    all_isbn=[]
    for i in cur:
        all_isbn.append(i[0])
    print(all_isbn)
    if isbn not in all_isbn:
        print('Sorry we do not have this book currently')
    else:
        quantity=int(input('Enter the quantity\n'))
        sql = f'select quantity from books where isbn={isbn}'
        cur.execute(sql)
        current_quantity = 0
        for i in cur:
            current_quantity = i[0]

        if quantity>current_quantity:
            print('Sorry we do not have sufficient stock at the moment')
        else:
            name=input('Enter your name\n')
            phno=int(input('Enter your phone number\n'))
            ################################################
            # ADDING DETAILS TO ISSUES TABLE
            #############################
            sql=f'insert into issues values ("{name}",{phno},{isbn},{quantity},"{date_of_issue}","{time_of_issue}");'
            cur.execute(sql)
            db.commit()

            #########################################################
            # Reducing quantity from original table
            #############################################
            new_quantity = current_quantity - quantity
            sql = f'update books set quantity={new_quantity} where isbn={isbn};'
            cur.execute(sql)
            db.commit()



def scan_code():
    import cv2
    import numpy as np
    from pyzbar.pyzbar import decode

    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    while True:
        try:
            success, img = cap.read()
            for barcode in decode(img):
                myData = barcode.data.decode('utf-8')
                # MAKING BOUNDARY
                pts = np.array([barcode.polygon], np.int32)
                pts = pts.reshape((-1, 1, 2))
                pts2 = barcode.rect
                cv2.polylines(img, [pts], True, (255, 0, 255), 5)
                print(myData)

            cv2.imshow('Result', img)
            cv2.waitKey(1)

            ##########################
            year=getDateAndTime()['Year']
            month=getDateAndTime()['Month']
            dt=getDateAndTime()['Date']
            hr=getDateAndTime()['Hour']
            minute=getDateAndTime()['Minute']
            seconds=getDateAndTime()['Second']

            date_of_issue=f'{year}-{month}-{dt}'
            time_of_issue=f'{hr}:{minute}:{seconds}'
            ###############################

            ##########################



            isbn=int(myData)
            issue(isbn, date_of_issue, time_of_issue)
            break
        except:
            pass




while True:
    try:
        print('Enter 1 to issue')
        print('Enter 2 to scan code')
        print('Enter q to exit')
        choice = input('Enter your choice\n').lower().strip()
        if choice == '1':
            isbn=int(input('Enter the isbn\n'))
            # INSERTING TIME
            year=getDateAndTime()['Year']
            month=getDateAndTime()['Month']
            dt=getDateAndTime()['Date']
            hr=getDateAndTime()['Hour']
            minute=getDateAndTime()['Minute']
            seconds=getDateAndTime()['Second']

            date_of_issue=f'{year}-{month}-{dt}'
            time_of_issue=f'{hr}:{minute}:{seconds}'
            ###############################
            issue(isbn,date_of_issue,time_of_issue)
        elif choice=='2':
            scan_code()
        elif choice=='q':
            break
    except Exception as e:
        print('Some Error occurred')
        print('Error Code : ',e)





