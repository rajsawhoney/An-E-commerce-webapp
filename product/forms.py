from django import forms
from reviews.models import Review
from questions_ans.models import QuestionAns
from product.models import Product


class RvwForm(forms.ModelForm):
    description = forms.CharField(label='', widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Your text goes here...', 'rows': '3', 'cols': '100'}))

    class Meta:
        model = Review
        fields = ('description',)


class QnAnsForm(forms.ModelForm):
    description = forms.CharField(label='', widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Your text goes here...', 'rows': '3', 'cols': '60'}))

    class Meta:
        model = QuestionAns
        fields = ('description',)


# class ReviewsForm(forms.Form):
#     name = forms.CharField(label="Your Name:", max_length=30, widget=forms.TextInput(
#         attrs={
#             "class": "form-control",
#             "type": "text",
#             "placeholder": "Your Name"
#         }))

#     email = forms.EmailField(
#         widget=forms.EmailInput(
#             attrs={
#                 "class": "form-control",
#                 "type": "email",
#                 "placeholder": "Your Email"}),

#     )

#     review = forms.CharField(
#         widget=forms.Textarea(
#             attrs={
#                 "class": "form-control",
#                 "type": "text",
#                 "placeholder": "Your Review Here"
#             }))

#     def clean_email(self):
#         data = self.cleaned_data["email"]
#         if not 'gmail' in data:
#             raise forms.ValidationError("Email must contain gmail.com!")
#         return data


# class QuestionForm(forms.Form):
#     name = forms.CharField(max_length=25, widget=forms.TextInput(
#         attrs={
#             "class": "form-control",
#             "type": "text",
#             "placeholder": "Your Name Please!"
#         }))
#     email = forms.EmailField(
#         widget=forms.EmailInput(
#             attrs={
#                 "class": "form-control",
#                 "type": "email",
#                 "placeholder": "Your Email"}),
#     )
#     question = forms.CharField(max_length=100,
#                                widget=forms.TextInput(
#                                    attrs={
#                                        "class": "form-control",
#                                        "type": "text",
#                                        "placeholder": "Your Question"
#                                    }))

#     def clean_email(self):
#         data = self.cleaned_data["email"]
#         if not 'gmail' in data:
#             raise forms.ValidationError("Email must contain gmail.com!")
#         return data

class ProductModelForm(forms.ModelForm):
    name = forms.CharField(label="Product Name:", max_length=30, widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "type": "text",
            "placeholder": "Product Name"
        }))

    description = forms.CharField(label='Description', widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Your text goes here...', 'rows': '3', 'cols': '60'}))

    class Meta:
        model = Product
        fields = ("name", "product_count", "product_type", "thumbnail",
                  "description", "category", "price_amount", "old_price", "charge_taxes",)
