<center>

# FINAL MEMORY

---

</center>

<right>

**_Authors:_** Alejandro Hernández, Dimas Abrante, Adrián Herrera
**_Date:_** --
**_Tutor:_** Alejandro Martín Zarza

</right>

<center>

# INDICE

</center>

1. [**_INTRODUCTION._**](#id1)
2. [**_USED TECHNOLOGIES._**](#id2)
3. [**_STANDARDS AND WEB STYLE GUIDE._**](#id3)
4. [**_RESEARCH._**](#id4)
5. [**_COPYRIGHTS._**](#id5)
6. [**_RISKS AND MEASURES._**](#id6)
7. [**_DEGREE OF COMPLIANCE IN SCOPE._**](#id7)
8. [**_DEGREE OF COMPLIANCE IN TIME._**](#id8)
9. [**_DEGREE OF COMPLIANCE IN COSTS._**](#id9)
10. [**_FINAL PRODUCT._**](#id10)
11. [**_LESSONS LEARNED TO BE TAKEN INTO ACCOUNT IN FUTURE PROJECTS._**](#id11)
12. [**_LESSONS LEARNED TO BE TAKEN INTO ACCOUNT IN FUTURE PROJECTS._**](#id12)

### 1. INTRODUCTION. <a name="id1"></a>

In an increasingly interconnected and dynamic world, efficiency in logistics management becomes a critical factor for business success. In order to meet this need, we have developed this application that focuses on the optimization of resource management in an inventory, a customized user management with different roles to meet the needs of administrators, store managers and couriers, and a router so that routes can be organized for the delivery of goods and couriers can start the journey knowing all the information they need to know.

Thus, the purpose of this document is to gather information on the most important points of the project development process, such as the technologies we have used, the research processes we have had to carry out, as well as what has been learned in the process, among other issues that will be detailed throughout this document.

#### Inventory management:

Our platform offers a robust inventory management tool that allows companies to maintain precise control of their stock. From product receipt to storage and distribution, our solution facilitates real-time monitoring of stock levels, identification of critical products and optimization of available resources. The developed application is prepared to manage both global stock and the stock of specific warehouses or stores. The optimization also applies to product loading, allowing the company to record stock entries through csv format.

#### User Management with Defined Roles:

We understand that each employee plays a unique role in the logistics process. Therefore, our platform offers a user management system with defined roles, which allows specific permissions and responsibilities to be assigned according to the needs of each individual. From administrators overseeing the system to warehouse operators and couriers, our solution ensures efficient and secure collaboration.

#### Dynamic Route Planning:

Efficient product distribution is essential to meet delivery deadlines and satisfy customer demands. With our integrated routing tool, companies can create delivery routes intuitively that are automatically optimized.

In summary, our web platform offers a comprehensive solution for logistics management, allowing companies to improve operational efficiency, reduce costs and provide exceptional service to their customers. With an intuitive interface and powerful tools, we are committed to helping companies achieve their logistics objectives effectively in an increasingly competitive and demanding business environment.

### 2. USED TECHNOLOGIES. <a name="id2"></a>

To build our logistics management web platform, we have carefully selected a set of advanced technologies that ensure optimal performance, exceptional user experience, and seamless scalability. Also these technologies were selected based on the experience of our development experience.

#### Backend:

- **_Python 3.12:_** Python is a versatile and powerful programming language that has allowed us to develop the backend of our application with efficiency and flexibility. We've been working with this language for almost 2 years so we got straight to the point and didn't have to learn any new technology for this part. The version used was 3.12 offers us the latest features and improvements, guaranteeing the most modern possible functionalities of Python.
- **_Django 5.0:_** Django is a high-level Python-based web framework that provides a solid foundation for fast and secure web application development. With its focus on simplicity and efficiency, we have used Django 5.0 to build the backend of our platform, taking advantage of its wide range of features, from user authentication to database management.
- **_Django Rest Framework 3.15:_** For creating and managing a robust and flexible API, we have integrated Django Rest Framework into our application. This powerful tool allows us to design and expose RESTful endpoints that facilitate communication between the frontend and backend efficiently and securely.
- **_PostgreSQL:_** For efficient database management, we have deployed a Docker container using a PostgreSQL image. Docker allows us to encapsulate the database and its dependencies in a consistent and portable environment, simplifying the deployment and management of our application. For keep the data even if the container fails, we've added volumes to ensure the data is correctly saved.

#### Frontend:

- Vue3:o offer a dynamic and responsive user experience, we have opted for Vue.js 3 together with the Composition API, a powerful combination that allows us to structure our code in a more intuitive and modular way. With the Composition API, we have created highly functional, interactive user interfaces that allow users to seamlessly interact with our backend. In the first steps of the application, the framework we had selected was React, but to take advantage of the technologies that were going to be used in the internship period we decided to change to Vue.

  The Composition API is a set of APIs that allows us to author Vue components using imported functions instead of declaring options. It is an umbrella term that covers the following APIs:

  - Reactivity API, e.g. ref() and reactive(), that allows us to directly create reactive state, computed state, and watchers.

  - Lifecycle Hooks, e.g. onMounted() and onUnmounted(), that allow us to programmatically hook into the component lifecycle.

  - Dependency Injection, i.e. provide() and inject(), that allow us to leverage Vue's dependency injection system while using Reactivity APIs..

#### Deployment:

- DigitalOcean Droplet: For our application deployment, we have chosen DigitalOcean, a reliable and easy-to-use cloud infrastructure platform. We have implemented our application in a basic DigitalOcean droplet, which has allowed us to launch our platform quickly and efficiently, guaranteeing optimal uptime and scalability appropriate to our needs. With this in mind, the hardware features that have been used for this project have been as follows:

  - vCPUs: 1vCPU
  - Memory: 1GB
  - SSD: 25GB
  - Transfer: 1TB

### 3. APPLICATION STYLE GUIDE. <a name="id3"></a>

In this section, we generally describe the style guide or standards that we have followed to develop the solution

#### Minimalism and Clarity:

The user interface should follow a minimalist approach, with a clean and organized design that makes it easy to navigate and understand the information.
Sober colors and appropriate contrasts to highlight important elements without distracting the user should be used to develop a clean and easy to use interface.

#### Color palette

In relation to the range of colors used, the following palette of colors has been chosen in order of presence in the application:

| Color      | Code    | Percentage |
| ---------- | ------- | ---------- |
| Light gray | #eeeeee | 60%        |
| White      | #ffffff | 30%        |
| Orange     | #ff6c37 | 10%        |

In the following photo you can see this 60/30/10 ratio:

![image](https://github.com/alherdom/Adalogix/assets/90780043/50618410-134c-43bd-8961-88c5b1dbe474)

#### Coherence and Consistency:

The development should maintain a coherent structure throughout the platform, with a uniform arrangement of elements and intuitive navigation that allows users to easily find what they are looking for.
Use consistent visual language in terms of typography, iconography and spacing to create a cohesive user experience.

#### Accessibility and Usability:

Prioritize accessibility by using descriptive tags, alt text on images, and implementing the solutions always thinking that they should be friendly and simple for the user, thus being able to be used without the need for documentation or explanation
Optimize usability by incorporating intuitive interactive elements, such as clear buttons and drop-down menus, that facilitate user interaction with the platform.

#### Focus on Functionality:

Place platform functionality at the forefront, ensuring that core features, such as inventory management and route planning, are easily accessible from the home page.
Provide a seamless and barrier-free experience that allows users to perform tasks efficiently and without complications.

#### Feedback and Confirmation:

Incorporate visual feedback elements, such as success or error messages, to inform users of the results of their actions and provide confirmation when necessary.
Use subtle animations and fluid transitions to improve the user experience and make the platform feel more dynamic and responsive.

#### Flexibility and Scalability:

Design the platform with flexibility and scalability in mind, allowing for future expansion and customization based on changing business and user needs.
Use modular technologies and architectures that facilitate the integration of new features and adaptation to different business contexts.

#### Feedback and Continuous Improvement:

Establish open communication channels with users to collect comments and suggestions about the platform, and use this feedback to make continuous improvements and ensure an optimal experience for all users.

### 4. INVESTIGATION. <a name="id4"></a>

In this project we have used technologies that in one way or another we had seen before, but that does not mean that we have had to investigate. We had to learn about some aspects so that the final product was the best possible. Some of the fields in which we have investigated have been:

#### Vue.js learning:

We faced with the need to build the frontend of the platform with another language/framework different from the backend, so we immersed ourselves in learning the Vue.js framework. Through tutorials, official documentation, and practical examples, we've acquired the skills necessary to develop dynamic and responsive user interfaces. This one was a hard challenge because is a very different way to code than using SSR.

#### Docker exploration:

We also faced the challenge of managing the PostgreSQL database in a controlled and portable environment. This decision was made to avoid the configuration of PostgreSQL database in every system (every developer system and also in production) so we decided to use Docker. We investigated fundamental Docker concepts, such as containers and images, and learned how to deploy and manage a PostgreSQL container for our application.

#### Connection with multiple map APIs::

To integrate map capabilities into the platform and develop router functionality, we explored various map API options, including Geoapify, Maptiler, and Maplibre-GL. We studied the documentation provided by these platforms and learned how to consume their APIs to display interactive maps and create delivery routes. This research process was crucial, as the router was one of the main focuses of our development.

By immersing ourselves in these technologies, we gained knowledge on how to properly authenticate, send requests and process responses to incorporate this vital functionality into our application. The choice of these tools was based on their ability to meet the specific requirements of our project and their compatibility with our technical architecture.

This research allowed us to not only expand our technical knowledge, but also to evaluate and select the most appropriate tools for our specific needs. Although we initially considered other options such as Mapbox, we found that Geoapify, Maptiler and Maplibre-GL offered the optimal combination of features and ease of integration for our project.

This process of technology exploration and selection underscored our ability to adapt and make informed decisions in constantly evolving development environments. These experiences not only strengthened our ability to solve technical problems, but also provided us with a solid foundation to address future challenges and continue to grow as a professional team in the technology field.

#### Backend-Frontend Integration:

Since we were using server-side rendering development during all the academic year, we faced a new challenge in connecting the Django backend with the Vue.js frontend. We investigated different methods of communication between the two, such as creating a RESTful API and handling HTTP requests, to achieve a smooth and efficient integration between both sides of the application. As we said in the last section, Django Rest Framework was the main resource to look in backend and asyn requests was the option for the front.

#### Conclusions and Reflections of investigation:

Throughout this learning process, we have demonstrated a remarkable ability to acquire new skills and address technical challenges effectively. Our willingness to investigate, experiment and solve problems has been essential to the successful development of the logistics management platform.
This project has not only expanded our technical skill set, but has also strengthened your ability to face new challenges and adapt to changing development environments. These experiences will surely serve us in future projects and will help to continue growing as a professional team in the field of technology.

Furthermore, and although it will be explained later, due to lack of time we have had to leave behind another functionality which was the chat

### 5. COPYRIGHTS. <a name="id5"></a>

In the development of our logistics management platform, we have been careful to respect copyrights, both in multimedia content and in the use of third-party libraries and tools. Below, we detail the origin and licenses associated with each type of content used:

#### Third Party Content Used

For the construction of the platform, we have integrated several third-party libraries and tools, all under open source licenses. Below, we detail each one along with its license:

- **Visual Studio Code:** Visual Studio Code version 1.89 has been used, an IDE ideal for working with Python and all frontend technologies. Visual Studio Code is an open source software distributed under the MIT license.
- **Prettier:** We have used Prettier 10.4.0 for the formatting of the frontend technologies. This extension is under MIT license.
- **Eslint:** We have used Eslint 2.4.4, a linting tool for JavaScript used to identify and correct code errors. This technology is under MIT license.
- **Ruff:** We have used Ruff 0.4.4, an extremely fast Python linter and code formatter. This technology is under MIT license.
- **Django:** We use version 5.0.3 of Django, a high-level web development framework in Python, distributed under the BSD License.
- **Django Rest Framework:** For the creation of RESTful APIs, we use Django Rest Framework version 3.14.0, also under BSD License.
- **Psycopg2-binary:** For the connection to the PostgreSQL database, we have used version 2.9.9 of Psycopg2-binary, which is available under the LGPL License.
- **pytest and pytest-django:** We used versions 8.1.1 and 4.8.0 respectively to write and run unit tests in our project. Both are under the MIT license.
- **django-cors-headers:** To enable access to resources from a domain other than that of the page requesting them, we use version 4.3.1 of this library, which is distributed under the BSD license.
- **Prettyconf:** We use prettyconf version 2.2.1 for managing environment variables in a more readable and simpler way, with an MIT license.
- **@mui/icons-material:** This library provides a wide range of icons for use in the user interface. It is licensed under the MI license
- **@quasar/extras y quasar:** We use these tools for the rapid development of responsive and beautifully designed web applications. Both are under the MIT license.
- **pinia:** For application state management in Vue.js, we have used pinia version 2.1.7, under the MIT license.
- **sweetalert2:** We used sweetalert2 version 11.6.13 to display custom modal windows in the user interface. It is under the MIT license.
- **tailwindcss:** This tool provides us with a class-based development approach for creating custom styles. We use version 3.4.3, under the MIT license.
- **vue and vue-router:** We use these libraries for the development of the dynamic user interface and route management in the Vue.js application. Both are under the MIT license.

These third-party libraries and tools were selected for their technical suitability and compatibility with our development requirements. We have ensured that all licenses are compatible for use in our project and have complied with the terms set by the relevant copyright owners.

#### License and Project Privacy

The project will be kept private, which means that its access will be limited to a specific group of authorized users. To meet these requirements, we have opted for a suitable license that allows private use of the software, such as the MIT License or the Apache License 2.0, both of which are compatible with the privacy and restricted access of the project.

### 6. RISKS AND MEASURES. <a name="id6"></a>

During the development of the logistics management project, we have faced various challenges and risks that have required a proactive response and specific measures to mitigate their impact on the progress of the project. Some of the issues that have arisen and the actions taken to address them are detailed below:

1. **Challenges in Learning New Technologies:**

   - Problem: One of the initial challenges was the need to learn and master new technologies, such as Vue.js and Docker, which were fundamental for the development of the project.
   - Action Taken: A training and self-learning plan was established for the team, which included tutorials, online courses and practice sessions. In addition, specific tasks were assigned and collaboration among team members was encouraged to share knowledge and solve technical challenges together.

2. **Delays in the Implementation of Functionalities:**

   - Problem: There were some delays in the implementation of certain functionalities due to technical complexity or lack of clarity in the requirements.
   - Action Taken: Additional meetings were held with the client to clarify requirements and prioritize critical functionalities. In addition, additional resources were allocated and the development plan was reevaluated to optimize the time and resources available.

3. **Task Overload at Specific Points in Time:**

   - Problem: At some stages of the project, there was an overload of tasks due to a backlog of deliverables or unequal allocation of work.
   - Action Taken: The work plan was reviewed and adjusted to distribute tasks evenly among team members. Prioritized key activities and allocated additional resources where necessary to ensure timely completion of deliverables.

4. **Challenges in the Integration of External Services:**

   - Issue: Difficulties were encountered during the integration of external services, such as the Mapbox API, due to lack of clear documentation or technical issues.
   - Action Taken: Performed extensive testing and worked closely with external service providers to resolve identified issues. Open and transparent communication was established to address any integration issues effectively and ensure proper system functionality.

5. **Combine Project Time with Internship Time:**
   - Problem: Difficulties arose in balancing the time dedicated to project development with the time required to complete the team's academic internships.
   - Action Taken: Coordinated flexible schedules and assigned tasks and responsibilities in a way that allowed team members to fulfill their academic obligations while contributing to the project's progress. Prioritized open and transparent communication to ensure effective collaboration and maintain a healthy balance between project work and academic internships.

In summary, throughout the development of the logistics management project, we have faced several challenges and risks that have required a proactive response and specific measures to address them. Through team collaboration, careful planning and effective communication with the client, we were able to overcome these challenges and move towards the successful delivery of the project.

### 7. DEGREE OF COMPLIANCE IN SCOPE. <a name="id7"></a>

#### Covered Features:

- Inventory Management: Solid functionality has been developed for inventory management, which allows precise tracking of stock levels, product receipt and storage.
- User Management with Roles: The platform includes a user management system with defined roles, ensuring that each team member has appropriate access and permissions based on their responsibilities.
- Router for Orders and Routes: A routing tool has been implemented that allows the creation and visualization of routes for orders, making it easier for truckers to efficiently distribute products.

#### Features Not Covered:

- Automation in Inventory Management: Although the inventory management functionality has been developed, it is recognized that it could have gone deeper into the automation of certain processes, such as inventory replenishment or the generation of alerts for low stock levels.
- Chat Functionality: The chat implementation, which was initially planned, has not been carried out. This could be due to time constraints, resources, or changed priorities during the development of the project.

#### Reasons:

The lack of automation in inventory management can be attributed to the additional complexity involved in implementing algorithms and business logic to manage these processes efficiently.
Non-implementation of chat was mainly due to time, as developing real-time chat functionality may require considerable dedication in terms of development and testing. We planned a little ambitiously what we wanted to do and we ran out of time.

In general, although most of the projected functionalities have been covered, it is important to evaluate the reasons behind the unimplemented functionalities and consider whether they can be addressed in future iterations of the project.

### 8. DEGREE OF COMPLIANCE ON TIME. <a name="id8"></a>

The development of the logistics management project has mostly followed the established planning, however, there were certain deviations that require attention. In general terms, the pace was maintained and the deadlines were met, with the exception of the chat functionality, which was not completed within the estimated time. This deviation could be attributed to an initial underestimation of the technical complexity or the resources required for its implementation. The fact of also having practice hours has affected not having arrived on time for the chat.

Additionally, some weeks were identified in which too many tasks were assigned, leading to a backlog of work and potential delays in completing some activities. However, the team demonstrated its ability to adapt and overcome these challenges by dedicating additional effort, keeping the project on track with minimal delays of one or two days. This meant many hours of work at specific times, but at least we managed to stay within the established dates with very little delay.

This process highlights the importance of proactive time management and careful planning to avoid task overload and ensure equitable distribution of work throughout the project. Furthermore, it highlights the need to regularly review and adjust project planning, as well as to effectively manage risks and maintain open and transparent communication within the team to identify and address potential obstacles during project execution.

Despite the aforementioned deviations, the team demonstrated its commitment and ability to adapt to the circumstances, which allowed it to keep the project on track and achieve most of the milestones satisfactorily. These experiences will serve as important learnings for future projects, reinforcing the team's ability to effectively manage time and resources in complex and dynamic projects.

### 9. DEGREE OF COMPLIANCE IN COST. <a name="id9"></a>

During the development of the logistics management project, we are pleased to report that we have managed to accurately estimate the associated costs and, in fact, we have observed that the expenses have been even lower than initially anticipated. This situation is largely due to the fact that DigitalOcean droplets, which made up a significant portion of our cloud infrastructure costs, turned out to be cheaper than we had anticipated in our financial planning.

Our initial estimate of project costs was carried out with a rigorous and detailed approach, taking into account various factors such as software development, cloud services, third-party tools and other related expenses. Despite this careful planning, we are pleased to note that our practical implementation has resulted in lower costs than budgeted.

The free nature of DigitalOcean droplets has been a pleasant surprise and has contributed significantly to this cost reduction. This situation has allowed us to not only meet our financial expectations, but also have additional resources that we can allocate to other areas of the project to further improve and optimize our logistics management platform.

This achievement is a testament to our ability to make accurate estimates and to efficiently manage our financial resources. We are proud to have demonstrated effective control over project costs and are committed to continuing to maintain this financial discipline throughout the entire project life cycle.

All costs are in the [preliminary project](https://github.com/alherdom/Adalogix/tree/final-memory?tab=readme-ov-file#6-cost-estimation-).

### 10. CLAUSES. <a name="id10"></a>

With the aim of establishing a clear and transparent development for the execution of the project, a series of contractual clauses have been defined that address various aspects related to the development, quality and financial management of the project.

1. Deadlines and Delays:

In the event of delay in the delivery of agreed milestones or deliverables, a mechanism for notification and evaluation of the causes of the delay will be established. Depending on the severity and circumstances of the delay, penalties or schedule adjustments may be applied to ensure timely completion of the project.

2. Payments and Billing:

Project-related payments will be made in accordance with specific milestones or deliverables achieved, as agreed in the contract. A payment schedule will be established that reflects important project milestones and corresponding invoices will be issued based on these milestones.

3. Quality Control:

A comprehensive quality control system will be implemented to ensure that all project products and deliverables meet established standards and requirements. This will include extensive testing, peer reviews and user validations to ensure the quality and functionality of the developed software.

4. Change Management:

A formal process will be established for managing changes to the scope, requirements or any other aspect of the project that may affect its execution. All proposed changes will be evaluated in terms of impact on schedule, budget and quality before implementation.

5. Intellectual Property and Copyright:

Clear clauses related to intellectual property and copyright will be established to ensure that all parties involved in the project maintain ownership and control over their respective intellectual assets. Appropriate use and protection of intellectual property rights related to the project will be agreed upon.

6. Confidentiality and Data Protection:

Appropriate confidentiality and data protection measures will be established to ensure the security and privacy of confidential information shared during the course of the project. Clear provisions will be agreed for the handling and protection of sensitive information of all parties involved.

7. Conflict Resolution:

In the event of disputes or conflicts related to the project, a formal conflict resolution procedure will be established that promotes open communication and the search for mutually satisfactory solutions. Mediation or arbitration options may be considered to resolve disputes quickly and efficiently.

These contractual clauses provide a robust and transparent framework for the execution of the logistics management project, ensuring that all parties involved clearly understand their roles, responsibilities and expectations throughout the project life cycle.

### 11. FINAL PRODUCT. <a name="id11"></a>

The implemented functionalities have been described in previous sections. To summarize again, the application has a customized inventory management in which we will be able to see all the products that the company has and also see in which stores they are located among other features that we will describe later. On the other hand, we have the customized management of users with different roles, in which there will be an administrator who can create profiles of workers with their respective role (this includes limited access to certain features depending on the role of the worker). Finally, we have a router where administrators can create delivery routes and assign them to the delivery workers, who will be able to see the assigned route in their routes section as well. Once this summary is done, we will explain the application in detail.

#### Home page

The home page currently only hosts the logo of our project. In future implementations, in this section could appear some of the automations that time has not allowed us to finalize. For example a notice with the products with low stock, a summary of the routes of the last week or a small box with the active users or employees available at the moment. Right now it acts as a welcome page. On the left, you will find a sidebar where the rest of the sections are hosted.

#### Inventory page

As we have already mentioned, our project is made up of several applications that could even work independently of the project. The first one is the inventory. We wanted to make an agile and efficient inventory management so that employees can have an overview of their products. In this section, you will find a table with all the products of the company and its stock in general (counting all the warehouses/stores). In the upper part there is a search engine, which will allow you to search for any product by several fields (Name, description, category). In this same table of products, on the right side there is a section of actions to interact with the products. The pencil button will allow you to edit the products and then save them, and the button on the right will allow you to access the product detail, in which you will see in detail in which stores/warehouses the product is found and how much stock there is in each of them. Also in the upper part there are three buttons to: delete and export to csv products (selecting them in the table on the left) and another one to load products through a CSV (following the structure of the table). Finally, in this section we can also modify how the products are displayed in the table. In the headers, we can sort the products by each of them and at the bottom right, we can also make a dynamic pagination by customizing how many products we want to see per page.

#### Router

The router is another of our applications. In it, the administrator will be able to create routes for the delivery of goods. This section of the application will look different depending on the role of the user, since the deliverymen will not be able to create routes but they will see the route assigned to them by a deliveryman. They will see in detail on the map the route that has been assigned to them ordered by points, where 1 is the warehouse of collection of products and the rest are the places of delivery. When the delivery person finishes his route he has a button at the bottom of the map where he can finish his work and this will automatically put him in the role of available again so that an administrator can assign him a new delivery. Generally speaking, this is all that a delivery person will encounter.

On the other hand, if the user has an administrator role, he will be able to manipulate this section much more. First of all, on the right hand side you will have a small sidebar that will allow you to configure some parameters for the route. First, you will be able to choose the starting point, which are the warehouses/stores that the company has registered. Secondly, you will be able to choose the delivery person to whom the route will be assigned. With the parameters configured, the administrator can begin to make the route. For this, you have two possibilities, first you can click on the map the points you want and these will be added or second you can use the option in the sidebar that allows you to search by street, in which you would put the name of the specific place and should give the add button. Finally, with the route done, the administrator can use the calculate button that is responsible for painting in order the most efficient route according to the points indicated and then you can save the route with the save button. If the administrator makes a mistake or changes his mind during this process, he can restart the process.

#### User management

User management is the last of our applications. It is a section very similar to the inventory one. As mentioned before, in this section the user with administrator role will be able to view, edit and create users for the company. As in the inventory, there is a search bar to be able to search for users by all their fields. Also, on the left side there are checkboxes to download the workers to CSV or to delete them with the buttons above. Another of the functionalities that an administrator can take advantage of is to create users, in which he/she will enter his/her data and the password generated will be sent to the e-mail. Finally, this section also has dynamic pagination and the possibility of editing the user data selected.

### 12. LESSONS LEARNED TO BE TAKEN INTO ACCOUNT IN FUTURE PROJECTS. <a name="id12"></a>

During the development of the Adalogix project, we have acquired a series of valuable experiences that will be fundamental to guide future projects. These lessons learned cover crucial aspects ranging from initial planning to project execution and stick to dates planed.

One of the key points we highlight is the importance of detailed resource planning. We have understood the need to exhaustively evaluate the necessary resources, both in terms of time, personnel, infrastructure and budget. This careful planning allowed us to have a clear view of the project requirements from the beginning and helped us avoid unpleasant surprises along the way. We could have been a little less ambitious at the beginning of the approach so as not to have had to leave behind a functionality, but that ambition is what has led us to achieve the rest of the functionalities in the most optimal way possible.

In addition, we have recognized the importance of continuous learning of new technologies. The willingness to master tools such as Vue.js, Docker and the integration of APIs from services such as Mapbox was fundamental to the success of the project. Investing time in team training and training allowed us to address technical challenges with confidence and effectiveness. We also highlight the adaptation that we have had to make to leave the SSR paradigm and integrate a fronted with the backend acting as an API

Another valuable lesson we have learned is the need for effective time management. Throughout the project, we have experienced the importance of maintaining an appropriate balance in the distribution of work and periodically adjusting the schedule to avoid overloads and meet established deadlines.

Regarding cost estimation, we have observed that an accurate estimate is essential for the viability of the project. It is essential to consider all possible variables and take into account factors such as the free nature of services such as DigitalOcean droplets, which can significantly influence total costs.

Additionally, we have reaffirmed the importance of quality management and change control. Implementing a strong quality control system and effective change management allowed us to deliver a high-quality final product that met the client's requirements.

In terms of communication and collaboration, we have learned that fostering open and collaborative communication within the team and with external stakeholders is essential to keeping the project on track and addressing challenges effectively.

On top of all this, we have learned how important it is to prioritize early deployment, as it not only streamlines the development process, but also allows us to identify and address integration challenges and potential bugs early on, promoting a more stable and efficient delivery.

In summary, the experiences learned during the development of the logistics management project have provided us with a solid foundation to face future projects with confidence and effectiveness. These lessons have taught us the importance of detailed planning, continuous learning, effective time and resource management, and open and collaborative communication. With these lessons in mind, we are prepared to address future challenges with determination and success.

### 13. CONCLUSIONS, COMMENTS AND FINAL ASSESSMENT. <a name="id13"></a>

The logistics management project has been a comprehensive learning process that has provided a deep understanding of the challenges and opportunities inherent in software development in a dynamic business environment. Through this project, we have strengthened our ability to address complex problems and consolidated our knowledge in various areas, from software development to resource management and effective communication.

One of the most significant conclusions is the importance of collaboration and teamwork in the success of any project. Our team's ability to collaborate effectively, share knowledge, and address challenges together has been instrumental in overcoming obstacles and achieving our goals. Additionally, we have learned the importance of clear communication and transparency at all stages of the project, from initial planning to final delivery.

Another notable finding is the need for rigorous planning and effective time and resource management. We have experienced the importance of carefully evaluating the resources required and adjusting our planning as necessary to ensure timely, high-quality project delivery. This ability to adapt and respond nimbly to changes in the project environment has been instrumental in staying on course and overcoming unexpected challenges.

Furthermore, we have reaffirmed the importance of quality at all stages of software development. Implementing a robust quality control system and conducting extensive testing has allowed us to deliver a final product that meets the highest standards of quality and customer satisfaction. This attention to quality not only ensures customer satisfaction, but also contributes to the long-term reputation and credibility of our company.

#### Final assessment:

Ultimately, we consider the logistics management project to have been a resounding success. We have managed to develop an innovative and functional software solution that meets customer requirements and offers real value to their business. In addition to meeting the technical and functional objectives of the project, we have strengthened our skills and capabilities as a team and established a solid foundation for future initiatives.

#### Additional comments:

As we reflect on the logistics management project, we are grateful for the lessons learned and experiences gained along the way. We would like to express our gratitude to all team members for their hard work, dedication and commitment to the success of the project. Your contribution has been fundamental to achieving our objectives and we are proud of what we have achieved together.

Looking to the future, we are excited by the opportunities that await us and the prospects for continued growth and development. We will continue to apply the lessons learned in this project to future initiatives, constantly seeking to improve and exceed our clients' expectations. We are eager to face new challenges and achieve new achievements as we continue to move forward as a team and as a company.
