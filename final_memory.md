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

1. [**_INTRODUCCIÓN._**](#id1)
2. [**_TECNOLOGÍAS UTILIZADAS._**](#id2)
3. [**_GUIA DE ESTILO DE LA WEB._**](#id3)
4. [**_INVESTIGACIÓN._**](#id4)
5. [**_DERECHOS DE AUTOR._**](#id5)
6. [**_RIESGOS Y MEDIDAS._**](#id6)
7. [**_GRADO DE CUMPLIMIENTO EN ALCANCE._**](#id7)
8. [**_GRADO DE CUMPLIMIENTO EN TIEMPO._**](#id8)
9. [**_GRADO DE CUMPLIMIENTO EN COSTE._**](#id9)
10. [**_PRODUCTO FINAL._**](#id10)
11. [**_EXPEIRNECIAS APRENDIDAS A TENER EN CUENTA EN PRÓXIMOS PROYECTOS._**](#id11)
12. [**_CONCLUSIONES, COMENTARIOS Y VALORACIÓN FINAL._**](#id12)

### 1. INTRODUCTION. <a name="id1"></a>

In an increasingly interconnected and dynamic world, efficiency in logistics management becomes a critical factor for business success. In order to meet this need, we have developed this application that focuses on the optimization of resource management in an inventory, a customized user management with different roles to meet the needs of administrators, store managers and couriers, and a router so that routes can be organized for the delivery of goods and couriers can start the journey knowing all the information they need to know.

#### Inventory management:

Our platform offers a robust inventory management tool that allows companies to maintain precise control of their stock. From product receipt to storage and distribution, our solution facilitates real-time monitoring of stock levels, identification of critical products and optimization of available resources. The developed application is prepared to manage both global stock and the stock of specific warehouses or stores. The optimization also applies to product loading, allowing the company to record stock entries through csv format.

#### User Management with Defined Roles:

We understand that each employee plays a unique role in the logistics process. Therefore, our platform offers a user management system with defined roles, which allows specific permissions and responsibilities to be assigned according to the needs of each individual. From administrators overseeing the system to warehouse operators and couriers, our solution ensures efficient and secure collaboration.

#### Dynamic Route Planning:

Efficient product distribution is essential to meet delivery deadlines and satisfy customer demands. With our integrated routing tool, companies can create delivery routes intuitively that are automatically optimized.

In summary, our web platform offers a comprehensive solution for logistics management, allowing companies to improve operational efficiency, reduce costs and provide exceptional service to their customers. With an intuitive interface and powerful tools, we are committed to helping companies achieve their logistics objectives effectively in an increasingly competitive and demanding business environment.

### 2. TECNOLOGÍAS UTILIZADAS. <a name="id2"></a>

To build our logistics management web platform, we have carefully selected a set of advanced technologies that ensure optimal performance, exceptional user experience, and seamless scalability. Also these technologies were selected based on the experience of our development experience.

#### Backend:

- **_Python 3.12:_** Python is a versatile and powerful programming language that has allowed us to develop the backend of our application with efficiency and flexibility. We've been working with this language for almost 2 years so we got straight to the point and didn't have to learn any new technology for this part. The version used was 3.12 offers us the latest features and improvements, guaranteeing the most modern possible functionalities of Python.
- **_Django 5.0:_** Django is a high-level Python-based web framework that provides a solid foundation for fast and secure web application development. With its focus on simplicity and efficiency, we have used Django 5.0 to build the backend of our platform, taking advantage of its wide range of features, from user authentication to database management.
- **_Django Rest Framework 3.15:_** For creating and managing a robust and flexible API, we have integrated Django Rest Framework into our application. This powerful tool allows us to design and expose RESTful endpoints that facilitate communication between the frontend and backend efficiently and securely.
- **_PostgreSQL:_** For efficient database management, we have deployed a Docker container using a PostgreSQL image. Docker allows us to encapsulate the database and its dependencies in a consistent and portable environment, simplifying the deployment and management of our application. For keep the data even if the container fails, we've added volumes to ensure the data is correctly saved.

#### Frontend:

- Vue 3: To offer a dynamic and responsive user experience, we have opted for Vue.js 3 together with the Composition API, a powerful combination that allows us to structure our code in a more intuitive and modular way. With the Composition API, we have created highly functional, interactive user interfaces that allow users to seamlessly interact with our backend. In the first steps of the application, the framework we had selected was React, but to take advantage of the technologies that were going to be used in the internship period we decided to change to Vue.

#### Deployment:

- DigitalOcean Droplet: For our application deployment, we have chosen DigitalOcean, a reliable and easy-to-use cloud infrastructure platform. We have implemented our application in a basic DigitalOcean droplet, which has allowed us to launch our platform quickly and efficiently, guaranteeing optimal uptime and scalability appropriate to our needs.

### 3. GUIA DE ESTILO DE LA WEB. <a name="id3"></a>

In this section, we generally describe the style guide or standards that we have followed to develop the solution

#### Minimalism and Clarity:

The user interface should follow a minimalist approach, with a clean and organized design that makes it easy to navigate and understand the information.
Sober colors and appropriate contrasts to highlight important elements without distracting the user should be used to develop a clean and easy to use interface.

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

### 4. INVESTIGACIÓN. <a name="id4"></a>

In this project we have used technologies that in one way or another we had seen before, but that does not mean that we have had to investigate. We had to learn about some aspects so that the final product was the best possible. Some of the fields in which we have investigated have been:

#### Vue.js learning:

We faced with the need to build the frontend of the platform with another language/framework different from the backend, so we immersed ourselves in learning the Vue.js framework. Through tutorials, official documentation, and practical examples, we've acquired the skills necessary to develop dynamic and responsive user interfaces. This one was a hard challenge because is a very different way to code than using SSR.

#### Docker exploration:

We also faced the challenge of managing the PostgreSQL database in a controlled and portable environment. This decision was made to avoid the configuration of PostgreSQL database in every system (every developer system and also in production) so we decided to use Docker. We investigated fundamental Docker concepts, such as containers and images, and learned how to deploy and manage a PostgreSQL container for our application.

#### Connection with Mapbox API:

To integrate mapping capabilities into the platform for developing the router, we dove into Mapbox's documentation and explored how to consume its API to display interactive maps and create delivery routes. We learned how to properly authenticate, send requests, and process responses to incorporate this vital functionality into your application. This was a very important part of investigation because the router was one of our main focus while developing the solution.

#### Backend-Frontend Integration:

Since we were using server-side rendering development during all the academic year, we faced a new challenge in connecting the Django backend with the Vue.js frontend. We investigated different methods of communication between the two, such as creating a RESTful API and handling HTTP requests, to achieve a smooth and efficient integration between both sides of the application. As we said in the last section, Django Rest Framework was the main resource to look in backend and asyn requests was the option for the front.

#### Conclusions and Reflections of investigation:

Throughout this learning process, we have demonstrated a remarkable ability to acquire new skills and address technical challenges effectively. Our willingness to investigate, experiment and solve problems has been essential to the successful development of the logistics management platform.
This project has not only expanded our technical skill set, but has also strengthened your ability to face new challenges and adapt to changing development environments. These experiences will surely serve us in future projects and will help to continue growing as a professional team in the field of technology.

Furthermore, and although it will be explained later, due to lack of time we have had to leave behind another functionality which was the chat

### 5. DERECHOS DE AUTOR. <a name="id5"></a>

Debes tener en cuenta todo el contenido multimedia de la web (imágenes, audio, vídeos, etc.) y también otro tipo contenido usado (librerías, plugins, etc). Para estos contenidos, especificar:

- Si es de desarrollo propio con qué aplicación se ha desarrollado y con qué licencia se publica
- Qué material de terceros ha sido utilizado, indicando qué tipo de licencia tiene en cada caso y justificando que puedes usarlo para tu web

### 6. RIESGOS Y MEDIDAS. <a name="id6"></a>

Qué problemas han surgido durante el desarrollo del proyecto y cómo se ha actuado.

### 7. GRADO DE CUMPLIMIENTO EN ALCANCE. <a name="id7"></a>

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

### 8. GRADO DE CUMPLIMIENTO EN TIEMPO. <a name="id8"></a>

The development of the logistics management project has mostly followed the established planning, however, there were certain deviations that require attention. In general terms, the pace was maintained and the deadlines were met, with the exception of the chat functionality, which was not completed within the estimated time. This deviation could be attributed to an initial underestimation of the technical complexity or the resources required for its implementation. The fact of also having practice hours has affected not having arrived on time for the chat.

Additionally, some weeks were identified in which too many tasks were assigned, leading to a backlog of work and potential delays in completing some activities. However, the team demonstrated its ability to adapt and overcome these challenges by dedicating additional effort, keeping the project on track with minimal delays of one or two days. This meant many hours of work at specific times, but at least we managed to stay within the established dates with very little delay.

This process highlights the importance of proactive time management and careful planning to avoid task overload and ensure equitable distribution of work throughout the project. Furthermore, it highlights the need to regularly review and adjust project planning, as well as to effectively manage risks and maintain open and transparent communication within the team to identify and address potential obstacles during project execution.

Despite the aforementioned deviations, the team demonstrated its commitment and ability to adapt to the circumstances, which allowed it to keep the project on track and achieve most of the milestones satisfactorily. These experiences will serve as important learnings for future projects, reinforcing the team's ability to effectively manage time and resources in complex and dynamic projects.

### 9. GRADO DE CUMPLIMIENTO EN COSTE. <a name="id9"></a>

During the development of the logistics management project, we are pleased to report that we have managed to accurately estimate the associated costs and, in fact, we have observed that the expenses have been even lower than initially anticipated. This situation is largely due to the fact that DigitalOcean droplets, which made up a significant portion of our cloud infrastructure costs, turned out to be cheaper than we had anticipated in our financial planning.

Our initial estimate of project costs was carried out with a rigorous and detailed approach, taking into account various factors such as software development, cloud services, third-party tools and other related expenses. Despite this careful planning, we are pleased to note that our practical implementation has resulted in lower costs than budgeted.

The free nature of DigitalOcean droplets has been a pleasant surprise and has contributed significantly to this cost reduction. This situation has allowed us to not only meet our financial expectations, but also have additional resources that we can allocate to other areas of the project to further improve and optimize our logistics management platform.

This achievement is a testament to our ability to make accurate estimates and to efficiently manage our financial resources. We are proud to have demonstrated effective control over project costs and are committed to continuing to maintain this financial discipline throughout the entire project life cycle.

### 10. CLAUSULAS. <a name="id10"></a>

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

### 11. PRODUCTO FINAL. <a name="id11"></a>

Describir el producto final obtenido, qué funcionalidades se han implementado, que hay que tener en cuenta para usarla, etc. Describirlo como si fuera un pequeño MANUAL DE USO de la aplicación, ya que se usará este punto para corregir el proyecto.

### 12. EXPERIENCIAS APRENDIDAS A TENER EN CUENTA EN PRÓXIMOS PROYECTOS. <a name="id12"></a>

During the development of the Adalogix project, we have acquired a series of valuable experiences that will be fundamental to guide future projects. These lessons learned cover crucial aspects ranging from initial planning to project execution and stick to dates planed.

One of the key points we highlight is the importance of detailed resource planning. We have understood the need to exhaustively evaluate the necessary resources, both in terms of time, personnel, infrastructure and budget. This careful planning allowed us to have a clear view of the project requirements from the beginning and helped us avoid unpleasant surprises along the way. We could have been a little less ambitious at the beginning of the approach so as not to have had to leave behind a functionality, but that ambition is what has led us to achieve the rest of the functionalities in the most optimal way possible.

In addition, we have recognized the importance of continuous learning of new technologies. The willingness to master tools such as Vue.js, Docker and the integration of APIs from services such as Mapbox was fundamental to the success of the project. Investing time in team training and training allowed us to address technical challenges with confidence and effectiveness. We also highlight the adaptation that we have had to make to leave the SSR paradigm and integrate a fronted with the backend acting as an API

Another valuable lesson we have learned is the need for effective time management. Throughout the project, we have experienced the importance of maintaining an appropriate balance in the distribution of work and periodically adjusting the schedule to avoid overloads and meet established deadlines.

Regarding cost estimation, we have observed that an accurate estimate is essential for the viability of the project. It is essential to consider all possible variables and take into account factors such as the free nature of services such as DigitalOcean droplets, which can significantly influence total costs.

Additionally, we have reaffirmed the importance of quality management and change control. Implementing a strong quality control system and effective change management allowed us to deliver a high-quality final product that met the client's requirements.

In terms of communication and collaboration, we have learned that fostering open and collaborative communication within the team and with external stakeholders is essential to keeping the project on track and addressing challenges effectively.

In summary, the experiences learned during the development of the logistics management project have provided us with a solid foundation to face future projects with confidence and effectiveness. These lessons have taught us the importance of detailed planning, continuous learning, effective time and resource management, and open and collaborative communication. With these lessons in mind, we are prepared to address future challenges with determination and success.

### 13. CONCLUSIONES, COMENTARIOS Y VALORACIÓN FINAL. <a name="id13"></a>

The logistics management project has been a comprehensive learning process that has provided a deep understanding of the challenges and opportunities inherent in software development in a dynamic business environment. Through this project, we have strengthened our ability to address complex problems and consolidated our knowledge in various areas, from software development to resource management and effective communication.

One of the most significant conclusions is the importance of collaboration and teamwork in the success of any project. Our team's ability to collaborate effectively, share knowledge, and address challenges together has been instrumental in overcoming obstacles and achieving our goals. Additionally, we have learned the importance of clear communication and transparency at all stages of the project, from initial planning to final delivery.

Another notable finding is the need for rigorous planning and effective time and resource management. We have experienced the importance of carefully evaluating the resources required and adjusting our planning as necessary to ensure timely, high-quality project delivery. This ability to adapt and respond nimbly to changes in the project environment has been instrumental in staying on course and overcoming unexpected challenges.

Furthermore, we have reaffirmed the importance of quality at all stages of software development. Implementing a robust quality control system and conducting extensive testing has allowed us to deliver a final product that meets the highest standards of quality and customer satisfaction. This attention to quality not only ensures customer satisfaction, but also contributes to the long-term reputation and credibility of our company.

#### Final assessment:

Ultimately, we consider the logistics management project to have been a resounding success. We have managed to develop an innovative and functional software solution that meets customer requirements and offers real value to their business. In addition to meeting the technical and functional objectives of the project, we have strengthened our skills and capabilities as a team and established a solid foundation for future initiatives.

#### Additional comments:

As we reflect on the logistics management project, we are grateful for the lessons learned and experiences gained along the way. We would like to express our gratitude to all team members for their hard work, dedication and commitment to the success of the project. Your contribution has been fundamental to achieving our objectives and we are proud of what we have achieved together.

Looking to the future, we are excited by the opportunities that await us and the prospects for continued growth and development. We will continue to apply the lessons learned in this project to future initiatives, constantly seeking to improve and exceed our clients' expectations. We are eager to face new challenges and achieve new achievements as we continue to move forward as a team and as a company.
