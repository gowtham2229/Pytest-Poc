import pytest


@pytest.mark.asyncio
async def test_create_task(client):
    payload = {"title": "Learn FastAPI", "description": "Understand async APIs"}

    response = await client.post("/create_tasks", json=payload)
    assert response.status_code == 200 # Check for 200 OK

    data = response.json()
    assert "status" in data
    assert "message" in data
    assert data["status"] == 1
    assert data["message"] == "Task created successfully"

# -------------------------------
# Test retrieving all tasks
# -------------------------------
@pytest.mark.asyncio
async def test_get_tasks(client):
    response = await client.get("/get_tasks")
    assert response.status_code == 200

    data = response.json()
    assert "status" in data
    assert "message" in data
    assert "data" in data
    assert data["status"] == 1
    assert data["message"] == "Task retrieved successfully"
    assert isinstance(data["data"], list)

# -------------------------------
# Test updating a task
# -------------------------------
@pytest.mark.asyncio
async def test_update_task(client):
    # Create a task first
    payload = {"title": "Learn FastAPI", "description": "Understand async APIs"}
    await client.post("/create_tasks", json=payload)

    # Get the task ID from GET /get_tasks
    get_response = await client.get("/get_tasks")
    tasks = get_response.json().get("data", [])
    assert tasks, "No tasks found to update"
    task_id = tasks[0]["id"]

    # Update the task
    update_payload = {
        "task_id": task_id,
        "title": "Learn FastAPI - Updated",
        "description": "Understand async APIs in depth"
    }
    update_response = await client.put("/update_task", json=update_payload)
    assert update_response.status_code == 200

    updated_data = update_response.json()
    assert "status" in updated_data
    assert "message" in updated_data
    assert "data" in updated_data
    assert updated_data["status"] == 1
    assert updated_data["message"] == "Task updated successfully"
    assert updated_data["data"]["title"] == update_payload["title"]
    assert updated_data["data"]["description"] == update_payload["description"]

# -------------------------------
# Test deleting a task
# -------------------------------
@pytest.mark.asyncio
async def test_delete_task(client):
    # Create a task first
    payload = {"title": "Learn FastAPI", "description": "Understand async APIs and Pytest"}
    await client.post("/create_tasks", json=payload)

    # Get the task ID from GET /get_tasks
    get_response = await client.get("/get_tasks")
    tasks = get_response.json().get("data", [])
    assert tasks, "No tasks found to delete"
    task_id = tasks[0]["id"]

    # Delete the task (send task_id in the body)
    delete_payload = {"task_id": task_id}
    delete_response = await client.request("DELETE", "/delete_tasks", json=delete_payload)
    assert delete_response.status_code == 200

    deleted_data = delete_response.json()
    assert "status" in deleted_data
    assert "message" in deleted_data
    assert deleted_data["status"] == 1
    assert deleted_data["message"] == "Task deleted successfully"

    # Verify the task is gone
    verify_response = await client.get("/get_tasks")
    remaining_tasks = verify_response.json().get("data", [])
    assert all(task["id"] != task_id for task in remaining_tasks)