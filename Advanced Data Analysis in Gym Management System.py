import mysql.connector

#Task 1
def get_members_in_age_range(start_age, end_age):
    try:
        conn = mysql.connector.connect(database="GymDB", user="root", password="my-secret-pw", host="127.0.0.1")
        cursor = conn.cursor()

        query = "select * from Members where age between %s and %s"
        age_range = (start_age, end_age)

        cursor.execute(query, age_range)
        print(cursor.fetchall())
        conn.commit()

    except Exception as e:
        print("Could not add workout session to database:")
        print(e)

    finally:
        conn.close()
        conn.close()
