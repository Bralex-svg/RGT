# Define a simple get_db function directly in the endpoints.py file
def get_db():
    # Implement your database connection logic here
    db = Session()  # Example: Create a database session
    try:
        yield db
    finally:
        db.close()  
