members={"m1":{"name":"raja",
               "role":"coding",
               "skill_set":"python",
               "hourly_rate":"6%",
               "assigned_tasks":[]}} 


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
 
def set_task_dependency(task_id,depends_on_task_id):
    if task_id not in task:
        return 'task not there'
    if depends_on_task_id not in task:
        return "task dependency on assigned"
    if task_id == depends_on_task_id:
        return 'a task cannot depend on itself'
    if depends_on_task_id not in task[task_id]['dependencies']:
        task[task_id]['dependencies'].append(depends_on_task_id)
        return task[task_id]
 










while True:
    print("""
    -------Task Manager -MENU----------------------------:
    Show projects.------------1
    Create a new project.-----2
    Add new member.-----------3
    Create a new task.--------4
    Exit----------------------5
    """)
    option=int(input("Enter number corresponding to the action you want to perfrom : "))

    if option==5:
        print("Closing Task Manager")
        break
    elif option==1:
        pid=input("Enter project name : ")
        na=input("Enter name : ")
        sd=input("Enter start Date : ")
        ed=input("Enter end Date : ")
        prio=input("Enter priority : ")
        create_project(pid,na,sd,ed,prio)
        print(project)
    elif option==2:
        m_id=input("Enter Member ID : ")
        m_name=input("Enter member name : ")
        m_rl=input("Enter role : ")
        m_ss=input("Enter Skill set : ")
        m_hr=input("Enter hourly rate : ")
        add_team_member(m_id,m_name,m_rl,m_ss,m_hr)
        print(members)
    elif option==3:
        t_id=input("Enter Task name : ")
        t_pid=input("Enter Project_id")
        t_tit=input("Enter Title")
        t_des=input("Enter description")
        t_eh=input("Estimated hours")
        create_task(t_id,t_pid,t_tit,t_des,t_eh)
        print(task)
       