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
                      "estimated_hours":10 ,
                      "remaining_hours":10 ,
                      "project_id":"p1",
                      "dependencies":[]}
}


##----adding project---------------------
def create_project(project_id, name, start_date, end_date, priority):
    if project_id in project:
        return "this project already exsists"
    
    project.update({project_id:{"name":name,"start_date":start_date,"end_date":end_date,"priority":priority,"task":{}}})
    print("project added sucessfully")


def update_project(project_id, name, start_date, end_date, priority):
    project.update({project_id:{"name":name,"start_date":start_date,"end_date":end_date,"priority":priority,"task":{}}})
    print("project updated sucessfully")


##----adding members---------------------------------

def add_team_member(member_id, name, role, skill_set, hourly_rate) :
    if member_id in members:
        return "this member already exsist"
    members.update({member_id:{"name":name,"role":role,"skill_set":skill_set,"hourly_rate":hourly_rate}})
def update_member(member_id, name, role, skill_set, hourly_rate) :
    members.update({member_id:{"name":name,"role":role,"skill_set":skill_set,"hourly_rate":hourly_rate}})
    print("member updated sucessfully")



##-------------tasks--------------------
def create_task(task_id, project_id, title, description, estimated_hours) :
    if task_id in task:
        return "this task already exist" 
    task.update({task_id:{"title":title,"description":description,"estimated_hours":estimated_hours,"remaining_hours":estimated_hours,"project_id":project_id}})

def assign_task(task_id,members_id,priority_level):
    assign = {'task_id':task_id,'priority_level':priority_level}
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
 
def log_time(member_id, task_id, hours_worked, date=0):
    if member_id not in members:
        return "'MEMBER ID' is not registered."
    if task_id not in task:
        return "'TASK ID' is not registered. "
 
    task[task_id]["remaining_hours"]-=hours_worked
    return task[task_id]["remaining_hours"]   
 

 
 
 
def update_task_progress(task_id):
    estimated_time  = int(task[task_id]["estimated_hours"])
    remaining_time= int(task[task_id]["remaining_hours"])
    if task_id in  task:
        completed_time = (remaining_time/estimated_time)*100
        completion_percentage = 100-completed_time
        return completion_percentage





while True:
    print("""
    -------Task Manager -MENU----------------------------:
    Manage projects.------------1
    Manage member.--------------2
    Manage new task.------------3
    Exit------------------------4
    """)
    option=int(input("Enter number corresponding to the action you want to perfrom : "))
    if option==4:
        print("Closing Task Manager")
        break
    #project
    elif option==1:
        while True:
            print("""
    Add project---------------1
    Update a project----------2
    Delete project------------3
    show project--------------4
    back----------------------5
""")
            op=int(input("Enter number corresponding to the action you want to perfrom : "))
            if op==5:
                break 
            elif op==1:        
                pid=input("Enter project name : ") 
                na=input("Enter name : ")
                sd=input("Enter start Date : ")
                ed=input("Enter end Date : ")
                prio=input("Enter priority : ")
                create_project(pid,na,sd,ed,prio)
                print(project)
            elif op==2:
                Update_pro=input("enter project_id you want to update")
                if Update_pro not in project:
                    print("no project found to update")
                else:
                    
                    na=input("Enter new(updated) name : ")
                    sd=input("Enter new(updated) start Date : ")
                    ed=input("Enter new(updated) end Date : ")
                    prio=input("Enter new(updated) priority : ")
                    update_project(Update_pro,na,sd,ed,prio)
                    print(project)
            elif op==3:
                delete_pro=input("enter project_id you want to delete")
                if delete_pro in project:
                   print(f"project { project.pop(delete_pro)} is deleted")
                else:
                    print("there exsist no such proect")
            elif op==4:
                print("Current projects: ")
                for i in project:
                    print(i, project[i])
    #members
    elif option==2:
        while True:
            print("""
    Add a member---------------1
    Update a member------------2
    Delete a member------------3
    Show members---------------4
    assign_task----------------5
    Log time-------------------6
    Back-----------------------7
""")
            op=int(input("Enter number corresponding to the action you want to perform : "))
            if op==7:
                break 
            elif op==1:        
                m_id=input("Enter Member ID : ")
                m_name=input("Enter member name : ")
                m_rl=input("Enter role : ")
                m_ss=input("Enter Skill set : ")
                m_hr=input("Enter hourly rate : ")
                add_team_member(m_id,m_name,m_rl,m_ss,m_hr)
                print(members)
            elif op==2:
                m_id=input("Enter Member ID you want to update : ")
                if m_id not in members:
                    print("No member found to update")
                else:
                    m_name=input("Enter updated member name : ")
                    m_rl=input("Enter updated role : ")
                    m_ss=input("Enter updated Skill set : ")
                    m_hr=input("Enter updated hourly rate : ")
                    update_member(m_id,m_name,m_rl,m_ss,m_hr)
                    print(members)
            elif op==3:
                m_id=input("Enter Member ID you want to delete: ")
                if m_id in members:
                    print(f"Member {members.pop(m_id)} is deleted")
                else:
                    print("No such member exists")
            elif op==4:
                print("Current Members: ")
                for i in members:
                    print(i, members[i])
                    
            elif op==5:
                tid=input("enter the task id: ")
                mid=input("enter the member id to assign: ")
                pl=input("enter priority level: ")
                assign_task(tid,mid,pl)
            elif op==6:
                mid = input("Enter Member ID: ")
                tid = input("Enter Task ID: ")
                hours = int(input("Enter Hours Worked: "))
                remaining = log_time(mid, tid, hours)
                print(f"Remaining hours for task '{tid}': {remaining}")

    elif option==3:
        while True:
            print("""
    Add task-------------------1
    Update task----------------2
    Delete task----------------3
    Show tasks-----------------4
    Set Task Dependency--------5
    Task Progress--------------6
    Back-----------------------7
""")
            op=int(input("Enter number corresponding to the action you want to perform: "))
            if op==7:
                break
            elif op==1:
                t_id = input("Enter Task ID: ")
                p_id = input("Enter Project ID: ")
                title = input("Enter Task Title: ")
                desc = input("Enter Description: ")
                est_hours = input("Enter Estimated Hours: ")
                print(create_task(t_id, p_id, title, desc, est_hours))
                print(task)
            elif op==2:
                t_id = input("Enter Task ID to update: ")
                if t_id not in task:
                    print("No such task found")
                else:
                    p_id = input("Enter new Project ID: ")
                    title = input("Enter new Title: ")
                    desc = input("Enter new Description: ")
                    est_hours = input("Enter new Estimated Hours: ")
                    task[t_id].update({
                        "title": title,
                        "description": desc,
                        "estimated_hours": est_hours,
                        "project_id": p_id
                    })
                    print("Task updated successfully")
                    print(task)
            elif op==3:
                t_id = input("Enter Task ID to delete: ")
                if t_id in task:
                    print(f"Task {task.pop(t_id)} is deleted")
                else:
                    print("No such task exists")
            elif op==4:
                print("All Tasks:")
                for i in task:
                    print(i)
            elif op==5:
                t_id = input("Enter Task ID to set dependency for: ")
                dep_id = input("Enter the Task ID it depends on: ")
                result = set_task_dependency(t_id, dep_id)
                print(result)
            elif op==6:
                t_id = input("Enter Task ID to update progress: ")
                if t_id in task:
                    print(f"{update_task_progress(t_id)} % is complete")
                else:
                    print("Task not found.")


