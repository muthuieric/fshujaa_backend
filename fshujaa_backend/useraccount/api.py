from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import User
from .serializers import UserDetailSerializer

from course.serializers import EnrollmentsListSerializer



@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def instructor_detail(request, pk):
    user = User.objects.get(pk=pk)

    serializer = UserDetailSerializer(user, many=False)

    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def enrollments_list(request):
    enrollments = request.user.enrollments.all()

    print('user', request.user)
    print(enrollments)
    
    serializer = EnrollmentsListSerializer(enrollments, many=True)
    return JsonResponse(serializer.data, safe=False)