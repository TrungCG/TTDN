from django.shortcuts import render
from rest_framework.response import Response
from .models import ProvinceOld, District, CommuneOld, ProvinceNew, CommuneNew, CommuneHistory
from .serializers import ProvinceNewSerializer, CommuneNewSerializer, CommuneHistorySerializer, ProvinceOldSerializer, DistrictSerializer, CommuneOldSerializer
from rest_framework.views import APIView
from django.db.models import Q

    
class CommuneHistoryList(APIView):
    def get(self, request):
        queryset = CommuneHistory.objects.all()
        
        q = request.query_params.get('q', None)
        if q:
            queryset = queryset.filter(Q(commune_old__name__icontains=q) | 
                                       Q(commune_new__name__icontains=q))
            
        Province = request.query_params.get('Province', None)
        if Province:
            queryset = queryset.filter(Q(commune_old__district__province__name__icontains=Province) | 
                                       Q(commune_new__province__name__icontains=Province))
            
        District = request.query_params.get('District', None)
        if District:
            queryset = queryset.filter(commune_old__district__name__icontains=District)
            
        serializer = CommuneHistorySerializer(queryset, many=True)        
       
       
        results = []
        for new_commune in CommuneNew.objects.filter(id__in=queryset.values("commune_new_id").distinct()):
            merged_from = queryset.filter(commune_new=new_commune).values(
                "commune_old__name",
                "commune_old__type",
                "commune_old__district__name"
            )
            results.append({
                "commune_new": f"{new_commune.type} {new_commune.name}",
                "province": new_commune.province.name,
                "merged_from": [
                    f"{item['commune_old__type']} {item['commune_old__name']} ({item['commune_old__district__name']})"
                    for item in merged_from
                ]
            })

        return Response(results)
            
    
