from django.shortcuts import render
import pyrebase

config = {
    "apiKey": "AIzaSyAGxlNqHpBsLGS6VqgQM2W5TfMPYAppcc4",
    "authDomain": "attendance-system-f3c35.firebaseapp.com",
    "databaseURL": "https://attendance-system-f3c35-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "attendance-system-f3c35",
    "storageBucket": "attendance-system-f3c35.appspot.com",
    "messagingSenderId": "583243067002",
    "appId": "1:583243067002:web:7546293b13e514c97015c3",
    "measurementId": "G-MP8VF3KBNF"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
firebase.storage()
def index(request):

    employee = db.child('Employee_sub').get()
    employee_m = db.child('Employee').get()
    context = {
        'employee': employee.val(),
        'employee_m': employee_m.val(),
        
    }


    return render(request, 'index.html', context)

