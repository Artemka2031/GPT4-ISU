from rest_framework.views import APIView
from rest_framework.response import Response
from .models import generate_response


class VicunaGenerateView(APIView):
    """
    API для генерации текста с помощью модели Vicuna-13B-v1.5.
    """

    def post(self, request):
        prompt = request.data.get("prompt")
        if not prompt:
            return Response({"error": "Prompt is required."}, status=400)

        try:
            response = generate_response(prompt)
            return Response({"response": response}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
