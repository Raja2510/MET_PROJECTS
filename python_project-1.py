members={ 

}
project={
    "p1":{
        "name":"project",
        "start_date":"30-05",
        "end_date":"30-06",
        "priority":1,
        "task":{}
            
        }
    }


def create_project(project_id, name, start_date, end_date, priority):
    if project_id in project:
        return "this project already exsists"
    
    project.update({project_id:{"name":name,"start_date":start_date,"end_date":end_date,"priority":priority,"task":{}}})
    print("project added sucessfully")



def add_team_member(member_id, name, role, skill_set, hourly_rate) :
    if member_id in members:
        return "this member already exsist"
    members.update({member_id:{"name":name,"role":role,"skill_set":skill_set,"hourly_rate":hourly_rate}})





# a =input("1.add project :")
# if a == "yes":
#     pid=input("enter project name")
#     na=input("enter name")
#     sd=input("sarte date")
#     ed=input("enter end date")
#     prio=input("entrt prio")
#     create_project(pid,na,sd,ed,prio)
# print(project)

