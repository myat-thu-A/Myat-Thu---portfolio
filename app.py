from flask import Flask, render_template, request, jsonify, send_from_directory
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# ---------- Email Config ----------
SENDER_EMAIL = "your_email@gmail.com"          # Change this
SENDER_PASSWORD = "your_app_password"          # App password from Gmail
RECEIVER_EMAIL = "your_email@gmail.com"        # Where messages go


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/download_resume")
def download_resume():
    # ✅ resume.pdf ရှိတဲ့ directory ကို ပြန်သုံး
    folder = os.path.join(os.getcwd(), "static")
    filename = "resume.pdf"
    file_path = os.path.join(folder, filename)

    file_path = os.path.join(folder, filename)
    if not os.path.exists(file_path):
        return "❌ Resume file not found. Please generate it first."

    # ✅ File ကို download အနေနဲ့ ပြန်ပေး
    return send_from_directory(folder, filename, as_attachment=False)


@app.route('/contact', methods=['POST'])
def contact():
    try:
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = f"Portfolio Message from {name}"

        body = f"From: {name}\nEmail: {email}\n\nMessage:\n{message}"
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()

        return jsonify({'success': True, 'message': 'Message sent successfully! ✅'})
    except Exception as e:
        print("Error:", e)
        return jsonify({'success': False, 'message': 'Error sending message ❌'})


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")