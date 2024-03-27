import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from datetime import datetime
import pytz
import webbrowser

def send_message(event=None):
    user_input = user_entry.get()
    if user_input.strip() == "":
        return
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, "You: " + user_input + "\n")
    chat_window.config(state=tk.DISABLED)
    user_entry.delete(0, tk.END)

    if "date" in user_input.lower() or "day" in user_input.lower():
        response = "Chatbot: Today's date is " + datetime.now().strftime("%d/%m/%Y") + "."
    elif "courses" in user_input.lower():
        response = "VCET bot: VCET offers a variety of courses in engineering and technology\nThe courses offered by VCET are:\n1. Computer Science and Engineering\n2. Data Science\n3. Artificial Intelligence and Machine Learning\n4. Mechanical Engineering\n5. Electronics and Communication Engineering\n6. Civil Engineering\n7. Master of Business Administration\n8. Master of Computer Application.\n"
    elif "time" in user_input.lower():
        tz = pytz.timezone('Asia/Kolkata')
        response = "VCET bot: The current time in VCET Puttur is " + datetime.now(tz).strftime("%I:%M %p") + "."
    elif "library" in user_input.lower() or "book" in user_input.lower():
        response = "The library of Vivekananda College of Engineering & Technology is a storehouse of knowledge. It is housed in a spacious new building called Krishna Chetana on the ground floor1. The library has a floor area of 877 square meters1 and is segregated into various sections like Lending, Reference, Digital library, Newspaper, Periodicals, Reading room, etc1.\n\nThe library’s collection is about 47237 volumes with 6596 titles on Engineering, Management, and Humanities1. It contains Abstracts, Directories, Yearbooks, Biographical sources, Textbooks, Thesis, Dissertations, Encyclopedias, and General books1. The library subscribes to 66 technical print journals and more than 29000 e-books1.\n\nThe digital library has 12 systems with high-speed internet facility1. The digital Library is exclusively used for the online access of e-Journals, e-books, conference proceedings, articles, educational videos, and e-resources1.\n\nThe library has subscribed to online e-journals and e-books from various publishers through a member of VTU Consortium1. Some of the e-resources include Elsevier Science Direct, Taylor & Francis (T&F), Springer Nature, Emerald Management, and more1.\n\nThe library can accommodate 200 students at a time and is enabled with Wi-Fi technology1. It has membership with VTU Consortium, DELNET, NDL\nwebsite: [VCET Library](https://vcetputtur.ac.in/facilities/library"
    elif "play" in  user_input.lower() or "sport" in user_input.lower() or "physical" in user_input.lower():
        response = "HOD:- Mr. Balachandra Gowda B Physical Education Director\nDepartment: Physical Education B.A, B.P.Ed, M.P.Ed\n\nOverall Champions in 23rd VTU Intercollegiate Athletic Meet 2021-22\nDuring the 23rd Intercollegiate Athletic Meet 2021-22, organized by Visvesvaraya Technological University held at SJCIT Chikkaballapur, our students are created a history of 6 new meet records. We are proud to announce that our students also bagged 13 Gold Medals, 2 Silver Medals and 4 Bronze Medals.\nThe VCET teams have a great history of glory by winning numerous trophies and making the college proud2. They have participated and won at various levels, including National Level, State Level, and University Level\n\nThe concept of physical education is generally understood as organisation of some games, sports or physical education activities. For the last 5 years our students are performing very well in physical education activities. Many students have represented VTU at All India Inter University Athletics, Swimming and Kabaddi tournaments. One of our students was also selected for All India Inter-University Khelo India Swimming Championship by VTU. We give training to the students during morning and evening sessions. To promote the sports, our management provides the best facility and financial support to the sports students."
    elif "job" in  user_input.lower() or "placement" in user_input.lower() or "work" in user_input.lower() or "company" in user_input.lower():
        response = "VCET bot:The Training & Placement Department at Vivekananda College of Engineering & Technology (VCET), Puttur, monitors the employment opportunities and arranges campus interviews for the final year students1. It is designed to function with a high degree of professionalism1. The department provides almost instantaneous data to the corporate sector with regard to the candidates available for consideration towards placement in accordance with the preserved requirements1. The team interacts with reputed organizations all over the country for arranging campus interviews for the final year students1. They make efforts to organize technical seminars, workshops, and corporate expectation sessions1. Industry personnel are invited periodically to enrich the knowledge of the student community with the latest technological innovations and industry practices1.\nThe department's campus recruitment program starts at the commencement of the 7th semester and keeps continuing till the end of the academic year1. Students are also given an opportunity to participate in Off-Campus drives\n1. The department has seen aggressive hiring from top-notch companies at VCET, Puttur1. A record high of 350 campus placement offers were awarded to students from various branches of both Under Graduate and Post Graduate streams from Engineering and MBA1. An average of 75+ companies visit the campus, plus students get an addition of 30 off-campus and pool opportunities for recruitment with the prominent ones being Indian Navy, Infosys, Wipro, TCS, SAP, Mercedes Benz, Bosch, Robosoft, Global delight, Mphasis, ACC Ltd, Indian Oil Sky Tanking, Indo Mim, Dilip Buildcon, Global Edge, 99Games, and Cadence to name a few\nFor more detailed information about the Training & Placement Department at VCET, you can visit their official website:\nhttps://vcetputtur.ac.in/departments/training-and-placement-department"
    elif "hi" in user_input.lower() or "hello" in user_input.lower() or "you" in user_input.lower():
        response = "VCET bot: Hi! I'm a friendly VCET bot."
    elif "e and c" in user_input.lower() or "ec" in user_input.lower() or "electronics" in user_input.lower():
        response = "VCET bot:The Department of Electronics & Communication Engineering at Vivekananda College of Engineering & Technology (VCET), Puttur, was established in 20011. The department offers a 4-year degree program in Electronics and Communication Engineering, affiliated to the Visvesvaraya Technological University (VTU). The program focuses on the practical application of science and math to solve problems in the field of communications. It includes designing, fabrication, testing, maintenance, supervision, and manufacturing of electronic equipment used in entertainment, media, hospitals (Medical Electronics), computer control systems, broadcast, communication systems, and in defense\nThe Department of Electronics & Communication Engineering at VCET, Puttur, has a team of highly qualified and experienced faculty members. Here are some of them:\n1.Dr. Mahesh Prasanna K - Principal, Professor, Teaching from 18 years, Department: Electronics & Communication Engineering, B.E., M.Tech, Ph.D\n2.Mr. Shrikanth Rao S K - Assistant Professor & Head, Teaching from 17 years, Department: Electronics & Communication Engineering, B.E, M.Tech, (Ph.D)\n3.Dr. Mahantesh R. Choudhari - Associate Professor, Teaching from 8 years, Department: Electronics & Communication Engineering, B.E., M.Tech, Ph.D\n4.Ms. Rajani Rai B - Assistant Professor, Teaching from 18 years, Department: Electronics & Communication Engineering, B.E., M.Tech\n5.Ms. Sowmya Anil - Assistant Professor, Department Coordinator, Teaching from 17 years, Department: Electronics & Communication Engineering, Placement and Training Department, B.E, M.Tech\n6.Ms. Prabha G S - Assistant Professor, Teaching from 17 years, Department: Electronics & Communication Engineering, B.E., M.Tech\n7.Mr. Shivaprasad - Assistant Professor, Teaching from 12 years, Department: Electronics & Communication Engineering, B.E., M.Tech\n8.Ms. Nirupama K - Assistant Professor, Teaching from 11 years, Department: Electronics & Communication Engineering, B.E., M.Tech\n9.Mr. Mahabaleshwara Bhat P - Assistant Professor, Teaching from 11 years, Department: Electronics & Communication Engineering, B.E., M.Tech\n10.Ms. Nisha G R - Assistant Professor, Teaching from 9 years, Department: Electronics & Communication Engineering, B.E., M.Tech\n11.Mr. Akshay S P - Assistant Professor, Teaching from 3 years, Department: Electronics & Communication Engineering, B.E., M.Tech\n12.Mr. Shreyas H - Assistant Professor, Teaching from 7 years, Department: Electronics & Communication Engineering, B.E, M.Tech\n13.Mr. Nithin - Assistant Professor, Teaching from 11 years, Department: Electronics & Communication Engineering, B.E, M.Tech\nFor more detailed information about the faculty at VCET, you can visit their [official website]: https://vcetputtur.ac.in/ug-department/ec-faculty\nFor more information about the Electronics & Communication Engineering department, you can visit: https://vcetputtur.ac.in/ug-department/electronics-and-communication-engineering"
    elif "data science" in  user_input.lower() or "cd" in user_input.lower() or "data" in user_input.lower() or "ds" in user_input.lower():
        response = "VCET bot: The Department of Computer Science & Engineering (Data Science) at Vivekananda College of Engineering & Technology (VCET), Puttur, offers a specialized undergraduate program, B.E in Computer Science & Engineering (Data Science). Data Science is an interdisciplinary study that uses scientific processes, methods, and algorithms to convert large amounts of data into actionable knowledge. The department uses techniques and theories from mathematics, statistics, and computer science domains to provide computational solutions to real-world problems rich in data. This specialization makes students proficient in tools and systems used by Data Science Professionals and gain the skills in developing intelligent models that cover many fields of Computer Science\nThe key highlights of the program include:\n- Career Essential Soft Skills Program and Placement Assistance (Job Opportunities Portal, Hiring Drives, Resume Building & many more)\n- Dedicated Student Success Mentor & Career Mentor for 360 Degree Support\n- Live Coding Classes & Profile Building Workshops\n- Mentorship Sessions from Industry Experts\n- Case Studies and Assignments\n- Practical Hands-on Projects\nThe core subjects of the program include Data Structures, Design and Analysis of Algorithms, Database Management Systems, Data Mining and Data Warehousing, Big Data Analytics, Programming: Python and R, Business Intelligence, and Cloud Computing.\nHere are some of the faculty members in the Department of Computer Science & Engineering (Data Science) at VCET:\n1. Dr. Govindaraj P- Associate Professor & Head, Teaching from 8 years, Department: Artificial Intelligence and Machine Learning Department, Data Science Diploma, B.E, MTech, Ph.D., Post-Doc (IIT Guwahati)\n2. Mrs. Akshaya D. Shetty- Assistant Professor, Teaching from 6 years, Department: Artificial Intelligence and Machine Learning Department, B.E, M.Tech, (Ph.D)\n3. Ms. Monica.K.P- Assistant Professor, Teaching from 4 years, Department: Artificial Intelligence and Machine Learning Department, B.E, M.Tech\n4. Mr. Abhishek Kumar K - Assistant Professor, Teaching from 2 years, Department: Artificial Intelligence and Machine Learning\n5. Mr. Ajay Shastry C G - Assistant Professor, Teaching from 1 year, Department: Artificial Intelligence and Machine Learning Department, B.E., M.Tech\n6. Mrs. Vaishnavi K V - Assistant Professor, Teaching from 1 year, Department: Artificial Intelligence and Machine Learning Department, B.E, M.Tech\n7. Ms. Harshitha - Lab Instructor, Department: Artificial Intelligence and Machine Learning Department, ITI, Diploma in ECE\nFor more detailed information about the Computer Science & Engineering (Data Science) department and its faculty at VCET, you can visit their [official website]: vcetputtur.ac.in/ug-department/computer-science-and-engineering-data-science. https://vcetputtur.ac.in/ug-department/faculty-ai"
    elif "ai" in user_input.lower() or "artificial" in user_input.lower():
        response = "VCET bot:The Department of Artificial Intelligence and Machine Learning at Vivekananda College of Engineering & Technology (VCET), Puttur, is dedicated to providing quality education in the emerging fields of Artificial Intelligence and Machine Learning. The curriculum of the AI&ML program is designed to provide necessary basics in Computer science engineering with specialized knowledge and skills in Artificial Intelligence, Machine Learning, Deep Learning, Reinforcement learning, NLP, HCI, Data Science, Meta Heuristics, Computer Vision, Business Intelligence, and other interdisciplinary areas.\nHere are some of the faculty members in the Department of Artificial Intelligence and Machine Learning at VCET:\n1. Dr. Govindaraj P- Associate Professor & Head, Teaching from 8 years, Department: Artificial Intelligence and Machine Learning Department, Data Science Diploma, B.E, MTech, Ph.D., Post-Doc (IIT Guwahati)\n2. Mrs. Akshaya D. Shetty - Assistant Professor, Teaching from 6 years, Department: Artificial Intelligence and Machine Learning Department, B.E, M.Tech, (Ph.D)\n3. Ms. Monica.K.P- Assistant Professor, Teaching from 4 years, Department: Artificial Intelligence and Machine Learning Department, B.E, M.Tech\n4. Mr. Abhishek Kumar K - Assistant Professor, Teaching from 2 years, Department: Artificial Intelligence and Machine Learning Department, B.E, M.Tech\n5. Mr. Ajay Shastry C G - Assistant Professor, Teaching from 1 year, Department: Artificial Intelligence and Machine Learning Department, B.E., M.Tech\n6. Mrs. Vaishnavi K V - Assistant Professor, Teaching from 1 year, Department: Artificial Intelligence and Machine Learning Department, B.E, M.Tech\n7. Ms. Harshitha - Lab Instructor, Department: Artificial Intelligence and Machine Learning Department, ITI, Diploma in ECE\nFor more detailed information about the Artificial Intelligence and Machine Learning department and its faculty at VCET, you can visit their [official website]:- vcetputtur.ac.in/ug-department/faculty-ai"
    elif "cs" in user_input.lower() or "computer" in user_input.lower(): 
        response = "VCET bot:  The Department of Computer Science & Engineering at Vivekananda College of Engineering & Technology (VCET), Puttur, was established in 2001 with the objective of imparting quality education in the field of Computer Science. The department has modern facilities for teaching, learning, and research.\nThe Department of Computer Science & Engineering at VCET, Puttur, has a team of highly qualified and experienced faculty members. Here are some of them:\n1. Mr. Krishna Mohana A J - HOD, Teaching from 14 years, B.E., M.Tech, (Ph.D)\n2. Dr. Lokesh M R - Professor, Teaching from 18 years, M. Tech, Ph.D\n3. Dr. Uma Pare - Associate Professor, Teaching from 17 years, Ph.D\n4. Dr. Jeevitha B K - Associate Professor, Teaching from 8 years, B.E, M.Tech, Ph.D\n5. Ms. Roopa G K - Assistant Professor, Teaching from 18 years, B.E., M.Tech, (Ph.D)\n6. Ms. Bharathi K -Assistant Professor, Teaching from 15 years, B.E., M.Tech\n7. Ms. Radhika Shetty D S - Assistant Professor, Teaching from 15 years, B.E., M.Tech, (Ph.D)\n8. Mrs. Savitha M - Assistant Professor, Teaching from 8 years, B.E, M.Tech\n9. Mr. Pradeep Kumar K G - Assistant Professor, Teaching from 13 years, DCSE, B. E., M. Tech, (Ph. D)\n10. Mr. Mohan A R - Assistant Professor, Teaching from 13 years, B.E, M.Tech\n11. Ms. Swapnalaxmi K - Assistant Professor, Teaching from 11 years, B.E., M.Tech, (Ph.D)\n12. Mr. Pramod Kumar P M - Assistant Professor, Teaching from 10 years, B.E., M.Tech\n13. Ms. Shwetha C H - Assistant Professor, Teaching from 10 years, B.E., M.Tech\n14. Ms. Thapaswini P S - Assistant Professor, Teaching from 7 years, B.E., M.Tech\n15. Ms. Deepthi M B - Assistant Professor, Teaching from 3 years, B.E., M.Tech\n16. Ms. Jayashree M - Assistant Professor, Teaching from 2 years, B.E, M.Tech\n17. Manohar Jha - Assistant Professor, Teaching from 3 years, B.E, M.Tech\n18. Mr. Shrinidhi A - Assistant Professor, Teaching from 4 years, B.E. M.Tech\n19. Ms. Manasa P - Assistant Professor, Teaching from 2 years, M.Tech\nFor more detailed information about the faculty at VCET, you can visit their official website: vcetputtur.ac.in/ug-department/cs-faculty"
    elif "fees" in user_input.lower():
        response = "VCET Bot: The fee structure for various courses at Vivekananda College of Engineering & Technology (VCET), Puttur is as follows:\n1. Bachelor of Engineering (BE): The annual fee for the BE course is ₹87,100.\n2. Master of Business Administration (MBA): The annual fee for the MBA course is ₹1,10,50.\n3. Master of Technology (M.Tech): The annual fee for the M.Tech course is ₹84,500.\nPlease note that these are the annual fees and may vary based on the course and specialization. For the most accurate and up-to-date information, I recommend checking the [official VCET website or contacting the college directly] through https://vcetputtur.ac.in/admissions/fee-structure."
    elif "vc" in user_input.lower() or "college" in user_input.lower():
        response = 'VCET bot: Vivekananda College of Engineering & Technology (VCET) is a prestigious engineering college located in Puttur, Karnataka. Established in 2001 by Vivekananda Vidyavardhaka Sangha Puttur (R), VCET has been committed to providing quality technical education to the rural parts of coastal Karnataka. The college offers a variety of undergraduate and postgraduate programs in various fields of engineering and technology. With a strong emphasis on innovation and research, VCET aims to equip its students with the necessary skills and knowledge to excel in their chosen fields. The college is well-equipped with state-of-the-art facilities and has a highly qualified and dedicated faculty. VCET is known for its vibrant campus life and a wide range of extracurricular activities.'
    elif "contact" in  user_input.lower():
        response = ("VCET bot: For contact information, you can reach VCET at:\n"
                    "Address: Vivekananda Campus, Nehru Nagar, Puttur, Karnataka 574203\n"
                    "Phone: +91-8251-235955\nFax: +91-8251-236444\nMobile: 9945575955/9945577955\n"
                    "Prof. Vandana Shankar, Training & Placement Officer\n"
                    "\tPhone:08251-234555\n\tCell: 9945575955\n"
                    "\tE-mail: placement@vcetputtur.ac.in\n"
                    "Principal: Dr. Mahesh Prasanna\n"
                    "\tEmail : principal@vcetputtur.ac.in\n"
                    "\tPhone: +91 99450 16992\n")
    elif "principal" in user_input.lower():
        response = ("VCET bot: Principal: Dr. Mahesh Prasanna\n"
                    "\tEmail : principal@vcetputtur.ac.in\n"
                    "\tPhone: +91 99450 16992\n")
    else:
        response = "VCET bot: Sorry, I can't seem to understand what you are saying."
    
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, response + "\n\n")
    chat_window.config(state=tk.DISABLED)
    chat_window.see(tk.END)

