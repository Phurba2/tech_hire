from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

# Sample services data
SERVICES = [
    {"id": 1, "name": "Washing Machine Service", "icon": "🧺", "description": "Professional washing machine repair and maintenance"},
    {"id": 2, "name": "Fridge Service", "icon": "❄️", "description": "Refrigerator repair and servicing"},
    {"id": 3, "name": "AC Service", "icon": "🌬️", "description": "Air conditioner installation and repair"},
    {"id": 4, "name": "Vacuum Service", "icon": "🌀", "description": "Vacuum cleaner repair and maintenance"},
    {"id": 5, "name": "Delivery Service", "icon": "📦", "description": "Fast and reliable delivery services"},
    {"id": 6, "name": "Electrician Service", "icon": "⚡", "description": "Professional electrical services"}
]

# Sample technicians data (matches technician.html hardcoded data)
TECHNICIANS = [
    {"id": 1, "name": "John Doe", "expertise": "Plumbing", "phone": "+1234567890", "photo_url": "/static/images/a.jpeg"},
    {"id": 2, "name": "Jane Smith", "expertise": "Electrical", "phone": "+1234567891", "photo_url": "/static/images/b.jpeg"},
    {"id": 3, "name": "Mike Johnson", "expertise": "HVAC", "phone": "+1234567892", "photo_url": "/static/images/c.jpeg"},
    {"id": 4, "name": "Sarah Brown", "expertise": "Carpentry", "phone": "+1234567893", "photo_url": "/static/images/a.jpeg"},
    {"id": 5, "name": "David Lee", "expertise": "Painting", "phone": "+1234567894", "photo_url": "/static/images/b.jpeg"},
    {"id": 6, "name": "Emily Davis", "expertise": "Appliance Repair", "phone": "+1234567895", "photo_url": "/static/images/c.jpeg"}
]

@app.route('/')
def hero():
    return render_template('hero.html')

@app.route('/services', methods=['GET', 'POST'])
def services():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        if not name or not phone:
            flash('Name and phone number are required', 'error')
            return render_template('services.html', services=SERVICES)
        return render_template('services.html', services=SERVICES, name=name, phone=phone)
    
    return render_template('services.html', services=SERVICES)

@app.route('/select-service', methods=['POST'])
def select_service():
    service_id = request.form.get('service_id')
    name = request.form.get('name')
    phone = request.form.get('phone')
    
    if not name or not phone:
        flash('Name and phone number are required', 'error')
        return redirect(url_for('services'))
    
    # Find the selected service
    selected_service = next((service for service in SERVICES if service['id'] == int(service_id)), None)
    
    if not selected_service:
        flash('Invalid service selected', 'error')
        return redirect(url_for('services'))
    
    # In a real application, save to database
    print(f"Service request: {name} ({phone}) selected {selected_service['name']}")
    
    # Redirect to technicians page
    return redirect(url_for('technicians', name=name, phone=phone, service_id=service_id))

@app.route('/technicians')
def technicians():
    name = request.args.get('name', '')
    phone = request.args.get('phone', '')
    service_id = request.args.get('service_id', '')
    return render_template('technician.html', technicians=TECHNICIANS, name=name, phone=phone, service_id=service_id)

@app.route('/select-technician', methods=['POST'])
def select_technician():
    technician_id = request.form.get('technician_id')
    name = request.form.get('name')
    phone = request.form.get('phone')
    service_id = request.form.get('service_id')
    
    if not name or not phone:
        flash('Name and phone number are required', 'error')
        return redirect(url_for('technicians'))
    
    # Find the selected technician
    selected_technician = next((tech for tech in TECHNICIANS if tech['id'] == int(technician_id)), None)
    
    if not selected_technician:
        flash('Invalid technician selected', 'error')
        return redirect(url_for('technicians'))
    
    # In a real application, save to database
    print(f"Technician request: {name} ({phone}) selected {selected_technician['name']} for service ID {service_id}")
    
    return render_template('technician.html', 
                         technician=selected_technician, 
                         name=name, 
                         phone=phone)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)