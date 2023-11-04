import pandas as pd
import json
from django.http import JsonResponse
from django.views import View
from .models import Registros_info

class RegisterView(View):
    def get(self, request, d_codigo):
        lista =[]
        registros = Registros_info.objects.filter(d_codigo=d_codigo)
        df = pd.DataFrame(list(registros.values()))
        print(df)
        for _, row in df.iterrows():
            lista.append( 
                {
                    "key": row['id_asenta_cpcons'],
                    "name": row['c_mnpio'],
                    "zone_type": row['d_zona'],
                    "settlement_type": {
                        "name": row['d_tipo_asenta']
                    }
                },
            )

        response = {
            "zip_code": df['d_codigo'].iloc[0],
            "locality": df['D_mnpio'].iloc[0],
            "federal_entity": {
                "key": df['c_estado'].iloc[0],
                "name": df['c_mnpio'].iloc[0],
                "code": df['c_CP'].iloc[0],
                },
            "settlements": lista,
            "municipality": {
                "key": df['c_mnpio'].iloc[0],
                "name": df['D_mnpio'].iloc[0]
            }
        }

        return JsonResponse(response, safe=False)