# billing/tests_services.py

import unittest
from unittest.mock import patch
from billing.services.send_email_service import EmailService  # Ajuste o caminho conforme sua estrutura de projeto

class EmailServiceTests(unittest.TestCase):
    
    @patch('logging.info')
    def test_send_email(self, mock_logging_info):
        # Instanciar o EmailService
        service = EmailService()

        # Dados de teste
        recipient = 'test@example.com'
        subject = 'Test Subject'
        message = 'This is a test message.'

        # Chamar o método send_email
        service.send_email(recipient, subject, message)

        # Verificar se logging.info foi chamado com os argumentos corretos
        expected_message = f"Simulated sending email to {recipient} with subject '{subject}' and message '{message}'"
        mock_logging_info.assert_called_once_with(expected_message)

if __name__ == '__main__':
    unittest.main()
