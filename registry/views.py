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
            
        # serializer = CommuneHistorySerializer(queryset, many=True)        
       
       
        data = []
        if a == CommuneOld:
            a = queryset.filter
        for q in CommuneNew.objects.filter(id__in=queryset.values("commune_new_id").distinct()):
            merged_list = queryset.filter(commune_new=q).values(
                "commune_old__name",
                "commune_old__type",
                "commune_old__district__name",
                "commune_old__district__type",
            )
            data.append({
                "commune_new": f"{q.type} {q.name}",
                "province": q.province.name,
                "merged_list": [
                    f"{item['commune_old__type']} {item['commune_old__name']} ({item['commune_old__district__type']} {item['commune_old__district__name']})"
                    for item in merged_list
                ]
            })

        return Response(data)
    
    

        '''
        # Lấy tất cả commune_new có liên quan và prefetch commune_old
        commune_news = (CommuneNew.objects.filter(id__in=queryset.values("commune_new_id").distinct()).prefetch_related("communehistory_set__commune_old__district"))

        data = []
        for new in commune_news:
            merged_list = [
                f"{h.commune_old.type} {h.commune_old.name} ({h.commune_old.district.name})"
                for h in new.communehistory_set.all()
            ]
            data.append({
                "commune_new": f"{new.type} {new.name}",
                "province": new.province.name,
                "merged_list": merged_list,
            })

        return Response(data)
        '''
            
def index(request):
    return render(request, "index.html")
    
