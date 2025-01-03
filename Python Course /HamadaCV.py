from manim import *

# Configure resolution for a vertical (portrait) video
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_rate = 30  # Optional: Set frame rate

class AnimatedCV(Scene):
    def construct(self):
        # **Section 1: Header with Name and Contact Information**
        self.create_header()
        self.wait(2)

        # **Section 2: Summary**
        self.show_summary()
        self.wait(2)

        # **Section 3: Projects**
        self.show_projects()
        self.wait(2)

        # **Section 4: Professional Experience**
        self.show_experience()
        self.wait(2)

        # **Section 5: Education**
        self.show_education()
        self.wait(2)

        # **Section 6: Skills**
        self.show_skills()
        self.wait(2)

    def create_header(self):
        # Name
        name = Text("Hamada Rae’d", font_size=60, color=BLUE).to_edge(UP)
        self.play(Write(name))
        self.wait(0.5)

        # Contact Information
        contacts = VGroup(
            Text("📞 0568463566", font_size=30),
            Text("✉️ hamadaraed19@gmail.com", font_size=30),
            Text("🌐 LinkedIn | GitHub | Codewars", font_size=30),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(name, DOWN, buff=0.5).align_to(name, LEFT)

        self.play(*[Write(contact) for contact in contacts])
        self.wait(1)

    def show_summary(self):
        # Section Title
        summary_title = Text("SUMMARY", font_size=50, color=YELLOW).to_edge(LEFT, buff=1).shift(UP * 0.5)
        self.play(Write(summary_title))
        self.wait(0.5)

        # Summary Text
        summary_text = Text(
            "A passionate Full-Stack Developer seeks opportunities to grow, share skills, \nand tackle coding challenges. Enthusiastic about finding bugs and solving coding puzzles, \nI thrive at the intersection of mathematics and computer science, bringing abstract concepts \nto life in practical applications.",
            font_size=30,
            t2c={"Full-Stack Developer": BLUE, "coding challenges": GREEN},
            line_spacing=1.5,
        ).next_to(summary_title, DOWN, buff=0.5).align_to(summary_title, LEFT)

        self.play(Write(summary_text, run_time=5))
        self.wait(1)

    def show_projects(self):
        # Section Title
        projects_title = Text("PROJECTS", font_size=50, color=YELLOW).to_edge(LEFT, buff=1).shift(UP * 0.5)
        self.play(Write(projects_title))
        self.wait(0.5)

        # Project 1
        project1_title = Text("StockMaster", font_size=40, color=BLUE).next_to(projects_title, DOWN, buff=0.5).align_to(projects_title, LEFT)
        project1_desc = Text(
            "A comprehensive web application leveraging Django, Python, and various frontend technologies \nto streamline inventory management across diverse industries with features including product \ndata entry, expiration tracking, and import/export operations.",
            font_size=28,
            line_spacing=1.5,
        ).next_to(project1_title, DOWN, buff=0.3).align_to(project1_title, LEFT)

        project1_link = Text("GitHub Link", font_size=28, color=GREEN).next_to(project1_desc, DOWN, buff=0.3).align_to(project1_desc, LEFT)
        self.play(Write(project1_title), Write(project1_desc, run_time=4), FadeIn(project1_link))
        self.wait(1)

        # Project 2
        project2_title = Text("KnowledgeSphere", font_size=40, color=BLUE).next_to(project1_link, DOWN, buff=0.7).align_to(project1_title, LEFT)
        project2_desc = Text(
            "An online Q&A platform for students, utilizing Django, Python, and frontend technologies \nto enhance the process of asking and receiving accurate answers on a wide range of topics.",
            font_size=28,
            line_spacing=1.5,
        ).next_to(project2_title, DOWN, buff=0.3).align_to(project2_title, LEFT)

        project2_link = Text("GitHub Link", font_size=28, color=GREEN).next_to(project2_desc, DOWN, buff=0.3).align_to(project2_desc, LEFT)
        self.play(Write(project2_title), Write(project2_desc, run_time=3), FadeIn(project2_link))
        self.wait(1)

        # Project 3
        project3_title = Text("Liqaa", font_size=40, color=BLUE).next_to(project2_link, DOWN, buff=0.7).align_to(project1_title, LEFT)
        project3_desc = Text(
            "An interview website application that enables users to connect, share insights, \nand expand their knowledge across various subjects. Coming Soon.",
            font_size=28,
            line_spacing=1.5,
        ).next_to(project3_title, DOWN, buff=0.3).align_to(project3_title, LEFT)

        self.play(Write(project3_title), Write(project3_desc, run_time=2.5))
        self.wait(1)

    def show_experience(self):
        # Section Title
        experience_title = Text("PROFESSIONAL EXPERIENCE", font_size=50, color=YELLOW).to_edge(LEFT, buff=1).shift(UP * 0.5)
        self.play(Write(experience_title))
        self.wait(0.5)

        # Experience 1
        exp1_title = Text("AI Engineer, Fratello Software House", font_size=40, color=BLUE).next_to(experience_title, DOWN, buff=0.5).align_to(experience_title, LEFT)
        exp1_dates = Text("May 2024 - Present", font_size=30).next_to(exp1_title, RIGHT, buff=1)
        exp1_details = Text(
            "- Developed machine learning models to optimize business processes.\n- Collaborated with cross-functional teams to integrate AI solutions into existing systems.",
            font_size=28,
            line_spacing=1.5,
        ).next_to(exp1_title, DOWN, buff=0.3).align_to(exp1_title, LEFT)

        self.play(Write(exp1_title), Write(exp1_dates), Write(exp1_details, run_time=3))
        self.wait(1)

        # Experience 2
        exp2_title = Text("Teaching Assistant, Birzeit University", font_size=40, color=BLUE).next_to(exp1_details, DOWN, buff=0.7).align_to(exp1_title, LEFT)
        exp2_dates = Text("August 2023 – Present", font_size=30).next_to(exp2_title, RIGHT, buff=1)
        exp2_details = Text(
            "- Assisted in teaching mathematics and computer science courses.\n- Provided academic support and guidance to students.",
            font_size=28,
            line_spacing=1.5,
        ).next_to(exp2_title, DOWN, buff=0.3).align_to(exp2_title, LEFT)

        self.play(Write(exp2_title), Write(exp2_dates), Write(exp2_details, run_time=2.5))
        self.wait(1)

    def show_education(self):
        # Section Title
        education_title = Text("EDUCATION", font_size=50, color=YELLOW).to_edge(LEFT, buff=1).shift(UP * 0.5)
        self.play(Write(education_title))
        self.wait(0.5)

        # Education Details
        edu1 = Text("MS in Mathematics, Birzeit University", font_size=38).next_to(education_title, DOWN, buff=0.5).align_to(education_title, LEFT)
        edu1_dates = Text("August 2023 - Present", font_size=30).next_to(edu1, RIGHT, buff=1)
        self.play(Write(edu1), Write(edu1_dates))
        self.wait(0.5)

        edu2 = Text("Full-Stack Developer Bootcamp, AXSOS Academy", font_size=38).next_to(edu1, DOWN, buff=0.5).align_to(edu1, LEFT)
        edu2_dates = Text("March - July 2023", font_size=30).next_to(edu2, RIGHT, buff=1)
        self.play(Write(edu2), Write(edu2_dates))
        self.wait(0.5)

        edu3 = Text("BA in Mathematics and Computer Science, Bethlehem University", font_size=38).next_to(edu2, DOWN, buff=0.5).align_to(edu1, LEFT)
        edu3_dates = Text("August 2018 - August 2022", font_size=30).next_to(edu3, RIGHT, buff=1)
        self.play(Write(edu3), Write(edu3_dates))
        self.wait(1)

    def show_skills(self):
        # Section Title
        skills_title = Text("SKILLS", font_size=50, color=YELLOW).to_edge(LEFT, buff=1).shift(UP * 0.5)
        self.play(Write(skills_title))
        self.wait(0.5)

        # Skills List
        skills = VGroup(
            Text("- Languages: Python, JavaScript, HTML, CSS, SQL, and C++.", font_size=30),
            Text("- Frameworks: Django, Django REST, Flask, Bootstrap, and React.", font_size=30),
            Text("- Databases: MySQL.", font_size=30),
            Text("- Libraries: NumPy, Pandas, Matplotlib, and PyTorch.", font_size=30),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(skills_title, DOWN, buff=0.5).align_to(skills_title, LEFT)

        self.play(*[Write(skill) for skill in skills], run_time=4)
        self.wait(1)