from PIL import Image
import mysql.connector
import pytesseract


def db_connect(host, user, password, database):
    db = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    print("db connected") if db else print("db not connected")
    return db


def is_solid_image(path):
    img = Image.open(path)
    # Convert to grey scale and get extreme point which is tuple
    extremes = img.convert("L").getextrema()
    if extremes[0] == extremes[1]:
        return True
    return False


def main():
    # connect to db
    db = db_connect(host="localhost",
                    user="c4c",
                    password="paradise",
                    database="bigsafar_dev_corrupt")
    sql = "SELECT * FROM account_ownerprofile WHERE is_owner =1"
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for x in result:
        #   2 is image field for this query
        # x[2] is path for query
        if not is_solid_image(x[2]):
            print("image  is okay")
        else:
            print("image is void")
            # Get ID of of that x field and remove from table
            delete_row(db, x[0])


def delete_row(db, id):
    cursor = db.cursor()
    sql = "DELETE FROM account_ownerprofile WHERE id = {id}".format(id=id)
    cursor.execute(sql)
    db.commit()
    print(cursor.rowcount, "record(s) deleted")
    return True


def check():
    black_img = Image.open("./images/blackey.jpg")
    extrema_black = black_img.convert("L").getextrema()
    white_img = Image.open("./images/whitey.jpg")
    extrema_white = white_img.convert("L").getextrema()
    mixed_img = Image.open("./images/slc.jpg")
    extrema_mixed = mixed_img.convert("L").getextrema()
    # clrs = img.getcolors()
    # print(type(extrema_black))

    print(" Extremes for black is:({a},{b})".format(a=extrema_black[0], b=extrema_black[1]))
    print(" Extremes for white is:({a},{b})".format(a=extrema_white[0], b=extrema_white[1]))
    print(" Extremes for mixed is:({a},{b})".format(a=extrema_mixed[0], b=extrema_mixed[1]))
    # TODO:if extrema[0]=extrema[1] it implies that the image is one solid color

    db = mysql.connector.connect(
        host="localhost",
        user="c4c",
        password="paradise",
        database="railway_recruit"
    )
    print(db)

    sql = "SELECT * FROM account_ownerprofile WHERE is_owner =1"
    mycursor = db.cursor()
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        #   2 is image field for this query
        print(x[2])
    return True


from urllib.request import urlretrieve


def imgtostring():
    # mixed_img = Image.open("./images/slc.jpg")
    # mixed_img = Image.open("https://nepalrailway.org/applicants/document/2020-09-14-06-50-14-SLC-(2).jpg")
    # extrema_mixed = mixed_img.convert("L")
    URL = "https://nepalrailway.org/applicants/document/2020-09-14-06-50-14-SLC-(2).jpg"
    # Image.open('./images/slc.jpg')
    # import urllib, cStringIO
    # urlretrieve('https://nepalrailway.org/applicants/document/2020-09-14-06-50-14-SLC-(2).jpg',
    #             'file.jpg')
    #
    # Open a pdf file

    # file = cStringIO.StringIO(urllib.urlopen(URL).read())
    # img = Image.open('file.jpg')
    corrupt_pdf = "https://nepalrailway.org/applicants/document/2020-09-28-10-59-11-Bachelor-mark-sweet-.pdf"
    urlretrieve("https://nepalrailway.org/applicants/document/2020-09-28-10-59-11-Bachelor-mark-sweet-.pdf",
                'file2.pdf')
    try:
        pdfFileObj = open('file2.pdf', 'rb')
    except:
        print('exception occurred')

    # print(pytesseract.image_to_string(extrema_mixed))
    # print(pytesseract.image_to_string(img, config="--psm 6"))
    # pdfFileObj = open('example.pdf', 'rb')


import PyPDF2


def checkValidDocument(table_name=None):
    db = db_connect("localhost", "c4c", "paradise", "railway_recruit")
    table_name = 'bachleors_kanun_adikrit'
    sql = "SELECT Distinct ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level,ei.grade FROM {table_name} ap,`education_infos` ei WHERE ap.id=ei.apply_post_id and ap.vacant_post_id=2 and (ei.level ='Bachelors')".format(
        table_name=table_name)
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    table_name = 'bachleors_kanun_adikrit'
    somebool = checkDocumentExistence(result, db, table_name)
    print('all is okay')
    return True


def checkDocumentExistence(result, db, table_name):
    for x in result:
        print("i am document")
        domain = "https://nepalrailway.org/"
        filepath = x[1]
        fullpath = domain + filepath
        filename, ext = (fullpath.split('/')[-1].split('.'))
        print("name:{filename} and extension:{ext}".format(filename=filename, ext=ext))
        temp_filename = "temp_file." + ext
        # Download Image locally
        urlretrieve(fullpath, temp_filename)
        print("temp_filename:{temp_filename}".format(temp_filename=temp_filename))
        print("id of apply post:{id}".format(id=x[5]))
        apply_post_id = x[5]
        if ext == "pdf":
            try:
                print("in try block")
                pdfFileObj = open(temp_filename, 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
                print('after creating  pdf object')
                cursor = db.cursor()
                sql = "UPDATE {table_name} SET remarks = 'Bachleors doc ok', status=0 WHERE id ={apply_post_id}".format(
                    table_name=table_name, apply_post_id=apply_post_id)
                cursor.execute(sql)
                db.commit()

            except:
                print('exception occurred pdf is not valid')
                cursor = db.cursor()
                sql = "UPDATE {table_name} SET remarks = 'Bachleors doc not accessible', status=1 WHERE id ={apply_post_id}".format(
                    table_name=table_name, apply_post_id=apply_post_id)
                cursor.execute(sql)
                db.commit()

        else:
            try:
                print('in try block of image')
                cursor = db.cursor()
                sql = "UPDATE {table_name} SET remarks = 'Bachleors doc ok', status=0 WHERE id ={apply_post_id}".format(
                    table_name=table_name, apply_post_id=apply_post_id)
                cursor.execute(sql)
                db.commit()
                img = Image.open(temp_filename)

            except:
                # image is not readable
                print('in except block of image')
                print('image is not readable')
                cursor = db.cursor()
                sql = "UPDATE {table_name} SET remarks = 'Bachleors doc ok', status=1 WHERE id ={apply_post_id}".format(
                    table_name=table_name, apply_post_id=apply_post_id)
                cursor.execute(sql)
                db.commit()
    return True


checkValidDocument()
