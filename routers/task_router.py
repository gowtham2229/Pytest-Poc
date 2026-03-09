from utilities import get_db , AsyncSession 
from config import Task
from model_states import TaskCreate , TaskUpdate , GetTask , GetDeleteTask
from services import create_task_service , get_task_service , update_task_service , delete_task_service , get_task_by_id_service
from fastapi import APIRouter , Depends
from fastapi import FastAPI

router = APIRouter()



@router.post("/create_tasks")
async def create_task_route(task:TaskCreate , db:AsyncSession = Depends(get_db)):
    try:
        return await create_task_service(task , db)
    except Exception as e:
        raise e

@router.get("/get_tasks")
async def get_task_route( db:AsyncSession = Depends(get_db)):
    try:
        return await get_task_service(db)
    except Exception as e:
        raise e
    
@router.put("/update_task")
async def update_task_route(task: TaskUpdate , db:AsyncSession = Depends(get_db)):
    try:
        return await update_task_service(task , db)
    except Exception as e:
        raise e

@router.delete("/delete_tasks")
async def delete_task_route(task: GetDeleteTask , db:AsyncSession = Depends(get_db)):
    try:
        return await delete_task_service(task , db)
    except Exception as e:
        raise e


@router.post("/get_task_by_id")
async def get_task_by_id_route(task: GetTask , db:AsyncSession = Depends(get_db)):
    try:
        return await get_task_by_id_service(task , db)
    except Exception as e:
        raise e

 