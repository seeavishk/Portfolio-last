import streamlit as st
import google.generativeai as genai

api_key = st.secrets["GOOGLE_API_KEYS"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

col1, col2 = st.columns(2)

with col1:
    st.subheader("Hi :fire:")
    st.title("I am Aviral Shukla")
    css = """
    <style>
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    .fade-in {
        animation: fadeIn 2s ease-in-out;
        color: #8a2be2; /* Purple color */
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; /* Cool font */
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3); /* Text shadow for cool effect */
    }
    </style>
    """

    # Display the CSS
    st.markdown(css, unsafe_allow_html=True)

    # Display animated and styled title
    st.markdown('<h1 class="fade-in">Welcome to my portfolio,'
                'if you wanted to know more about me then have a scroll:)</h1>',
                unsafe_allow_html=True)

with col2:
    st.image("images/WhatsApp Image 2024-01-31 at 09.44.11_b97d0588.jpg")

st.title(" ")

persona = """
You are Aviral Shukla AI bot. You help people answer questions about yourself (i.e., Aviral Shukla).
Answer as if you are responding. Don't answer in second or third person.
If you don't know the answer, you simply say "That's a secret".
Here is more info about Aviral Shukla:

Aviral Shukla resides in Lucknow, Uttar Pradesh. You can reach him via email at avishkshukla@gmail.com.
He is currently pursuing his Bachelor of Technology in Computer Science and Engineering from APJ Abdul Kalam Technical University, Lucknow, Uttar Pradesh.
Aviral has demonstrated strong academic performance with a current SGPA of 8.5.
His educational background includes MG Convent School, where he achieved 91.8% in Class 12th and 95.7% in Class 10th.

Work Experience:
- Full Stack Developer Intern at Zidio Development, Lucknow, Uttar Pradesh (Jan 2021 – Oct 2021)
  - Developed and deployed three large-scale projects using the MERN stack.
  - Collaborated with a team of six members to ensure successful project completion.

- Operational Intern at Teleperformance, Lucknow, Uttar Pradesh (May 2019 – Aug 2019)
  - Utilized operational management skills across different domains within the organization.

- Freelance Tutor at Filo Tutor (Remote) (Jan 2021 – Oct 2021)
  - Tutored students online for Physics, Maths, and Computer Science subjects.
  - Designed personalized study plans based on students’ strengths and weaknesses.

Skills:
- Data Structure and Algorithms with C++
- Web Development: HTML, CSS, JavaScript
- Computer Vision and Machine Learning with Python (OpenCV)
- SEO Optimization
- MERN Stack: MongoDB, Express.js, React, Node.js

Projects:
- Let’s Buy - An E-Commerce Platform (HTML, CSS, JavaScript, Node.js, MongoDB)
- GetHired - Job Searching Portal (Node.js, MongoDB)

Achievements & Awards:
- 23rd rank in Pitchstorm Startup among 500 teams at an event organized by Ramanujan College, Delhi University.
- Completed nearly 500 coding questions focusing on Data Structures and Algorithms on platforms like LeetCode, GeeksforGeeks, and CodingStudios.
- Created over 100 frontend projects and 50 MERN stack projects, all fully functional and deployed.

Interests:
- Blogging: Writing blogs on finance and self-help.
- Financial Analysis
- Book Writing: Authored a personal book named "TheMatman" (E-book on Amazon).

Connect with Aviral Shukla:
- GitHub: github.com/seeavishk
- LinkedIn: linkedin.com/in/seeavishk
- LeetCode: leetcode.com/yourusername
"""

st.title("Aviral's AI Bot")

user_question = st.text_input("Ask anything about me")
if st.button("ASK", use_container_width=400):
    prompt = persona + "Here is the question that the user asked: " + user_question
    response = model.generate_content(prompt)
    st.write(response.text)

st.title(" ")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Coder")
    st.write("- Developer (MERN stack)")
    st.write("- 500+ coding questions")
    st.write("- 50+ frontend projects")
    st.write("- 50+ MERN projects")
    st.write("- Competitive coding on platforms")

with col2:
    st.markdown(f"""
           <style>
           .image-container {{
               text-align: right;  /* Aligns the image to the right */
               margin-right: 20px;  /* Adds right margin to the image */
           }}
           .image-container img {{
               width: 300px;  /* Adjust image width as needed */
           }}
           </style>

           <div class="image-container">
               <a href="https://www.linkedin.com/build-relation/newsletter-follow?entityUrn=7191518770056593408">
                   <img src="https://cdn.pixabay.com/photo/2017/03/07/09/14/newsletter-2123474_640.jpg" alt="Newsletter">
               </a>
           </div>
       """, unsafe_allow_html=True)
st.title(" ")

st.title("My Leetcode")
st.image("images/leetcode.png")

st.write(" ")
st.title("My Skills")
st.slider("Programming", 0, 100, 70)
st.slider("Teaching", 0, 100, 85)
st.slider("Problem solving", 0, 100, 90)
st.slider("Full stack development", 0, 100, 80)
st.slider("Wordpress devlopment", 0, 100, 85)
st.slider("Computer vision", 0, 100, 75)

st.write(" ")
st.title("Gallery (Projects)")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/Screenshot 2024-06-30 122035.png")
    st.image("images/Screenshot 2024-06-30 122635.png")
    st.image("images/Screenshot 2024-07-04 180238.png")
    st.image("images/Screenshot 2024-07-14 022329.png")


with col2:
    st.image("images/Screenshot 2024-07-04 180250.png")
    st.image("images/Screenshot 2024-07-14 022103.png")
    st.image("images/Screenshot 2024-07-14 022129.png")

with col3:
    st.image("images/Screenshot 2024-07-14 022156.png")
    st.image("images/Screenshot 2024-07-14 022226.png")
    st.image("images/Screenshot 2024-07-14 022310.png")


st.subheader(" ")
st.write("CONTACT")
st.title("For any inquiries, email at:")
st.subheader("avishkshukla@gmail.comm")
st.markdown("""
    <div style="margin-top: 10px;">
        <a href="https://github.com/seeavishk" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/128/15452/15452650.png" alt="GitHub" style="width: 40px; margin-right: 10px;">
        </a>
        <a href="https://linkedin.com/in/seeavishk" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/128/4494/4494497.png" alt="LinkedIn" style="width: 40px; margin-right: 10px;">
        </a>
        <a href="https://leetcode.com/yourusername" target="_blank">
            <img src="https://cdn.iconscout.com/icon/free/png-512/free-leetcode-3521542-2944960.png?f=webp&w=256" alt="LeetCode" style="width: 40px;">
        </a>
    </div>
""", unsafe_allow_html=True)