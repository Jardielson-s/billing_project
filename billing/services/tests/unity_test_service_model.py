import unittest
from unittest.mock import patch, MagicMock
from billing.services.create_bill_service import CreateBillService  # Ajuste o caminho conforme sua estrutura de projeto

class CreateBillServiceTests(unittest.TestCase):
    
    @patch('billing.models.Bill')
    def test_create_bills_when_none_exist(self, MockBill):
        service = CreateBillService(MockBill)

        reader = [
            {'name': 'John Doe', 'email': 'john@example.com', 'governmentId': '12345',
             'debtAmount': 500, 'debtDueDate': '2024-12-31', 'debtId': 'debt001'}
        ]

        MockBill.objects.filter.return_value.exists.return_value = False

        mock_bill_instance = MagicMock()
        MockBill.return_value = mock_bill_instance

        result = service.create(reader)

        MockBill.objects.bulk_create.assert_called_once_with([mock_bill_instance])

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], mock_bill_instance)

    @patch('billing.models.Bill')
    def test_create_bills_when_some_exist(self, MockBill):
        service = CreateBillService(MockBill)

        reader = [
            {'name': 'Jane Doe', 'email': 'jane@example.com', 'governmentId': '67890',
             'debtAmount': 1000, 'debtDueDate': '2024-11-30', 'debtId': 'debt002'}
        ]

        MockBill.objects.filter.return_value.exists.return_value = True

        result = service.create(reader)

        MockBill.objects.bulk_create.assert_not_called()

        self.assertEqual(result, [])

    @patch('billing.models.Bill')
    def test_create_bills_with_complex_filter(self, MockBill):
        service = CreateBillService(MockBill)

        reader = [
            {'name': 'Alice Smith', 'email': 'alice@example.com', 'governmentId': '54321',
             'debtAmount': 750, 'debtDueDate': '2024-10-31', 'debtId': 'debt003'}
        ]

        MockBill.objects.filter.return_value.exists.return_value = False
        mock_bill_instance = MagicMock()
        MockBill.return_value = mock_bill_instance
        result = service.create(reader)
        MockBill.objects.bulk_create.assert_called_once_with([mock_bill_instance])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], mock_bill_instance)

if __name__ == '__main__':
    unittest.main()
