from flask import Flask, render_template, redirect, url_for, request

from Module.CV_template1 import Template1

import mlab

mlab.connect()


app = Flask(__name__)

# create collection
#
# service = Service(name='Hera Kieu Anh', yob= 1998, gender=0, height= 160, phone ='091234567', address='Hanoi', status=True)
#
# service.save()
#
#
@app.route('/')
def index():
    return render_template('CV_detail_page3/CV_student.html')

@app.route('/index')
def index1():
    return render_template('index.html',)


@app.route('/form')
def form():
    template1 = Template1.objects
    return render_template('CV_detail_page3/CV_form_edit.html', all_templates=template1)

@app.route('/search/<gender>')
def search(gender):
    services= Service.objects(gender=gender, yob__lte = '1998', height__gte = "160", address__contains = "Hanoi")
    return render_template('search.html', all_services= services)

@app.route('/student')
def student():
    return render_template('service-student.html')

@app.route('/worker')
def worker():
    return render_template('service-worker.html')

@app.route('/template')
def template():
    return "form"

@app.route('/admin')
def admin():
    services = Service.objects()
    return render_template('admin.html', services= services)

@app.route('/delete/<service_id>')
def delete(service_id):
    service_to_delete = Service.objects.with_id(service_id)

    if service_to_delete is None:
        return "Not found"

    service_to_delete.delete()

    return redirect(url_for('admin'))

@app.route('/new_service', methods = ['GET','POST'])
def created():
    if request.method == 'GET':
        return render_template('new_service.html')
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        yob = form['yob']
        phone = form['phone']

        new_service = Service(name=name, yob = yob, phone = phone, address = "Hà Nội", status = True, gender = 0, height = 169)
        new_service.save()

        return "Saved"




if __name__ == '__main__':
  app.run(debug=True)
