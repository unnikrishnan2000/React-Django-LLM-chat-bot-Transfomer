# myapp/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import SearchQuery
from .serializers import SearchQuerySerializer
from transformers import pipeline

@api_view(['GET', 'POST'])
def search_query_list(request):
    if request.method == 'GET':
        queries = SearchQuery.objects.all()
        serializer = SearchQuerySerializer(queries, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        # Extract the 'query' data from the request body
        query_data = request.data.get('query')
        print( type(query_data))
        a=query_data.split("Question")
        b=a[-1]
        a= "".join(a[0:-1])
        qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

            # Get the answer
        result = qa_pipeline({'question':  b, 'context': a})
        answer = result.get('answer', 'No answer found.')

   
      
       

        # Initialize the serializer with the extracted 'query' data
        serializer = SearchQuerySerializer(data={'query': answer})

        # Validate and save if valid
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # If validation fails, return errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Default response if not GET or POST
    return Response({'error': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
