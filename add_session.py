import mysql.connector
from mysql.connector import Error

#Task 2: Add a Workout Session

#Develop a Python function to add a new workout session to the 'WorkoutSessions' table for a specific member.
    # Example code structure
#    def add_workout_session(member_id, session_date, session_time, activity):
        # SQL query to add a new workout session
        # Error handling for invalid member ID or other constraints
#Expected Outcome: A Python function that adds a new workout session to the 'WorkoutSessions' table in the gym's database for a specific 
#member. The function should handle errors gracefully, such as invalid member IDs or violations of other constraints.


from connect_mysql import connect_database

def add_workout_session(member_id, session_date, session_time, activity):
    conn = connect_database()
    if conn is None:
        return

    try:
        cursor = conn.cursor()

        # Check if the member ID exists
        cursor.execute("SELECT id FROM members WHERE id = %s", (member_id,))
        member = cursor.fetchone()
        if member is None:
            print("Error: Member ID does not exist.")
            return

        # Insert the new workout session
        insert_query = """
        INSERT INTO WorkoutSessions (member_id, session_date, session_time, activity)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(insert_query, (member_id, session_date, session_time, activity))

        # Commit the transaction
        conn.commit()
        print(f"Workout session added for member ID {member_id} on {session_date} at {session_time} for {activity}")

    except Error as e:
        print("Error while adding a workout session", e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

# Example usage
if __name__ == "__main__":
    add_workout_session(1, '2023-08-01', '14:00:00', 'Running')
