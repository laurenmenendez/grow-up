# GrowUp!

## About
GrowUp! is an application that allows parents to digitally document their children privately. Parents can create profiles for each of their children and add features for each child, such as milestones, to memorialize their child's achievements.

## Links
### Front-end repository
https://github.com/laurenmenendez/grow-up-client
### Deployed Client
https://laurenmenendez.github.io/grow-up-client
### Deployed API
https://grow-up2021.herokuapp.com

## Technologies
- Django (Django-rest-framework)
- Python
- PostgreSQL

## ERD
![GrowUp (1)](https://media.git.generalassemb.ly/user/34617/files/55471600-c2c5-11eb-8279-4f14c83eb4f8)

## Routes
### Auth
- (/sign-up/)
  - POST
- (/sign-in/)
  - POST
- (/change-pw/)
  - PATCH (partial_update)
### Child
- (/children/)
  - GET
  - POST
- (/children/<int:child_pk>/)
  - GET
  - PATCH (partial_update)
  - DELETE
### Milestone
- (/children/<int:child_pk>/milestones/)
  - GET
  - POST
- (/children/<int:child_pk>/milestones/<int:pk>/)
  - GET
  - PATCH (partial_update)
  - DELETE

## Planning
### Process
- I decided on building the front-end in React and the back-end in Django from the start. So, I built the back-end first in a way I know would be optimal with how I planned to build in React (i.e. how I would render all of a child's milestones.) This helped me avoid needing to continuously refactor my backend.
- Having my ERD and overall plan for what I wanted the app to do first helped me narrow down what I needed this API to do
- When problem solving, I made heavy use of the internet. I learned a lot from reading through React and Bootstrap documentation, as well as combing through Stack Overflow threads. I submitted an issue request to GA instructors as well.

### Future versions
- More sophisticated design (animations, transitions)
- Utilize more react-bootstrap Components
- Add nav links (FAQ, About Us, Contact Us)
- Create logo
- Refactor UX based on future expansion of API
