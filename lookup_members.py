import mysql.connector
from mysql.connector import Error

#Problem Statement: Retrieve the details of members whose ages fall between 25 and 30.
#Expected Outcome: A list of members (including their names, ages, etc) who are between the ages of 25 and 30.
#Example Code Structure:
#    def get_members_in_age_range(start_age, end_age):
        # SQL query using BETWEEN
        # Execute and fetch results
#Note: The database structure used for this assignment is the same as the previous one, consisting of the Members and WorkoutSessions 
# tables.


from connect_mysql import connect_database

def get_members_in_age_range(start_age, end_age):
    conn = connect_database()
    if conn is None:
        return

    try:
        cursor = conn.cursor()

        # SQL query to retrieve members within the specified age range
        query = """
        SELECT id, name, age
        FROM members
        WHERE age BETWEEN %s AND %s
        """
        cursor.execute(query, (start_age, end_age))

        # Fetch all results
        members = cursor.fetchall()

        # Print the results
        if members:
            print(f"Members aged between {start_age} and {end_age}:")
            for member in members:
                print(f"ID: {member[0]}, Name: {member[1]}, Age: {member[2]}")
        else:
            print(f"No members found in the age range {start_age} to {end_age}.")

    except Error as e:
        print("Error while retrieving members", e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

# Example usage
if __name__ == "__main__":
    get_members_in_age_range(25, 30)

    