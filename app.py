from frame import getRoutes, db  # Import the 'db' instance from the frame module
app = getRoutes()

if __name__ == "__main__":
    # Initialize the database tables before running the app
    with app.app_context():
        db.create_all()

    app.run(host='0.0.0.0', debug=True)
