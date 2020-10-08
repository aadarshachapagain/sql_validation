from PIL import Image
import mysql.connector
import pytesseract
from urllib.request import urlretrieve
# from urllib.parse import urlparse
import urllib.parse
# from urllib.parse import unquote
from urllib.parse import unquote_to_bytes
import PyPDF2


def db_connect(host, user, password, database):
    db = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    print("db connected") if db else print("db not connected")
    return db


def is_solid_image():
    img = Image.open('temp_file.JPG')
    print('image opened')
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


def checkValidDocument(table_name=None):
    db = db_connect("localhost", "c4c", "paradise", "railway_recruit")
    # table_name = 'bachleors_kanun_adikrit'
    no_level = ''

    cursor = db.cursor()
    # table_name = 'bachleors_kanun_adikrit'
    # vacant_post_id = 2
    table_name = 'bachleors_station_master'
    vacant_post_id = 3

    """ Bachleors"""
    level_bach = 'Bachelors'
    bach_sql = "SELECT Distinct ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level,ei.grade FROM {table_name} ap,`education_infos` ei WHERE ap.id=ei.apply_post_id and ap.vacant_post_id={vacant_post_id} and (ei.level ='{level_bach}')".format(
        table_name=table_name, level_bach=level_bach, vacant_post_id=vacant_post_id)
    cursor.execute(bach_sql)
    result_bach = cursor.fetchall()

    """ Bachleors"""

    """ Plus2"""
    level_alevel = 'A-LeveL'
    level_plus2 = '+2/PCL'
    plus2_sql = "SELECT Distinct ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level,ei.grade FROM {table_name} ap,`education_infos` ei WHERE ap.id=ei.apply_post_id and ap.vacant_post_id=2 and (ei.level ='{level_alevel}' or ei.level='{level_plus2}')".format(
        table_name=table_name, level_alevel=level_alevel, level_plus2=level_plus2)
    cursor.execute(plus2_sql)
    result_plus2 = cursor.fetchall()
    """ Plus2"""

    """ SlC"""
    level_see = 'SEE'
    level_slc = 'SLC'
    level_olevel = 'O-LeveL'
    slc_sql = "SELECT Distinct ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level,ei.grade FROM {table_name} ap,`education_infos` ei WHERE ap.id=ei.apply_post_id and ap.vacant_post_id=2 and (ei.level ='{level_see}' or ei.level='{level_slc}' or ei.level='{level_olevel}')".format(
        table_name=table_name, level_see=level_see, level_slc=level_slc, level_olevel=level_olevel)
    cursor.execute(slc_sql)
    result_slc = cursor.fetchall()
    """ SlC"""

    slc_somebool = checkDocumentExistence(result_bach, db, table_name, level_slc)
    plus2_somebool = checkDocumentExistence(result_plus2, db, table_name, level_plus2)
    bach_somebool = checkDocumentExistence(result_slc, db, table_name, level_bach)

    print('Processing is Completed')
    return True


