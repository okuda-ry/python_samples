from django import forms
from .models import Link, Profile

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['title', 'url', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Link Title'}),
            'url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://example.com'}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Display Order'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_image']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Tell us about yourself'}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }

    def clean_profile_image(self):
        image = self.cleaned_data.get('profile_image', False)
        if image:
            if image.size > 2 * 1024 * 1024:  # 2MB limit
                raise forms.ValidationError("Image file too large ( > 2MB )")
        return image