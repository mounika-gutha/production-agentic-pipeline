import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'backend'))
from app import app
def test_home():
 r=app.test_client().get('/');assert r.status_code==200 and r.get_json()['status']=='running'
def test_health_route(): assert app.test_client().get('/health').status_code in (200,503)
def test_chat_requires_message(): assert app.test_client().post('/api/chat',json={}).status_code==400
