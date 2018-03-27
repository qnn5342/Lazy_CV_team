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
    #     print(template1)
        return render_template('CV_detail_page3/CV_form_edit.html', all_templates=[template1])
    elif request.method == 'POST':
        # print (template1)
        if template1 is not None:
            # list1 = ['name', 'street_address', 'Phonenumber', 'Email', 'city', 'country', 'university', 'uni_location', 'major', 'graduation_date', 'GPA', 'SAT', 'Honors', 'Relevant_Coursework', 'Company1', 'Company1_location', 'Company1_Position', 'Company1_duration', 'Company1_Bullet1', 'Company1_Bullet2', 'Company1_Bullet3', 'Company1_Bullet4', 'Company2', 'Company2_location', 'Company2_Position', 'Company2_duration', 'Company2_Bullet1', 'Company2_Bullet2', 'Company2_Bullet3', 'Company2_Bullet4', 'Company3', 'Company3_location', 'Company3_Position', 'Company3_duration', 'Company3_Bullet1', 'Company3_Bullet2', 'Company3_Bullet3', 'Company3_Bullet4', 'Languages', 'Technical_skills', 'Training', 'Activities', 'Interests']
            form = request.form
            if form['name'] != "":
                name = form['name']
            else:
                name = template1['name']

            if form['street_address'] != "":
                street_address = form['street_address']
            else:
                street_address = template1['street_address']
            #
            # if str(form['Phonenumber']) != "":
            #     Phonenumber = form['Phonenumber']
            # else:
            #     Phonenumber = template1['Phonenumber']
            #
            # if form['Email] != "":
            #     Email = form['Email']
            # else:
            #     Email = template1['Email']
            #
            # if form['city'] != "":
            #     city = form['city']
            # else:
            #     city = template1['city']
            #
            # if form['country'] != "":
            #     country = form['country']
            # else:
            #     country = template1['country']

            # country = form['country']
            # Phonenumber = form['Phonenumber']
            # Email = form['Email']
            # university = form ['university']
            # uni_location = form ['uni_location']
            # SAT = form['SAT']
            # print(name)
            # print(template1['name'])
            # print(street_address)
            # print(city)
            # print(country)
            # print(SAT)
            # list1 = [name, street_address]
            # list2 = []
            # for item in list1:
            #     if item != '':
            #         list2.append(item)
            # print(list2)
            print (name)
            template1.update(set__name= name,
            set__street_address= street_address)
            # set__Phonenumber= Phonenumber)
            # set__Email= Email,)
             # set__city= city, set__country= country)
              # set__SAT = SAT)
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
