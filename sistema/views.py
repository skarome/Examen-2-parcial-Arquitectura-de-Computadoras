from django.shortcuts import render
from django.http import JsonResponse
import psutil
import platform  

def get_system_info():
    try:
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory()
        disk = psutil.disk_usage('C:/')
        
        sistema_op = platform.system()
        version = platform.release()
        arquitectura = platform.machine()

        return {
            'cpu': cpu,
            'ram_total': round(mem.total / (1024**3), 2),
            'ram_usada': round(mem.used / (1024**3), 2),
            'ram_porcentaje': mem.percent,
            'disco_total': round(disk.total / (1024**3), 2),
            'disco_usado': round(disk.used / (1024**3), 2),
            'disco_libre': round(disk.free / (1024**3), 2),
            'disco_porcentaje': round((disk.used / disk.total) * 100, 2),
            'nucleos': psutil.cpu_count(),
            'so': f"{sistema_op} {version} ({arquitectura})",
        }
    except Exception as e:
        return {'error': str(e)}


def index(request):
    datos = get_system_info()
    return render(request, 'sistema/principal.html', datos)


def system_data(request):
    return JsonResponse(get_system_info())