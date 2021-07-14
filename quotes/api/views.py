from rest_framework import generics

from quotes.models import Quote
from quotes.api.serializers import QuoteSerializer


class QuoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Quote.objects.all().order_by("created_at")
    serializer_class = QuoteSerializer


class QuoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all().order_by("created_at")
    serializer_class = QuoteSerializer
