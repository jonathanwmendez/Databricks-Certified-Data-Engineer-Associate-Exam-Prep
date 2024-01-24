# Databricks notebook source
# MAGIC %md
# MAGIC **Describe the relationship between the data lakehouse and the data warehouse.**
# MAGIC
# MAGIC A Data Lakehouse can handle structured, semi-structured, and unstructured data, has cost-effective, fast, and flexible storage costs, is ACID-compliant, and is suitable for both data analytics and machine learning workloads. A Data Warehouse can only handle structured data, has costly and time-consuming storage costs, is ACID-compliant, and is only optimal for data analytics and business intelligence (BI) use-cases.

# COMMAND ----------

# MAGIC %md
# MAGIC **Identify the improvement in data quality in the data lakehouse over the data lake.**
# MAGIC
# MAGIC A Data Lakehouse has schema enforcement to improve data quality, ACID Transactions to prevent data duplication, inconsistencies, and incomplete data sets, data governance tools like metadata management, data cataloging, and lineage tracking for better organized, more traceable, and higher-quality data, easier and more efficient data cleaning and processing because it can handle both structured and unstructured data in a more organized manner, provides a unified data management platform which reduces the risks of data becoming siloed or unmanageable improving the overall quality of the data.

# COMMAND ----------

# MAGIC %md
# MAGIC **Compare and contrast silver and gold tables, which workloads will use a bronze table as a source, which workloads will use a gold table as a source.**
# MAGIC
# MAGIC Silver tables have gone through initial data processing, but are not fully refined for tailored use cases like gold tables. Bronze tables are the rawest form of data. Bronze tables are used as a source for more refined data processing stages like ETL (Extract, Transform, Load) processes, initial data cleaning, and data validation tasks. Silver tables serve as a source for data science and machine learning models that require cleaner but not fully processed data. Gold tables are the source for high-level analytical workloads such as business intelligence reporting, data visualization, and decision-making processes.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC **Identify elements of the Databricks Platform Architecture, such as what is located in the
# MAGIC data plane versus the control plane and what resides in the customer’s cloud account**
# MAGIC
# MAGIC The elements located in the data plane are the data storage like AWS. Azure, or Google Cloud, compute resources like clusters or virtual machines, and Databricks Runtime which is an optimized version of Apache Spark with additional performance enhancements and security features. The control plane consists of the web application and user interface, including the notebook environment, job scheduler, and dashboard; cluster manager responsible for the lifecycle of compute clusters (creation, scaling, & termination); job scheduler responsible for scheduling and managing the execution of data jobs and workflows; Security and access management which includes managing user authentication, authorization, and overall control access to the Databricks environment; APIs and Integrations for programmatically interacting with the Databricks environment  and integrates with other tools and platforms. The customer’s cloud account handles data residency, which is where all of the data resides for better control over data security and compliance; Resource Utilization because the account is used for running compute instances and storing data, cost and usage are tied to the customer’s cloud billing. Data Security and Compliance are maintained because the data receives security benefits from both the cloud provider and Databricks.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC **Differentiate between all-purpose clusters and jobs clusters.**
# MAGIC
# MAGIC All-purpose clusters are designed for a wide range of tasks, run for extended periods of time, can be configured to auto-scale based on workload, multiple user access simultaneously for collaborative work and can run multiple commands and jobs concurrently, can be more costly if not managed carefully. Jobs clusters are used for running specific workloads, such as ETL jobs, data processing tasks, and scheduled jobs, created to run a specific job and are terminated upon the job’s completion, configured for the job at hand (not meant for scaling), does not support interactive use, can be more cost-effective because they only exist for the job and are tailored to the job’s requirements.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC **Identify how cluster software is versioned using the Databricks Runtime.**
# MAGIC
# MAGIC Each release of the Databricks Runtime is assigned a unique version number. This version number reflects the specific set of enhancements, performance improvements, and additional features that have been added to the standard Apache Spark in that particular release of the Databricks Runtime.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC **Identify how clusters can be filtered to view those that are accessible by the user**
# MAGIC
# MAGIC Filtering clusters can be achieved through the Databricks workspace interface. Users will only be able to view the clusters if they have access to. Users with “Can View” are only able to view the clusters and users with “Can Manage” will be able to see, configure, and terminate the clusters. Clusters can be filtered by cluster name, status, and tags. Clusters can also be queried automatically using APIs.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC **Describe how clusters are terminated and the impact of terminating a cluster.**
# MAGIC
# MAGIC Clusters can be terminated by the user or automatically based on conditions like inactivity or a specified time-to-live (TTL) setting. Upon termination, all computational resources allocated to the cluster are released. This can lead to cost savings because resource usage directly impacts cloud billing. Any data stored in the cluster’s memory and local storage is lost, but cloud data remains intact. Any ongoing processes, computations, or jobs running will be stopped, these processes will either need to be rerun or resumed when the cluster is restarted or created. Notebooks connected to the terminated cluster will lose their execution context and will need to be attached to an active cluster to continue their work. The configuration and settings of the terminated cluster are retained within Databricks and users can create new clusters with the same configuration or modify it as needed. These configurations include the cluster’s setup, installed libraries, and other settings. 
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC **Identify a scenario in which restarting the cluster will be useful.**
# MAGIC
# MAGIC Restarting clusters can help by clearing memory to resolve memory leak issues, resetting state can help avoid potential errors and inconsistencies caused by stale data, resolves performance issues due to long-term use improving responsiveness, changes in configuration or updates to software (Databricks runtime, spark, or library updates) will take effect when restarted, and troubleshooting when the cause of an issue is not apparent; can be a quick way to see if an issue persists.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC **Describe how to use multiple languages within the same notebook.**
# MAGIC
# MAGIC You can choose a default language for the notebook (Python, Scala, SQL, or R). The chosen language will be used for all code cells unless specified otherwise. You can use the magic commands: %python, %scala, %sql, %r which will change the language of the specified cell. The benefit is that the data can be shared between the languages to utilize features of the language with the tradeoff of that converting data structures between languages could require extra handling.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC **Identify how to run one notebook from within another notebook.**
# MAGIC
# MAGIC You can run a notebook from another notebook using the %run magic command followed by the path of the notebook you want to run. The basic syntax is `%run "/path/to/notebook"`. You can also pass parameters to the notebook that you are running. For instance, if `DataProcessing` notebook has a widget (parameter) named date, you can pass a value to it by using `%run "/Workflows/DataProcessing" -d date="2021-01-01"`.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC **Identify how notebooks can be shared with others.**
# MAGIC
# MAGIC Notebooks can be shared by directly sharing through the workspace using the share button with the permissions “can view”, “can edit”, ”can run”, exported in formats like HTML, PDF, DBC (Databricks archive), and IPython notebook (IPYNB), shared via Databricks repos and git integration, publishing a notebook as a webpage, and emailing notebooks directly from Databricks. 
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC **Describe how Databricks Repos enables CI/CD workflows in Databricks.**
# MAGIC
# MAGIC It enables workflows by being able to link notebooks and code to Git repositories, allows notebooks to be tested automatically with external continuous integration tools, CI test can be applied to continuous deployment CD pipelines that help create different environments (development, staging, production). This allows multiple people to work on different parts of the project simultaneously without overwriting each other’s work.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC **Identify Git operations available via Databricks Repos.**
# MAGIC
# MAGIC Clone, create and switch branches, commit changes, pull changes, push changes, resolve merge conflicts, view commit history, create pull requests.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC **Identify limitations in Databricks Notebooks version control functionality relative to Repos.**
# MAGIC
# MAGIC - Databricks Notebooks: have basic version control consisting of only checkpointing and revision history, limited support for branching and merging, does not natively support external git repositories, limited capabilities for handling merge conflicts, lacks the functionality to handle pull requests, limited support for CI/CD pipelines.
# MAGIC - Databricks repos: have full git integration including line-by-line tracking, supports branching and merging, seamlessly supports external Git repositories, leverages Git’s capabilities to handle merge conflicts, allows users to handle pull requests via their Git providers’ platform, better support for CI/CD integrations because of its Git compatibility allowing automated processes triggered on commits and merges.
# MAGIC
