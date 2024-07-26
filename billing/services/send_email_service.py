import logging

class EmailService:
    def send_email(self, recipient, subject, message):
        logging.info(f"Simulated sending email to {recipient} with subject '{subject}' and message '{message}'")
