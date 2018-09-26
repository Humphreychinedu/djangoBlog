
'''
curl -X POST -d "username=humphrey&password=Oracle123*" http://127.0.0.1:8000/api/auth/token/

token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Imh1bXBocmV5IiwiZXhwIjoxNTE0NDA2MDYzLCJlbWFpbCI6IiJ9.FwhVihARNeyAWo-kcWHYuPvebAToT6WWRmFaRMfEssA"}
#token2 eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Imh1bXBocmV5IiwiZXhwIjoxNTE0NDA3MTU5LCJlbWFpbCI6IiJ9.yqpfn5d63GpJAe5xXNTGVnoDyZRDwkNkBSPT5QxWVDo"}



curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Imh1bXBocmV5IiwiZXhwIjoxNTE0NDA3MTU5LCJlbWFpbCI6IiJ9.yqpfn5d63GpJAe5xXNTGVnoDyZRDwkNkBSPT5QxWVDo"  http://127.0.0.1:8000/api/comments/

curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Imh1bXBocmV5IiwiZXhwIjoxNTE0NDA3MTU5LCJlbWFpbCI6IiJ9.yqpfn5d63GpJAe5xXNTGVnoDyZRDwkNkBSPT5QxWVDo" -X POST -H "Content-Type: application/json" -d '{"content": "another try"}' http://127.0.0.1:8000/api/comments/create/?type=post&slug=new-content
curl http://127.0.0.1:8000/api/comments/


'''