from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.exceptions import NotFound
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


def handling_500(response):
    context = {}
    return render(response,"peterplysside/fejl500.html", context)

############# PostNummer
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def postNummer_liste(request):
    postnr = PostNummer.objects.all()
    serializer = PostNummerSerializer(postnr, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def postNummer_create(request):
    serializer = PostNummerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def postNummer_view(request, pk):
    postnr = PostNummer.objects.get(postNr=pk)
    serializer = PostNummerSerializer(postnr, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def postNummer_update(request, pk):
    postnr = PostNummer.objects.get(id=pk)
    serializer = PostNummerSerializer(instance=postnr, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def postnummer_delete(request, pk):
    postnr = PostNummer.objects.get(id=pk)
    postnr.delete()

    return Response('Post Nummer Deleted Successfully')
############# PostNummer_Slut


############# Person
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def person_liste(request):
    person = Person.objects.all()
    serializer = PersonSerializer(person, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def person_create(request):
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def person_view(request, pk):
    person = Person.objects.get(id=pk)
    serializer = PersonSerializer(person, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def person_view_navn(request, pk):
    person = Person.objects.get(brugernavn=pk)
    if( not person ):
        raise NotFound('person not found')
    serializer = PersonSerializer(person, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def person_update(request, pk):
    person = Person.objects.get(id=pk)
    serializer = PersonSerializer(instance=person, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def person_delete(request, pk):
    person = Person.objects.get(id=pk)
    person.delete()

    return Response('Person er stadig i live "wink"')
############# Person_Slut


############# Handlinger
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def handlinger_liste(request):
    handling = Handlinger.objects.all()
    serializer = HandlingerSerializer(handling, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def handlinger_create(request):
    serializer = HandlingerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def handlinger_view(request, pk):
    handlinger = Handlinger.objects.get(id=pk)
    serializer = HandlingerSerializer(handlinger, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def handlinger_update(request, pk):
    handlinger = Handlinger.objects.get(id=pk)
    serializer = HandlingerSerializer(instance=handlinger, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def handlinger_delete(request, pk):
    handlinger = Handlinger.objects.get(id=pk)
    handlinger.delete()

    return Response('Handlinger has been deleted')
############# Handlinger_Slut


############# Handling_Junctions
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def hj_liste(request):
    hj = Handling_Junctions.objects.all()
    serializer = HandlingJunctionsSerializer(hj, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def hj_create(request):
    serializer = HandlingJunctionsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def hj_view(request, pk):
    hj = Handling_Junctions.objects.get(id=pk)
    serializer = HandlingJunctionsSerializer(hj, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def hj_update(request, pk):
    hj = Handling_Junctions.objects.get(id=pk)
    serializer = HandlingerSerializer(instance=hj, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def hj_delete(request, pk):
    hj = Handling_Junctions.objects.get(id=pk)
    hj.delete()

    return Response('hj has been deleted')
############# Handling_Junctions_Slut


############# Rapport
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def rapport_liste(request):
    rapport = Rapport.objects.all()
    serializer = RapportSerializer(rapport, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def rapport_create(request):
    serializer = RapportSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def rapport_view(request, pk):
    rapport = Rapport.objects.get(id=pk)
    serializer = RapportSerializer(rapport, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def rapport_update(request, pk):
    rapport = Rapport.objects.get(id=pk)
    serializer = RapportSerializer(instance=rapport, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def rapport_delete(request, pk):
    rapport = Rapport.objects.get(id=pk)
    rapport.delete()

    return Response('hj has been deleted')
############# Rapport_Slut


############# Rapport_junctions
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def rj_liste(request):
    rj = Rapport_junctions.objects.all()
    serializer = RapporjunctionstSerializer(rj, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def rj_create(request):
    serializer = RapporjunctionstSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def rj_view(request, pk):
    rj = Rapport_junctions.objects.get(id=pk)
    serializer = RapporjunctionstSerializer(rj, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def rj_view2(request, pk):
    rj = Rapport_junctions.objects.get(suspectId=pk)
    serializer = RapporjunctionstSerializer(rj, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def rj_update(request, pk):
    rj = Rapport_junctions.objects.get(id=pk)
    serializer = RapporjunctionstSerializer(instance=rj, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def rj_delete(request, pk):
    rj = Rapport_junctions.objects.get(id=pk)
    rj.delete()

    return Response('hj has been deleted')
############# Rapport_junctions_Slut


############# PointGrade
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def pointGrade_liste(request):
    pg = PointGrade.objects.all()
    serializer = PointGradeSerializer(pg, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def pointGrade_create(request):
    serializer = PointGradeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def pointGrade_view(request, pk):
    pg = PointGrade.objects.get(id=pk)
    serializer = PointGradeSerializer(pg, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def pointGrade_update(request, pk):
    pg = PointGrade.objects.get(id=pk)
    serializer = PointGradeSerializer(instance=pg, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def pointGrade_delete(request, pk):
    pg = PointGrade.objects.get(id=pk)
    pg.delete()

    return Response('hj has been deleted')
############# PointGrade_Slut


############# Permissions
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def permissions_liste(request):
    permissions = Permissions.objects.all()
    serializer = PermissionsSerializer(permissions, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def permissions_create(request):
    serializer = PermissionsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def permissions_view(request, pk):
    permissions = Permissions.objects.get(id=pk)
    serializer = PermissionsSerializer(permissions, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def permissions_update(request, pk):
    permissions = Permissions.objects.get(id=pk)
    serializer = PermissionsSerializer(instance=permissions, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def permissions_delete(request, pk):
    pg = Permissions.objects.get(id=pk)
    pg.delete()

    return Response('hj has been deleted')
############# Permissions_Slut


############# Uddel_Permissions
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def up_liste(request):
    up = Uddel_Permissions.objects.all()
    serializer = Uddel_PermissionsSerializer(up, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def up_create(request):
    serializer = Uddel_PermissionsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def up_view(request, pk):
    up = Uddel_Permissions.objects.get(id=pk)
    serializer = Uddel_PermissionsSerializer(up, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def up_update(request, pk):
    up = Uddel_Permissions.objects.get(id=pk)
    serializer = Uddel_PermissionsSerializer(instance=up, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def up_delete(request, pk):
    up = Uddel_Permissions.objects.get(id=pk)
    up.delete()

    return Response('hj has been deleted')
############# Uddel_Permissions_Slut

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def liste(request):
    up = Person.objects.all()
    serializer = BPID(up, many=True)
    return Response(serializer.data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cprliste(request):
    up = Person.objects.all()
    serializer = BCPR(up, many=True)
    return Response(serializer.data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def appperson_view(request, pk):
    person = Person.objects.get(brugernavn=pk)
    serializer = PersonSerializer(person, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def setting(request):
    settings = Settings.objects.all()
    serializer = SettingSerializer(settings, many=True)
    return Response(serializer.data)

