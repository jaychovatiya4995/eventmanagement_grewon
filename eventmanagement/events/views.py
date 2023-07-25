"""
    Views for the Event.

    EventMangement 2023.

    Author - Jay Chovatiya - Grewon Technologies Pvt Ltd
"""
import datetime

from django.db.models import Count, Exists, OuterRef, Q, F
from django.utils import timezone
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response

from .backends import CustomUserAuthenticationBackend
from .models import CustomUser, Event


class AvailableUserList(APIView):
    """
        This view returns the list of available users for a given event day
    """
    authentication_classes = [CustomUserAuthenticationBackend,]

    @staticmethod
    def is_valid_date(date_string):
        try:
            datetime.datetime.strptime(date_string, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def get(self, request, *args, **kwargs):
        """
            Currently, we just get an avability of user based on particlure one day.

            To check a user avability based on more then one day or based on hours,
            we needs to modify below code.
        """
        queryset = CustomUser.objects.all().prefetch_related('user_event')
        date = self.request.data.get('event_date', timezone.now().date())

        if isinstance(date, str) and not self.is_valid_date((date)):
            raise ValidationError('Invalid date format. Date must be in YYYY-MM-DD format.')

        queryset = queryset.annotate(is_not_available=Exists(
            Event.objects.filter(user=OuterRef('pk'), start_datetime__gte=date, end_datetime__lte=date))
        ).aggregate(
            total_user=Count('id'),
            is_avilable_count=Count('id', filter=Q(is_not_available=False)),
            is_not_avilable_count=Count('id', filter=Q(is_not_available=True)),
            avability_percentage=((F('is_avilable_count') * 100) / F('total_user'))
        )

        return Response(queryset)
