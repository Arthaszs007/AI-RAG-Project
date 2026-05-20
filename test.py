from back.services import chat_service

chat_service.add_message(user_id="100011", role="user", content="43534534")

res = chat_service.read_messages("100011")

print(res)
