import mysql.connector


def get_parameter_values():
    db_obj = mysql.connector.connect(
        host = "http://192.168.0.102",
        user = "root",
        password = "password",
        database="pt_tech"
    )

    cursor = db_obj.cursor()

    mycursor.execute("SELECT * FROM site_parameters")

    myresult = cursor.fetchall()
    res = {}
    for x in myresult:
      res["parameter_id"] = x[3]
      res["value"] = x[14]
     return res
