from schemas import create_task , get_task , update_task , delete_task , get_task_by_id
from model_states import TaskCreate , TaskUpdate , GetTask , GetDeleteTask
from fastapi import HTTPException


async def create_task_service(task , db):
    try :
        new_task = await create_task(task , db)
        if not new_task:
           return{
            'status':0,
            'message':'Failed to create task'
        }
        return{
        'status':1,
        'message':'Task created successfully',
    }
    except Exception as e:
          raise HTTPException(status_code=500, detail=str(e)) 
    
async def get_task_service(db):
    try:
        res = await get_task(db)
        if not res:
           return{
            'status':0,
            'message':'Task not found'
        }
        return{
        'status':1,
        'message':'Task retrieved successfully',
        "data": [task.__dict__ for task in res]
    }
    except Exception as e:
          raise HTTPException(status_code=500, detail=str(e))

async def update_task_service(task , db):
    try:
        res = await update_task(task , db)
        if not res:
           return{
            'status':0,
            'message':'Task not found'
        }
        return{
        'status':1,
        'message':'Task updated successfully',
        'data':res
    }
    except Exception as e:
          raise HTTPException(status_code=500, detail=str(e))

async def delete_task_service(task , db):
    try:
        res = await delete_task(task , db)
        if not res:
           return{
            'status':0,
            'message':'Task not found'
        }
        return{
        'status':1,
        'message':'Task deleted successfully',
    }
    except Exception as e:
          raise HTTPException(status_code=500, detail=str(e))

    
async def get_task_by_id_service(task , db):
    try : 
        res = await get_task_by_id(task , db)
        if not res:
           return{
            'status':0,
            'message':'Task not found'
        }
        return{
        'status':1,
        'message':'Task retrieved successfully',
        "data": res.__dict__
    }
    except Exception as e:
          raise HTTPException(status_code=500, detail=str(e))
    