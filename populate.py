import mlab
from Module.CV_template1 import Template1
from faker import Faker
from random import randint, choice


mlab.connect()

fake = Faker()
# for i in range (50):
#     print("Saving service", i +1, '.....')
template1 = Template1(name='Victor Tatarinov',
                      street_address = "185 Giang Vo",
                        city = "Hanoi",
                        country = "Vietnam",
                        university = "Moscow University",
                        uni_location = "Moscow, Russia",
                        major = "CEO Support",
                        graduation_date = "January 2012",
                        GPA = "3.99/4.0",
                        SAT = "bliek",
                        Honors = "Highest Dreamer",
                        Relevant_Coursework = "Coc Coc Analytics, Trac Master of Excellence, Staff Tool Expert ",
                        Company1 = "Coc Coc Company Ltd.",
                        Company1_location = "Giang Vo",
                        Company1_Position = "CEO of Support",
                        Company1_duration = "Feb 2016 - Present",
                        Company1_Bullet1 = "Managed 4000 products in footwear category by creating online marketing campaigns, resulting in 12% monthly growth in revenue",
                        Company1_Bullet2 = "Analyzed past marketing campaigns and led the team’s effort to implement three sales campaigns, resulting in a 3x increase in sales",
                        Company1_Bullet3 = "Analyzed ROI and created marketing campaigns that lowered customer acquisition cost by 25%",
                        Company1_Bullet4 = "Created an Excel tool which automatically processed more than 10,000 data entries daily, resulting in a 4x increase in time efficiency",
                        Company2 = "FPT Software",
                        Company2_location = "StringField()",
                        Company2_Position = "StringField()",
                        Company2_duration = "StringField()",
                        Company2_Bullet1 = "Created an Excel tool which automatically processed more than 10,000 data entries daily, resulting in a 4x increase in time efficiency",
                        Company2_Bullet2 = 'StringField()',
                        Company2_Bullet3 = 'StringField()',
                        Company2_Bullet4 = 'StringField()',
                        Company3 = 'StringField()',
                        Company3_location = 'to be updated',
                        Company3_Position = 'to be updated',
                        Company3_duration = 'to be updated',
                        Company3_Bullet1 = 'to be updated',
                        Company3_Bullet2 = 'to be updated',
                        Company3_Bullet3 = 'to be updated',
                        Company3_Bullet4 = 'to be updated',
                        Languages = 'to be updated',
                        Technical_skills = 'to be updated',
                        Training = 'to be updated',
                        Activities = 'to be updated',
                        Interests = 'to be updated',)
template1.save()
