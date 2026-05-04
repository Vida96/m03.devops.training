# this file contains a SQL injection vulnerability

def get_user_data(username):
    query = "SELECT * FROM users WHERE username = %s"
    params = (username,)
    
    cursor.execute(query, params)
    
    # Simulated execution output (safe logging)
    print("Executing query with params:", query, params)


if __name__ == "__main__":
    get_user_data("admin'; DROP TABLE users; --")
