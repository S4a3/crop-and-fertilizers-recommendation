from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout
import random
import string
import smtplib
from email.mime.text import MIMEText


# === HOME ===
def home(request):
    return render(request, 'main/home.html')


# === LOGIN ===
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('otp')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'main/login.html')


# === REGISTER ===
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')

    return render(request, 'main/register.html')


# === LOGOUT ===
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


# === PREDICTION ===
# def predict_view(request):
#     if request.method == 'POST':
#         crop = "Wheat"
#         fertilizer = "Urea"
#         return render(request, 'main/predict.html', {
#             'crop': crop,
#             'fertilizer': fertilizer
#         })
#     return render(request, 'main/predict.html')


# === OTP SECTION ===

def generate_otp():
    return ''.join(random.choice(string.digits) for _ in range(6))


def send_otp_email(user_email, otp):
    subject = "Your OTP Code"
    body = f"Your One-Time Password (OTP) is: {otp}"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = "santhoshkumarm170@gmail.com"
    msg['To'] = user_email

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("santhoshkumarm170@gmail.com", "gnscscskqmvtvcob")
        server.sendmail(msg['From'], [msg['To']], msg.as_string())
        server.quit()
    except Exception as e:
        print("Failed to send email:", e)


@login_required
def otp_request_view(request):
    user = request.user
    otp = generate_otp()
    request.session['otp'] = otp  # Store in session
    send_otp_email(user.email, otp)
    print(f"✅ OTP sent to {user.email}: {otp}")  # Debug
    return render(request, 'main/otp_verify.html')


@login_required
def otp_verify_view(request):
    if request.method == 'POST':
        input_otp = ''.join([
            request.POST.get('first', ''),
            request.POST.get('second', ''),
            request.POST.get('third', ''),
            request.POST.get('fourth', ''),
            request.POST.get('fifth', ''),
            request.POST.get('sixth', ''),
        ])

        session_otp = request.session.get('otp')
        print(f"🧾 Entered: {input_otp}, 🔒 Session: {session_otp}")

        if session_otp and input_otp == session_otp:
            del request.session['otp']
            messages.success(request, "✅ OTP verified successfully!")
            return redirect('home')
        else:
            messages.error(request, "❌ Invalid OTP. Please try again.")

    return render(request, 'main/otp_verify.html')


@login_required
def resend_otp(request):
    otp = generate_otp()
    request.session['otp'] = otp
    send_otp_email(request.user.email, otp)
    messages.success(request, "🔁 OTP resent successfully.")
    return redirect('otp_verify')


#-------------AdminLogin------------#
def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('otp')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'main/adminlogin.html')

#-----------------AdminHome-------------#

def adminhome(request):
    return render(request, 'main/adminhome.html')

#==============Admin LogOut ============#

def adminlogout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('adminhome')
    
from django.shortcuts import render
from .models import Product

# def predict_view(request):
#     products = Product.objects.all()
#     return render(request, 'main/predict.html', {'products': products})






###Prediction ...
import joblib
import os
from django.shortcuts import render

# Load the ML model
model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'ml_models', 'crop_model.pkl')
model = joblib.load(model_path)

def predict_view(request):
    crop = None
    fertilizer = None

    if request.method == 'POST':
        try:
            n = float(request.POST['nitrogen'])
            p = float(request.POST['phosphorus'])
            k = float(request.POST['potassium'])
            temp = float(request.POST['temperature'])
            humidity = float(request.POST['humidity'])

            # Optional fixed values
            ph = 6.5
            rainfall = 100.0

            # Predict using the model
            prediction = model.predict([[n, p, k, temp, humidity, ph, rainfall]])
            crop = prediction[0]

            # Simple logic for fertilizer (customize later)
            fertilizer = "Urea" if crop.lower() in ['rice', 'wheat'] else "DAP"

        except Exception as e:
            print("Prediction error:", e)

    return render(request, 'main/predict.html', {
        'crop': crop,
        'fertilizer': fertilizer
    })
