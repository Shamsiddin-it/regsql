from context import *

create_database_tables()

def register():
    conn = open_connection()
    cur = conn.cursor()
    cur.execute(f""" insert into users(username, password, first_name, last_name, email) values
                ('{input("Enter username: ")}',
                '{input("password: ")}',
                '{input("name: ")}',
                '{input("last name: ")}',
                '{input("email: ")}'
                )
                """)
    conn.commit()
    close_connection(conn,cur)

# register()

def get_all_users():
    conn = open_connection()
    cur = conn.cursor()
    cur.execute("select * from users")
    users = cur.fetchall()
    conn.commit()
    close_connection(conn,cur)
    return users

# print(get_all_users())



def login():
    conn = open_connection()
    cur = conn.cursor()
    cur.execute(f"select * from users where username = '{input("username: ")}' and password = '{input("password: ")}'")
    user = cur.fetchone()
    close_connection(conn,cur)
    return user

# print(login())
