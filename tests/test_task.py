import pytest


@pytest.mark.asyncio
async def test_create_task(client):

    payload = {
        "title": "Learn FastAPI",
        "description": "Understand async APIs"
    }

    response = await client.post("/tasks", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["description"] == payload["description"]

@pytest.mark.asyncio
async def test_get_tasks(client):

    response = await client.get("/tasks")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)

@pytest.mark.asyncio
async def test_update_task(client):
    # First, create a task to update
    payload = {
        "title": "Learn FastAPI",
        "description": "Understand async APIs"
    }
    create_response = await client.post("/tasks", json=payload)
    task_id = create_response.json()["id"]

    # Now, update the task
    update_payload = {
        "task_id": task_id,
        "title": "Learn FastAPI - Updated",
        "description": "Understand async APIs in depth"
    }
    update_response = await client.put(f"/tasks/{task_id}", json=update_payload)

    assert update_response.status_code == 200

    updated_data = update_response.json()

    assert updated_data["title"] == update_payload["title"]
    assert updated_data["description"] == update_payload["description"]

@pytest.mark.asyncio
async def test_delete_task(client): 
    # First, create a task to delete
    payload = {
        "title": "Learn FastAPI",
        "description": "Understand async APIs and Pytest"
    }
    create_response = await client.post("/tasks", json=payload)
    task_id = create_response.json()["id"]

    # Now, delete the task
    delete_response = await client.delete(f"/tasks/{task_id}")

    assert delete_response.status_code == 200

    # Verify the task is deleted
    get_response = await client.get("/tasks")
    tasks = get_response.json()
    assert all(task["id"] != task_id for task in tasks) # Ensure the deleted task is not in the list of tasks

