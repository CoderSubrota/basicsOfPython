employees =[
    {"name":"Subrota Chandra", "age":23, "education":"Diploma IT", "profession":"Web developer"},
     {"name":"Bijoy Chandra", "age":20, "education":"BBE", "profession":"Architect"},
     {"name":"Binoy Chandra", "age":22, "education":"CSE", "profession":"Web developer"},
     {"name":"Surjo Chandra", "age":20, "education":"EEE", "profession":"Web developer"},
     {"name":"Turjo Chandra", "age":21, "education":"MBBS", "profession":"Surgeon specialist"},
     {"name":"Dhorjo Chandra", "age":23, "education":"FCBS", "profession":"Doctor"},
     {"name":"Kala Can", "age":23, "education":"BBA", "profession":"Teacher"},
     {"name":"Dhola Patra", "age":23, "education":"BSC", "profession":"Teacher"},
     {"name":"Sakib Hossen", "age":22, "education":"BBE", "profession":"Architect"},
     {"name":"Rakib Hossen", "age":24, "education":"CSE", "profession":"Web developer"},
    
]
print(f"{'Name : ':<25} {'Age : ':<8} {'Education : ':<20} {'Profession : ':<20}")
print("="*78)

for item in employees:
    print(f"{item['name']:<25} {item['age']:<8}  {item['education']:<20}  {item['profession']:<20}")
    
