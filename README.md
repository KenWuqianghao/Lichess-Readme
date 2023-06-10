# Lichess-Readme

<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
lichess-readme
</h1>
<h3 align="center">📍 Show off Your Chess Skill - Make the Most of lichess!</h3>
<h3 align="center">🚀 Developed with the software and tools below.</h3>
<p align="center">

<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="" />
<img src="https://img.shields.io/badge/Jinja-B41717.svg?style=for-the-badge&logo=Jinja&logoColor=white" alt="idna" />
<img src="https://img.shields.io/badge/Flask-000000.svg?style=for-the-badge&logo=Flask&logoColor=white" alt="python" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="pyc" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white" alt="pack" />
</p>

</div>

---
## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍Overview](#-introdcution)
- [⚙️ Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🏎💨 Getting Started](#-getting-started)
- [🤝 Contributing](#-contributing)
- [🪪 License](#-license)
---

## 📍Overview

Lichess-readme is a GitHub project designed to help authors of GitHub repositories easily create lichess elo rating badges on their github readme page. 

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## ⚙️ Project Structure

```bash
repo
├── app.py
├── LICENSE
├── lichess.yml
├── __pycache__
│   ├── app.cpython-311.pyc
│   └── app.cpython-39.pyc
├── README.md
├── requirements.txt
├── templates
│   └── card.html.j2
└── vercel.json

2 directories, 9 files
```
---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 💻 Modules
<details closed><summary>Root</summary>

| File   | Summary                                                                                                                                                                                                                                            | Module   |
|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
| app.py | This code creates a Flask application that uses the Lichess API to generate an SVG card with the user 's rating for a given time control . The time control is set in an environment variable and the user 's rating is retrieved from the Lichess | app.py   |

</details>

<details closed><summary>Templates</summary>

| File         | Summary                                                                                                                                                                                                     | Module                 |
|:-------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------|
| card.html.j2 | This code creates an SVG graphic with two rectangles , one in # 555 and one in # 007ec6 , and two text elements displaying the values of the variables " time_control " and " elo " . The graphic is 139x20 | templates/card.html.j2 |

</details>
<hr />

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> `Register a Vercel account`

### 💻 Installation

1. Fork the lichess-readme repository:
<img width="149" alt="Screenshot 2023-06-10 at 04 41 18" src="https://github.com/KenWuqianghao/Lichess-Readme/assets/20444505/e62cc33f-c7d6-4937-8923-6d66da49647b">

2. Go to vercel, create a project using the forked github repo
<img width="1512" alt="Screenshot 2023-06-10 at 04 41 30" src="https://github.com/KenWuqianghao/Lichess-Readme/assets/20444505/56fdad6f-16a1-4394-b788-2c62f3687f2e">
<img width="1512" alt="Screenshot 2023-06-10 at 04 41 41" src="https://github.com/KenWuqianghao/Lichess-Readme/assets/20444505/89b80e19-0c67-4815-96c2-ef00015a7b8a">

3. Provide environment variables including username and time_control, time_control options are bullet, blitz and rapid.
<img width="1512" alt="Screenshot 2023-06-10 at 04 42 08" src="https://github.com/KenWuqianghao/Lichess-Readme/assets/20444505/e6bb786e-2954-41db-8bee-a3943d6f5f29">

4. Deploy and enjoy

### 🤖 Using lichess-readme

```sh
<img src="link-to-your-vercel-app/?">
```
---

## 🤝 Contributing
Contributions are always welcome! Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).
```sh
git checkout -b new-feature-branch
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin new-feature-branch
```
7. Create a pull request to the original repository.
Open a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 🪪 License

This project is licensed under the `MIT` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---
