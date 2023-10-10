from user import User
from post import Post

app_user_one = User("ss@gmail.com", "Selcan ATAK", "pwd", "Software Engineer")
app_user_one.get_user_info()

app_user_two = User("kk@kk.com", "Demet ATAK", "pwd", "Software Engineer")
app_user_two.get_user_info()

new_post = Post("on a secret mission today", app_user_two)
new_post.get_post_info()
