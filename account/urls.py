from django.urls import path
from account.views import SignUpView

urlpatterns = [
    # path('url_letter/', YOUR_VIEW_CLASS.as_view(), name='starts'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
