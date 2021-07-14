from rest_framework import generics

from quotes.models import Quote
from .permissions import IsAdminUserOrReadOnly
from .serializers import QuoteSerializer


class QuoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Quote.objects.all().order_by("created_at")
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class QuoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all().order_by("created_at")
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]
