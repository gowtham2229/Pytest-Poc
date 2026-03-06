import pytest
@pytest.mark.asyncio
async def test_create_task(client):
    payload = {"title": "Learn FastAPI", "description": "Understand async APIs"}

    response = await client.post("/tasks", json=payload)
    assert response.status_code == 200

    data = response.json()
    # Only status and message for create
    assert "status" in data
    assert "message" in data
    assert data["status"] == 1
    assert data["message"] == "Task created successfully"

# -------------------------------
# Test retrieving all tasks
# -------------------------------
@pytest.mark.asyncio
async def test_get_tasks(client):
    response = await client.get("/tasks")
    assert response.status_code == 200

    data = response.json()
    # Only status and message for get
    assert "status" in data
    assert "message" in data
    assert data["status"] == 1
    assert data["message"] == "Task retrieved successfully"

# -------------------------------
# Test updating a task
# -------------------------------
@pytest.mark.asyncio
async def test_update_task(client):
    # First, create a task
    payload = {"title": "Learn FastAPI", "description": "Understand async APIs"}
    create_response = await client.post("/tasks", json=payload)
    task_id = create_response.json().get("id")  # Optional: might be None if create doesn't return id

    # Update the task
    update_payload = {
        "task_id": task_id,
        "title": "Learn FastAPI - Updated",
        "description": "Understand async APIs in depth"
    }
    update_response = await client.put(f"/tasks/{task_id}", json=update_payload)
    assert update_response.status_code == 200

    updated_data = update_response.json()
    # For update, data field is present
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
    # Create a task to delete
    payload = {"title": "Learn FastAPI", "description": "Understand async APIs and Pytest"}
    create_response = await client.post("/tasks", json=payload)
    task_id = create_response.json().get("id")  # Optional: might be None

    # Delete the task
    delete_response = await client.delete(f"/tasks/{task_id}")
    assert delete_response.status_code == 200

    deleted_data = delete_response.json()
    # Only status and message for delete
    assert "status" in deleted_data
    assert "message" in deleted_data
    assert deleted_data["status"] == 1
    assert deleted_data["message"] == "Task deleted successfully"