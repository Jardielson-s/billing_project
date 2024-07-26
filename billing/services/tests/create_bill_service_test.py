from django.test import TestCase
from unittest.mock import MagicMock
from billing.services.create_bill_service import CreateBillService

class CreateBillServiceTest(TestCase):
    def setUp(self):
        self.mock_model = MagicMock()
        self.service = CreateBillService(self.mock_model)

    def test_create_bills_when_none_exist(self):
        reader = [
            {'name': 'John Doe', 'email': 'john@example.com', 'governmentId': '12345',
             'debtAmount': 500, 'debtDueDate': '2024-12-31', 'debtId': 'd57fe519-94c8-427c-92bb-77a72c898837'}
        ]

        self.mock_model.objects.filter.return_value.exists.return_value = False

        result = self.service.create(reader)

        mock_bill_instance = self.mock_model(
            name='John Doe',
            email='john@example.com',
            government_id='12345',
            debt_amount=500,
            debt_due_date='2024-12-31',
            debt_id='d57fe519-94c8-427c-92bb-77a72c898837',
            sended=False
        )

        # Verifica se bulk_create foi chamado com a instância mock
        self.mock_model.objects.bulk_create.assert_called_once_with([mock_bill_instance])

        # Verifica se o resultado é o esperado
        self.assertEqual(result, [mock_bill_instance])

    def test_create_bills_when_some_exist(self):
        reader = [
            {'name': 'Jane Doe', 'email': 'jane@example.com', 'governmentId': '67890',
             'debtAmount': 1000, 'debtDueDate': '2024-11-30', 'debtId': 'd57fe519-94c8-427c-92bb-77a72c898837'}
        ]

        self.mock_model.objects.filter.return_value.exists.return_value = True
        result = self.service.create(reader)
        self.mock_model.objects.bulk_create.assert_not_called()
        self.assertEqual(result, [])

    def test_create_bills_with_complex_filter(self):
        reader = [
            {'name': 'Alice Smith', 'email': 'alice@example.com', 'governmentId': '54321',
             'debtAmount': 750, 'debtDueDate': '2024-10-31', 'debtId': 'd57fe519-94c8-427c-92bb-77a72c898837'}
        ]

        self.mock_model.objects.filter.return_value.exists.return_value = False
        result = self.service.create(reader)
        mock_bill_instance = self.mock_model(
            name='Alice Smith',
            email='alice@example.com',
            government_id='54321',
            debt_amount=750,
            debt_due_date='2024-10-31',
            debt_id='d57fe519-94c8-427c-92bb-77a72c898837',
            sended=False
        )

        self.mock_model.objects.bulk_create.assert_called_once_with([mock_bill_instance])
        self.assertEqual(result, [mock_bill_instance])
