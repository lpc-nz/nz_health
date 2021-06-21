from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('person', views.person, name='person_list'),
    path('person/<int:id>', views.person_form, name="person_update"),
    path('delete/<int:id>', views.person_delete, name="person_delete"),
    path('details/<int:id>', views.person_details, name="person_details"),
    path('details/<int:person_id>/add_referral', views.add_referral, name="add_referral"),
    path('person_form', views.person_form, name='person_form'),

    path('referrals', views.referrals, name='referral_list'),

    path('referrals/<int:id>', views.referral_form, name="referral_update"),
    path('referral_delete/<int:id>', views.referral_delete, name="referral_delete"),
    path('referral-details/<int:id>', views.referral_details, name="referral_details"),
    path('referral_form', views.referral_form, name='referral_form'),

    # path('position', views.position, name='position'),
    # path('position/<int:id>', views.position_form, name="position_update"),
    # path('position/<int:id>', views.position_delete, name="position_delete"),
    # path('position_form', views.position_form, name='position_form'),

]
