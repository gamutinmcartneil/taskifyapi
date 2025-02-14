from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Test')

    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            price = request.POST.get('price')
            data, error = supabase.table('products').insert([{'name': name, 'price': price}]).execute()
            if error:
                print(f"Error inserting product: {error}")
                # Handle error
            else:
                # Redirect or show success message
                pass
    except Exception as e:
        print(f"Error creating product: {e}")
        # Handle error