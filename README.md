# django-backend-youtube

### (1) 모델 구조
1. User (Custom)
- email
- password
- nickname
- is_business(boolean): personal, business

2. Video
- title
- link
- description
- category
- views_count
- thumbnail
- video_uploaded_url (S3)
- video_file(FileField)
- User:FK

3. Reaction
- User:FK
- Video:FK
- reaction

4. Comment
- User:FK
- Video:FK
- like
- dislike
- content

5. Subcription (채널 구독)
- User:FK => subscriber (구독한) -> 내가 구독한 사람
- User:FK => subscribed_to (구독을 당한) -> 나를 구독한 사람

6. Notification

- User:FK
- message
- is_read

7. Common

- created_at
- updated_at

8. Chatting (예정)
- User:FK (nickname)

* 만들어야 하는 테이블(모델)
- users, videos, reactions, comments, subscriptions, common
