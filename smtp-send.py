import smtplib

# 1. กำหนดโครงสร้างข้อความอีเมล (รวม Header และ Content แบบ HTML)
message = """From: From Joe <joe@blow.com>
To: To Henry <ubuntu@ubuntu>
MIME-Version: 1.0
Content-type: text/html
Subject: Test HTML Email

This is an email message sent as HTML.

<b>This is a test HTML Message.</b>
<h1>This is headling 1</h1>
"""

# 2. เริ่มกระบวนการเชื่อมต่อและส่งอีเมลด้วยบล็อก try-except
try:
    # เชื่อมต่อไปยัง SMTP Server (เปลี่ยน IP ให้ตรงกับเครื่องปลายทางของคุณ)
    smtp = smtplib.SMTP("192.168.188.128",25)
    
    # ส่งอีเมล: sendmail(ผู้ส่ง, ผู้รับ, ข้อความ)
    smtp.sendmail("ubuntu@ubuntu", "ubuntu@ubuntu", message)
    
    print("Email sent successfully")
    
except Exception as err:
    # แสดงข้อผิดพลาดหากไม่สามารถเชื่อมต่อหรือส่งเมลได้
    print(str(err))