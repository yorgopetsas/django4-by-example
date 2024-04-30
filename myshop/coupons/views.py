from django.shortcuts import redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import Coupon
from .forms import CouponApplyForm

def codes_in_cart():
    pass

@require_POST
def coupon_apply(request):
    if code_used == 1:
        code_used = 0
    code_used = 0
    now = timezone.now()
    form = CouponApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['discount_code']
        try:
            coupon = Coupon.objects.get(discount_code__iexact=code, discount_validity_start__lte=now, discount_validity_end__gte=now, discount_active=True)
            code_used = 1
            request.session['coupon_id'] = coupon.id
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
    return redirect('cart:cart_detail')
