import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Genetic Algorithm")
st.header("Student Survey")

# Load CSV from GitHub
url = "https://raw.githubusercontent.com/wannurizzatiwanabdazizktb-arch/EC2024/refs/heads/main/arts_faculty_data.csv"

try:
    arts_df = pd.read_csv(url)
    st.dataframe(arts_df.head())
except Exception as e:
    st.error(f"An error occurred while reading the CSV file: {e}")

# Pie chart: Arts Program distribution
program_counts = arts_df['Arts Program'].value_counts().reset_index()
program_counts.columns = ['Arts Program', 'Count']

fig = px.pie(program_counts, names='Arts Program', values='Count',
             title='Arts Program Distribution',
             color_discrete_sequence=px.colors.qualitative.Pastel)
st.plotly_chart(fig)

print("The most popular arts program among the surveyed students is B.A. in English, representing 77.5% of the 89 students. Additionally, 2 students did not specify their program during this survey.")

# Grouped bar chart: Bachelor Academic Year by Gender
fig = px.histogram(
    data_frame=arts_df,
    x='Bachelor  Academic Year in EU',  # exact column name
    color='Gender',
    barmode='group',
    title='Bachelor Academic Year by Gender',
    text_auto=True,
    color_discrete_sequence=px.colors.qualitative.Set2
)
st.plotly_chart(fig)

print("Most of the bachelor students participating in this survey are second-year students, with a total of 31 students, and the group is predominantly female.")

# Grouped bar chart: Masters Academic Year by Gender
fig = px.histogram(
    data_frame=arts_df,
    x='Masters Academic Year in EU',  # exact column name
    color='Gender',
    barmode='group',
    title='Masters Academic Year by Gender',
    text_auto=True,
    color_discrete_sequence=px.colors.qualitative.Set2
)
st.plotly_chart(fig)

print("Most of the master’s students participating in this survey are first-year students, while there is only one student in the second year.")

# Line plot: Students with GPA > 3.7
semesters = [
    '1st Year Semester 1','1st Year Semester 2','1st Year Semester 3',
    '2nd Year Semester 1','2nd Year Semester 2','2nd Year Semester 3',
    '3rd Year Semester 1','3rd Year Semester 2','3rd Year Semester 3'
]

above_37_counts = [(arts_df[sem] > 3.7).sum() for sem in semesters]
plot_df = pd.DataFrame({'Semester': semesters, 'Students Above 3.7': above_37_counts})

fig = px.line(plot_df, x='Semester', y='Students Above 3.7',
              title='Number of Students with GPA > 3.7 per Semester',
              markers=True)
fig.update_layout(xaxis_title='Semester', yaxis_title='Number of Students')
st.plotly_chart(fig)

# Line plot: Students with GPA < 2.5
below_25_counts = [(arts_df[sem] < 2.5).sum() for sem in semesters]
plot_df = pd.DataFrame({'Semester': semesters, 'Students Below 2.5': below_25_counts})

fig = px.line(plot_df, x='Semester', y='Students Below 2.5',
              title='Number of Students with GPA < 2.5 per Semester',
              markers=True)
fig.update_layout(xaxis_title='Semester', yaxis_title='Number of Students')
st.plotly_chart(fig)
