from django.shortcuts import render,redirect
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
# Create your views here.
def add_new_employee(request):

    if request.method == 'POST':
        id = request.POST.get('enterID')
        name = request.POST.get('enterName')
        dob = request.POST.get('enterDOB')
        position = request.POST.get('enterPosition')
        year = request.POST.get('enterYear')
        address = request.POST.get('enterAddress')
        print(id, name, dob, year, position, address)
        context = {
            "ID": id,
            "Address": address,
            "Date_of_Birth": dob,
            "Name": name,
            "Position": position,
            "Starting_Year": year,
            "Last_attendance_in": "",
            "Last_attendance_out": "",
            "List_of_Workday": "",
            "Total_attendance_in_Month": 0,
        }

        context_sub = {
            "ID": id,
            "Address": address,
            "Date_of Birth": dob,
            "Name": name,
            "Position": position,
            "Starting_Year": year,
            "Total_attendance_in_Month": 0,
        }



        db.child(f"Employee/{id}").set(context)
        db.child(f"Employee_sub/{id}").set(context_sub)

        return redirect('index')

    return render(request, 'index.html')