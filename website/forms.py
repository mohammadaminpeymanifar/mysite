from django import forms
from website.models import contact                     # مدل دیتابیس

class NameForm(forms.Form):
    name = forms.CharField(max_length=255)             # فیلد متنی
    email = forms.EmailField()                         # اعتبارسنجی ایمیل
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)

class contactForm (forms.ModelForm):                   # فرم متصل به مدل (ModelForm)
    class Meta:
        model = contact                                # مدلی که فرم به آن متصل است
        fields = '__all__'                             # تمام فیلدهای مدل در فرم نمایش داده شوند