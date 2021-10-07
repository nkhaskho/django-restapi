


from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from django.http import Http404

from .models import Reservation
from .serializers import ReservationSerializer


class ReservationList(generics.ListCreateAPIView):
    """
    List all reservations, or create a new equipment reservation.
    """
    queryset = Reservation.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('user', 'equipment_type', 'status')
    serializer_class = ReservationSerializer
    #permission_classes = (IsAuthenticated,)


class ReservationDetail(APIView):
    """
    Retrieve, update or delete a reservation instance.
    """
    def get_object(self, pk):
        try:
            return Reservation.objects.get(pk=pk)
        except Reservation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        reservation = self.get_object(pk)
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        reservation = self.get_object(pk)
        serializer = ReservationSerializer(reservation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        reservation = self.get_object(pk)
        #reservation.is_active = False
        reservation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)