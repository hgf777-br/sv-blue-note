from django.http import HttpResponse
import json
from django.core import serializers
from boat.cadastro.models import Servico, Setor

def servico_api(request):
    servicos = Servico.objects.all()
    response = []
    for servico in servicos:
        registro = {}
        registro['id'] = servico.id
        registro['name'] = servico.name
        registro['setor'] = str(servico.setor)
        registro['period'] = str(servico.period) + " meses" if servico.period != 0 else 'pontual'
        response.append(registro)
    # response = serializers.serialize('json', servicos, fields=('name', 'setor', 'period'))
        
    return HttpResponse(json.dumps(response))
