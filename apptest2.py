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
    template1 = Template1.objects
    return render_template('CV_detail_page3/CV_student.html', all_templates=template1)

@app.route('/index')
def index1():
    return render_template('index.html',)

@app.route('/')
#
# @app.route('/form')
# def form():
#     template1 = Template1.objects()
#     return render_template('CV_detail_page3/CV_form_edit.html',all_templates= template1)


@app.route('/form/<template1_id>',methods = ['GET','POST'])
def form(template1_id):
    id_to_find = template1_id
    # template1 = Template1.objects()
    # print(template1)
    template1 = Template1.objects().with_id(id_to_find)
    # print(template2)
    if request.method == 'GET':
        print(template1)
        return render_template('CV_detail_page3/CV_form_edit.html', all_templates=[template1], id_to_find=id_to_find)
    elif request.method == 'POST':
        print (template1)
        if template1 is not None:
            form = request.form
            name = form['name']
            street_address = form['street_address']
            city = form['city']
            country = form['country']
            Phonenumber = form['Phonenumber']
            Email = form['Email']
            university = form ['university']
            uni_location = form ['uni_location']

            print(name)
            print(street_address)
            print(city)
            print(country)


            template1.update(set__name= name,
            set__street_address= street_address,
             set__city= city, set__country= country)
            template1.reload()
            print(template1.to_mongo())
            # return "Updated!!"
            return redirect(url_for('preview'))

        else:
            return("Not found")


@app.route('/preview')
def preview():
    template1 = Template1.objects
    return render_template('CV_detail_page3/CV_student.html', all_templates=template1)



#
# @app.route('/update_service/<service_id>',methods = ['GET','POST'])
# def update(service_id):
#     id_to_find = service_id
#     service_to_update= Service.objects().with_id(id_to_find)
#     # search = Service.objects.with_id(id_to_find)
#     if request.method == 'GET':
#         return render_template('update_service.html', service_to_update = service_to_update)
#     elif request.method == 'POST':
#         print (service_to_update)
#         if service_to_update is not None:
#             form = request.form
#             name = form['name']
#             yob = form['yob']
#             phone = form['phone']
#             image = form['image']
#             description = form['description']
#             measurements = form['measurements']
#             height = form['height']
#             # return (name + str(yob)+ str(phone) + str(image) + str(description) + str(measurements))
#             service_to_update.update(set__name= name,
#             set__yob= yob,set__phone= phone, set__image= image, set__height = height,set__description= description,set__measurements=measurements)
#             service_to_update.reload()
#             print(service_to_update.to_mongo())
#             # return "Updated!!"
#             return redirect(url_for('admin'))
#
#         else:
#             return("Not found")






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
