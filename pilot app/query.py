import mlab
from Module.service import Service

mlab.connect()

id_to_find = '5a95625edec2189c34bf2d80'
find = Service.objects().with_id(id_to_find)

# all_services = Service.objects()
#
# first_service = all_services[0]
# last_service = all_services[11]
#
# print(first_service['name'])
#
# print(last_service['name'])
#
print(find.to_mongo())

if find is not None:
    # find.delete()
    find.update(set__status= True)
    find.reload()
    print(find.to_mongo())
else:
    print("Not found")
