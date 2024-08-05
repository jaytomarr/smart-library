import streamlit as st
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import random

# Define the dataset
categories = [
    "Artificial Intelligence", "Cybersecurity", "Blockchain",
    "IoT", "Electronic Systems", "DSA"
]

subcategories = {
    "Artificial Intelligence": ["Machine Learning", "Deep Learning", "Data Science"],
    "Cybersecurity": ["Cybersecurity Architecture", "Cloud Security", "Encryption"],
    "Blockchain": ["Blockchain Architecture", "Blockchain Law", "Cryptocurrency"],
    "IoT": ["IoT Security", "IoT Protocols", "Industrial IoT"],
    "Electronic Systems": ["Embedded Systems", "Integrated circuits", "VLSI"],
    "DSA": ["Data Structures", "Graphs", "Algorithms"]
}

purposes = ["Theoretical", "Practical", "Exam Preparation"]

# Map categories, subcategories, and purposes to numerical values
category_mapping = {category: idx for idx, category in enumerate(categories)}
subcategory_mapping = {category: {subcat: idx for idx, subcat in enumerate(subcats)} for category, subcats in subcategories.items()}
purpose_mapping = {purpose: idx for idx, purpose in enumerate(purposes)}

# Define the dataset
X = []
y = []

for category in categories:
    for subcategory in subcategories[category]:
        for purpose in purposes:
            X.append([category_mapping[category], subcategory_mapping[category][subcategory], purpose_mapping[purpose]])
            y.append(category + " - " + subcategory + " - " + purpose)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the decision tree classifier
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

def get_recommendation(category, subcategory, purpose):
    category_idx = category_mapping.get(category)
    subcategory_idx = subcategory_mapping.get(category, {}).get(subcategory)
    purpose_idx = purpose_mapping.get(purpose)

    if category_idx is None or subcategory_idx is None or purpose_idx is None:
        return "Invalid input."

    prediction = model.predict([[category_idx, subcategory_idx, purpose_idx]])
    return random.choice(prediction)

def main():
    st.title("Book Recommendation")
    # st.write("The book you need !!")

    category = st.selectbox("Select Category", categories)
    subcategory = st.selectbox("Select Subcategory", subcategories[category])
    purpose = st.selectbox("Select Purpose", purposes)

    if st.button("Get Recommendation"):
        recommendation = get_recommendation(category, subcategory, purpose)
        st.success(f"Based on your inputs, here is a book recommendation for you: {recommendation}")

if __name__ == "__main__":
    main()

