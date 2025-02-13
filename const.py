token = ""
url = "url"
classes = [
  {
    "id": 4861,
    "isSpecialClass": False,
    "institutionId": 65,
    "spClassId": "7",
    "spClassNameId": "19",
    "spStudyLangId": "1",
    "yearOfStudy": 2024,
    "classDegree": 7,
    "students": [],
    "subClasses": [],
    "curatorId": 5387,
    "spClassCategoryId": 2,
    "comment": "tabiiy yo'nalish",
    "countOfStudents": 24,
    "lastUpdatedDate": "11.11.2024 15:13:51"
  }
]
class_names = [
    {
        "label": "01",
        "value": "27",
        "dataInt": None,
        "code": None,
        "rootCode": None,
        "dataStr": None,
        "dataStr2": None,
        "dateTime": None,
        "comment": None,
        "booleanProperty": None
    },
    {
        "label": "02",
        "value": "28",
        "dataInt": None,
        "code": None,
        "rootCode": None,
        "dataStr": None,
        "dataStr2": None,
        "dateTime": None,
        "comment": None,
        "booleanProperty": None
    },
    {
        "label": "03",
        "value": "29",
        "dataInt": None,
        "code": None,
        "rootCode": None,
        "dataStr": None,
        "dataStr2": None,
        "dateTime": None,
        "comment": None,
        "booleanProperty": None
    }
]

def getClassName(id):
    try:
        classInfo = {}
        for i in classes:
            if id==i["id"]:
                classInfo=i
                break
        for i in class_names:
            if i["value"] == classInfo["spClassNameId"]:
                return str(classInfo["classDegree"]) + i["label"]+"-Sinf"
    except:
        return "Unknaun"