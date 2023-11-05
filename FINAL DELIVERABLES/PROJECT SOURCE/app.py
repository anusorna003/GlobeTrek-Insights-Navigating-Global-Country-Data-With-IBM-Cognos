from flask import Flask, send_from_directory

app = Flask(_name_)

@app.route('/')
def open_html():
    folder_path = 'C:/Users/samue/Desktop/'  # Specify the path to your desktop folder
    return send_from_directory(folder_path, 'Global Data Analysis.html')

if _name_ == '_main_':
    app.run(debug=True)
