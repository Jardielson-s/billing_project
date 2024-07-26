# billing/tests.py

import os
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from unittest.mock import patch
from billing.models import Bill

class BillUploadTests(APITestCase):
    @patch('billing.services.send_email_service.EmailService.send_email')
    def test_upload_csv(self, mock_send_email):
        test_csv_path = os.path.join(os.path.dirname(__file__), 'test_data', 'test.csv')
        with open(test_csv_path, 'rb') as file:
            response = self.client.post(reverse('upload_csv'), {'file': file}, format='multipart')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Bill.objects.exists())
        self.assertTrue(mock_send_email.called)
