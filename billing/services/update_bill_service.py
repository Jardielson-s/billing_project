from django.db.models import Q

class UpdateBillService:
    def __init__(self, model) -> None:
        self.bill_model = model

    def update(self, bill):
        self.bill_model.objects.filter(government_id=bill.government_id, email=bill.email).update(sended=True)

