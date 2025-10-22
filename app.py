from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample services data
SERVICES = [
    {"id": 1, "name": "Washing Machine Service", "icon": "🧺", "description": "Professional washing machine repair and maintenance"},
    {"id": 2, "name": "Fridge Service", "icon": "❄️", "description": "Refrigerator repair and servicing"},
    {"id": 3, "name": "AC Service", "icon": "🌬️", "description": "Air conditioner installation and repair"},
    {"id": 4, "name": "Vacuum Service", "icon": "🌀", "description": "Vacuum cleaner repair and maintenance"},
    {"id": 5, "name": "Delivery Service", "icon": "📦", "description": "Fast and reliable delivery services"},
    {"id": 6, "name": "Electrician Service", "icon": "⚡", "description": "Professional electrical services"}
]

@app.route('/')
def hero():
    return render_template('hero.html')

@app.route('/services', methods=['GET', 'POST'])
def services():
    if request.method == 'POST':
        # Handle form submission from hero page
        name = request.form.get('name')
        phone = request.form.get('phone')
        return render_template('services.html', services=SERVICES, name=name, phone=phone)
    
    return render_template('services.html', services=SERVICES)

@app.route('/select-service', methods=['POST'])
def select_service():
    service_id = request.form.get('service_id')
    name = request.form.get('name')
    phone = request.form.get('phone')
    
    # Find the selected service
    selected_service = next((service for service in SERVICES if service['id'] == int(service_id)), None)
    
    # In a real application, you would save this to a database
    print(f"Service request: {name} ({phone}) selected {selected_service['name']}")
    
    return render_template('success.html', 
                         service=selected_service, 
                         name=name, 
                         phone=phone)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)