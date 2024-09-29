### Project Update Rubric

| **Criteria**                             | **Excellent (4 points)**                       | **Good (3 points)**                     | **Fair (2 points)**                    | **Needs Improvement (1 point)**           | **Score** |
|------------------------------------------|------------------------------------------------|-----------------------------------------|-----------------------------------------|-------------------------------------------|-----------|
| **.env File Configuration**              | All required variables updated correctly.      | Most required variables updated.       | Some required variables updated.       | Few or no required variables updated.      | /4        |
| **run_docker.sh File Configuration**    | All required variables updated, optional fields appropriately handled. | Most required variables updated.       | Some required variables updated.       | Few or no required variables updated.      | /4        |
| **upload_to_gcp.sh File Configuration** | All required variables updated; optional fields addressed. | Most required variables updated.       | Some required variables updated.       | Few or no required variables updated.      | /4        |
| **deploy_to_cloud_run.sh File Configuration** | All required variables updated; correct image tag version matched. | Most required variables updated; minor tag mismatch. | Some required variables updated; tag mismatch. | Few or no required variables updated; major tag issue. | /4        |
| **Documentation and Clarity**           | Clear documentation of changes made; well-organized and easy to follow. | Mostly clear documentation; minor organizational issues. | Some documentation; clarity and organization lacking. | Poor or no documentation; hard to follow. | /4        |
| **Functionality and Testing**            | Project runs successfully with all updates; tested thoroughly. | Project runs with minor issues; some testing performed. | Project runs with major issues; little testing performed. | Project fails to run; no testing conducted. | /4        |

### Total Score: /24

---

Here’s a comprehensive project plan that incorporates all the requirements for creating and configuring a Google Cloud Platform project, including IAM identities, VPC networks, VM instances, storage buckets, MySQL databases, and deploying a Docker image to Cloud Run.

### Project Plan for Google Cloud Platform Setup

---

#### **1. Preparation Phase**

**A. Understand Requirements**
- Review the project objectives and scope.
- Ensure you have a Google Cloud account with billing enabled.

**B. Gather Tools**
- Install the Google Cloud SDK.
- Install Docker on your local machine.
- Choose a code editor for updating configuration files.

---

#### **2. IAM Configuration**

**A. Create IAM Identity**
- Navigate to **IAM & Admin** in Google Cloud Console.
- Create a new service account with the following permissions:
  - **Cloud SQL Admin**
  - **Storage Admin**
  - **Artifact Registry Admin**
  - **Cloud Run Admin**
- Record the service account email for later use.

---

#### **3. Networking Configuration** *(Optional)*

**A. Create VPC Network**
- Go to the **VPC network** section in the Google Cloud Console.
- Create a new VPC network with:
  - **Development Subnet**
  - **Production Subnet**

**B. Configure Firewall Rules**
- Set up appropriate firewall rules to allow necessary traffic (e.g., HTTP, HTTPS).

---

#### **4. VM Instance Setup** *(Optional)*

**A. Create a VM Instance**
- Navigate to the **Compute Engine** section.
- Create a new VM instance and:
  - Attach the previously created service account.
  - Grant access to Cloud SQL, Cloud Storage, Artifact Registry, and Cloud Run.
- Configure machine type and other settings as needed.

---

#### **5. Storage Bucket Configuration**

**A. Create a Storage Bucket**
- Go to the **Cloud Storage** section.
- Create a new storage bucket with:
  - A globally unique name.
  - Appropriate access permissions (e.g., public or private based on your use case).
  - Enable versioning if necessary.

---

#### **6. MySQL Database Setup**

**A. Create MySQL Database**
- Navigate to the **Cloud SQL** section.
- Create a new MySQL instance and:
  - Configure instance settings (e.g., region, tier).
  - Set root password and create a new database.
  - Note connection details for future use.

---

#### **7. Artifact Registry Setup**

**A. Create a Repository**
- Navigate to the **Artifact Registry** section.
- Create a new Docker repository to store your images.

---

#### **8. Docker Image Creation and Upload**

**A. Create Docker Image Locally**
- Write your Dockerfile and necessary application files.
- Build the Docker image using the command:
  
```bash
./run_docker.sh
```

**B. Upload Image to Artifact Registry**

Tag and push the Docker image to the Artifact Registry repository using the command:
  
```bash
./upload_to_gcp.sh
```

---

#### **9. Deployment to Cloud Run**

**A. Deploy the Image**
- Navigate to the **Cloud Run** section.
- Deploy the Docker image from Artifact Registry, ensuring you:
  - Set the service name.
  - Select the appropriate region.
  - Configure necessary environment variables (e.g., connection details for Cloud SQL).
- Enable authentication if needed.

Then run the deployment script:
  ```bash
  ./deploy_to_cloud_run.sh
  ```

---

#### **10. Update Website with Data**

**A. Configure the Website**
- Update your application code to connect to the MySQL database and use the data stored there.
- Ensure that the website is retrieving and displaying the data as intended.

---

**B. Update the Website data**
- Upload images and other content to the Cloud Storage bucket.
- Update the database with relevant information for the website like your name, bio, and other details.

#### **11. Testing and Verification**

**A. Test the Application**
- Access the Cloud Run service URL.
- Verify that the website functions as expected and interacts correctly with the database.

---

### Variables to Update in the Project

#### Notes
These variables must be updated to ensure the project functions properly. Make sure to review each section carefully.