def show_about():
    about_text = "I was developed by the team Syntax Sorcerers of CD Branch \n The teammates are \nSricharan\n Nishan Kumar\n Kedar Pai\n Manohara \n Shreyas\n Gaurav "
    messagebox.showinfo("About", about_text)

def open_email(email_address):
    webbrowser.open("mailto:" + email_address)

def contact_placement():
    open_email("placement@vcetputtur.ac.in")

def contact_college():
    open_email("college@vcetputtur.ac.in")

def contact_principal():
    open_email("principal@vcetputtur.ac.in")

def open_vcet_website():
    webbrowser.open("https://vcetputtur.ac.in")

# Initialize the introductory message
intro_message = "Hello! I'm VCET chat bot. I am here to give information about VCET."

root = tk.Tk()
root.title("UI Friendly VCET bot")

# Header label
header_label_text = "VCET Chatbot"
header_label = tk.Label(root, text=header_label_text, font=('Arial', 16, 'bold'), bg='blue', fg='white', padx=20, pady=0, justify=tk.RIGHT)
header_label.pack(fill=tk.X)

# Developed by line
developed_line_text = "Developed by Syntax Sorcerers"
developed_line = tk.Label(root, text=developed_line_text, font=('Arial', 12), bg='blue', fg='white', padx=20, pady=0, justify=tk.RIGHT)
developed_line.pack(fill=tk.X)


