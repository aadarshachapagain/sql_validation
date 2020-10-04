from PIL import Image
import mysql.connector




def db_connect(host, user, password, database):
    db = mysql.connector.connect(
        host=host,
        user="user",
        password="password",
        database="database"
    )
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
        database="bigsafar_dev_corrupt"
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


