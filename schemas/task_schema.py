from model_states import TaskCreate , TaskUpdate , TaskResponse , TaskUpdateResponse
from config import Task
from sqlalchemy.future import select


async def create_task(task , db):
    try:

        new_task = Task(**task.model_dump())
        db.add(new_task)
    
        await db.commit()
    
        await db.refresh(new_task)
        return new_task
    except Exception as e:
        await db.rollback()
        raise e

async def get_task(db):
    try:

        task = await db.execute(select(Task))
        res = task.scalars().all()
    
        return res
    except Exception as e:
        await db.rollback()
        raise e


async def update_task(task , db):
    try:

        task_to_update = await db.execute(select(Task).where(Task.id == task.task_id))
        res = task_to_update.scalars().first()
        if res:
          res.title = task.title
          res.description = task.description
        
          await db.commit()
          await db.refresh(res)
        return res
    except Exception as e:
        await db.rollback()
        raise e

async def delete_task(task , db):
    try:

      task_to_delete = await db.execute(select(Task).where(Task.id == task.task_id))
      res = task_to_delete.scalars().first()
      if res:
         await db.delete(res)
         await db.commit()
      return True
    except Exception as e:
        await db.rollback()
        raise e
    
async def get_task_by_id(task , db):
    try :
        task_by_id = await db.execute(select(Task).where(Task.id == task.task_id))
        res = task_by_id.scalars().first()
        return res
    except Exception as e:
        raise e
    


