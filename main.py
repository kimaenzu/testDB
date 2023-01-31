import streamlit as st
from google.cloud import firestore

# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("finalpjt-14eb3-firebase-adminsdk-2rcyn-aaaadce745.json")

# Create a reference to the Google post.
doc_ref = db.collection("user0001").document("2023-01-30")

# Then get the data at that reference.
doc = doc_ref.get()

# Let's see what we got!
st.write("The id is: ", doc.id)
st.write("The contents are: ", doc.to_dict())

## Reading ALL posts
# Now let's make a reference to ALL of the posts
posts_ref = db.collection("posts")

# For a reference to a collection, we use .stream() instead of .get()
for doc in posts_ref.stream():
	st.write("The id is: ", doc.id)
	st.write("The contents are: ", doc.to_dict())
###############################
# Streamlit widgets to let a user create a new post
title = st.text_input("일기 작성 칸")
url = st.text_input("감정 입력 칸")
submit = st.button("완료")

# Once the user has submitted, upload it to the database
if title and url and submit:
	doc_ref = db.collection("user0001").document("2023-01-31")
	doc_ref.set({
		"title": title,
		"url": url
	})

# And then render each post, using some light Markdown
posts_ref = db.collection("user0001")
for doc in posts_ref.stream():
	post = doc.to_dict()
	title = post["title"]
	url = post["url"]

	st.subheader(f"Post: {title}")
	st.write(f":link: [{url}]({url})")