# Customize appearance of the chat box
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, bg='black', fg='white', font=('Times New Roman', '12','bold'))
chat_window.pack(padx=20, pady=20)
chat_window.insert(tk.END, intro_message + "\n\n")
chat_window.config(state=tk.DISABLED)

user_entry = tk.Entry(root, width=30)
user_entry.pack(padx=10, pady=(0, 10))
user_entry.bind("<Return>", send_message)

send_button = tk.Button(root, text="Send", command=send_message, width=10, height=2, bg='white', fg='black')
send_button.pack()

# Place Exit button in the right-down corner
exit_button = tk.Button(root, text="Exit", command=root.destroy, width=10, height=2, bg='white', fg='black')
exit_button.pack(side=tk.RIGHT, anchor=tk.SE)

# About button
about_button = tk.Button(root, text="About", command=show_about, bg='blue', fg='white')
about_button.pack(side=tk.LEFT, anchor=tk.SW)

# Contact Menubutton
contact_button = tk.Menubutton(root, text="Contact", bg='green', fg='white')
contact_button.pack(side=tk.LEFT, anchor=tk.SW)

# VCET Website button
vcet_website_button = tk.Button(root, text="VCET Website", command=open_vcet_website, bg='orange', fg='white')
vcet_website_button.pack(side=tk.LEFT, anchor=tk.SW)

# Contact submenu
contact_menu = tk.Menu(contact_button, tearoff=0)
contact_menu.add_command(label="Contact Placement", command=contact_placement)
contact_menu.add_command(label="Contact College", command=contact_college)
contact_menu.add_command(label="Contact Principal", command=contact_principal)

contact_button.config(menu=contact_menu)

root.mainloop()