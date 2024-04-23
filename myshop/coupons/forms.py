from django import forms

class CouponApplyForm(forms.Form):
    discount_code = forms.CharField()