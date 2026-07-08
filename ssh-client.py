import paramiko

# 1. ตั้งค่าข้อมูลการเชื่อมต่อ (ปรับให้ตรงกับเครื่อง Ubuntu ของคุณแล้ว)
hostname = "192.168.188.128"  # IP เครื่อง Ubuntu ของคุณ
port = 22                     # พอร์ตมาตรฐานของ SSH
user = "ubuntu"               # ชื่อผู้ใช้
passwd = "T123456789"     # ใส่รหัสผ่านของเครื่อง Ubuntu คุณตรงนี้แทนในเครื่องหมายคำพูด

try:
    # 2. เริ่มสร้าง SSH Client
    client = paramiko.SSHClient()
    
    # โหลด Host Keys ของระบบที่มีอยู่เดิม
    client.load_system_host_keys()
    
    # ตั้งนโยบายให้ยอมรับ SSH Key อัตโนมัติ (เหมือนการพิมพ์ 'yes' ตอนรีโมทครั้งแรก)
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    # ทำการเชื่อมต่อไปยังเซิร์ฟเวอร์ปลายทาง
    print(f"Connecting to {hostname}...")
    client.connect(hostname, port=port, username=user, password=passwd)
    print("Connected successfully!\n")
    
    # 3. ลูปวนรับคำสั่งเพื่อควบคุมเครื่องปลายทางแบบ Real-time
    while True:
        try:
            # รับคำสั่งจากหน้าจอ (เช่น ls, pwd, ip a)
            cmd = input("$> ")
            
            # ถ้าพิมพ์คำว่า exit ให้หลุดออกจากลูปเพื่อปิดโปรแกรม
            if cmd.strip() == "exit":
                break
                
            # ส่งคำสั่งไปรันบนเครื่องเซิร์ฟเวอร์ปลายทาง
            stdin, stdout, stderr = client.exec_command(cmd)
            
            # อ่านผลลัพธ์ที่เซิร์ฟเวอร์ตอบกลับมา แปลงรหัส แล้วแสดงบนหน้าจอ
            output = stdout.read().decode()
            error = stderr.read().decode()
            
            if output:
                print(output, end="")
            if error:
                print(f"Error: {error}", end="")
                
        except KeyboardInterrupt:
            # รองรับการกด Ctrl+C เพื่อออกจากโปรแกรมอย่างปลอดภัย
            print("\nDisconnecting...")
            break
            
    # ปิดการเชื่อมต่อเมื่อเลิกใช้งาน
    client.close()
    print("Connection closed.")
    
except Exception as err:
    # แสดงข้อผิดพลาดหากเชื่อมต่อไม่สำเร็จ (เช่น รหัสผิด หรือยังไม่ได้เปิดบริการ SSH)
    print(f"Connection Failed: {str(err)}")