def checkDocumentExistence(result, db, table_name, level):
    for x in result:
        print("i am document")
        domain = "https://nepalrailway.org/"
        filepath = x[1]
        filestring = (filepath.split('.'))
        filename = filestring[:-1]
        ext = filestring[-1]
        cleaned_filepath = urllib.parse.quote(filepath)
        fullpath = domain + cleaned_filepath

        # filename, ext = (fullpath.split('/')[-1].split('.'))
        print("name:{filename} and extension:{ext}".format(filename=filename, ext=ext))
        temp_filename = "temp_file." + ext
        # Download Image locally
        urlretrieve(fullpath, temp_filename)
        # temp_filename = 'temp_file.JPG'
        # ext = 'JPG'
        print("temp_filename:{temp_filename}".format(temp_filename=temp_filename))
        print("id of apply post:{id}".format(id=x[5]))
        apply_post_id = x[5]
        if ext == "pdf":
            try:
                print("in try block of pdf level:{level}".format(level=level))
                pdfFileObj = open(temp_filename, 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
                print('after creating  pdf object')
                cursor = db.cursor()
                sql = "UPDATE {table_name} SET remarks = '{level} doc ok' WHERE id ={apply_post_id}".format(
                    table_name=table_name, apply_post_id=apply_post_id, level=level)
                cursor.execute(sql)
                db.commit()

            except:
                print('exception occurred pdf is not valid level:{level}'.format(level=level))
                cursor = db.cursor()
                sql = "UPDATE {table_name} SET remarks = '{level} doc not accessible', status=status+1 WHERE id ={apply_post_id}".format(
                    table_name=table_name, apply_post_id=apply_post_id, level=level)
                cursor.execute(sql)
                db.commit()
        else:
            try:
                print("temp_filename:{temp_filename}".format(temp_filename=temp_filename))
                img = Image.open(temp_filename)
                print('in try block of image level:{level}'.format(level=level))
                cursor = db.cursor()
                sql = "UPDATE {table_name} SET remarks = '{level} doc ok' WHERE id ={apply_post_id}".format(
                    table_name=table_name, apply_post_id=apply_post_id, level=level)
                cursor.execute(sql)
                db.commit()

            except:
                # image is not readable
                print('in except block of image')
                print('image is not readable level:{level}'.format(level=level))
                cursor = db.cursor()
                sql = "UPDATE {table_name} SET remarks = '{level} doc not ok', status=status+1 WHERE id ={apply_post_id}".format(
                    table_name=table_name, apply_post_id=apply_post_id, level=level)
                cursor.execute(sql)
                db.commit()
    return True


def test_string():
    teststring = "applicants/document/2020-09-18-06-28-32-+२-transcript.png"
    filestring = (teststring.split('.'))
    filename = filestring[:-1]
    ext = filestring[-1]
    secondhalf = "/applicants/document/2020-09-18-06-28-32-+२-transcript.png"
    print("filename:{filename},ext:{ext}".format(filename=filename, ext=ext))
    "/applicants/document/2020-09-18-06-28-32-+२-transcript.png"
    fullpath = "https://nepalrailway.org//applicants/document/2020-09-18-06-28-32-+२-transcript.png"
    "https://nepalrailway.org//applicants/document/2020-09-18-06-28-32-+%E0%A5%A8-transcript.png"
    # "https://nepalrailway.org//applicants/document/2020-09-18-06-28-32-+%E0%A5%A8-transcript.png"
    # newpath=fullpath.encode('ascii', 'ignore')
    # newpath = urlparse(fullpath)
    # newpath = unquote(fullpath, encoding='utf-8')
    # newpath = unquote(fullpath)
    # newpath = unquote_to_bytes(fullpath)
    # print(newpath)
    import urllib.parse
    # urllib.parse.unquote(url)
    # encodedurl = fullpath.encode('ascii','replace')
    # print(encodedurl)
    print('encodedurl')

    newpath = urllib.parse.quote(secondhalf)
    firsthalf = "https://nepalrailway.org"
    fullpath = firsthalf + newpath
    newpath_again = urllib.parse.unquote(newpath)
    print('newpath')
    print(fullpath)
    print('newpath_again')
    print(newpath_again)

    # urlretrieve(fullpath, 'newfile.png')
    # "https://nepalrailway.org//applicants/document/2020-09-18-06-28-32-+%E0%A5%A8-transcript.png"
    print("i am document")
    domain = "https://nepalrailway.org/"
    filepath = "/applicants/document/2020-09-18-06-28-32-+२-transcript.png"
    filestring = (filepath.split('.'))
    filename = filestring[:-1]
    ext = filestring[-1]
    # urllib.parse.unquote(newpath)
    # cleaned_filepath = urllib.parse.unquote(filepath)
    cleaned_filepath = urllib.parse.unquote(filepath)
    fullpath = domain + cleaned_filepath
    return True


def check_final():
    print("i am document")
    domain = "https://nepalrailway.org/"
    filepath = "/applicants/document/2020-09-18-06-28-32-+२-transcript.png"
    filestring = (filepath.split('.'))
    filename = filestring[:-1]
    ext = filestring[-1]
    print("ext:{ext}, filename={filename}".format(ext=ext, filename=filename))
    cleaned_filepath = urllib.parse.quote(filepath)
    fullpath = domain + cleaned_filepath
    print('fullpath')
    print(fullpath)
    urlretrieve(fullpath, 'check.'+ext)

    # urllib.parse.unquote(newpath)
    # cleaned_filepath = urllib.parse.unquote(filepath)
    return True


# checkValidDocument()
# test_string()
# check_final()
# is_solid_image()
