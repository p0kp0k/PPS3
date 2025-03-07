from rest_framework import serializers

from banks_app.models import Bank, BankOffice, Employee, BankAtm, Client, PaymentAccount, CreditAccount


class BankCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ('id', 'name',)


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = "__all__"


class BankOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankOffice
        fields = (
            'id', 'bank', 'name', 'address', 'status', 'can_place_atm', 'can_provide_credit', 'dispense_money',
            'accept_money', 'rent_cost'
        )


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class BankAtmSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAtm
        fields = (
            'id', 'bank', 'bank_office', 'employee', 'name', 'status', 'dispense_money', 'accept_money',
            'maintenance_cost')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'banks', 'full_name', 'birth_date', 'job', 'monthly_income')


class PaymentAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentAccount
        fields = '__all__'


class CreditAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditAccount
        fields = (
            'id', 'employee', 'payment_account', 'client', 'bank_name', 'start_date', 'end_date',
            'loan_duration_months',
            'loan_amount', 'monthly_payment')


class CreateCreditAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditAccount
        fields = (
            'id', 'employee', 'payment_account', 'client', 'bank_name', 'end_date',
            'loan_amount', 'monthly_payment')
