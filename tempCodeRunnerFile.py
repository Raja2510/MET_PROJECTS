members={"m1":{"name":"raja",
               "role":"coding",
               "skill_set":"python",
               "hourly_rate":"6%",
               "assigned_tasks":[],
               "log":[]}} 


project={
    "p1":{
        "name":"project",
        "start_date":"30-05",
        "end_date":"30-06",
        "priority":1,
        "status":"active"
            
        }
    }

task={"t1":{"title":"task-1",
                      "description":"complete task",
                      "estimates_hours":"10 hours",
                      "project_id":"p1",
                      "dependencies":[]}
}


##----adding project---------------------
def create_project(project_id, name, start_date, end_date, priority):
    if project_id in project:
        return "this project already exsists"
    
    project.update({project_id:{"name":name,"start_date":start_date,"end_date":end_date,"priority":priority,"task":{}}})
    print("project added sucessfully")


##----adding members---------------------

def add_team_member(member_id, name, role, skill_set, hourly_rate) :
    if member_id in members:
        return "this member already exsist"
    members.update({member_id:{"name":name,"role":role,"skill_set":skill_set,"hourly_rate":hourly_rate}})





def create_task(task_id, project_id, title, description, estimated_hours) :
    if task_id in task:
        return "this task already exist" 
    task.update({task_id:{"title":title,"description":description,"estimated_hours":estimated_hours,"project_id":project_id}})




def assign_task(task_id,members_id,priority_level):
    assign = {'task_id':task_id,'members_id':members_id,'priority_level':priority_level}
    members[members_id]["assigned_tasks"].append(assign)
    return 'task assigned'
assign_task("t1","m1",0)
print(members["m1"]["assigned_tasks"])