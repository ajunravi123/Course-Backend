from fastapi.testclient import TestClient
from index import app

client = TestClient(app)

# Define test cases for each endpoint with possible test cases
def test_get_all_courses_sortby_name():
    response = client.get("/course?sort_by=name")
    assert response.status_code == 200
    response_json = response.json()
    assert isinstance(response_json, list)
    assert len(response_json) > 0
    name = ""
    for i in response_json:
        name = i.get('name') if name == "" else name
        assert i.get("name") >= name
        name = i.get("name")

def test_get_all_courses_sortby_date():
    response = client.get("/course?sort_by=date")
    assert response.status_code == 200
    response_json = response.json()
    assert isinstance(response_json, list)
    assert len(response_json) > 0
    date = ""
    for i in response_json:
        date = i.get('date') if date == "" else date
        assert i.get("date") <= date
        date = i.get("date")
        
def test_get_all_courses_sortby_rating():
    response = client.get("/course?sort_by=rating")
    assert response.status_code == 200
    response_json = response.json()
    assert isinstance(response_json, list)
    assert len(response_json) > 0
    overall_rating = 0
    for i in response_json:
        overall_rating = i.get('overall_rating') if overall_rating == 0 else overall_rating
        assert i.get("overall_rating") <= overall_rating
        overall_rating = i.get("overall_rating")

def test_get_all_courses_filterby_domain():
    #Positive Scenario
    test_domain = "artificial intelligence"
    response = client.get(f"/course?domain={test_domain}")
    assert response.status_code == 200
    response_json = response.json()
    for i in response_json:
        domains = i["domain"]
        assert test_domain in domains

    #Negative Scenario
    test_domain = "None-Existing-Domain"
    response = client.get(f"/course?domain={test_domain}")
    assert response.status_code == 200
    response_json = response.json()
    for i in response_json:
        domains = i["domain"]
        assert test_domain not in domains

#----------------------------------------------------------------

def test_get_chapters_by_filters():
    #Filter by chapter name
    test_name = "CS50 2021 in HDR - Lecture 0 - Scratch"
    response = client.get(f"/chapter?name={test_name}")
    assert response.status_code == 200
    response_json = response.json()
    for i in response_json:
        assert test_name == i["name"]

    #Filter by chapter id
    test_id = "646b09f29362892e1995adaf"
    response = client.get(f"/chapter?id={test_id}")
    assert response.status_code == 200
    response_json = response.json()
    for i in response_json:
        assert test_id == i["id"]

    #Filter by course id
    test_course_id = "646b09f29362892e1995add0"
    response = client.get(f"/chapter?course_id={test_course_id}")
    assert response.status_code == 200
    response_json = response.json()
    for i in response_json:
        assert test_course_id == i["course_id"]

#----------------------------------------------------------------

def test_get_chapeter_path_api():
    #Get chapter by chapter id
    test_id = "646b09f29362892e1995adaf"
    response = client.get(f"/chapter/{test_id}")
    assert response.status_code == 200
    response_json = response.json()
    assert test_id == response_json["id"]

#----------------------------------------------------------------

def test_get_course_path_api():
    response = client.get("/course/646b09f29362892e1995adbe")
    assert response.status_code == 200
    assert response.json() == {
        "_id": "646b09f29362892e1995adbe",
        "name": "Computer Vision Course",
        "date": "2017-08-10T21:00:00",
        "description": "Computer Vision has become ubiquitous in our society, with applications in search, image understanding, apps, mapping, medicine, drones, and self-driving cars. Core to many of these applications are visual recognition tasks such as image classification, localization and detection. Recent developments in neural network (aka “deep learning”) approaches have greatly advanced the performance of these state-of-the-art visual recognition systems. This lecture collection is a deep dive into details of the deep learning architectures with a focus on learning end-to-end models for these tasks, particularly image classification. From this course, students will learn to implement, train and debug their own neural networks and gain a detailed understanding of cutting-edge research in computer vision.\n",
        "domain": [
            "computer vision",
            "artificial intelligence"
        ],
        "overall_rating": 0,
        "total_chapters": 17
    }
    #Schema validation also can be added here

#----------------------------------------------------------------

def test_post_rating_api():
    chapter_id = "646b09f29362892e1995adaf"
    response = client.post(f"/rating/chapter/{chapter_id}", json={"user": "user-1", "point" : 4})
    assert response.status_code == 200
    assert response.json() == {"success" : "Rating details updated into the system"}


#----------------------------------------------------------------

# Run all the defined test cases
def run_tests():
    test_get_all_courses_sortby_name()
    test_get_all_courses_sortby_date()
    test_get_all_courses_sortby_rating()
    test_get_all_courses_filterby_domain()
    test_get_chapters_by_filters()
    test_get_chapeter_path_api()
    test_get_course_path_api()
    test_post_rating_api()


# Run the tests
if __name__ == "__main__":
    run_tests()
