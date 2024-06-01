# myapp/views.py

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from bs4 import BeautifulSoup

@api_view(['GET'])
def scrape_page(request):
    url = request.query_params.get('url')

    if not url:
        return Response({'error': 'URL parameter is missing'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract page title
        page_title = soup.find('h1').text if soup.find('h1') else ""

        # Extract links
        links = [link.get('href') for link in soup.find_all('a') if link.get('href')]

        # Create response data
        scraped_data = {
            'url': url,
            'page_title': page_title,
            'links': links
        }

        return Response(scraped_data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