---

| **File**                       | **Variable**                       | **Description**                                                                                               |
|--------------------------------|------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **1. `.env` File**            | **PROJECT_ID**                     | Unique identifier for your Google Cloud project.                                                              |
|                                | **BUCKET_NAME**                    | Name of the Google Cloud Storage bucket.                                                                      |
|                                | **MYSQL_UNIX_SOCKET**              | Socket for connecting to the MySQL database.                                                                   |
|                                | **CLOUD_SQL_CONNECTION_NAME**      | Connection name for the Cloud SQL instance.                                                                    |
|                                | **MYSQL_USER**                     | Username for MySQL database access.                                                                            |
|                                | **MYSQL_PASSWORD**                 | Password for the MySQL user.                                                                                  |
|                                | **MYSQL_HOST** (Optional)          | Specify if using an IP address for offline access to the SQL instance.                                         |
|                                | **MYSQL_DB**                       | Name of the MySQL database.                                                                                    |
| **2. `run_docker.sh` File**   | **PROJECT_ID**                     | Same as in the `.env` file.                                                                                   |
|                                | **[Optional] gcr.io/$PROJECT_ID/** | Remove this line if using a local Docker image instead of one from Google Container Registry.                  |
|                                | **Version** (Optional)             | Specify the version of the Docker image.                                                                       |
|                                | **Image Name** (Optional)          | Name of the Docker image.                                                                                     |
| **3. `upload_to_gcp.sh` File**| **PROJECT_ID**                     | Same as above.                                                                                                 |
|                                | **REGION**                         | The region where the resources will be deployed.                                                               |
|                                | **REPOSITORY**                     | Name of the container repository.                                                                               |
|                                | **IMAGE_NAME**                     | Name of the image being uploaded.                                                                              |
|                                | **Version in IMAGE_TAG**           | Version tag for the Docker image.                                                                              |
| **4. `deploy_to_cloud_run.sh` File** | **PROJECT_ID**                | Same as in previous sections.                                                                                  |
|                                | **REGION**                         | The region for deploying the Cloud Run service.                                                                |
|                                | **SERVICE_NAME**                   | Name of the Cloud Run service.                                                                                 |
|                                | **Version in IMAGE_TAG**           | Must match the version specified in `upload_to_gcp.sh`.                                                       |
|                                | **CLOUD_SQL_CONNECTION_NAME**      | Connection details for the Cloud SQL instance.                                                                 |
|                                | **MYSQL_USER**                     | Username for the MySQL database.                                                                                |
|                                | **MYSQL_PASSWORD**                 | Password for the MySQL user.                                                                                   |
|                                | **MYSQL_DB**                       | Name of the MySQL database.                                                                                    |
|                                | **MYSQL_UNIX_SOCKET**              | Socket for connecting to the MySQL database.                                                                   |
|                                | **BUCKET_NAME**                    | Name of the Google Cloud Storage bucket.                                                                       |

---

By updating these variables appropriately, you will ensure that your project is configured correctly and can operate as intended on Google Cloud Platform.

### Value of the Project

This Google Cloud Platform (GCP) project offers significant educational and practical value for students, providing them with hands-on experience in several key areas of cloud computing and software development. Upon completing the project, students will gain invaluable skills and knowledge that are essential in today’s technology landscape.

#### Key Learning Outcomes

1. **Cloud Infrastructure Management:**
   - Students will learn how to set up and configure cloud infrastructure, including IAM roles, VPC networks, and virtual machine instances. This knowledge is crucial for managing resources in a cloud environment.

2. **Networking and Security:**
   - Students will gain knowledge about networking concepts, including setting up firewall rules and securing cloud resources. Understanding security practices in cloud environments is essential for protecting sensitive data.

3. **Database Management:**
   - Configuring a MySQL database on GCP will provide insights into database setup, management, and connectivity. Students will learn how to store and retrieve data effectively, a core aspect of application development.

4. **Storage Management:**
   - Students will create and manage Google Cloud Storage buckets, learning about data storage best practices, access controls, and versioning. This understanding is critical for efficient data management in cloud environments.

5. **Docker and Containerization:**
   - Through the creation and deployment of Docker images, students will understand containerization concepts. They will learn how to build, run, and manage containers, which is a vital skill for modern software development and deployment.

6. **Serverless Architecture:**
   - Students will learn how to deploy applications using serverless architecture with Cloud Run, gaining experience with configuring environment variables, managing service settings, and understanding how to scale applications automatically based on demand.

7. **Troubleshooting and Problem-Solving:**
   - Working through the various stages of setup and deployment will enhance students’ troubleshooting skills. They will learn to identify issues and implement solutions, fostering a mindset of problem-solving.

8. **Documentation and Communication:**
   - The emphasis on clear documentation throughout the project will improve students' ability to communicate technical information effectively. This skill is vital for collaboration in team environments and for future project management roles.

9. **Real-World Application:**
   - By simulating real-world cloud projects, students will gain experience that is directly applicable to careers in software development, data engineering, and IT operations. This practical knowledge enhances their employability and prepares them for industry challenges.

### Conclusion

Overall, this project not only equips students with technical skills but also promotes critical thinking, collaboration, and effective communication. By the end of the project, students will emerge with a comprehensive understanding of cloud technologies and a strong foundation to pursue further studies or careers in the tech industry.