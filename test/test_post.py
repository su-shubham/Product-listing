from .database import client,session
def test_app_main(client):
    response = client.get('/')
    assert response.json()=={"msg":"Hello world!!!"}

def test_topics(client):
    res = client.post('/topics/',json={
  "image_url": "hello",
  "topic_url": "hello",
  "name": "stringggg",
  "content": "string"
})
    assert res.json().get('name')=="stringggg"
    assert res.status_code==201
