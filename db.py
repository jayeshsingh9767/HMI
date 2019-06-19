import mysql.connector


def get_parameter_values():
    # temp = [{"parameter_id": "paramter_80", "value": 25.30}]
    # return temp
    db_obj = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "password",
        database="pt_tech"
    )

    cursor = db_obj.cursor()

    cursor.execute("SELECT * FROM site_parameters")

    myresult = cursor.fetchall()

    arr = []

    for x in myresult:
        res = {}
        res["parameter_id"] = x[3]
        res["value"] = x[14]
        arr.append(res)
    return arr
