from PIL import Image, ImageDraw, ImageFont
from uuid import uuid4
import textwrap

def build_resume_png(resume, output_size=(1200, 1600), bg_color="white") -> str:
    img = Image.new("RGB", output_size, color=bg_color)
    draw = ImageDraw.Draw(img)

    # Layout config
    x_margin = 60
    column_gap = 40
    left_col_width = int((output_size[0] - 3 * x_margin) * 0.65)
    right_col_x = x_margin + left_col_width + column_gap
    y_left = 60
    y_right = 60

    # Fonts
    try:
        font_name = ImageFont.truetype("arialbd.ttf", 48)
        font_title = ImageFont.truetype("arialbd.ttf", 26)
        font_section = ImageFont.truetype("arialbd.ttf", 24)
        font_text = ImageFont.truetype("arial.ttf", 20)
        font_small = ImageFont.truetype("arial.ttf", 18)
    except:
        font_name = font_title = font_section = font_text = font_small = ImageFont.load_default()

    def draw_wrapped_text(text, font, x, y, max_width, fill="black"):
        lines = []
        avg_char_width = font.getlength('x')
        max_chars = int(max_width / avg_char_width)

        for segment in text.split('\n'):
            lines.extend(textwrap.wrap(segment, width=max_chars))

        for line in lines:
            draw.text((x, y), line, fill=fill, font=font)
            y += font.size + 10
        return y

    # --- HEADER ---
    if resume.full_name:
        draw.text((x_margin, y_left), resume.full_name.upper(), fill="#222222", font=font_name)
        y_left += 60

    if resume.title:
        draw.text((x_margin, y_left), resume.title, fill="#A23E2A", font=font_title)
        y_left += 40

    # Contact line
    contact_bits = []
    if resume.contact_email: contact_bits.append(resume.contact_email)
    if resume.contact_phone: contact_bits.append(resume.contact_phone)
    if resume.linkedin_url: contact_bits.append("LinkedIn")

    contact_str = "   ".join(contact_bits)
    y_left = draw_wrapped_text(contact_str, font_small, x_margin, y_left, left_col_width, fill="#666666")
    y_left += 20

    # Divider
    draw.line([(x_margin, y_left), (output_size[0] - x_margin, y_left)], fill="#CCCCCC", width=2)
    y_left += 30
    y_right = y_left

    # Section helper
    def draw_section(title, x, y):
        draw.text((x, y), title.upper(), fill="#222222", font=font_section)
        y += 30
        draw.line([(x, y), (x + 250, y)], fill="#222222", width=2)
        y += 15
        return y

    # --- LEFT COLUMN ---

    # Summary
    if resume.summary:
        y_left = draw_section("Career Objective", x_margin, y_left)
        y_left = draw_wrapped_text(resume.summary, font_text, x_margin, y_left, left_col_width)
        y_left += 20

    # Experience
    if resume.experience:
        y_left = draw_section("Work Experience", x_margin, y_left)

        for exp in resume.experience:
            draw.text((x_margin, y_left), exp.job_title, fill="#222222", font=font_title)
            y_left += 26

            draw.text((x_margin, y_left), exp.company_name, fill="#A23E2A", font=font_text)
            y_left += 22

            sub = f"{exp.start_date} - {exp.end_date} | {exp.location}"
            draw.text((x_margin, y_left), sub, fill="#1F1D1D", font=font_small)
            y_left += 24

            for resp in (exp.responsibilities or []):
                y_left = draw_wrapped_text(f"• {resp}", font_text, x_margin + 15, y_left, left_col_width - 15)

            y_left += 15

    # --- RIGHT COLUMN ---

    # Education
    if resume.education:
        y_right = draw_section("Education", right_col_x, y_right)

        for edu in resume.education:
            text = f"{edu.degree}\n{edu.institution}\n{edu.start_year} - {edu.end_year}"
            y_right = draw_wrapped_text(text, font_text, right_col_x, y_right, output_size[0] - right_col_x - x_margin)
            y_right += 15

    # Skills
    if resume.skills:
        y_right = draw_section("Skills", right_col_x, y_right)

        skills_text = "\n".join(resume.skills)
        y_right = draw_wrapped_text(skills_text, font_text, right_col_x, y_right, output_size[0] - right_col_x - x_margin)

    # Save
    filename = f"resume_{uuid4().hex[:8]}.png"
    img.save(filename)
    return filename





