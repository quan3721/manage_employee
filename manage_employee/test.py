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

employee = db.child('Employee_sub/1').get().val()
print(employee)
for v,y in employee.items():
    print(y)

# print(employee)
# for emp in employee:
#     print(emp)