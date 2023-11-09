import os
import sqlite3

#Delete Database if it already exists
#Database is created and right now does not need to be edited
#os.remove("student_database.db")

# Initialize the SQLite database and create tables
db = ":memory:"
connection = sqlite3.connect(db)
cursor = connection.cursor()

"""
statement = "SELECT * FROM curriculums"
result = cursor.execute(statement)
print(result)
"""

# Create the "users" table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
)''')

# Create the "curriculums" table
cursor.execute('''CREATE TABLE IF NOT EXISTS curriculums (
    curriculum_id INTEGER PRIMARY KEY,
    curriculum_name TEXT
)''')


# Create the "topics" table
cursor.execute('''CREATE TABLE IF NOT EXISTS topics (
    topic_id INTEGER PRIMARY KEY,
    curriculum_id INTEGER,
    topic_name TEXT,
    CONSTRAINT FK_curriculum
    FOREIGN KEY (curriculum_id) REFERENCES curriculums (curriculum_id)
)''')

# Create the "notes" table
cursor.execute('''CREATE TABLE IF NOT EXISTS notes (
    note_id INTEGER PRIMARY KEY,
    topic_id INTEGER,
    note_text TEXT,
    CONSTRAINT FK_topic
    FOREIGN KEY (topic_id) REFERENCES topics (topic_id)
)''')



# Create the students_curriculum table to form a many-to-many relationship
cursor.execute('''CREATE TABLE IF NOT EXISTS user_curriculum (
    user_id INTEGER,
    curriculum_id INTEGER,
    CONSTRAINT user_cur_pk PRIMARY KEY (user_id, curriculum_id),
    CONSTRAINT FK_user
    FOREIGN KEY (user_id) REFERENCES users (user_id),
    CONSTRAINT FK_curriculum
    FOREIGN KEY (curriculum_id) REFERENCES curriculums (curriculum_id)
)''')

#Created the database and inserted starter values to get started


cursor.execute('''
   INSERT INTO users (username,password) 
    VALUES 
        ('noahaus','1234'),
        ('jbrown','1234'),
        ('tsally','1234');
''')

connection.commit()


cursor.execute('''
INSERT INTO curriculums (curriculum_name) 
    VALUES 
        ('The Early Roman Empire'),
        ('How to make a PBJ')    
''') 

connection.commit()



#test if it worked out
cursor.execute('''
       SELECT * from users
''')
print(cursor.fetchall())

def actions():
    #these need to be filled for faster SQL queries 
    current_curriculum = ""
    current_curriculum_id = ""
    current_topic = ""
    current_topic_id = ""
    while(True):
        
        print("[1] view curriculums\n[2] change current curriculum\n[3] add curriculum\n[4] change topic\n[5] add topic\n[6] view topics\n[7] add note\n[8] logout")
        selection = input("Select your action:")

        if selection == "8":
            connection.close()
            break
        elif selection == "1":
            statement = f"SELECT curriculum_name from curriculums"
            cursor.execute(statement)
            print(cursor.fetchall())
        elif selection == "2":
            user_input = input("which curriculum would you like to work in:")
            statement = f"SELECT curriculum_name, curriculum_id FROM curriculums WHERE curriculum_name='{user_input}'"
            cursor.execute(statement)
            result = cursor.fetchone()
            print(result)
            if result is None: 
                print(f"'{user_input}' is not present - please pick an existing curriculum")
            else:
                current_curriculum = result[0]
                current_curriculum_id = result[1]
                print(f"'{current_curriculum}' is now the current working curriculum")
        elif selection == "3":
            user_input = input("what would you like to name the curriculum?")
            statement = f"INSERT INTO curriculums (curriculum_name) VALUES  ('{user_input}')"
            cursor.execute(statement)
            print("curriculum successfully created")
            connection.commit()
        elif selection == "4":
            user_input = input("which topic would you like to work in:")
            statement = f"SELECT topic_name,topic_id FROM topics WHERE topic_name='{user_input}'"
            cursor.execute(statement)
            result = cursor.fetchone()
            print(result)
            if result is None: 
                print(f"'{user_input}' is not present - please pick an existing topic")
            else:
                current_topic = result[0]
                current_topic_id = result[1]
                print(f"'{current_topic}' is now the current working topic")
        elif selection == "5":
            user_input = input("what would you like to name this topic?")
            try:
                statement = f"INSERT INTO topics (curriculum_id,topic_name) VALUES  ({result[1]},'{user_input}')"
                cursor.execute(statement)
                print(f"topic '{user_input}' added to curriculum '{current_curriculum}'")
                connection.commit()
            except:
                print("current curriculum not selected")

        elif selection == "6":
            statement = f"SELECT topic_name FROM topics WHERE curriculum_id = {current_curriculum_id}"
            cursor.execute(statement)
            result = cursor.fetchall()
            for topic in result:
                print(topic)
        elif selection == "7":
            user_input = input("upload the note file:")
            note_file = open(user_input)
            note = ""
            for line in note_file.readline():
                note = f"{note} " + line
            try:
                statement = f"INSERT INTO notes (topic_id, note_text) VALUES ({current_topic_id},'{note}')"
                cursor.execute(statement)
                print(f"note added to topic '{current_topic}'")
                connection.commit()
            except:
                print("something is wrong - check if the curriculum and/or topic is selected")
                
#give multiple attempts to login, database has three values so far
while(True): 
    username = input("username:")
    password = input("password:")
    login = f"SELECT * from users where username='{username}' AND password = '{password}'"
    cursor.execute(login)

    if not cursor.fetchone():  # An empty result evaluates to False.
        print("login failed - try again")
        continue
    else:
        print("welcome to project")
        actions()