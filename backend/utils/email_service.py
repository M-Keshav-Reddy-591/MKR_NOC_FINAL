import smtplib

from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart


EMAIL = "yourgmail@gmail.com"

PASSWORD = "your_app_password"


def send_email(
    receiver_email,
    subject,
    body
):

    try:

        msg = MIMEMultipart()

        msg["From"] = EMAIL

        msg["To"] = receiver_email

        msg["Subject"] = subject

        msg.attach(
            MIMEText(body, "plain")
        )

        server = smtplib.SMTP(
            "smtp.gmail.com",
            587
        )

        server.starttls()

        server.login(
            EMAIL,
            PASSWORD
        )

        server.sendmail(
            EMAIL,
            receiver_email,
            msg.as_string()
        )

        server.quit()

        print(
            f"Email sent to {receiver_email}"
        )

    except Exception as e:

        print(
            "Email Error:",
            str(e)
        )
