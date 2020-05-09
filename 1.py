import json

biodata = {
  "name": "Muhamad Irvan Rizki",
  "age": 22,
  "address": "Jl Bintara 8 Rt 03 Rw 03 No.15",
  "is_married": False,
  "list_school": [
    {"Name": "Smk Negeri 1 Bekasi"},
    {"year_in": 2013},
    {"year_out": 2016},
    {"major": "Multimedia"},
  ],
  "skill": [
    {"Name": "python"},
    {"Level": "advanced"}
  ],
  "interest_in_coding": True
}

print(json.dumps(biodata))
