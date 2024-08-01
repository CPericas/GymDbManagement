import mysql.connector
from mysql.connector import Error

#Task 1: Add a Member
#Write a Python function to add a new member to the 'Members' table in the gym's database.
    # Example code structure
#    def add_member(id, name, age):
        # SQL query to add a new member
        # Error handling for duplicate IDs or other constraints
#Expected Outcome: A Python function that successfully adds a new member to the 'Members' table in the gym's database. The function 
#should handle errors gracefully, such as duplicate member IDs or violations of other constraints.

from connect_mysql import connect_database

def add_member(name, age):
    conn = connect_database()
    if conn is None:
        return

    try:
        cursor = conn.cursor()

        # Get the current maximum id
        cursor.execute("SELECT MAX(id) FROM members;")
        result = cursor.fetchone()
        max_id = result[0] if result[0] is not None else 0

        # Calculate new id
        new_id = max_id + 1

        # Insert the new member
        insert_query = "INSERT INTO members (id, name, age) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (new_id, name, age))

        # Commit the transaction
        conn.commit()
        print(f"Member {name} added with ID {new_id}")

    except Error as e:
        print("Error while adding a new member", e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

# Example usage
if __name__ == "__main__":
    add_member("Alex Anderson", 30)


    
        

