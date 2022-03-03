#!/usr/bin/env python3

import emails
import psutil, shutil, socket

def cpu_health():
    if psutil.cpu_percent(interval=None) > 80.0:
        error_msg = 'Error - CPU usage is over 80%'
        send_email_alert(error_msg)

def memory_health():
    # memory
    mem = psutil.virtual_memory()
    min_memory = 500 * 1024 * 1024
    if mem.available < min_memory:
        error_msg = 'Error: Available memory is less than 500MB'
        send_email_alert(error_msg)

def disk_health():
    # disk space check
    disk_info = shutil.disk_usage('/')
    twenty_percent_disk = int((disk_info.total / 100) * 20)
    if disk_info.free < twenty_percent_disk:
        error_msg = 'Error: Available disk space is less than 20%'
        send_email_alert(error_msg)

def localhost_resolve():
    # localhost check
    ip_addr = socket.gethostbyname('localhost')
    if ip_addr != '127.0.0.1':
        error_msg = 'Error - localhost cannot be resolved to 127.0.0.1'
        send_email_alert(error_msg)


def send_email_alert(error_msg):
    msg = emails.generate_email('automation@example.com', 'username@example.com', error_msg, 'Please check your system and resolve the issue as soon as possible.', '')
    emails.send_email(msg)


if __name__ == '__main__':
    cpu_health()
    memory_health()
    disk_health()
    localhost_resolve()
