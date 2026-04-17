<div align="center">

# 🚀 Django Professional Portfolio

### _A production-grade, data-driven portfolio management system built with Django._

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.2-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com)
[![Swiper](https://img.shields.io/badge/Swiper.js-Latest-6332F6?style=for-the-badge&logo=swiper&logoColor=white)](https://swiperjs.com)
[![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)]()
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)]()

</div>

---

## � Source Code

This is a real-world production project.  
The source code is kept in a **private repository** to protect intellectual property.

However, I’m happy to provide access to:

- 👨‍💻 **Interviewers** – to review code quality and architecture
- 🤝 **Collaborators** – if you're interested in contributing

[![Email](https://img.shields.io/badge/Email-Contact_Me-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:fahmialhafidza@gmail.com)

---

## �📌 Overview

> **Django Portfolio** is not just a static website—it's a **Content Management System (CMS)** designed for developers to showcase their work professionally.

Unlike robust static site generators, this system allows you to manage your **Projects**, **Skills**, **Experience**, and **Profile Information** directly through a secure Admin Panel. No more editing HTML files to add a new project or update your resume.

Built with performance and SEO in mind, it features a responsive design, dark/light mode toggle, and a dynamic project showcase engine.

---

## ✨ Features

- 📝 **Dynamic Content Management** — Update bio, social links, and CV via Django Admin
- 🌟 **Featured Project Spotlight** — Highlight key projects with a premium "Featured" layout
- 📂 **Project Archive** — Automatically organize regular projects in a responsive grid
- 🛠️ **Skill Categorization** — Manage tech stack with categories (Backend, DevOps, etc.) and proficiency levels
- 🌓 **Theme System** — Dark/Light mode with local storage persistence & system preference detection
- 📱 **Mobile-First Design** — Fully responsive layout using Bootstrap 5 & custom CSS
- 📬 **Contact System** — Secure form handling with SMTP email notifications
- 📄 **Resume Integration** — Upload and manage PDF CVs directly from the dashboard

---

## 🛠️ Tech Stack

| Layer              | Technology               | Purpose                               |
| ------------------ | ------------------------ | ------------------------------------- |
| **Backend**        | Django 4.2 (Python 3.12) | Core logic, ORM, Admin Interface      |
| **Database**       | SQLite / MySQL           | Data persistence                      |
| **Frontend**       | Bootstrap 5, Swiper.js   | Responsive UI & Carousel components   |
| **Storage**        | Django Media Files       | Image & Document handling             |
| **Infrastructure** | Gunicorn + Nginx         | Production serving (Deployment ready) |
| **Dev Tools**      | Git, Virtualenv          | Version control & isolation           |

---

## 🏗️ Architecture

The project follows the standard **Django M_T (Model-View-Template)** architecture:

```
┌────────────────────────┐
│    Browser / Client    │
└───────────┬────────────┘
            │ HTTP Request
┌───────────▼────────────┐
│      Django URLs       │  Routes requests to views
└───────────┬────────────┘
            │
┌───────────▼────────────┐    ┌─────────────────┐
│       Main Views       │◄───┤    Templates    │
│  (Home, Contact, etc.) │    │ (HTML + Django) │
└───────────┬────────────┘    └─────────────────┘
            │ Query
┌───────────▼────────────┐
│      Data Models       │
│ (UserProfile, Project) │
└───────────┬────────────┘
            │ SQL
┌───────────▼────────────┐
│   Database (SQLite)    │
└────────────────────────┘
```

### Key Modules:

- **`main`**: Handles core pages, user profile, skills, and configuration.
- **`projects`**: Manages project entries, categories, and featured status.
- **`users`**: Extended user management (admin customization).

---

## 🔄 Workflow

1.  **Admin Entry**: You log into `/admin` and add a new Project (e.g., "E-Commerce API").
2.  **Data Processing**:
    - Image is processed and stored.
    - `is_featured` flag determines layout priority.
3.  **Rendering**:
    - The Homepage view queries `Project.objects.all()`.
    - Splits results into `featured_projects` (top slider) and `regular_projects` (grid).
4.  **Presentation**:
    - Template renders the data using Swiper.js for the carousel.
    - Dark mode script checks user preference before rendering.

---

## 📸 Screenshots

<div align="center">

|                                   |                                       |
| :-------------------------------: | :-----------------------------------: |
|      **Hero Section (Dark)**      |         **Featured Projects**         |
|   ![Hero](screenshots/hero.png)   | ![Featured](screenshots/featured.png) |
|      **Skills & Tech Stack**      |          **Admin Dashboard**          |
| ![Skills](screenshots/skills.png) |    ![Admin](screenshots/admin.png)    |

</div>

> _Note: Placeholders for screenshots. Run the app to see live._

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Git

### Installation

1.  **Clone the repository**

    ```bash
    git clone https://github.com/yourusername/portfolio.git
    cd portfolio
    ```

2.  **Create virtual environment**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3.  **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run migrations**

    ```bash
    python manage.py migrate
    ```

5.  **Create superuser (Admin)**

    ```bash
    python manage.py createsuperuser
    ```

6.  **Run server**
    ```bash
    python manage.py runserver
    ```

Visit `http://127.0.0.1:8000` to see the site, or `http://127.0.0.1:8000/admin` to manage content.

---

## 📊 Project at a Glance

| Metric              | Value                                             |
| ------------------- | ------------------------------------------------- |
| **Modules**         | 3 (Main, Projects, Users)                         |
| **Database Tables** | 10+ (Projects, Skills, Experience, Profile, etc.) |
| **CSS Framework**   | Bootstrap 5 + Custom SCSS                         |
| **Responsiveness**  | 100% Mobile Ready                                 |

---

## 🗺️ Roadmap

- [x] Project & Skill Management
- [x] Featured vs Regular Project Logic
- [x] Dark Mode
- [x] Contact Form with Email
- [ ] Blog / Article Section (Future)
- [ ] SEO Optimization (Sitemap & Meta Tags)
- [ ] Docker Support

---

## 👤 Author

<div align="center">

**Achmad Fahmi Al Hafidz**
_Backend Engineer · Python · Django_

[![GitHub](https://img.shields.io/badge/GitHub-Visit-181717?style=for-the-badge&logo=github)](https://github.com/fidzst)
[![Email](https://img.shields.io/badge/Email-Contact-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:your-email@example.com)

</div>

---

<div align="center">

_Built with ❤️ using Django & Python._

</div>
