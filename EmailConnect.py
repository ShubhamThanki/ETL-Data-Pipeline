import smtplib
import os
from email.message import EmailMessage
import csv
import datetime

def send_error_file_via_email(file_path, sender_email, sender_password, receiver_email):
    """
    Args:
        file_path (str): Path to the file to attach.
        sender_email (str): Your email address (Gmail, etc.).
        sender_password (str): Your email password or app password.
        receiver_email (str): The recipient email address.
    """

    try:
        # Create the email
        msg = EmailMessage()
        msg['Subject'] = '🚨 ETL Project Alert: Missing Data Report'
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg.set_content('Hello,\n\nMissing data was found during ETL processing.\nPlease find the attached report if available.\n\nBest Regards,\nYour ETL Bot')

        # Check if the file exists
        if os.path.exists(file_path):
            # Attach the file
            with open(file_path, 'rb') as f:
                file_data = f.read()
                file_name = os.path.basename(file_path)

            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
            print(f"✅ File {file_name} attached to the email.")
        else:
            print(f"⚠️ File {file_path} does not exist. Sending email without attachment.")

        # Send the email using SMTP server (Gmail example)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)

        print(f"✅ Email sent successfully to {receiver_email}.")

    except Exception as e:
        print(f"❌ Failed to send email: {e}")

# Example usage:
# send_error_file_via_email('missing_rows_2025-04-27_19-00-00.txt', 'your_email@gmail.com', 'your_password', 'receiver_email@gmail.com')