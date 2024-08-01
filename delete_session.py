import mysql.connector
from mysql.connector import Error

#Task 4: Delete a Workout Session

#Create a Python function to delete a workout session based on its session ID. Include error handling for cases where the session ID 
# does not exist.
    # Example code structure
#    def delete_workout_session(session_id):
        # SQL query to delete a session
        # Error handling for non-existent session ID
#Expected Outcome: A Python function that can delete a workout session using its session ID, with proper error handling for invalid IDs.


from connect_mysql import connect_database

def delete_workout_session(session_id):
    conn = connect_database()
    if conn is None:
        return

    try:
        cursor = conn.cursor()

        # Check if the session ID exists
        cursor.execute("SELECT session_id FROM WorkoutSessions WHERE session_id = %s", (session_id,))
        session = cursor.fetchone()
        if session is None:
            print("Error: Workout session ID does not exist.")
            return

        # Delete the workout session
        delete_query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
        cursor.execute(delete_query, (session_id,))

        # Commit the transaction
        conn.commit()
        print(f"Workout session ID {session_id} deleted")

    except Error as e:
        print("Error while deleting workout session", e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

# Example usage
if __name__ == "__main__":
    delete_workout_session(1)
