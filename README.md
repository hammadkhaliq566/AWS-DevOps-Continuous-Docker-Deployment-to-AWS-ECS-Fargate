# AWS DevOps Continuous Docker Deployment to AWS ECS Fargate using CloudFormation
## Application Architecture
![Alt](https://github.com/hammadkhaliq566/AWS-DevOps-Continuous-Docker-Deployment-to-AWS-ECS-Fargate/blob/64d25d1bf76e1f02eba460c0b4340a1c48242c29/resources/AWS%20DevOps%20Project%20ECS.drawio.png)

## Project Overview
<p align="justify"> Welcome to this cutting-edge DevOps project, where I'll guide you through a professional workflow for continuously deploying your Dockerized application to AWS Elastic Container Service (ECS) Fargate. Our primary goal is to create a robust CI/CD pipeline that will automatically build and deploy your application whenever you push changes to your GitHub repository. Thanks to AWS CodePipeline, this process becomes a breeze as it will trigger the pipeline whenever it detects changes in your source code. Leveraging the power of AWS CodeBuild, we'll smoothly build the Docker image and securely store it in Amazon Elastic Container Registry (ECR) for impeccable version control. Then, we'll set up an automated deployment process on ECS Fargate to ensure your updated service runs seamlessly without any manual intervention. And guess what? We've got you covered with a pre-configured CloudFormation stack template, so you won't have to worry about any manual infrastructure creation. Just deploy the stack, and your CI/CD workflow will be up and running in no time!
 </p>

## AWS Services Utilized

The project employs various AWS services to create a scalable, reliable, and fully automated CI/CD pipeline. The AWS services used are as follows:

- __Amazon Virtual Private Cloud (VPC)__: A logically isolated section of the AWS Cloud to deploy resources securely.
- __Internet Gateway__: Provides internet access to the VPC's public subnets.
- __Public and Private Subnets__: Segregates resources with public and private network access.
- __NAT Gateway__: Enables instances in the private subnets to access the internet.
- __Application Load Balancer (ALB)__: Distributes incoming traffic to ECS tasks in the Private subnet for high availability.
- __Amazon ECS Cluster__: A managed cluster to deploy and run ECS tasks.
- __Amazon ECS Service__: Defines the task definition and desired task count to run on the ECS cluster.
- __Amazon Elastic Container Registry (ECR)__: A fully managed Docker container registry to store Docker images.
- __AWS CodeBuild__: Builds the Docker image from the application source code and pushes it to ECR.
- __AWS CodePipeline__: Orchestrates the CI/CD workflow and integrates different stages.
- __Amazon EventBridge__: Monitors CodeBuild and ECS events and triggers SNS notifications.
- __Amazon Simple Notification Service (SNS)__: Sends notifications to subscribers about build and deployment events.
- __AWS CloudFormation__: Used to create and manage the AWS resources for the infrastructure as code.
- __AWS Identity and Access Management (IAM)__: Manages access and permissions to AWS resources.
- __Amazon CloudWatch__: Monitors and collects metrics, sets alarms, and provides insights into the performance of AWS resources and applications.
- __GitHub__: Version control repository that stores the application code and is integrated with AWS CodePipeline to trigger builds and deployments.

## Project Workflow

1. **VPC and Subnets Setup**: The project sets up a VPC with public and private subnets across multiple Availability Zones (AZs). ECS tasks run in private subnets, while resources requiring internet access are deployed in public subnets.

2. **Internet Access with NAT Gateway**: Instances in the private subnets can access the internet through a NAT Gateway for updates and package installations.

3. **ALB for Load Balancing**: The Application Load Balancer distributes incoming traffic to ECS tasks in the public subnet, ensuring high availability and scalability.

4. **ECS Cluster and Service**: The managed ECS cluster orchestrates the deployment of ECS tasks. The ECS service defines the task definition and desired task count to run on the ECS cluster.

5. **Amazon ECR for Docker Images**: Docker images are stored in Amazon ECR, a fully managed container registry.

6. **CI/CD with AWS CodePipeline**: AWS CodePipeline automates the CI/CD workflow. It watches the GitHub repository for changes, triggers the pipeline, and manages the build and deployment stages.

7. **AWS CodeBuild for Docker Builds**: CodeBuild fetches the source code from the GitHub repository, builds the Docker image, and pushes it to ECR.

8. **ECS Fargate Deployment**: CodePipeline updates the ECS service with the new Docker image, creating a rolling update without downtime.

9. **EventBridge and SNS Notifications**: Amazon EventBridge monitors for CodeBuild and ECS events and triggers SNS notifications. Subscribers receive email notifications about build and deployment events.

## Getting Started

### Prerequisites
Here are the prerequisites for this solution:

- __AWS Account__: You must have an AWS Account and relevant Permissions.
- __Fork GitHub Repo__: Fork and clone your own hammadkhaliq566/AWS-DevOps-Continuous-Docker-Deployment-to-AWS-ECS-Fargate GitHub repository
- __OAuth Token__: Create an OAuth token in GitHub and provide access to the admin:repo_hook and repo scopes.

### Implementation

- __AWS CloudFormation__: All of the resource generation of this solution is described in CloudFormation which is a declarative code language that can be written in YAML.
### Deployment Steps

1. Fork this GitHub repository.
  
2. Clone to you local Machine

3. Modify the necessary parameters in the CloudFormation templates to match your requirements, such as region, VPC settings, etc.

4. Deploy the CloudFormation stack that creates the VPC, subnets, and ECS cluster etc

5. Sign in to the AWS Management Console and navigate to the CloudFormation service.
   
6. Click on the "Create Stack" button to start creating a new stack.
Choose a template:
In the "Choose a template" section, select "Template is ready" and "Upload a template file."
Click on "Choose file" and select the CloudFormation template file from your local machine.
Click "Next" to proceed.

![Alt](https://github.com/hammadkhaliq566/AWS-DevOps-Continuous-Docker-Deployment-to-AWS-ECS-Fargate/blob/3a89525f8f804d564b4048e2c9f299a20783ae8e/resources/cloudformation%201.png)

7. In the "Specify stack details" section, provide a Stack Name to identify your CloudFormation stack and Click "Next" to proceed
   
![Alt](https://github.com/hammadkhaliq566/AWS-DevOps-Continuous-Docker-Deployment-to-AWS-ECS-Fargate/blob/3a89525f8f804d564b4048e2c9f299a20783ae8e/resources/cloudformation%202.png)

8. Review the settings you have chosen for the CloudFormation stack.
If everything looks correct, click "Create stack" to start the stack creation process.

![Alt](https://github.com/hammadkhaliq566/AWS-DevOps-Continuous-Docker-Deployment-to-AWS-ECS-Fargate/blob/3a89525f8f804d564b4048e2c9f299a20783ae8e/resources/cloudformation%203.png)

9. Monitor the stack creation:
The stack creation process may take a few minutes to complete. You can monitor the progress in the AWS CloudFormation console.
Once the stack creation is complete, the status will change to "CREATE_COMPLETE."

![Alt](https://github.com/hammadkhaliq566/AWS-DevOps-Continuous-Docker-Deployment-to-AWS-ECS-Fargate/blob/d30813a98d1c1106739dcccbaa700fcdcfc3d8a9/resources/cloudformation%204.png)

10. Congratulations! You have successfully created a CloudFormation stack using the AWS Management Console. The stack should now be up and running, and you can access the resources created by the stack, such as the VPC, subnets, ECS cluster, ALB, etc.

### Let's take a look at some of the resources
1. __VPC__:
   
![Alt](https://github.com/hammadkhaliq566/AWS-DevOps-Continuous-Docker-Deployment-to-AWS-ECS-Fargate/blob/5b29b306d1595c6843d1500cf460f1dd71b90f23/resources/cloudformation%208.png)

2. __ECS Service__:
   
![Alt](https://github.com/hammadkhaliq566/AWS-DevOps-Continuous-Docker-Deployment-to-AWS-ECS-Fargate/blob/5b29b306d1595c6843d1500cf460f1dd71b90f23/resources/cloudformation%205.png)

3. __ECR Repository__:
   
![Alt](https://github.com/hammadkhaliq566/AWS-DevOps-Continuous-Docker-Deployment-to-AWS-ECS-Fargate/blob/5b29b306d1595c6843d1500cf460f1dd71b90f23/resources/cloudformation%206.png)

4. __Application Load Balancer (ALB)__:
   
![Alt](https://github.com/hammadkhaliq566/AWS-DevOps-Continuous-Docker-Deployment-to-AWS-ECS-Fargate/blob/5b29b306d1595c6843d1500cf460f1dd71b90f23/resources/cloudformation%207.png)

### To Access Application
To access the application, follow these steps:
1. Go to the AWS Management Console and navigate to the CloudFormation service.
2. Find the stack you created for this project and click on it.
3. In the stack details page, go to the "Outputs" tab.
4. Under "Outputs," you will see a key-value pair named "ALBDNSName." This value represents the DNS name of the Application Load Balancer (ALB) that is distributing traffic to the ECS tasks.
5. Click on the "ALBDNSName" value to open the application in your web browser.

![Alt](https://github.com/hammadkhaliq566/AWS-DevOps-Continuous-Docker-Deployment-to-AWS-ECS-Fargate/blob/7bd9104b2f4dc259b56ce54579f8cde0d9b4ec6c/resources/cloudformation%2010.png)

### Now take a look at Application:
![Alt](https://github.com/hammadkhaliq566/AWS-DevOps-Continuous-Docker-Deployment-to-AWS-ECS-Fargate/blob/ac7209c75bf2027b5fee6855a63a3bee6b808adf/resources/cloudformation%2011.png)

### Test Deployment:
1. Make the desired changes:
   
Open the app.py file of your application.
Locate the section responsible for the background color.
Change the background color to green.
Save the changes.
![Alt](https://github.com/hammadkhaliq566/AWS-DevOps-Continuous-Docker-Deployment-to-AWS-ECS-Fargate/blob/a2f3f8a4a0abf4b890983fa0f5e8fd30baa7e751/resources/changing%20Code.png)

2. Commit Changes to GitHub:
   
Push the modified app.py file to your GitHub repository.
Ensure that the changes are successfully pushed to the main branch.
![Alt](https://github.com/hammadkhaliq566/AWS-DevOps-Continuous-Docker-Deployment-to-AWS-ECS-Fargate/blob/a2f3f8a4a0abf4b890983fa0f5e8fd30baa7e751/resources/git%20commands.png)

3. Check the AWS CodePipeline:

Navigate to the AWS Management Console and go to the CodePipeline service.
Locate the CodePipeline associated with your project.
You will notice that the pipeline has been triggered automatically due to the code change.
![Alt](https://github.com/hammadkhaliq566/AWS-DevOps-Continuous-Docker-Deployment-to-AWS-ECS-Fargate/blob/a2f3f8a4a0abf4b890983fa0f5e8fd30baa7e751/resources/pipeline-triggered.png)

4. Observe the Deployment:

Once the pipeline starts executing, it will build the Docker image with the updated code.
The new Docker image will be pushed to the Amazon ECR repository.
The AWS CodeDeploy stage will update the ECS service, ensuring a rolling update without downtime.
![Alt](https://github.com/hammadkhaliq566/AWS-DevOps-Continuous-Docker-Deployment-to-AWS-ECS-Fargate/blob/a2f3f8a4a0abf4b890983fa0f5e8fd30baa7e751/resources/cloudformation%209.png)

5. View the Updated Green App:

Go to the Amazon ECS service and select your ECS cluster.
Click on the ECS service that corresponds to your application.
Observe the "Events" tab to track the deployment progress.
Once the deployment is complete, you will see the "Running" status for the tasks.
To access the updated green app, copy the ALB DNS name from the CloudFormation output section.
Open your web browser and paste the ALB DNS name in the address bar.
Hit "Enter" or click "Go," and you will see the new green app with the updated background color.
![Alt](https://github.com/hammadkhaliq566/AWS-DevOps-Continuous-Docker-Deployment-to-AWS-ECS-Fargate/blob/a2f3f8a4a0abf4b890983fa0f5e8fd30baa7e751/resources/green%20app.png)

### CleanUp Resources
To clean up the CloudFormation stack, you can follow these steps:
1. Open the AWS Management Console and navigate to the CloudFormation service.
2. Select the stack you want to delete from the list of existing stacks.
3. Click on the "Delete" button from the top menu to initiate the stack deletion process.
4. Confirm the stack deletion when prompted. Please note that this action will delete all resources created by the stack.
5. Wait for the stack deletion to complete. Depending on the complexity of the stack, it may take some time to remove all the resources.
6. Verify that the stack has been successfully deleted from the list of stacks.

## Contributing
Pull requests are welcome. For major changes or enhancements, please open an issue first to discuss what you would like to change.

## Thank You
Thank you for exploring this cutting-edge DevOps project! I hope this README file provided you with valuable insights into our professional workflow for continuously deploying Dockerized applications to AWS Elastic Container Service (ECS) Fargate. As technology evolves, we are committed to staying at the forefront of innovation and offering seamless solutions for our users. If you have any questions, feedback, or suggestions, please don't hesitate to reach out to me. Thank you for being a part of our journey toward excellence in DevOps and cloud computing. Happy coding!
