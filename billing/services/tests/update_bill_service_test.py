from django.test import TestCase
from unittest.mock import MagicMock
from billing.models import Bill
from billing.services.update_bill_service import UpdateBillService

class UpdateBillServiceTests(TestCase):

    def setUp(self):
        self.update_bill_service = UpdateBillService(Bill)

    def test_update_bill(self):
        bill = Bill(
            government_id='12345',
            email='test@example.com',
            debt_amount=500,
            debt_due_date='2024-12-31',
            debt_id='d57fe519-94c8-427c-92bb-77a72c898837',
            sended=False
        )
        bill.save()

        self.update_bill_service.update(bill)

        updated_bill = Bill.objects.get(government_id='12345', email='test@example.com')
        self.assertTrue(updated_bill.sended)

    def test_update_bill_no_matching_records(self):
        bill = Bill(
            government_id='99999',
            email='no-match@example.com',
            debt_amount=500,
            debt_due_date='2024-12-31',
            debt_id='debt999',
            sended=False
        )

        self.update_bill_service.update(bill)

        matching_records = Bill.objects.filter(government_id='99999', email='no-match@example.com')
        self.assertEqual(matching_records.count(), 0)

    def test_update_bill_no_sended_field(self):
        bill = Bill(
            government_id='67890',
            email='another_test@example.com',
            debt_amount=1000,
            debt_due_date='2024-11-30',
            debt_id='d57fe519-94c8-427c-92bb-77a72c898837'
        )

        bill.save()
        self.update_bill_service.update(bill)
        updated_bill = Bill.objects.get(government_id='67890', email='another_test@example.com')
        self.assertTrue(updated_bill.sended)

