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
# @app.route('/')
# def index():
#     template1 = Template1.objects
#     return render_template('CV_detail_page3/CV_student.html', all_templates=template1)

@app.route('/')
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
            if str(form['Phonenumber']) != "":
                Phonenumber = form['Phonenumber']
            else:
                Phonenumber = template1['Phonenumber']

            Email = template1['Email'] if form['Email'] == '' else form['Email']
            city = template1['city'] if form['city'] == '' else form['city']
            country = template1['country'] if form['country'] == '' else form['country']
            university = template1['university'] if form['university'] == '' else form['university']
            uni_location = template1['uni_location'] if form['uni_location'] == '' else form['uni_location']
            major = template1['major'] if form['major'] == '' else form['major']
            graduation_date = template1['graduation_date'] if form['graduation_date'] == '' else form['graduation_date']
            GPA = template1['GPA'] if form['GPA'] == '' else form['GPA']
            SAT = template1['SAT'] if form['SAT'] == '' else form['SAT']
            Honors = template1['Honors'] if form['Honors'] == '' else form['Honors']
            Relevant_Coursework = template1['Relevant_Coursework'] if form['Relevant_Coursework'] == '' else form['Relevant_Coursework']
            Company1 = template1['Company1'] if form['Company1'] == '' else form['Company1']
            Company1_location = template1['Company1_location'] if form['Company1_location'] == '' else form['Company1_location']
            Company1_Position = template1['Company1_Position'] if form['Company1_Position'] == '' else form['Company1_Position']
            Company1_duration = template1['Company1_duration'] if form['Company1_duration'] == '' else form['Company1_duration']
            Company1_Bullet1 = template1['Company1_Bullet1'] if form['Company1_Bullet1'] == '' else form['Company1_Bullet1']
            Company1_Bullet2 = template1['Company1_Bullet2'] if form['Company1_Bullet2'] == '' else form['Company1_Bullet2']
            Company1_Bullet3 = template1['Company1_Bullet3'] if form['Company1_Bullet3'] == '' else form['Company1_Bullet3']
            Company1_Bullet4 = template1['Company1_Bullet4'] if form['Company1_Bullet4'] == '' else form['Company1_Bullet4']
            Company2 = template1['Company2'] if form['Company2'] == '' else form['Company2']
            Company2_location = template1['Company2_location'] if form['Company2_location'] == '' else form['Company2_location']
            Company2_Position = template1['Company2_Position'] if form['Company2_Position'] == '' else form['Company2_Position']
            Company2_duration = template1['Company2_duration'] if form['Company2_duration'] == '' else form['Company2_duration']
            Company2_Bullet1 = template1['Company2_Bullet1'] if form['Company2_Bullet1'] == '' else form['Company2_Bullet1']
            Company2_Bullet2 = template1['Company2_Bullet2'] if form['Company2_Bullet2'] == '' else form['Company2_Bullet2']
            Company2_Bullet3 = template1['Company2_Bullet3'] if form['Company2_Bullet3'] == '' else form['Company2_Bullet3']
            Company2_Bullet4 = template1['Company2_Bullet4'] if form['Company2_Bullet4'] == '' else form['Company2_Bullet4']
            Company3 = template1['Company3'] if form['Company3'] == '' else form['Company3']
            Company3_location = template1['Company3_location'] if form['Company3_location'] == '' else form['Company3_location']
            Company3_Position = template1['Company3_Position'] if form['Company3_Position'] == '' else form['Company3_Position']
            Company3_duration = template1['Company3_duration'] if form['Company3_duration'] == '' else form['Company3_duration']
            Company3_Bullet1 = template1['Company3_Bullet1'] if form['Company3_Bullet1'] == '' else form['Company3_Bullet1']
            Company3_Bullet2 = template1['Company3_Bullet2'] if form['Company3_Bullet2'] == '' else form['Company3_Bullet2']
            Company3_Bullet3 = template1['Company3_Bullet3'] if form['Company3_Bullet3'] == '' else form['Company3_Bullet3']
            Company3_Bullet4 = template1['Company3_Bullet4'] if form['Company3_Bullet4'] == '' else form['Company3_Bullet4']
            # Company4 = template1['Company4'] if form['Company4'] == '' else form['Company4']
            # Company4_location = template1['Company4_location'] if form['Company4_location'] == '' else form['Company4_location']
            # Company4_Position = template1['Company4_Position'] if form['Company4_Position'] == '' else form['Company4_Position']
            # Company4_duration = template1['Company4_duration'] if form['Company4_duration'] == '' else form['Company4_duration']
            # Company4_Bullet1 = template1['Company4_Bullet1'] if form['Company4_Bullet1'] == '' else form['Company4_Bullet1']
            # Company4_Bullet2 = template1['Company4_Bullet2'] if form['Company4_Bullet2'] == '' else form['Company4_Bullet2']
            # Company4_Bullet3 = template1['Company4_Bullet3'] if form['Company4_Bullet3'] == '' else form['Company4_Bullet3']
            # Company4_Bullet4 = template1['Company4_Bullet4'] if form['Company4_Bullet4'] == '' else form['Company3_Bullet4']
            Languages = template1['Languages'] if form['Languages'] == '' else form['Languages']
            Technical_skills = template1['Technical_skills'] if form['Technical_skills'] == '' else form['Technical_skills']
            Training = template1['Training'] if form['Training'] == '' else form['Training']
            Activities = template1['Activities'] if form['Activities'] == '' else form['Activities']
            Interests = template1['Interests'] if form['Interests'] == '' else form['Interests']

            # print (university)
            template1.update(set__name= name,
            set__street_address= street_address,
            set__Phonenumber= Phonenumber,
            set__Email= Email,
            set__city= city,
            set__country= country,
            set__university= university,
            set__uni_location= uni_location,
            set__major= major,
            set__graduation_date= graduation_date,
            set__GPA= GPA,
            set__SAT= SAT,
            set__Honors= Honors,
            set__Relevant_Coursework= Relevant_Coursework,
            set__Company1= Company1,
            set__Company1_location= Company1_location,
            set__Company1_Position= Company1_Position,
            set__Company1_duration= Company1_duration,
            set__Company1_Bullet1= Company1_Bullet1,
            set__Company1_Bullet2= Company1_Bullet2,
            set__Company1_Bullet3= Company1_Bullet3,
            set__Company1_Bullet4= Company1_Bullet4,
            set__Company2= Company2,
            set__Company2_location= Company2_location,
            set__Company2_Position= Company2_Position,
            set__Company2_duration= Company2_duration,
            set__Company2_Bullet1= Company2_Bullet1,
            set__Company2_Bullet2= Company2_Bullet2,
            set__Company2_Bullet3= Company2_Bullet3,
            set__Company2_Bullet4= Company2_Bullet4,
            set__Company3= Company3,
            set__Company3_location= Company3_location,
            set__Company3_Position= Company3_Position,
            set__Company3_duration= Company3_duration,
            set__Company3_Bullet1= Company3_Bullet1,
            set__Company3_Bullet2= Company3_Bullet2,
            set__Company3_Bullet3= Company3_Bullet3,
            set__Company3_Bullet4= Company3_Bullet4,
            # set__Company4_location= Company4_location,
            # set__Company4_Position= Company4_Position,
            # set__Company4_duration= Company4_duration,
            # set__Company4_Bullet1= Company4_Bullet1,
            # set__Company4_Bullet2= Company4_Bullet2,
            # set__Company4_Bullet3= Company4_Bullet3,
            # set__Company4_Bullet4= Company4_Bullet4,
            set__Languages= Languages,
            set__Technical_skills= Technical_skills,
            set__Training= Training,
            set__Activities= Activities,
            set__Interests= Interests,
            )

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
