import mysql.connector

#Task 1
def add_member(id, name, age):
    try:
        #These credentials are default for the docker container version of MySQL, which is what I am using to bug test
        conn = mysql.connector.connect(database="GymDB", user="root", password="my-secret-pw", host="127.0.0.1")
        cursor = conn.cursor()

        query = "insert into Members(id, name, age) values (%s, %s, %s)"
        new_member = (id, name, age)

        cursor.execute(query, new_member)
        conn.commit()

    except Exception as e:
        print("Could not add user to database:")
        print(e)

    finally:
        cursor.close()
        conn.close()

#Task 2
def add_workout_session(member_id, date, duration_minutes, calories_burned):
    try:
        conn = mysql.connector.connect(database="GymDB", user="root", password="my-secret-pw", host="127.0.0.1")
        cursor = conn.cursor()

        query = "insert into WorkoutSessions(member_id, date, duration_minutes, calories_burned) values (%s, %s, %s, %s)"
        new_workout = (member_id, date, duration_minutes, calories_burned)

        cursor.execute(query, new_workout)
        conn.commit()

    except Exception as e:
        print("Could not add workout session to database:")
        print(e)

    finally:
        cursor.close()
        conn.close()

#Task 3
def update_member_age(member_id, new_age):
    try:
        conn = mysql.connector.connect(database="GymDB", user="root", password="my-secret-pw", host="127.0.0.1")
        cursor = conn.cursor()

        query = "update Members set age = %s where id = %s"
        updated_info = (new_age, member_id)

        cursor.execute(query, updated_info)
        conn.commit()

    except Exception as e:
        print("Could not update the member's age in the database:")
        print(e)

    finally:
        cursor.close()
        conn.close()

#Task 4
def delete_workout_session(session_id):
    try:
        conn = mysql.connector.connect(database="GymDB", user="root", password="my-secret-pw", host="127.0.0.1")
        cursor = conn.cursor()

        query = "delete from WorkoutSessions where session_id = %s"
        id = [session_id]

        cursor.execute(query, id)
        conn.commit()

    except Exception as e:
        print("Could not delete workout from the database:")
        print(e)

    finally:
        cursor.close()
        conn.close()