def build_resume_png_second(resume, output_size=(1200, 1600), bg_color="white") -> str:
    img = Image.new("RGB", output_size, color=bg_color)
    draw = ImageDraw.Draw(img)

    x_margin = 80
    max_width = output_size[0] - 2 * x_margin
    y = 80

    # Fonts
    try:
        font_name = ImageFont.truetype("arialbd.ttf", 40)
        font_section = ImageFont.truetype("arialbd.ttf", 22)
        font_sub = ImageFont.truetype("arialbd.ttf", 20)
        font_text = ImageFont.truetype("arial.ttf", 20)
        font_small = ImageFont.truetype("arial.ttf", 18)
    except:
        font_name = font_section = font_sub = font_text = font_small = ImageFont.load_default()

    def draw_wrapped(text, font, x, y, width, spacing=8, fill="#333"):
        avg_char = font.getlength('x')
        max_chars = int(width / avg_char)

        lines = []
        for seg in text.split('\n'):
            lines.extend(textwrap.wrap(seg, width=max_chars))

        for line in lines:
            draw.text((x, y), line, font=font, fill=fill)
            y += font.size + spacing
        return y

    def section(title, y):
        draw.text((x_margin, y), title.upper(), font=font_section, fill="#222")
        y += 28
        draw.line([(x_margin, y), (output_size[0]-x_margin, y)], fill="#222", width=2)
        y += 20
        return y

    # --- HEADER (CENTERED) ---
    if resume.full_name:
        w = font_name.getlength(resume.full_name)
        draw.text(((output_size[0]-w)/2, y), resume.full_name, font=font_name, fill="#2c3e50")
        y += 50

    contact = []
    if hasattr(resume, "location") and resume.location:
        contact.append(resume.location)
    if resume.contact_email:
        contact.append(resume.contact_email)
    if resume.contact_phone:
        contact.append(resume.contact_phone)
    if resume.linkedin_url:
        contact.append("LinkedIn")

    contact_text = "  •  ".join(contact)
    w = font_small.getlength(contact_text)
    draw.text(((output_size[0]-w)/2, y), contact_text, font=font_small, fill="#555")
    y += 30

    draw.line([(x_margin, y), (output_size[0]-x_margin, y)], fill="#CCCCCC", width=2)
    y += 30

    # --- SUMMARY ---
    if resume.summary:
        y = section("Professional Summary", y)
        y = draw_wrapped(resume.summary, font_text, x_margin, y, max_width)
        y += 20

    # --- EXPERIENCE ---
    if resume.experience:
        y = section("Professional Experience", y)

        for exp in resume.experience:
            # Title
            draw.text((x_margin, y), exp.job_title, font=font_sub, fill="#222")

            # Right aligned date/location
            right_text = f"{exp.start_date} — {exp.end_date}, {exp.location}"
            w = font_small.getlength(right_text)
            draw.text((output_size[0]-x_margin-w, y), right_text, font=font_small, fill="#555")

            y += 26

            # Company
            draw.text((x_margin, y), exp.company_name, font=font_text, fill="#444")
            y += 24

            # Bullet points
            for resp in (exp.responsibilities or []):
                y = draw_wrapped(f"• {resp}", font_text, x_margin + 10, y, max_width - 10, spacing=10)

            y += 20

    # --- EDUCATION ---
    if resume.education:
        y = section("Education", y)

        for edu in resume.education:
            text = f"{edu.degree}"
            draw.text((x_margin, y), text, font=font_sub, fill="#222")

            right = f"{edu.start_year} — {edu.end_year}"
            w = font_small.getlength(right)
            draw.text((output_size[0]-x_margin-w, y), right, font=font_small, fill="#555")

            y += 26
            y = draw_wrapped(edu.institution, font_text, x_margin, y, max_width)
            y += 15

    # --- SKILLS ---
    if resume.skills:
        y = section("Expert-Level Skills", y)
        skills_text = ", ".join(resume.skills)
        y = draw_wrapped(skills_text, font_text, x_margin, y, max_width)

    # Save
    filename = f"resume{uuid4().hex[:8]}.png"
    img.save(filename)
    return filename





