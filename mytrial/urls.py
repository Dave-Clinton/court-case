from django.urls import path
from . import views  
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
        path('',views.index,name='index'),
        path('login/', views.login_view, name='login'),
        path('logout/', views.logout_view, name='logout'),
        path('verify/', views.verify, name='verify'),
        path('register/', views.register, name='register'),
        path('password_reset/', views.password_reset_request, name='password_reset'),
        path('verify_email/<uidb64>/<token>/', views.verify_email, name='verify_email'),
        path('homeland/', views.homeland, name='homeland'),
        path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
        path('details/', views.details, name='details'),
        path('dashboard/', views.dashboard, name='dashboard'),
        path('review_dashboard/', views.review_dashboard, name='review_dashboard'),
        path('create-pass-ticket/<int:case_file_id>/', views.create_pass_ticket, name='create_pass_ticket'),
        path('update_pass_ticket_status/<int:ticket_id>/', views.update_pass_ticket_status, name='update_pass_ticket_status'),
        path('edit_pass_ticket/<int:ticket_id>/', views.edit_pass_ticket, name='edit_pass_ticket'),
        path('delete_pass_ticket/<int:ticket_id>/', views.delete_pass_ticket, name='delete_pass_ticket'),
        path('edit_profile/', views.edit_profile, name='edit_profile'),
        path('delete_profile/', views.delete_profile, name='delete_profile'),
        path('ticket/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
        path('case/<int:case_id>/', views.case_detail, name='case_detail'),
        path('case/export/<int:case_id>/', views.export_case_to_word, name='export_case_to_word'),
        path('ticket/export/<int:ticket_id>/', views.export_ticket_to_word, name='export_ticket_to_word'),
        path('make-payment/<int:ticket_id>/', views.make_payment, name='make_payment'),
        path('capture-payment/', views.capture_payment, name='capture_payment'),
        path('make_payment/<int:ticket_id>/', views.make_payment, name='make_payment'),

        ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
           urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
                urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)