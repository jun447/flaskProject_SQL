from website import create_app

app = create_app()




if __name__ == '__main__':
    app.run(debug=True)
# explain above written code
# 1. import Flask class from flask module
# 2. create Flask object and pass __name__ as parameter
# 3. create route for home page
# 4. create function for home page
# 5. return string from function
# 6. run the application
