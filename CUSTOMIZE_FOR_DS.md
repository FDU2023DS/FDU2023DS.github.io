# CUSTOMIZE FOR DS

## 0.1

    There're two customizing files in this project. If you're going to change the page, please refer to CUSTOMIZE.md.

## 1.1 structure

    The structure of the project is as follows(only essential files are shown):

    ```
    ├── _config.yml
    ├── README.md
    ├── CUSTOMIZE.md
    ├── CUSTOMIZE_FOR_DS.md
    ├── _pages
    │   ├── 404.md
    │   ├── about.md(this is the home page)
    │   ├── blog.md
    │   ├── calender.md
    │   ├── gallery.md
    │   ├── people.md
    │   ├── news.md(this is the news page, hidden under dropdown, which is used for checking history announcements ad news)  
    │   ├── dropdown.md(dropdown menu on the homepage)
    ├── _posts
    ├── _news
    ├── _projects(which is actually people file)
    ├── assets
    │   ├── img(images except for person)
    │   ├── person_img
    │   ├── json
    │   │   ├── calendar_events.json(for calendar)
    ├── reference_and_tools
    │   ├── data_to_md.py
    ```

## 2.1 deploy

    The project is deployed on github pages. You can refer to INSTALL.md for more details.
    For giscus, you can refer to https://giscus.app/ for more details and change code in `_layouts/about.liquid`(last several rows  which start as `{% if site.giscus and page.giscus_comments %}`).

## 2.2 reference

    The reference is in `reference_and_tools/`. All kinds of references are provided.

## 3.1 homepage

    The text on homepage can be changed in `_pages/about.md`.
    The photo on homepage can be changed in `_pages/about.md` and `assets/img/`.
    The giscus comment zone can be turned on or off.
    The dropdown menu can be changed in `_pages/dropdown.md`.

## 3.2 news page

    The news page is hidden under dropdown menu. The news can be added in `_news/`, which is mostly used as announcement.
    The news will be shown on homepage and history news can be found in news page hidden under dropdown on homepage.
    The maximal number of news on homepage is 5, which can be changed in `_config.yml`.

## 3.3 calendar

    The calendar events can be changed in `assets/json/calendar_events.json`.
    The calendar initial time can be changed in `_pages/calendar.md`.

## 3.4 gallery

    The gallery can be changed in `_pages/gallery.md` and `assets/img/`.
    examples -> `reference_and_tools/`

## 3.5 people

    The people can be changed in `_rojects/` and `assets/person_img/`.
    iIf you want to add new people, please put the excel file in the main folder, rename it `raw0.xlsx`, copy the file `reference_and_tools/data_to_md.py` to the main folder and run it. Finally, remember to delete the excel file and the python file.

## 3.6 blog

    The blog can be changed in `_posts/`.
    examples -> `reference_and_tools/`

## 4.1 page view

    The page view is not included in this project, but it is automatically recorded by github pages which can be found in your repository->insights->traffic.