def build_resume_png_third(resume, output_size=(1200, 1600), bg_color="white") -> str:
    img = Image.new("RGB", output_size, color=bg_color)
    draw = ImageDraw.Draw(img)

    x_margin = 80
    max_width = output_size[0] - 2 * x_margin
    y = 80

    # Fonts
    try:
        font_name = ImageFont.truetype("arialbd.ttf", 38)
        font_section = ImageFont.truetype("arialbd.ttf", 22)
        font_sub = ImageFont.truetype("arialbd.ttf", 20)
        font_text = ImageFont.truetype("arial.ttf", 20)
        font_small = ImageFont.truetype("arial.ttf", 18)
    except:
        font_name = font_section = font_sub = font_text = font_small = ImageFont.load_default()

    def draw_wrapped(text, font, x, y, width, spacing=8, fill="#333"):
        if not text:
            return y

        avg_char = max(font.getlength('x'), 7)
        max_chars = int(width / avg_char)

        lines = []
        for seg in str(text).split('\n'):
            lines.extend(textwrap.wrap(seg, width=max_chars))

        for line in lines:
            draw.text((x, y), line, font=font, fill=fill)
            y += font.size + spacing
        return y

    def section(title, y):
        draw.text((x_margin, y), title.upper(), font=font_section, fill="#1f4e79")
        y += 26
        draw.line([(x_margin, y), (output_size[0]-x_margin, y)], fill="#1f4e79", width=2)
        y += 20
        return y

    # -------------------------------
    # MAIN BOX
    # -------------------------------
    box_top = 200
    box_bottom = output_size[1] - 60

    draw.rounded_rectangle(
        [(50, box_top), (output_size[0]-50, box_bottom)],
        outline="#222",
        width=3,
        radius=20
    )

    y = box_top + 30

    # -------------------------------
    # NAME
    # -------------------------------
    if resume.full_name:
        w = font_name.getlength(resume.full_name)
        draw.text(((output_size[0]-w)/2, y), resume.full_name, font=font_name, fill="#1f4e79")
        y += 45

    # -------------------------------
    # CONTACT
    # -------------------------------
    contact = []
    if resume.contact_email:
        contact.append(str(resume.contact_email))
    if resume.contact_phone:
        contact.append(resume.contact_phone)
    if resume.linkedin_url:
        contact.append("LinkedIn")

    contact_text = " • ".join(contact)
    if contact_text:
        w = font_small.getlength(contact_text)
        draw.text(((output_size[0]-w)/2, y), contact_text, font=font_small, fill="#555")
        y += 30

    # -------------------------------
    # BAR
    # -------------------------------
    bar_y = y
    draw.rounded_rectangle(
        [(100, bar_y), (output_size[0]-100, bar_y+18)],
        fill="#1f2a44",
        radius=10
    )

    draw.text((120, bar_y+1), "Professional Resume", font=font_small, fill="white")
    y += 35

    # -------------------------------
    # SUMMARY
    # -------------------------------
    if resume.summary:
        y = section("Summary", y)
        y = draw_wrapped(resume.summary, font_text, x_margin, y, max_width)
        y += 15

    # -------------------------------
    # EXPERIENCE
    # -------------------------------
    if resume.experience:
        y = section("Experience", y)

        for exp in resume.experience:
            title = f"{exp.job_title or ''} | {exp.company_name or ''}"
            draw.text((x_margin, y), title.strip(), font=font_sub, fill="#222")

            right = f"{exp.start_date or ''} - {exp.end_date or ''}"
            w = font_small.getlength(right)
            draw.text((output_size[0]-x_margin-w, y), right, font=font_small, fill="#333")

            y += 26

            if exp.location:
                y = draw_wrapped(exp.location, font_small, x_margin, y, max_width, fill="#666")

            for resp in (exp.responsibilities or []):
                y = draw_wrapped(f"• {resp}", font_text, x_margin + 10, y, max_width - 10, spacing=10)

            y += 20  # 🔥 FIX: spacing between jobs

    # -------------------------------
    # EDUCATION
    # -------------------------------
    if resume.education:
        y = section("Education", y)

        for edu in resume.education:
            draw.text((x_margin, y), edu.degree or "", font=font_sub, fill="#222")

            right = f"{edu.start_year or ''} - {edu.end_year or ''}"
            w = font_small.getlength(right)
            draw.text((output_size[0]-x_margin-w, y), right, font=font_small, fill="#333")

            y += 26

            if edu.institution:
                y = draw_wrapped(edu.institution, font_text, x_margin, y, max_width)

            y += 15

    # -------------------------------
    # SKILLS
    # -------------------------------
    if resume.skills:
        y = section("Skills", y)

        col_width = max_width // 3  # better than 4 (more readable)

        for i, skill in enumerate(resume.skills):
            col = i % 3
            row = i // 3

            x = x_margin + col * col_width
            y_offset = y + row * 24

            draw.text((x, y_offset), f"• {skill}", font=font_small, fill="#222")

        y += ((len(resume.skills)//3) + 1) * 24 + 10

    # -------------------------------
    # PROJECTS
    # -------------------------------
    if resume.projects:
        y = section("Projects", y)

        for proj in resume.projects:
            title = f"{proj.name or ''}"
            if proj.technologies:
                title += f" | {', '.join(proj.technologies)}"

            draw.text((x_margin, y), title, font=font_sub, fill="#1f4e79")
            y += 24

            if proj.description:
                y = draw_wrapped(proj.description, font_text, x_margin + 10, y, max_width - 10)

            y += 15

    # -------------------------------
    # CERTIFICATIONS
    # -------------------------------
    if resume.certifications:
        y = section("Certifications", y)

        for cert in resume.certifications:
            text = f"{cert.name or ''} - {cert.issuing_organization or ''}"
            y = draw_wrapped(text, font_text, x_margin, y, max_width)

    # Save
    filename = f"resume_{uuid4().hex[:8]}.png"
    img.save(filename)
    return filename