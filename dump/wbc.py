import sqlite3


def execute_sql_file(filename, db_name):
    # Connect to SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Open and read the file as a single buffer
    sql_file = open(filename, 'r').read()

    # Execute the SQL commands
    sql_commands = sql_file.split(';')
    lenth = len(sql_commands)
    print(f"lenth:{lenth}")
    limit = 100
    n = 0
    for command in sql_commands:
        n += 1
        if n > limit:
            break
        try:
            if command.strip() != '':
                print(command)
                cursor.execute(command)
        except sqlite3.Error as e:
            print(f"An error occurred: {e.args[0]}")

    # Commit your changes and close the connection
    conn.commit()
    conn.close()


file_path = "/content/wikidatawiki-20230801-wbc_entity_usage.sql"

# Call the function with your SQL file and desired SQLite database
execute_sql_file(file_path, 'my_database.db')
