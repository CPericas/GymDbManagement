import mysql.connector
from mysql.connector import Error

#Task 3: Updating Member Information

#Implement a function to update the age of a member. Ensure that your function checks if the member exists before attempting the update.
    # Example code structure
#    def update_member_age(member_id, new_age):
        # SQL query to update age
        # Check if member exists
        # Error handling
#Expected Outcome: A Python function that updates the age of a member and handles cases where the member does not exist.


from connect_mysql import connect_database

def update_member_age(member_id, new_age):
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

        # Update the member's age
        update_query = """
        UPDATE members
        SET age = %s
        WHERE id = %s
        """
        cursor.execute(update_query, (new_age, member_id))

        # Commit the transaction
        conn.commit()
        print(f"Member ID {member_id}'s age updated to {new_age}")

    except Error as e:
        print("Error while updating member age", e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

# Example usage
if __name__ == "__main__":
    update_member_age(1, 35)
