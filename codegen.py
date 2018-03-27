#    Email = template1['Email'] if form['Email'] == '' else form['Email']

list1 = ['name', 'street_address', 'Phonenumber', 'Email', 'city', 'country', 'university', 'uni_location', 'major', 'graduation_date', 'GPA', 'SAT', 'Honors', 'Relevant_Coursework', 'Company1', 'Company1_location', 'Company1_Position', 'Company1_duration', 'Company1_Bullet1','Company1_Bullet2'
, 'Company1_Bullet3',
'Company1_Bullet4',
'Company2',
'Company2_location',
'Company2_Position', 'Company2_duration', 'Company2_Bullet1', 'Company2_Bullet2', 'Company2_Bullet3', 'Company2_Bullet4', 'Company3', 'Company3_location', 'Company3_Position', 'Company3_duration', 'Company3_Bullet1', 'Company3_Bullet2', 'Company3_Bullet3', 'Company3_Bullet4', 'Languages', 'Technical_skills', 'Training', 'Activities', 'Interests']

for item in list1:
    print('{0} = template1[\'{0}\'] if form[\'{0}\'] == \'\' else form[\'{0}\']'.format(item))
    # print('set__{0}= {0},'.format(item))
