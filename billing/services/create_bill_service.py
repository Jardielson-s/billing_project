from django.db.models import Q

class CreateBillService:
    def __init__(self, model) -> None:
        self.bill_model = model

    def create(self, reader):
        to_create_bills = []

        for row in reader:
            obj = {
                'name': row.get('name'),
                'email': row.get('email'),
                'government_id': row.get('governmentId'),
                'debt_amount': row.get('debtAmount'),
                'debt_due_date': row.get('debtDueDate'),
                'debt_id': row.get('debtId'),
                'sended': False
            }
            bill = self.bill_model(**obj)
        if not self.bill_model.objects.filter(
            Q(government_id=bill.government_id) &
            Q(email=bill.email) &
            Q(debt_id=bill.debt_id) or
            Q(sended=False)
        ).exists():
            to_create_bills.append(bill)

        if to_create_bills:
            self.bill_model.objects.bulk_create(to_create_bills)
        return to_create_bills