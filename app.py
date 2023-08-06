from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    name = os.getenv("NAME", "World")
    # Custom CSS styles to center the text and set the background color
    style = """
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f0f0f0; /* Change this to your desired background color */
            }
            .text-container {
                text-align: center;
                background-color: #008000; /* Change this to your desired text container background color */
                padding: 20px;
            }
        </style>
    """
    # HTML content with the custom styles and dynamic text
    content = f"""
        {style}
        <div class="text-container">
            <h1>Hello, {name}!</h1>
            <p>The primary goal of this project is to deploy containers to the Amazon Elastic Container Service (ECS) Cluster, utilizing a highly secure and scalable Virtual Private Cloud (VPC) architecture with private subnets distributed across multiple availability zones. The deployment process will be optimized through the use of AWS Developer tools, facilitating a streamlined continuous integration and continuous deployment (CI/CD) pipeline. By distributing resources across multiple availability zones and employing the ALB, the system achieves high fault tolerance, minimizing the risk of single points of failure. Additionally, the implementation of Amazon EventBridge and Simple Notification Service (SNS) will ensure proactive notifications and feedback in case of pipeline failures.</p>
        </div>
    """
    return content

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 80)))
