from django.shortcuts import render

def pagina_inicio(request):
    informacion_personal = {
        'nombre': 'Víctor',
        'apellido': 'Mondaca',
        'ciudad': 'Cumpeo',
        'profesion': 'Administrador de Empresas',
        'carrera': 'Tecnico Analista Programador',
        'descripcion': 'Apasionado por la tecnología y el desarrollo de software',
        'musica_favorita': 'Rock Alternativo'
    }
    return render(request, 'miPrimerApp/index.html', {'datos': informacion_personal})


def galeria_fotografias(request):
    coleccion_imagenes = [
        {
            'titulo': 'Paisaje Montañoso',
            'descripcion': 'Hermosa vista de las montañas nevadas al atardecer, capturando la majestuosidad de la naturaleza en su máximo esplendor.',
            'autor': 'Carlos Mendoza',
            'fecha_captura': '15 de Marzo, 2024',
            'url_imagen': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&h=600&fit=crop',
            'url_completa': 'https://images.unsplash.com/photo-1549366021-9f761d450615?w=1200&h=800&fit=crop'
        },
        {
            'titulo': 'Ciudad Moderna',
            'descripcion': 'Panorámica urbana que muestra la arquitectura contemporánea y el desarrollo tecnológico de las ciudades del futuro.',
            'autor': 'Ana Rodríguez',
            'fecha_captura': '22 de Febrero, 2024',
            'url_imagen': 'https://images.unsplash.com/photo-1449824913935-59a10b8d2000?w=800&h=600&fit=crop',
            'url_completa': 'https://images.unsplash.com/photo-1549366021-9f761d450615?w=1200&h=800&fit=crop'
        },
        {
            'titulo': 'Naturaleza Salvaje',
            'descripcion': 'Impresionante captura de la vida silvestre en su hábitat natural, mostrando la belleza y diversidad de nuestro planeta.',
            'autor': 'Miguel Torres',
            'fecha_captura': '8 de Enero, 2024',
            'url_imagen': 'https://images.unsplash.com/photo-1549366021-9f761d450615?w=800&h=600&fit=crop',
            'url_completa': 'https://images.unsplash.com/photo-1549366021-9f761d450615?w=1200&h=800&fit=crop'
        }
    ]
    return render(request, 'miPrimerApp/fotos.html', {'fotos': coleccion_imagenes})

