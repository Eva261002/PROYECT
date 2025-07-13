from django.shortcuts import render

def index(request):
    return render(request, 'books/index.html')
 
def book_list(request):
    
    books = [
        {'id': 1, 'title': 'Cien años de soledad', 'author': 'García Márquez'},
        {'id': 2, 'title': '1984', 'author': 'George Orwell'}
    ]
    return render(request, 'books/list.html', {'books': books})

def book_detail(request, book_id):
    # Ejemplo estático
    book = {'id': book_id, 'title': f'Libro Ejemplo {book_id}', 'author': 'Autor Desconocido'}
    return render(request, 'books/detail.html', {'book': book})

def book_search(request):
    query = request.GET.get('q', '')
    # Aquí implementarías la lógica de búsqueda real
    results = []
    if query:
        # Ejemplo de búsqueda estática
        all_books = [
            {'id': 1, 'title': 'Cien años de soledad', 'author': 'García Márquez'},
            {'id': 2, 'title': 'Desventajas de ser yo', 'author': 'George Orwell'},
            {'id': 3, 'title': 'El Principito', 'author': 'Antoine Baudelaire'},
            
        ]
        results = [book for book in all_books if query.lower() in book['title'].lower()]
 