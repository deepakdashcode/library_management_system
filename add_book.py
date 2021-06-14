import mysql.connector as c
db=c.connect(host='localhost', user='root', passwd='2580',database='my_library')
def add_by_ISBN(isbn):
    cur=db.cursor()
    #isbn=int(input('Enter the ISBN\n'))
    sql='select ISBN from books'
    cur.execute(sql)
    all_isbn=[]
    for i in cur:
        all_isbn.append(i[0])
    if isbn in all_isbn:
        try:
            quantity = int(input('Enter the number of books to add\n'))
            sql = f'select quantity from books where isbn={isbn}'
            cur.execute(sql)
            current_quantity = 0
            for i in cur:
                current_quantity = i[0]
            new_quantity = current_quantity + quantity
            sql = f'update books set quantity={new_quantity} where isbn={isbn};'
            cur.execute(sql)
            db.commit()
        except Exception as e:
            print('Some Error Occurred')
            print('Error Code : ',e)

    else:
        try:
            bname = input('Enter the book name\n')
            std=input('Enter the standard if any else type q\n').lower().strip()

            quantity = int(input('Enter the number of books to add\n'))
            if std=='q':
                sql=f'insert into books values ({isbn},"{bname}",NULL,{quantity}  )'
                print(sql)
                cur.execute(sql)
                db.commit()
            else:
                sql = f'insert into books values ({isbn},"{bname}","{std}",{quantity}  )'
                cur.execute(sql)
                db.commit()

        except Exception as e:
            print('Some Error Occurred')
            print('Error Code : ',e)

#add_by_ISBN()

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

            isbn=int(myData)
            add_by_ISBN(isbn)
            break
        except:
            pass



#scan_code()
while True:
    print('Enter 1 to input ISBN')
    print('Enter 2 to scan code')
    print('Enter q to exit')
    try:

        choice = (input('Enter the choice\n').lower().strip())
        if choice == '1':
            isbn = int(input('Enter the ISBN\n'))
            add_by_ISBN(isbn)
        elif choice=='2':
            scan_code()
        elif choice=='q':
            break
    except Exception as e:
        print('Some error occurred')
        print('Error code : ',e)





