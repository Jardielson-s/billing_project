# billing/views.py

import csv
from django.views.decorators.csrf import csrf_exempt   
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status

from billing.services.send_email_service import EmailService
from .models import Bill


@api_view(['POST'])
@csrf_exempt
def upload_csv(request):
    file = request.FILES.get('file')
    if not file:
        return JsonResponse({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

    if not file.name.endswith('.csv'):
        return JsonResponse({'error': 'Invalid file type'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        csv_file = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(csv_file)
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
            bill = Bill(**obj)
            if not Bill.objects.filter(government_id=bill.government_id, email=bill.email, debt_id=bill.debt_id).exists():
                to_create_bills.append(bill)

        if to_create_bills:
            Bill.objects.bulk_create(to_create_bills)
            email_service = EmailService()
            for bill in to_create_bills:
                email_service.send_email(
                    recipient=bill.email,
                    subject='Your bill',
                    message=f'Hello {bill.name},\n\nYour bill of {bill.debt_amount} is due on {bill.debt_due_date}.\n\nBest regards,\nYour Company'
                )

        return JsonResponse({'status': 'File processed successfully'}, status=status.HTTP_200_OK)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
