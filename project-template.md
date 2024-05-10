<center>

# Dpto. INFORMÁTICA - I.E.S. PUERTO DE LA CRUZ – TELESFORO BRAVO

---

### MÓDULO PROYECTO (PRW)

### C.F.G.S. Desarrollo de Aplicaciones Web (DAW)

ADALOGIX

</center>

<right>

**_Author/s:_** Alejandro Hernández, Dimas Abrante, Adrián herrera
**_Date:_** 10/05/2024
**_Tutor:_** Alejandro Martín Zarza

</right>

<center>

# INDICE

</center>

1. [**_INTRODUCTION._**](#id1)
2. [**_ORIGIN, CONTEXTUALIZATION AND JUSTIFICATION OF THE PROJECT._**](#id2)
3. [**_GENERAL OBJECTIVE OF THE PROJECT._**](#id3)
4. [**_GENERAL DESCRIPTION OF THE PROJECT (SCOPE)._**](#id4)
5. [**_TASKS._**](#id5)
6. [**_CRONOGRAM._**](#id6)
7. [**_SUMMARY OF HUMAN AND MATERIAL RESOURCES._**](#id7)
8. [**_RISK CONTROL._**](#id8)
9. [**_MONITORING, EVALUATION AND QUALITY CONTROL POLICY._**](#id9)
10. [**_CLAUSES._**](#id10)
11. [**_BIBLIOGRAPHY._**](#id11)
12. [**_GLOSSARY._**](#id12)
13. [**_ATTACHMENTS._**](#id13)

### 1. INTRODUCTION. <a name="id1"></a>

In the business environment that we know and that surrounds us, we have detected that the software used by many of them is very outdated and they are not agile at all. In this context, the need arises to develop a technological solution to optimize and streamline the processes related to inventory management, route planning and human resources management in the logistics field.

The main objective of the logistics management project is to develop a functional web platform that will provide companies with a comprehensive tool for the efficient management of their logistics. This platform will provide key functionalities, such as inventory management, the assignment of optimized routes for product delivery, and the administration of users with different roles and permissions. At all times, priority will be given to optimized functionality and usability, designed to be simple and easy to use for any user without much knowledge.

The platform will be designed to be highly scalable and customizable, which will allow to adapt it to the specific needs of each company and sector, so we are going to develop it in a relatively generic way allowing to adapt it to any field. In addition, technologies such as Vue.js for the frontend and Django for the backend will be integrated, along with Docker for container/database management, ensuring optimal performance and easy implementation in different working environments.

In summary, the logistics management project aims to provide companies with a complete and adaptable technological solution to optimize their logistics operations. With a focus on efficiency, scalability and customization, this platform will become an indispensable tool to improve the competitiveness and performance of companies in today's market.

### 2. ORIGIN, CONTEXTUALIZATION AND JUSTIFICATION OF THE PROJECT. <a name="id2"></a>

The logistics management project arises as a response to a series of needs and challenges identified in the business environment, which we have known from family and friends who have experienced problems with outdated and poorly optimized software, in addition to a very poor usability.

#### Origin of the Idea:

The idea of developing a logistics management platform arises from the observation of the difficulties and limitations faced by many companies in the administration of their logistics processes. As we mentioned in the introduction, we know of several close cases of store/warehouse managers who suffer day to day with having to deal with very old software. This is where the idea of optimizing and improving all this software was born, as well as doing it with cutting-edge technologies to improve the user experience.

#### Needs Detected:

- Inventory Management:
  Many companies face difficulties in keeping accurate control of their inventory, which can lead to financial losses and delays in product delivery. Managing the stock of a large company and being able to see where that stock is distributed among the different stores and warehouses in an efficient and simple way is one of the main needs we have detected regarding this point.
- Route Planning:
  Manual planning of delivery routes can be inefficient and error-prone, resulting in extended delivery times and higher operating costs. In addition, we know of cases where there is not even a software prepared for the management of these routes and they continue to be done manually or on paper. With this we want to streamline the process both for the administrators who create the routes and for the delivery drivers to be able to consult directly in an application the places they have to deliver to.
- Team Coordination:
  Coordinating work teams, especially in distributed logistics environments, can be a challenge, with communication and task tracking issues. In this particular need we have detected the need to make the same application that can distinguish the type of user that is accessing it. In this way we avoid having to use several applications or sacrifice the usability of some users to give it to others.

#### Problems to be addressed:

The project seeks to address these issues by providing a comprehensive platform that allows companies to efficiently manage their logistics operations. By centralizing inventory management, route planning and team coordination on a single platform, it is expected to improve operational efficiency, reduce costs and improve customer satisfaction.

#### Project Justification:

The justification for carrying out this project lies in the need for companies to have advanced technological tools that allow them to compete effectively in an increasingly demanding and competitive market. By providing a comprehensive and adaptable solution to the specific needs of each company, the logistics management project seeks to improve the efficiency and competitiveness of companies in the logistics field.

In summary, the logistics management project arises as a response to the needs and challenges identified in the business environment, with the objective of providing a comprehensive technological solution that allows companies to optimize their logistics operations and improve their competitiveness in today's market.

### 3. GENERAL OBJECTIVE OF THE PROJECT. <a name="id3"></a>

The main purpose of this project is to develop and implement a complete and robust web platform that optimizes business logistics management. This platform aims to offer an adaptable solution capable of effectively addressing the challenges of the logistics sector. In essence, we seek to optimize and automate key logistics processes, centralize relevant information in a single application, improve the customer and business experience always seeking to reduce the time spent using the software, ensure adaptability and scalability so that the application fits in all logistics companies that would like to use the application, integrate advanced technologies and ensure continuous improvement and constant updating of the platform among other objectives related to increasing productivity for the company. In short, we aspire to create an innovative tool that not only improves operational efficiency and reduces costs, but also boosts business competitiveness and raises customer satisfaction standards in the logistics field.

### 4. GENERAL DESCRIPTION OF THE PROJECT (SCOPE). <a name="id4"></a>

The project will be developed as a logistics management web application covering multiple aspects of business operations, from inventory management to delivery route planning and coordination of work teams with role differentiation. Each aspect of the project is detailed in greater depth below:

Architecture and Structure:

The application will be divided into three main components: frontend, backend and database.
For the frontend, Vue.js will be used with the Composition API, which will allow a modular and reusable structure for the user interface.

For the backend, Django will be used as the main framework, using Django Rest Framework for the creation of a RESTful API to handle requests and responses between the frontend and the database.

The database will be hosted in a Docker container and PostgreSQL will be used as the relational database management system, ensuring security and data integrity.

It is a relatively simple architecture as we do not stop communicating things through an API, so no complex architecture is needed.

2. General Operation:

Users will be able to access the application through an authentication system that will use JWT tokens (JSON Web Tokens) for user authentication.

Once authenticated, users will have access to different functionalities according to their role, such as inventory management, route planning and user administration.

Inventory management will allow users to add, edit and delete products, as well as track stock and generate inventory reports.

Route planning will allow users to create optimized routes for product delivery, taking into account factors such as distance, delivery time and resource availability. If you are a user with a delivery role, you will be able to see which route has been assigned to you and you will be able to finalize it in order to appear as available again.

3. Data Validation and Security:

A validation layer will be implemented on both the frontend and backend to ensure the integrity and accuracy of the data entered by users.

On the frontend, form validation methods provided by Vue.js will be used to ensure that the data entered by users meets the specified criteria.

On the backend, data validation mechanisms will be implemented using Django's form validation capabilities, as well as custom validations as needed.

To ensure the security of the application, standard security measures will be implemented, such as protection against CSRF (Cross-Site Request Forgery) and XSS (Cross-Site Scripting) attacks, as well as secure storage of passwords using hashing algorithms.

4. Integration of Development Tools:

Development tools such as Git will be used for code version control, allowing detailed tracking of changes and efficient collaboration between team members.
An agile development flow will be implemented, using methodologies such as Scrum or Kanban through github itself, to guarantee an iterative and continuous delivery of features and improvements. As for the development technologies, they will be those previously mentioned.

In summary, the logistics management project will be developed as a complete and robust web application that will use modern technologies and development practices to provide an efficient and secure solution for managing enterprise logistics operations. With a focus on modularity, scalability and security, the application will provide an intuitive and functional user experience, improving operational efficiency and business competitiveness in today's marketplace.

### 5. TASKS. <a name="id5"></a>

All the tasks defined in the project are here:

- Roadmap view: https://github.com/users/alherdom/projects/2/views/1?layout=roadmap
- Kanban board view: https://github.com/users/alherdom/projects/2/views/1
- General issues: https://github.com/alherdom/Adalogix/issues?q=is%3Aissue+is%3Aclosed

All costs are defined in preliminary project.

### 6. CRONOGRAMA. <a name="id6"></a>

The schedule has been defined through a github project, in which all the tasks have been broken down and all the sprints have been defined. The link to the project is the following: https://github.com/users/alherdom/projects/2

And Milestones are defined here: https://github.com/alherdom/Adalogix/milestones

### 7. SUMMARY OF HUMAN AND MATERIAL RESOURCES. <a name="id7"></a>

<center>

| TAREA                                                                                | Recursos Humanos                           | Recursos materiales    |
| ------------------------------------------------------------------------------------ | ------------------------------------------ | ---------------------- |
| Create inventory product list template                                               | Fronted developer: 1                       | -                      |
| Add products from a csv file backend                                                 | Backend Developer: 1                       | -                      |
| Change product list view to add quantity and new fields backend                      | Backend Developer: 1                       | -                      |
| Add new fields to product (Quantity and Description) backend                         | Backend Developer: 1                       | -                      |
| Review of the first delivery of the project documentation                            | -                                          | -                      |
| Create user detail endpoint backend                                                  | Backend Developer: 1                       | -                      |
| Create user delete and multiple delete endpoint backend                              | Backend Developer: 1                       | -                      |
| Create user edit endpoint backend                                                    | Backend Developer: 1                       | -                      |
| Create user list endpoint backend                                                    | Backend Developer: 1                       | -                      |
| Add a function to delete multiple products at once backend                           | Backend Developer: 1                       | -                      |
| Change views to manage permissions backend                                           | Backend Developer: 1                       | -                      |
| Fix the auth method to token authorization with DRF backend                          | Backend Developer: 1                       | -                      |
| Add Docker to the project for postgresql backend                                     | Backend Developer: 1                       | Docker, Database Image |
| Generate commands to automatically fill data for products, store / inventory backend | Backend Developer: 1                       | -                      |
| Creation of inventory models/structure backend                                       | Backend Developer: 1                       | -                      |
| Assigns the found router solution to the courier frontend                            | Fronted developer: 1                       | -                      |
| Show solution found router frontend                                                  | Fronted developer: 1                       | -                      |
| Create router template frontend                                                      | Fronted developer: 1                       | -                      |
| Create edit product endpoint backend                                                 | Backend Developer: 1, Fronted developer: 1 | -                      |
| Create remove product endpoint backend                                               | Backend Developer: 1                       | -                      |
| Create add product endpoint backend                                                  | Backend Developer: 1                       | -                      |
| Create product detail endpoint backend                                               | Backend Developer: 1                       | -                      |
| Create product list endpoint backend                                                 | Backend Developer: 1                       | -                      |
| Button to search products to the inventory template frontend                         | Fronted developer: 1                       | -                      |
| Button to edit products to the inventory template frontend                           | Fronted developer: 1                       | -                      |
| Button to remove products to the inventory template frontend                         | Fronted developer: 1                       | -                      |
| Button to add products to the inventory template frontend                            | Fronted developer: 1                       | -                      |
| Create dashboard template frontend                                                   | Fronted developer: 1                       | -                      |

</center>

### 8. RISK CONTROL. <a name="id8"></a>

During project planning and execution, it is crucial to identify and manage potential risks that could affect the success of the project. Three identified risks are listed below, each classified according to their likelihood, impact and risk type, along with the proposed action to mitigate or manage the risk.

- Risk of Unexpected Changes in Requirements:

  - Likelihood: Moderate (0.50)
  - Impact: High (0.80) → May cause significant development delays and increase project cost.
  - Risk Type: High
  - Action to be taken:
  - Mitigation Plan: Establish a regular requirements review process with stakeholders to anticipate and address changes. Maintain clear and constant communication with the client to manage expectations and adapt to changes effectively.

- Lack of Human Resources Risk:

  - Likelihood: Low (0.30)
  - Impact: Medium (0.60) → May generate delays in the delivery of tasks and affect the quality of the final product.
  - Risk Type: Medium
  - Action to be taken:
  - Contingency Plan: Maintain a reserve of available resources or establish collaboration agreements with external teams to cover possible shortfalls in human resources in case of need.

- Risk of Technological Infrastructure Failure:

  - Probability: High (0.70)
  - Impact: High (0.80) → May completely paralyze development and negatively affect the quality of the final product.
  - Risk Type: High
  - Action to be taken:
  - Mitigation Plan: Implement robust security measures and perform extensive testing on the technology infrastructure. Establish a rapid response protocol for possible failures, including the availability of a trained technical team to address emergencies and restore the system in the shortest possible time.

- Requirements Escalation Risk:

  - Probability: High (0.70)
  - Impact: Medium (0.60) → May lead to a significant increase in project scope and possible delivery delays.
  - Risk Type: High
  - Action to be taken:
  - Mitigation Plan: Establish a robust change management process that includes detailed assessment of new requirements and their impact on the project schedule and budget. Limit changes outside the initially agreed scope and regularly review project status with stakeholders to avoid escalation of requirements.

- Communication Failure Risk

      - Likelihood: Moderate (0.40)
      - Impact: Medium (0.60) → May lead to misunderstandings, conflicts and delays in decision making.
      - Risk Type: Medium
      - Action to be taken:
      - Contingency Plan: Establish clear and efficient communication channels between all team members and stakeholders. Conduct regular meetings to review project progress and encourage open and transparent communication.

- Data Security Failure Risk:

  - Probability: High (0.70)
  - Impact: High (0.80) → May result in the loss or theft of sensitive data, damaging the company's reputation and causing financial losses.
  - Risk Type: High
  - Action to be taken:
  - Mitigation Plan: Implement robust security measures, such as data encryption, two-factor authentication, and regular security audits. Train staff on secure data handling practices and keep abreast of the latest security threats and vulnerabilities.

- Risk of Missed Deadlines due to Dependency on Third Parties:

  - Likelihood: Moderate (0.50)
  - Impact: High (0.75) → Lack of timely delivery by third party vendors may result in project delays.
  - Risk Type: High
  - Action to be taken:
  - Mitigation Plan: Identify and carefully evaluate the reliability of external suppliers. Establish clear contracts that specify timelines and deliverables, and have alternative plans in case problems arise with expected suppliers.

### 9. MONITORING, EVALUATION AND QUALITY CONTROL POLICY. <a name="id9"></a>

The project's monitoring, evaluation and quality control policy will focus on ensuring that the objectives are met and that the project progresses in accordance with the established expectations. To this end, the following actions will be implemented:

Detailed Project Planning: A detailed plan will be developed that includes objectives, key milestones, deliverables and timelines. This will provide a clear structure for tracking project progress.

Regular Progress Tracking: Regular tracking of project progress will be conducted through regular team meetings and progress reviews. This will allow any early deviations to be identified and corrective action to be taken in a timely manner.

Managed Change Control: A formal process will be established to manage changes to the scope, requirements and other aspects of the project. Each proposed change will be carefully evaluated in terms of its impact on schedule, budget and quality prior to implementation.

Comprehensive Testing: A detailed test plan will be developed covering unit, integration, system and acceptance testing. These tests will ensure that the final product meets the required quality and functionality standards.

Code and Documentation Review: Regular reviews of the code and associated documentation will be conducted to ensure quality and consistency. Resources will be allocated to conduct peer reviews and provide constructive feedback.

User Feedback: Feedback will be collected from users throughout the project life cycle to assess customer satisfaction and make adjustments as needed.

Ongoing Risk Management: Regular assessment of project risks will be performed and mitigation strategies will be implemented to address them. This will help prevent potential deviations and keep the project on track.

Quality Reviews: Periodic quality reviews will be conducted to assess compliance with established quality standards. This will include review of project processes, documentation and deliverables.

These actions will ensure that the project is executed efficiently, meeting established objectives and maintaining high quality standards at all stages of development.

### 10. CLAUSES. <a name="id10"></a>

With the aim of establishing a clear and transparent development for the execution of the project, a series of contractual clauses have been defined that address various aspects related to the development, quality and financial management of the project.

Deadlines and Delays:
In the event of delay in the delivery of agreed milestones or deliverables, a mechanism for notification and evaluation of the causes of the delay will be established. Depending on the severity and circumstances of the delay, penalties or schedule adjustments may be applied to ensure timely completion of the project.

Payments and Billing:
Project-related payments will be made in accordance with specific milestones or deliverables achieved, as agreed in the contract. A payment schedule will be established that reflects important project milestones and corresponding invoices will be issued based on these milestones.

Quality Control:
A comprehensive quality control system will be implemented to ensure that all project products and deliverables meet established standards and requirements. This will include extensive testing, peer reviews and user validations to ensure the quality and functionality of the developed software.

Change Management:
A formal process will be established for managing changes to the scope, requirements or any other aspect of the project that may affect its execution. All proposed changes will be evaluated in terms of impact on schedule, budget and quality before implementation.

Intellectual Property and Copyright:
Clear clauses related to intellectual property and copyright will be established to ensure that all parties involved in the project maintain ownership and control over their respective intellectual assets. Appropriate use and protection of intellectual property rights related to the project will be agreed upon.

Confidentiality and Data Protection:
Appropriate confidentiality and data protection measures will be established to ensure the security and privacy of confidential information shared during the course of the project. Clear provisions will be agreed for the handling and protection of sensitive information of all parties involved.

Conflict Resolution:
In the event of disputes or conflicts related to the project, a formal conflict resolution procedure will be established that promotes open communication and the search for mutually satisfactory solutions. Mediation or arbitration options may be considered to resolve disputes quickly and efficiently.

These contractual clauses provide a robust and transparent framework for the execution of the logistics management project, ensuring that all parties involved clearly understand their roles, responsibilities and expectations throughout the project life cycle.

### 11. BIBLIOGRAPHY. <a name="id11"></a>

- Tutorial de Vue.js en español: https://es.vuejs.org/v2/guide/
- Documentación oficial de PostgreSQL sobre consultas avanzadas: https://www.postgresql.org/docs/current/queries-table-expressions.html
- Blog sobre buenas prácticas en la gestión de bases de datos relacionales: https://www.databasestar.com/relational-database-design-best-practices/
- Foro de discusión sobre Docker y contenedores en Docker Forums: https://forums.docker.com/c/general/4
- Documentación oficial de Vue Test Utils para pruebas unitarias en Vue.js: https://vue-test-utils.vuejs.org/
- Página de recursos y tutoriales sobre Python en Real Python: https://realpython.com/
- Comunidad de desarrolladores de Django en Stack Overflow: https://stackoverflow.com/questions/tagged/django
- Guía oficial de Vue.js: https://vuejs.org/
- Documentación de Django ORM: https://docs.djangoproject.com/en/stable/topics/db/models/
- Tutorial de Docker para principiantes: https://www.docker.com/get-started
- Blog sobre prácticas recomendadas en el diseño de bases de datos: https://www.databasestar.com/
- Foro de discusión sobre desarrollo web en general en Reddit: https://www.reddit.com/r/webdev/
- Documentación de HTML5: https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5
- Tutorial de Vue Router: https://router.vuejs.org/
- Comunidad de desarrolladores de Python en Discord: https://discord.gg/python

### 12. GLOSSARY. <a name="id12"></a>

Django: A high-level web framework written in Python that encourages fast and clean development.

Vue.js: A progressive JavaScript framework used to build interactive user interfaces.

Docker: An open source platform that allows you to package, distribute and run applications inside containers.

API: Application Programming Interface. Allows communication between different software programs.

PostgreSQL: A powerful open source relational database management system.

REST: Representational State Transfer. A software architecture style that defines a set of constraints for creating web services.

Frontend: The part of a web application that users see and interact with.

Backend: The part of a web application that is behind the scenes and handles server and database logic.

RESTful API: An API that follows REST principles for communication between systems.

Vue Router: An official Vue.js plugin for web application navigation.

WebSocket: A bi-directional, full-duplex communication protocol over a single TCP socket.

ORM: Object-Relational Mapper. Allows interacting with a database using objects instead of direct SQL queries.

JWT: JSON Web Token. An open standard that defines a compact, self-contained way to securely transmit information between parties as a JSON object.

DRF: Django REST Framework. A powerful and flexible library for building web APIs in Django.

Testing: The process of evaluating a system or application to verify that it meets requirements and functions correctly.
Framework: A set of tools, libraries and conventions that provide a structure for software development.

Container: A lightweight, portable environment that encapsulates applications and their dependencies for execution on any operating system.

User Interface (UI): The point of interaction between users and a device or application.

Application Programming Interface (API): A set of rules and definitions that allows different applications or systems to communicate with each other.

Client: A program or device that accesses a service or resource on a server.

Server: A program or device that provides services or resources to other programs or devices, usually over a network.

MVC (Model-View-Controller): A software design pattern that separates information representation, business logic and user interaction into different components.

RESTful API: An application programming interface that follows REST principles for communication between systems.

Relational Database: A type of database that organizes data in related tables.

Middleware: Software that acts as an intermediary between different applications or systems to facilitate communication and interoperability.

Cache: A temporary data storage area used to speed up access to recurring data.

Token: A string of characters representing a user's authorization or identification in a system.

Security: Measures and practices to protect data and systems from unauthorized access, malicious use, theft or damage.

Unit Testing: Automated tests that verify the individual behavior of components or units of code.

Continuous Integration: A software development practice in which code changes are automatically integrated and tested on a frequent and regular basis.

### 13. ATTACHMENTS. <a name="id13"></a>

All the information needed in this section is in the preliminary project.
